---
name: supervisor
description: Multi-agent supervisor protocol - execute multiple agents without context explosion. Keywords: multi-agent, supervisor, parallel, sequential
user-invocable: true
---

# JARVIS Multi-Agent Supervisor Protocol

**Goal:** Execute multiple agents without blowing up context window.

---

## 🚨 The Problem

```
❌ WRONG WAY (what we used to do):
Launch 5 agents → All read full context → BOOM (200K limit)

✅ RIGHT WAY (supervisor pattern):
Agents write to files → Supervisor reads summaries → Context stays small
```

---

## 📋 How To Use

### Step 1: Define Tasks

Create/edit `~/.claude/skills/supervisor/tasks.json`:

```json
[
  {
    "id": "task-1",
    "name": "Review Profile Screen",
    "execution": "parallel",
    "agent_type": "Explore",
    "prompt": "Analyze profile screen. Return: file paths, 3 findings, 1 fix priority.",
    "depends_on": []
  },
  {
    "id": "task-2",
    "name": "Review Wallet System",
    "execution": "parallel",
    "agent_type": "Explore",
    "prompt": "Analyze wallet system. Return: file paths, 3 findings, 1 fix priority.",
    "depends_on": []
  },
  {
    "id": "task-3",
    "name": "Implement Fixes",
    "execution": "sequential",
    "agent_type": "general-purpose",
    "prompt": "Using findings from task-1 and task-2, implement priority fixes.",
    "depends_on": ["task-1", "task-2"]
  }
]
```

### Step 2: Review Plan

```bash
python ~/.claude/skills/supervisor/supervisor.py plan
```

Shows:
- 📦 PARALLEL tasks (can run together)
- 📝 SEQUENTIAL tasks (must wait for dependencies)

### Step 3: Execute (Claude Code)

**For PARALLEL tasks** - launch agents one after another, they write to files:

```
For each task in parallel:
  → Launch Agent with SCOPED prompt
  → Agent writes output to ~/.claude/skills/supervisor/output/{task-id}.json
  → ONLY return brief findings to chat
```

**For SEQUENTIAL tasks** - wait for previous, then launch next:

```
Wait for task-1 to complete → Launch task-2
```

### Step 4: View Summary

```bash
python ~/.claude/skills/supervisor/supervisor.py summary
```

Shows aggregated findings from all agents.

---

## 🔑 Key Rules

### When Launching Agents

**DO:**
- Scope prompts tightly ("Return ONLY 3 bullet points")
- One agent at a time for sequential
- Ask for summaries, not code dumps
- Let agents write to files, not chat

**DON'T:**
- Launch 5+ agents at once
- Ask for full code returns
- Let agents dump everything to chat
- Ignore dependencies

### Prompt Template for Agents

```
**SCOPE:** {specific area}
**OUTPUT:** Brief summary only - do NOT dump code

Task:
{specific task}

Return ONLY:
- File paths (max 3)
- 3 bullet points of findings
- 1 thing to fix first

Do NOT return full code. Just essentials.
```

---

## 📁 Files

| File | Purpose |
|------|---------|
| `supervisor.py` | Main coordinator script |
| `tasks.json` | Task definitions (you edit this) |
| `output/*.json` | Agent outputs (external storage) |
| `summary.json` | Aggregated findings |

---

## 🎯 Example Session

```
User: "Review profile, wallet, refunds"

Assistant: [Creates tasks.json, runs plan]

📦 PARALLEL (2 tasks):
  - task-1: Review Profile Screen
  - task-2: Review Wallet System

[Launches agent for task-1 → writes to output/task-1.json]
[Launches agent for task-2 → writes to output/task-2.json]

[Reads outputs, returns summary]
✅ task-1: No profile screen exists. Create first.
✅ task-2: Wallet exists but old/new not integrated.

User: "Fix both"

Assistant: [Creates task-3 dependent on 1,2]
📝 SEQUENTIAL: Implement fixes (after task-1, task-2)

[Launches agent → writes to output/task-3.json]
✅ task-3: Fixed.
```

---

## 🚨 Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|---------------|-----|
| Launch 5 agents at once | All read context → BOOM | Launch 1-2 at a time |
| Ask for "full analysis" | Returns 100KB → BOOM | Ask for "3 bullet points" |
| Let agent dump code | Chat fills up | "Do NOT return code" |
| Ignore dependencies | Wrong order, rework | Check depends_on[] |

---

## Reset

```bash
python ~/.claude/skills/supervisor/supervisor.py reset
```

Clears all outputs, start fresh.
