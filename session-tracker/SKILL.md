---
name: session-tracker
description: Track sessions, auto-save state, recover after crashes. Keywords: sessions, recover, crash, resume, where was i
user-invocable: true
---

# Session Tracker - Auto-Save & Recovery

**Purpose:** Never lose context after computer crash. Track what you're working on.

---

## How It Works

1. **Auto-saves** session state every 15 minutes
2. **Logs** all actions taken
3. **Recovers** full context after crash
4. **Lists** recent sessions on demand

---

## Commands

| Command | What It Does |
|---------|--------------|
| `/sessions` | List recent sessions |
| `/session current` | Show current session details |
| `/session recover` | Restore after crash |
| `/session save` | Manual save snapshot |

---

## What Gets Tracked

| Data | Example |
|------|---------|
| Session ID | 2025-03-07-session-1 |
| Start time | 2025-03-07T10:30:00 |
| Project | pickleballbn |
| Branch | claude/issue-7-demo-fixes |
| Current task | "Fix BottomNav clipping" |
| Completed tasks | ["Updated BottomNav.tsx"] |
| Next steps | "Test on preview URL" |
| Last action | "Edited line 45 of BottomNav.tsx" |
| Context notes | "User wants glassmorphism consistency" |

---

## Crash Recovery Dialogue

```
Claude: 🔄 I detect you had an active session that crashed.

        Session: 2025-03-07-s3
        Project: PickleballBN
        Branch: claude/issue-7-demo-fixes
        Last action: Updated BottomNav.tsx line 45

        What would you like to do?
        1. Resume this session
        2. View full details
        3. Start fresh

User: 1

Claude: ✅ Resuming session...
        Working on: BottomNav fixes (1/2 complete)
        Next: Test on preview
        Last file: src/magicpatterns/src/components/BottomNav.tsx

        Continue?
```

---

## Auto-Save Triggers

Session saves when:
- ⏱️ Every 15 minutes (automatic)
- 📝 Task marked complete
- 💬 User says "save", "checkpoint"
- 🔀 Before git operations
- 📤 Before pushing

---

## Session List Output

```
Recent Sessions (last 5):

┌──────────────┬──────────┬─────────┬─────────────┬──────────────┐
│ ID           │ Time     │ Status  │ Project     │ Branch        │
├──────────────┼──────────┼─────────┼─────────────┼──────────────┤
│ 03-07-s3     │ 14:00    │ ACTIVE  │ pickleballbn│ issue-7-fix  │
│ 03-07-s2     │ 10:30    │ ended   │ pickleballbn│ main         │
│ 03-06-s5     │ 16:45    │ ended   │ pickleballbn│ issue-5      │
│ 03-06-s4     │ 14:20    │ ended   │ pickleballbn│ issue-4      │
│ 03-06-s3     │ 11:00    │ ended   │ pickleballbn│ main         │
└──────────────┴──────────┴─────────┴─────────────┴──────────────┘

Current: 03-07-s3
Working on: BottomNav fixes
Progress: 50% (1/2 tasks)
```

---

## File Locations

```
~/.claude/.session-log/
├── sessions.json              ← Master list of all sessions
├── latest-session.json         ← Current active session
├── current-context.json        ← Quick load for resume
└── archive/                   ← Past sessions by month
    ├── 2025-03/
    └── 2025-02/
```

---

## Integration with Memory Bank

```
Session Tracker          Memory Bank
    ↓                        ↓
Current work        →    activeContext.md
(what I'm doing)        (deep context)
    ↓                        ↓
Auto-saves to      →    Manual update
JSON every 15min        at session end
    ↓                        ↓
Fast recovery        →    Full history
after crash           (all sessions)
```

---

## Recovery Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    AFTER CRASH                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. User starts new session                                 │
│     ↓                                                       │
│  2. Skill detects: latest-session.json has recent activity  │
│     ↓                                                       │
│  3. Ask: "Recover previous session?"                        │
│     ↓                                                       │
│  4. If yes: Load context                                   │
│     - Project name                                          │
│     - Current branch                                        │
│     - Tasks in progress                                     │
│     - Last file edited                                      │
│     - Next steps                                           │
│     ↓                                                       │
│  5. User confirms: Resume / Start fresh                    │
│     ↓                                                       │
│  6. Continue from where left off ✅                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

On session start, skill checks:
1. Does `latest-session.json` exist?
2. Is it less than 4 hours old?
3. Was status "active" (not properly closed)?

If all yes → Offer recovery

---

## Commands for Scripts

**List sessions:**
```bash
cat ~/.claude/.session-log/sessions.json | jq -r '.sessions[] | [.id, .time, .status, .project] | @tsv'
```

**Show current:**
```bash
cat ~/.claude/.session-log/latest-session.json | jq '.'
```

**Recover:**
```bash
cat ~/.claude/.session-log/latest-session.json
```

---

## Summary

| Feature | Benefit |
|---------|---------|
| Auto-save every 15 min | Never lose more than 15 min of work |
| Session list | See what you worked on recently |
| Crash recovery | Resume exactly where you left off |
| Task tracking | Know what's in progress |
| Branch tracking | Remember which branch you were on |

**Yes, after crash you can run `/sessions` or `/session recover` to get everything back.**
