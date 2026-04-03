---
name: observability
description: Use observability MCP tools to investigate logs and traces
always: true
---

# Observability Skill

You have access to observability tools that query VictoriaLogs (structured logs) and VictoriaTraces (distributed traces). Use them to diagnose errors and understand system behavior.

## Available tools

| Tool | What it does |
|------|-------------|
| `mcp_obs_logs_search` | Search VictoriaLogs with a LogsQL query |
| `mcp_obs_logs_error_count` | Count errors per service over a time window |
| `mcp_obs_traces_list` | List recent traces, optionally filtered by service |
| `mcp_obs_traces_get` | Fetch a full trace by ID |

## Strategy

- **"What went wrong?" / "Check system health" — one-shot investigation.** When the user asks what went wrong or to check system health, run this full chain in one pass:
  1. Call `mcp_obs_logs_error_count` with a fresh window (e.g. `window: "10m"`, `service: "Learning Management Service"`) to see if there are recent errors.
  2. If errors exist, call `mcp_obs_logs_search` with a scoped query like `_time:10m service.name:"Learning Management Service" severity:ERROR` to get the actual error entries.
  3. Extract a `trace_id` from the most recent error log entry.
  4. Call `mcp_obs_traces_get` with that `trace_id` to fetch the full trace and see the complete request flow.
  5. Write one short explanation that cites **both** the log evidence (what the error was) **and** the trace evidence (where in the request flow it happened), naming the affected service and the root failing operation.

- **Error investigation.** When the user asks about errors, failures, or "what went wrong":
  1. Start with `mcp_obs_logs_error_count` to check if there are recent errors and which services are affected.
  2. Use `mcp_obs_logs_search` with a scoped query (e.g. `_time:10m service.name:"Learning Management Service" severity:ERROR`) to find specific error entries.
  3. If log entries contain a `trace_id`, use `mcp_obs_traces_get` to fetch the full trace and see where the failure occurred in the request flow.

- **Scoped queries.** Prefer narrow time windows (`_time:10m`) and specific service names to avoid surfacing unrelated historical errors.

- **Healthy state.** If the user asks "is everything OK?" or "any errors?", run `mcp_obs_logs_error_count` with a short window first. If zero errors, report that the system is healthy.

- **Trace analysis.** When examining a trace, look for spans with error tags, unusually long durations, or failed operations. Summarize which service and operation failed.

## Response formatting

- Lead with the answer — "There are 3 errors in the LMS backend from the last 10 minutes" or "No errors found — the system is healthy."
- Summarize key findings: service name, error type, count, and any trace IDs.
- Do not dump raw JSON — extract the meaningful information.
- If you find a trace ID, mention it so the user can look it up in the UI if needed.

## Capabilities

When asked what you can do, explain that you can:
- Search structured logs by service, severity, time window, or keywords
- Count errors per service over configurable time windows
- List recent traces and fetch full trace details by ID
- Diagnose failures by correlating log errors with trace spans

You **cannot** modify logs, traces, or fix infrastructure issues — you can only observe and report.
