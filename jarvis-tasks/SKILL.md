---
name: jarvis-tasks
description: How and when to use JARVIS's centralized task system (mcp__claude_ai_JARVIS__* tools) — worktree/branch/machine tracking, staleness checks, git reconciliation, maintenance-request logging. Use whenever creating a worktree/branch, starting or finishing work, or logging a client maintenance request.
---

# JARVIS Tasks — usage playbook

Backend is infrastructure (Cloudflare Worker `jarvis-mcp` + Supabase `jarvis_tasks`, PROD project `zolxejafzbxgcmimarsz`), source at `workers/jarvis-mcp/index.js` in `uniplay-development`. This skill is the *how-to*, not the plumbing — edit this file freely as usage patterns change; edit the worker source only for real capability changes.

n8n (`jarvis-tasks` MCP, `task_claim`/`task_complete`) is retired — dead, laptop-dependent, don't use. Everything below is Cloudflare/Supabase-backed, always-on.

## Tool reference

- `create_task({title, description?, priority?, assigned_to?, worktree_path?, branch_name?, machine?, category?, actual_hours?, depends_on?, scheduled_at?})`
- `list_tasks({status?, limit?})` — newest-first, default limit 10.
- `check_stale_tasks({limit?})` — read-only, pure arithmetic. Flags `pending` unclaimed 3+ days, `in_progress` idle 7+ days.
- `update_task_status({task_id, status?, merge_status?, branch_name?, worktree_path?, machine?, worked_by?, work_channel?, category?, actual_hours?, depends_on?, scheduled_at?, tier?, execution_mode?, max_access_level?, planning_complete?, notes?})` — the write primitive. Nothing else moves a task off `pending`. Moving a task to `in_progress`/`completed` while it still has unmet `depends_on` returns a non-blocking `warning` field (never fails the write) — a dangling/deleted dependency id shows up as `status: "not_found"`, still counted as unmet.
- `sync_task_git({apply?, limit?})` — dry-run by default. Checks GitHub for merged PRs on open tasks' branches, reports drift. `apply:true` writes `merge_status` only, never `status`.
- `check_due_tasks({limit?})` — read-only. Lists `pending` tasks whose `scheduled_at` has passed, soonest-overdue first. Surfaces what's due; starts nothing.
- `check_auto_execute_eligible({task_id?, limit?})` — read-only classification of the CLAUDE.md SAFE formula (`tier<=quick AND execution_mode=auto AND max_access_level<=L2 AND planning_complete`). Pass `task_id` for one task, omit to scan all `pending`. Returns `eligible` + which clauses fail. **Does not execute anything** — unattended dispatch is deliberately unimplemented, needs separate sign-off before it ever exists.

## When to call what

**Starting a worktree/branch** — call `create_task` with provenance filled in, don't leave it null:
```
worktree_path: $(git rev-parse --show-toplevel)
branch_name:   $(git branch --show-current)
machine:       $(hostname)
```
This is what makes cross-machine task tracking actually work — an empty `worktree_path`/`machine` is indistinguishable from any other task later.

**Session start** — a `check_stale_tasks` nudge already fires via the SessionStart hook (worktree-scoped where possible). Actually call it, don't just acknowledge the reminder — surface anything genuinely relevant to the user.

**Claiming/finishing work** — `update_task_status`:
- Claim: `status: "in_progress"`, `worked_by: "<your agent/session name>"`, `work_channel: "cli"` (or `"cloud"` if running remotely).
- Finish: `status: "completed"` — `completed_at` is set automatically, don't pass it.
- Branch created after the task existed: `update_task_status({task_id, branch_name})` — the common case, since tasks usually predate their branch.

**Before merge, or periodically** — `sync_task_git({})` (dry-run) to catch tasks whose branch already merged but the task's still open. Only `apply:true` if you want it to actually write `merge_status`; it never touches `status`.

**Client maintenance requests** — `category: "maintenance"`, log time in `actual_hours` (not `execution_cost` — that's reserved for AI-run cost, different thing, don't collide). Rollup against a monthly allowance = `list_tasks`/a query filtered `category='maintenance'`, summed `actual_hours` — no new table needed for this.

**Dependencies/scheduling** — set `depends_on` (array of task uuids) on `create_task`/`update_task_status` when a task genuinely can't start before another finishes; set `scheduled_at` (ISO timestamp) when a task shouldn't be picked up before a given time. Check `check_due_tasks` at session start alongside `check_stale_tasks` if anything might be scheduled. `check_auto_execute_eligible` is a classification lens only — use it to see which of CLAUDE.md's SAFE clauses a task fails, not to actually run anything unattended (that capability doesn't exist here).

## Category taxonomy (reuse, don't invent)

Live buckets as of 2026-07-02: `design`, `legal`, `infrastructure`, `maintenance`. Check `list_tasks` / query live data before adding a new one — a near-duplicate category (`infra` vs `infrastructure`) fragments rollups.

## Workflow gate — task status ↔ the repo's Standard Workflow

Don't treat `status` as free-form — it should track the phase in `uniplay-development/CLAUDE.md`'s **Standard Workflow Per Branch/Worktree** table (Plan → Execute → Verify → Review → Merge). That table is the canonical source for model routing and gates — this section only maps task fields onto it, doesn't restate it; if the two drift, CLAUDE.md wins.

**Model routing → `executor`/`executor_model`/`complexity` fields (real columns, CHECK-constrained on PROD, verified 2026-07-02):**
- `executor` — one of `aider` / `claude_code` / `manual` (DB constraint, nothing else validates). Set it when claiming (`update_task_status`), don't leave it null once work starts.
- `complexity` — one of `low` / `medium` / `high` / `critical` (DB constraint). Route by CLAUDE.md's rule: Opus for architecture/planning-complete, Haiku/Sonnet for execution sized to the task (Subagent Scope Guard — cap effort to task size, don't default to Opus).
- `tier` field exists too (schema has it, currently unused on every row) — leave null until there's a real reason to populate it; don't invent a taxonomy for it here.

**Status transitions and what must be true first:**
- `pending → in_progress`: claim via `update_task_status` (`worked_by`, `work_channel`, `executor`). This is Plan/Execute starting.
- `in_progress → completed`: **do not set this until CLAUDE.md's verification gate has actually passed** — lint + build clean, and for code changes touching the app, E2E (`npx playwright test`) or at minimum smoke tests (`npm run test:smoke`) green, and (before merge to `main`) a Codex review returning "no discrete actionable bugs" (iterate, don't stop at first pass — the 11→0 convergence pattern is the benchmark, not the exception, per CLAUDE.md). Record what actually ran in `notes` (e.g. `"lint+build+smoke green, codex clean after 2 passes"`) — don't mark completed on a bare claim.
- A task that's `in_progress` with no verification evidence and no recent `updated_at` is exactly what `check_stale_tasks` is designed to catch — that's the intended failure mode this guards, not a separate concern.

**Reviewer pattern** — mirrors what this session used all night: Opus (or Codex) reviews before merge; an independent second reviewer (Fable-5, or a second Codex profile) for anything touching PROD or a live worker. Don't self-certify a task `completed` without at least one of these having actually run — "I wrote it correctly" is not a verification step.

## Toolchain integration — which tool runs at which phase

Ties the task lifecycle to the rest of the stack, verified 2026-07-02:

- **jcodemunch (mandatory, per CLAUDE.md's Tool Gates table)** — `plan_turn` is the first move of *any* task touching code, before the task tool even. If it recommends specific files, that maps onto the task's `target_files` field (real column, currently unused on every row) — populate it via `update_task_status` so the task record shows what was actually in scope, not just a title. `get_blast_radius` before rename/delete, `get_hotspots` before refactor — same gate, unrelated to JARVIS, but the task's `notes` should record that it ran (`"blast radius checked, 3 callers"`), not just that code was written.
- **Ponytail (this session's default mode)** — governs *how* a claimed task gets implemented: reuse before build, stdlib/native before a dependency, smallest correct diff. Tonight's own jarvis-mcp changes are the worked example — one shared table, no new route, no new infra, additive-only. Route `complexity` accordingly: a ponytail-sized task is `low`/`medium`, not `high`.
- **Caveman (this session's default mode)** — governs `notes`/status text specifically: terse, information-dense, no filler. `"lint+build+smoke green, codex clean 2 passes"` not a paragraph.
- **Headroom (`mcp__headroom__headroom_compress`/`_retrieve`)** — available, not yet exercised tonight (verify behavior before treating this as a hard rule, not just inferring from the tool description). Shrinks large content, keeps a retrievable hash. Candidate use: a task's `description`/`implementation_plan`/`execution_log`/`error_log` getting long — compress before writing it into the task row via `update_task_status`, so `list_tasks` stays cheap to read back; retrieve the hash only when full detail is actually needed.
- **Opus planning** — for `complexity: high`/`critical` tasks, planning happens in Opus and lands as `docs/plans/<date>-<slug>.md` (this session's whole convention) before any code — `update_task_status({..., notes: "plan: docs/plans/2026-07-02-x.md"})` links the two.
- **Fable-5 review** — adversarial review of the *plan*, before execution starts. Used repeatedly tonight (brain-sync hook, staleness monitoring, task provenance/git-sync) — catches real bugs before they're built, not after. Gate: don't move `pending → in_progress` on a `high`/`critical` task until a Fable pass has actually run on its plan.
- **Codex — second eye, mandatory before merge to `main`** — see the Workflow gate section above; this is the same Codex review CLAUDE.md's Code Review Workflow already mandates, referenced here as the completion gate, not a separate rule.

## Honest limits

- **No live sync.** `sync_task_git` only runs when called — an agent, not a cron. A merged branch shows as drift until someone asks.
- **No cross-tool guarantee.** These tools are a Claude.ai account-level connector (`mcp__claude_ai_JARVIS__*`) — unconfirmed whether Codex or other non-Claude agents can reach them. Verify before assuming a Codex session sees the same task list.
- **Staleness thresholds are informational, not enforced.** `check_stale_tasks` flags, never blocks, never auto-escalates.
