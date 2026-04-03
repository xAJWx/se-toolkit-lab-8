---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to live LMS (Learning Management System) data through MCP tools.
Use them to answer questions about labs, learners, scores, and progress.

## Available tools

| Tool | What it does | Needs a lab? |
|------|-------------|:------------:|
| `lms_health` | Check backend health, returns item count | No |
| `lms_labs` | List all available labs | No |
| `lms_learners` | List all registered learners | No |
| `lms_pass_rates` | Avg score and attempt count per task for a lab | Yes |
| `lms_timeline` | Submission timeline (date + count) for a lab | Yes |
| `lms_groups` | Group performance (avg score + student count) for a lab | Yes |
| `lms_top_learners` | Top learners by avg score for a lab | Yes |
| `lms_completion_rate` | Completion rate (passed / total) for a lab | Yes |
| `lms_sync_pipeline` | Trigger the LMS sync pipeline | No |

## Strategy

- **No lab specified.** If the user asks for scores, pass rates, completion, groups, timeline, or top learners **without naming a lab**, call `lms_labs` first. If multiple labs are available, let the shared `structured-ui` skill decide how to present the choice on supported channels. On plain CLI, list the labs briefly and ask the user to pick one.
- **Lab identifiers.** Use each lab's `title` from `lms_labs` as the user-facing label. When calling tools that need a `lab` parameter, use the lab's `id` field (e.g. `"lab-01"`), not the title.
- **Comparing across labs.** If the user asks "which lab has the lowest pass rate?" or similar cross-lab questions, call `lms_labs` first, then call the relevant tool for each lab, and compare the results.
- **Empty results.** If a tool returns empty data for a lab, tell the user — it may mean no submissions yet, not an error.
- **Sync.** If data looks stale or empty and the user expects results, offer to run `lms_sync_pipeline` and retry.

## Response formatting

- Keep responses concise. Lead with the answer, not with "Let me check…".
- Format percentages with one decimal place (e.g. `93.9%`).
- Show counts as plain numbers (e.g. `108 out of 115`).
- Use short tables or bullet lists for multi-value results.
- Do not dump raw JSON — summarize the key numbers.

## Capabilities

When the user asks "what can you do?", explain that you can query live LMS data:
- Check if the LMS backend is healthy
- List available labs
- Show pass rates, completion rates, group performance, and top learners **for a specific lab**
- Show submission timelines
- List registered learners
- Trigger a data sync

You **cannot** modify data, submit work, or change grades — you are read-only.
