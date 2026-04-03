"""Tool specifications for the observability MCP server."""

from __future__ import annotations

import json
from typing import Any, Protocol

from mcp.types import Tool
from pydantic import BaseModel, Field

from mcp_obs.client import ObsClient


class ToolPayload(Protocol):
    def model_dump(self) -> dict[str, Any]: ...


class ToolSpec:
    def __init__(
        self,
        name: str,
        description: str,
        model: type[BaseModel],
        handler: Any,
    ) -> None:
        self.name = name
        self.description = description
        self.model = model
        self.handler = handler

    def as_tool(self) -> Tool:
        return Tool(
            name=self.name,
            description=self.description,
            inputSchema=self.model.model_json_schema(),
        )


# ── Log tools ─────────────────────────────────────────────────────

class LogsSearchParams(BaseModel):
    query: str = Field(
        description="LogsQL query string, e.g. '_time:10m service.name:\"Learning Management Service\" severity:ERROR'"
    )
    limit: int = Field(
        default=20,
        description="Maximum number of log entries to return",
    )


async def logs_search_handler(client: ObsClient, args: LogsSearchParams) -> str:
    results = await client.search_logs(query=args.query, limit=args.limit)
    if not results:
        return "No log entries found for the given query."
    return json.dumps(results, indent=2, ensure_ascii=False)


class LogsErrorCountParams(BaseModel):
    service: str = Field(
        default="",
        description="Service name to filter errors (e.g. 'Learning Management Service'). Leave empty for all services.",
    )
    window: str = Field(
        default="10m",
        description="Time window for the count, e.g. '10m', '1h', '24h'",
    )


async def logs_error_count_handler(client: ObsClient, args: LogsErrorCountParams) -> str:
    service = args.service if args.service else None
    results = await client.count_errors(service=service, window=args.window)
    if not results:
        return f"No errors found in the last {args.window}."
    return json.dumps(results, indent=2, ensure_ascii=False)


# ── Trace tools ───────────────────────────────────────────────────

class TracesListParams(BaseModel):
    service: str = Field(
        default="",
        description="Service name to filter traces (e.g. 'Learning Management Service'). Leave empty for all services.",
    )
    limit: int = Field(
        default=10,
        description="Maximum number of traces to return",
    )


async def traces_list_handler(client: ObsClient, args: TracesListParams) -> str:
    service = args.service if args.service else None
    results = await client.list_traces(service=service, limit=args.limit)
    if not results:
        return "No traces found."
    summaries = []
    for trace in results:
        spans = trace.get("spans", [])
        summaries.append({
            "trace_id": trace["traceID"],
            "span_count": len(spans),
            "operations": list({s["operationName"] for s in spans}),
        })
    return json.dumps(summaries, indent=2, ensure_ascii=False)


class TracesGetParams(BaseModel):
    trace_id: str = Field(
        description="The trace ID to fetch (hex string, e.g. '0ec62ffa010a5bd7dd9b5649f17daca5')"
    )


async def traces_get_handler(client: ObsClient, args: TracesGetParams) -> str:
    trace = await client.get_trace(args.trace_id)
    if not trace:
        return f"No trace found with ID: {args.trace_id}"
    spans = trace.get("spans", [])
    summary = {
        "trace_id": trace["traceID"],
        "span_count": len(spans),
        "spans": [
            {
                "operation": s["operationName"],
                "duration_us": s.get("duration", 0),
                "tags": {t["key"]: t["value"] for t in s.get("tags", []) if t["key"] in ("error", "http.status_code", "db.statement")},
            }
            for s in spans
        ],
    }
    return json.dumps(summary, indent=2, ensure_ascii=False)


# ── Registry ──────────────────────────────────────────────────────

TOOL_SPECS: list[ToolSpec] = [
    ToolSpec(
        name="mcp_obs_logs_search",
        description="Search structured logs in VictoriaLogs using a LogsQL query. Use fields like service.name, severity, event, trace_id. Example query: '_time:10m service.name:\"Learning Management Service\" severity:ERROR'",
        model=LogsSearchParams,
        handler=logs_search_handler,
    ),
    ToolSpec(
        name="mcp_obs_logs_error_count",
        description="Count errors per service over a time window in VictoriaLogs. Specify a service name and window (e.g. '10m', '1h'). Returns error counts grouped by service.",
        model=LogsErrorCountParams,
        handler=logs_error_count_handler,
    ),
    ToolSpec(
        name="mcp_obs_traces_list",
        description="List recent traces from VictoriaTraces. Optionally filter by service name. Returns trace summaries with trace IDs, span counts, and operation names.",
        model=TracesListParams,
        handler=traces_list_handler,
    ),
    ToolSpec(
        name="mcp_obs_traces_get",
        description="Fetch a full trace by ID from VictoriaTraces. Returns span details including operation names, durations, and error tags. Use trace_id from log entries.",
        model=TracesGetParams,
        handler=traces_get_handler,
    ),
]

TOOLS_BY_NAME: dict[str, ToolSpec] = {spec.name: spec for spec in TOOL_SPECS}
