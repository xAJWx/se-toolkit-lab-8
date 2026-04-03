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

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
