# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Q: "What is the agentic loop?"**

The agentic loop is the core cycle that an AI agent follows to accomplish tasks autonomously:

1. **Perceive** — The agent receives input (a user request, tool output, or environmental signal).
2. **Reason** — The agent analyzes the situation, decides what to do next, and plans its approach.
3. **Act** — The agent executes an action — calling a tool, running code, making an API call, etc.
4. **Observe** — The agent receives feedback from the action (output, error, state change).
5. **Repeat** — Based on the observation, the agent loops back to step 2, refining its plan until the task is complete or a stopping condition is met.

What makes it "agentic" (vs. a simple chatbot) is the loop itself — the agent doesn't just produce one response and stop. It iterates, using tool outputs to inform subsequent decisions, self-correcting when things go wrong, and continuing until the goal is achieved.

**Q: "What labs are available in our LMS?"**

The agent found 8 labs by inspecting local repo files and querying the backend directly:

| ID | Lab |
|----|-----|
| 1 | Lab 01 – Products, Architecture & Roles |
| 2 | Lab 02 — Run, Fix, and Deploy a Backend Service |
| 3 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
| 4 | Lab 04 — Testing, Front-end, and AI Agents |
| 5 | Lab 05 — Data Pipeline and Analytics Dashboard |
| 6 | Lab 06 — Build Your Own Agent |
| 7 | Lab 07 — Build a Client with an AI Coding Agent |
| 8 | lab-08 |

Note: At this stage the agent has no MCP tools configured — it used its built-in file/exec tools to discover the data. Part B will add proper LMS MCP tools.

## Task 1B — Agent with LMS tools

**Q: "What labs are available?"**

The agent called `mcp_lms_lms_labs` and returned real lab names from the backend:

| # | Lab Title |
|---|-----------|
| 1 | Lab 01 – Products, Architecture & Roles |
| 2 | Lab 02 — Run, Fix, and Deploy a Backend Service |
| 3 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
| 4 | Lab 04 — Testing, Front-end, and AI Agents |
| 5 | Lab 05 — Data Pipeline and Analytics Dashboard |
| 6 | Lab 06 — Build Your Own Agent |
| 7 | Lab 07 — Build a Client with an AI Coding Agent |
| 8 | lab-08 |

**Q: "Is the LMS backend healthy?"**

The agent called `mcp_lms_lms_health` and responded: "Yes, the LMS backend is healthy! It currently has 56 items in the system."

**Q: "Which lab has the lowest pass rate?"**

The agent chained multiple tool calls: first `mcp_lms_lms_labs` to get lab list, then `mcp_lms_lms_pass_rates` for all labs, then fell back to `mcp_lms_lms_completion_rate`. Result: Lab 01 is the only lab with data (93.9% completion, 108/115 passed). Labs 02–08 have 0 submissions.

## Task 1C — Skill prompt

**Q: "Show me the scores"** (no lab specified)

With the LMS skill prompt, the agent now follows the correct strategy:
1. Called `lms_health` to verify backend is up (56 items)
2. Called `lms_labs` to get the list of 8 labs
3. Asked the user to pick a lab: "Which one would you like to see scores for?" and listed all 8 labs with their titles

This is the expected behavior — the skill teaches the agent that score-related queries need a lab parameter, and if not provided, it should list available labs first.

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

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
