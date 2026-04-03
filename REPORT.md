# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Q: "What is the agentic loop?"**

The **agentic loop** is the iterative cycle an AI agent follows to accomplish tasks autonomously. Instead of just generating a single response, the agent continuously reasons, acts, and adapts until a goal is reached.

A typical agentic loop looks like this:

1. **Observe** — Read the user's request, check the current state, and gather context.
2. **Plan** — Decide what steps or tools are needed to make progress.
3. **Act** — Execute a tool call (e.g., read a file, run a command, search the web).
4. **Reflect** — Analyze the tool's output. Did it work? What's the next step?
5. **Repeat** — Loop back to planning until the task is complete or clarification is needed.

This is different from a standard chatbot, which typically does a single "prompt → response" exchange. An agentic loop enables multi-step reasoning, error recovery, and tool use — essentially letting the agent *work through* a problem rather than just *talking about* it.

In my own case, when you ask me to do something like "fix this bug," I don't just guess the answer — I read the file, analyze the code, make an edit, verify it, and report back. That entire flow is the agentic loop in action.

**Q: "What labs are available?"**

Here are the 8 available labs:

| ID | Title |
|----|-------|
| lab-01 | Lab 01 – Products, Architecture & Roles |
| lab-02 | Lab 02 — Run, Fix, and Deploy a Backend Service |
| lab-03 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
| lab-04 | Lab 04 — Testing, Front-end, and AI Agents |
| lab-05 | Lab 05 — Data Pipeline and Analytics Dashboard |
| lab-06 | Lab 06 — Build Your Own Agent |
| lab-07 | Lab 07 — Build a Client with an AI Coding Agent |
| lab-08 | lab-08 |

Let me know if you'd like stats for any of them!

## Task 1B — Agent with LMS tools

**Q: "What labs are available?"**

Here are the 8 available labs:

| ID | Title |
|----|-------|
| lab-01 | Lab 01 – Products, Architecture & Roles |
| lab-02 | Lab 02 — Run, Fix, and Deploy a Backend Service |
| lab-03 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
| lab-04 | Lab 04 — Testing, Front-end, and AI Agents |
| lab-05 | Lab 05 — Data Pipeline and Analytics Dashboard |
| lab-06 | Lab 06 — Build Your Own Agent |
| lab-07 | Lab 07 — Build a Client with an AI Coding Agent |
| lab-08 | lab-08 |

Let me know if you'd like stats for any of them!

**Q: "Is the LMS backend healthy?"**

Yes, the LMS backend is **healthy** with **56 items** in the system.

**Q: "Which lab has the lowest pass rate?"**

Only **lab-01** has pass rate data so far — labs 02 through 08 have no submissions yet.

For **lab-01**, the overall completion rate is **93.9%** (108 out of 115 passed). Here's a breakdown by task:

| Task | Avg Score | Attempts |
|------|-----------|----------|
| Lab setup | 97.2% | 119 |
| Task 0: Practice the Git workflow | 65.2% | 214 |
| Task 1: Product & architecture description | 59.4% | 90 |
| Task 2: Roles and skills mapping | 53.9% | 42 |
| Optional: Resolve a merge conflict | 41.7% | 6 |
| Optional: Create a release | 50.0% | 2 |
| Optional: Add a CI check | 25.0% | 4 |
| Optional: Plan skill development | 0.0% | 1 |

The toughest task in lab-01 is **"Optional: Plan skill development"** (0.0% avg score), followed by **"Optional: Add a CI check"** (25.0%). Among the core tasks, **"Task 2: Roles and skills mapping"** has the lowest average score at 53.9%.

## Task 1C — Skill prompt

**Q: "Show me the scores"** (no lab specified)

Only **lab-01** has submission data so far. Here are the scores:

| Task | Avg Score | Attempts |
|------|-----------|----------|
| Lab setup | 97.2% | 119 |
| Task 0: Practice the Git workflow | 65.2% | 214 |
| Task 1: Product & architecture description | 59.4% | 90 |
| Task 2: Roles and skills mapping | 53.9% | 42 |
| Optional: Resolve a merge conflict | 41.7% | 6 |
| Optional: Create a release | 50.0% | 2 |
| Optional: Add a CI check | 25.0% | 4 |
| Optional: Plan skill development | 0.0% | 1 |

Labs 02–08 have no submissions yet. Want me to check group performance, top learners, or the submission timeline for lab-01?

## Task 2A — Deployed agent

Nanobot gateway startup log excerpt:

```
Using config: /app/nanobot/config.resolved.json
🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
✓ Channels enabled: webchat
✓ Heartbeat: every 1800s
MCP server 'lms': connected, 9 tools registered
MCP server 'webchat': connected, 1 tools registered
Agent loop started
```

All services running via `docker compose --env-file .env.docker.secret up -d`.

## Task 2B — Web client

**WebSocket test via Caddy:**

```
$ echo '{"content":"What labs are available?"}' | websocat "ws://localhost:42002/ws/chat?access_key=my-nanobot-key"
```

Response:
> Here are the available labs:
> 
> | ID | Title |
> |----|-------|
> | lab-01 | Lab 01 – Products, Architecture & Roles |
> | lab-02 | Lab 02 — Run, Fix, and Deploy a Backend Service |
> | lab-03 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
> | lab-04 | Lab 04 — Testing, Front-end, and AI Agents |
> | lab-05 | Lab 05 — Data Pipeline and Analytics Dashboard |
> | lab-06 | Lab 06 — Build Your Own Agent |
> | lab-07 | Lab 07 — Build a Client with an AI Coding Agent |
> | lab-08 | lab-08 |
> 
> There are **8 labs** in total. Let me know if you'd like details on any specific lab — I can check pass rates, completion rates, group performance, top learners, or submission timelines.

**Flutter web client:** accessible at `http://<vm-ip>:42002/flutter`
- Login screen appears, accepts `NANOBOT_ACCESS_KEY`
- Agent answers questions using real LMS data via MCP tools
- Structured UI choices render properly when multiple labs exist

## Task 3A — Structured logging

**Happy-path log excerpt** from VictoriaLogs (query: `_time:1h service.name:"Learning Management Service" severity:INFO`):

```json
{"_msg":"auth_success","_time":"2026-04-03T17:09:59.837106432Z","event":"auth_success","service.name":"Learning Management Service","severity":"INFO","trace_id":"3028b642f9f2e36865de3de55e0f46df","span_id":"bec5e6e74aaf80d3","scope.name":"lms_backend.auth"}
{"_msg":"db_query","_time":"2026-04-03T17:09:59.837420544Z","event":"db_query","operation":"select","table":"item","service.name":"Learning Management Service","severity":"INFO","trace_id":"3028b642f9f2e36865de3de55e0f46df","span_id":"bec5e6e74aaf80d3","scope.name":"lms_backend.db.items"}
{"_msg":"request_completed","_time":"2026-04-03T17:10:00.082043648Z","event":"request_completed","method":"GET","path":"/items/","status":"200","duration_ms":"245","service.name":"Learning Management Service","severity":"INFO","trace_id":"3028b642f9f2e36865de3de55e0f46df","span_id":"bec5e6e74aaf80d3","scope.name":"lms_backend.main"}
```

**Error-path log excerpt** from VictoriaLogs (query: `_time:1h service.name:"Learning Management Service" severity:ERROR`):

```json
{"_msg":"db_query","_time":"2026-04-03T17:10:00.08096768Z","event":"db_query","operation":"select","table":"item","service.name":"Learning Management Service","severity":"ERROR","error":"[Errno -2] Name or service not known","trace_id":"3028b642f9f2e36865de3de55e0f46df","span_id":"bec5e6e74aaf80d3","scope.name":"lms_backend.db.items"}
{"_msg":"db_query","_time":"2026-04-03T17:09:57.8908672Z","event":"db_query","operation":"select","table":"item","service.name":"Learning Management Service","severity":"ERROR","error":"[Errno -2] Name or service not known","trace_id":"fa4084bbc0674d22eb44f499c4774423","span_id":"bc1affc4056eb495","scope.name":"lms_backend.db.items"}
```

**VictoriaLogs query** (`_time:10m service.name:"Learning Management Service" severity:ERROR`):
Returns structured JSON log entries with consistent fields: `service.name`, `severity`, `event`, `error`, `trace_id`, `span_id`, `scope.name`. Much easier than grepping `docker compose logs` — instant filtering by time window, service, and severity level.

## Task 3B — Traces

**Healthy trace** (trace_id: `caf5fd36d7f09e03e3d7407c8eee7212`):
- `GET /items/` → `connect` (22ms) → `SELECT db-lab-8` (297ms) → `http send` (65μs) → `request_completed`
- Total: ~350ms, all spans successful.

**Error trace** (trace_id: `0ec62ffa010a5bd7dd9b5649f17daca5`):
- `GET /items/` → `connect` (3191ms) → `SELECT` failed → `db_query` ERROR → `items_list_failed_as_not_found` → `request_completed` (404)
- The error appears in the `db_query` span — connection failure due to PostgreSQL being down.

## Task 3C — Observability MCP tools

**Normal conditions — "Any LMS backend errors in the last 10 minutes?"**

> No errors found in the LMS backend over the last 10 minutes — the system looks healthy. ✅

**Failure conditions** (PostgreSQL stopped, 3 failed requests triggered):

> Yes, there are **6 errors** in the Learning Management Service over the last 10 minutes.
>
> **Root cause:** DNS resolution failure — `[Errno -2] Name or service not known`
>
> All 6 errors are identical:
> - **Event:** `db_query` (SELECT on the `item` table)
> - **Scope:** `lms_backend.db.items`
> - **Error:** The service can't resolve the database hostname
>
> This is an **infrastructure/connectivity issue**, not an application bug.

## Task 4A — Multi-step investigation

**"What went wrong?"** (with PostgreSQL stopped):

> Here's what I found:
>
> ## 2 Errors in Learning Management Service (last 10 minutes)
>
> **Root cause:** DNS resolution failure — `[Errno -2] Name or service not known`
>
> **Details:**
> - **Service:** Learning Management Service
> - **Operation:** Database `SELECT` query on the `item` table (`lms_backend.db.items`)
> - **Error:** The service cannot resolve the database hostname
> - **Impact:** `GET /items/` requests are returning **HTTP 404**
> - **Timeline:** Two failures at 17:32:27 and 17:32:30 UTC
>
> **Trace evidence** (`db0c724eff4bbb15cc00f6e8fe733b94`):
> - The `connect` span failed after ~289ms with an error tag
> - This caused the parent `GET /items/` request to fail and return 404
> - 6 spans total in the trace, with the database connection being the root failure
>
> **Likely fix:** Check the database connection configuration — the hostname for the database is either misspelled, the DNS entry doesn't exist, or the database service is down/unreachable from the LMS backend.

The agent chained `logs_error_count` → `logs_search` → `traces_get` and produced a coherent investigation citing both log and trace evidence.

## Task 4B — Proactive health check

Created a recurring cron job (every 2 minutes) via the web chat. While PostgreSQL was stopped, the agent proactively posted:

> ⚠️ **LMS Health Check — Errors Detected**
>
> **2 errors** found in the Learning Management Service over the last 2 minutes.
>
> **Root cause:** DNS resolution failure — `[Errno -2] Name or service not known`
>
> All errors are identical `db_query` failures on the `item` table. The LMS backend cannot reach its database. This is an infrastructure/connectivity issue.

Nanobot logs confirm: `Cron: executing job 'Run health check'` → `mcp_obs_logs_error_count({"service": "Learning Management Service", "window": "2m"})` → UI message posted to chat → `evaluate_response: should_notify=True`.

## Task 4C — Bug fix and recovery

**Root cause:** In `backend/src/lms_backend/routers/items.py`, the `GET /items/` endpoint caught all exceptions with a broad `except Exception` and returned a misleading `HTTP 404 NOT_FOUND` with detail `"Items not found"`. This hid the real database/infrastructure failure behind a "not found" message.

**Fix:** Changed the exception handler to return `HTTP 500 INTERNAL_SERVER_ERROR` with the actual error message, and upgraded the log level from `warning` to `error`:

```diff
     except Exception as exc:
-        logger.warning(
-            "items_list_failed_as_not_found",
-            extra={"event": "items_list_failed_as_not_found"},
+        logger.error(
+            "items_list_failed",
+            extra={"event": "items_list_failed", "error": str(exc)},
         )
         raise HTTPException(
-            status_code=status.HTTP_404_NOT_FOUND,
-            detail="Items not found",
+            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
+            detail=f"Failed to retrieve items: {exc}",
         ) from exc
```

**Post-fix failure check** (PostgreSQL stopped, after redeploy):

> Here's what I found:
>
> **12 errors** in the **Learning Management Service** over the last 10 minutes.
>
> ### Root Cause: DNS Resolution Failure
> All errors share the same underlying issue: **`[Errno -2] Name or service not known`**
>
> ### Error Flow
> | Layer | Component | What Happened |
> |-------|-----------|---------------|
> | Database | `lms_backend.db.items` | `SELECT` on `item` table fails with DNS error |
> | Router | `lms_backend.routers.items` | `items_list_failed` event logged |
> | HTTP | `lms_backend.main` | `GET /items/` returns **500** |

After the fix, the agent now correctly reports **HTTP 500** (not the misleading 404) and the `items_list_failed` event (not `items_list_failed_as_not_found`).

**Healthy follow-up** (PostgreSQL restarted): The system is healthy — no backend errors in the last 2 minutes. The cron health check reports the system looks healthy.
