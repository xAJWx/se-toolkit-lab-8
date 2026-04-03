"""HTTP client for VictoriaLogs and VictoriaTraces APIs."""

from __future__ import annotations

import json
from typing import Any

import httpx


class ObsClient:
    """Client for VictoriaLogs and VictoriaTraces HTTP APIs."""

    def __init__(self, victorialogs_url: str, victoriatraces_url: str) -> None:
        self.logs_base = victorialogs_url.rstrip("/")
        self.traces_base = victoriatraces_url.rstrip("/")
        self._client = httpx.AsyncClient(timeout=15.0)

    async def close(self) -> None:
        await self._client.aclose()

    # ── VictoriaLogs ──────────────────────────────────────────────

    async def search_logs(
        self,
        query: str,
        limit: int = 20,
        start: str | None = None,
        end: str | None = None,
    ) -> list[dict[str, Any]]:
        """Search VictoriaLogs with a LogsQL query."""
        params: dict[str, Any] = {"query": query, "limit": limit}
        if start:
            params["start"] = start
        if end:
            params["end"] = end
        resp = await self._client.get(
            f"{self.logs_base}/select/logsql/query",
            params=params,
        )
        resp.raise_for_status()
        results: list[dict[str, Any]] = []
        for line in resp.text.strip().splitlines():
            if line.strip():
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    results.append({"_raw": line})
        return results

    async def count_errors(
        self,
        service: str | None = None,
        window: str = "10m",
    ) -> list[dict[str, Any]]:
        """Count errors per service over a time window."""
        query = f"_time:{window} severity:ERROR"
        if service:
            query += f' service.name:"{service}"'
        resp = await self._client.get(
            f"{self.logs_base}/select/logsql/query",
            params={"query": query, "limit": 1000},
        )
        resp.raise_for_status()
        # Count by service.name
        counts: dict[str, int] = {}
        for line in resp.text.strip().splitlines():
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
                svc = entry.get("service.name", "unknown")
                counts[svc] = counts.get(svc, 0) + 1
            except json.JSONDecodeError:
                counts["unknown"] = counts.get("unknown", 0) + 1
        return [{"service": k, "error_count": v} for k, v in counts.items()]

    # ── VictoriaTraces (Jaeger-compatible API) ────────────────────

    async def list_traces(
        self,
        service: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """List recent traces."""
        params: dict[str, Any] = {"limit": limit}
        if service:
            params["service"] = service
        resp = await self._client.get(
            f"{self.traces_base}/select/jaeger/api/traces",
            params=params,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])

    async def get_trace(self, trace_id: str) -> dict[str, Any] | None:
        """Fetch a specific trace by ID."""
        resp = await self._client.get(
            f"{self.traces_base}/select/jaeger/api/traces/{trace_id}",
        )
        resp.raise_for_status()
        data = resp.json()
        traces = data.get("data", [])
        return traces[0] if traces else None

    async def __aenter__(self) -> "ObsClient":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.close()
