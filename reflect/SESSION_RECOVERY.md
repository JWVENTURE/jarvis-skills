# JARVIS Session Recovery System

**Problem:** Computer crash = session context lost
**Solution:** Auto-save session state + recovery commands

---

## Current Gaps

| System | What It Tracks | Survives Crash? |
|--------|----------------|-----------------|
| activeContext.md | Manual updates only | ❌ No (unless manually saved) |
| Supabase KB | Static knowledge | ❌ No session state |
| Skills | Rules only | ❌ No current work |
| Git history | Commits only | ❌ Unsaved work lost |

---

## Solution: Session Auto-Tracker

Creates:
1. **Session log** - Every session recorded
2. **Auto-save snapshots** - Periodic state saves
3. **Recovery command** - Restore after crash
4. **Session list** - See recent sessions

---

## Files Created

```
~/.claude/
├── .session-log/                    ← Session history
│   ├── sessions.json                ← All sessions list
│   ├── 2025-03-07-session-1.json    ← Session snapshots
│   ├── 2025-03-07-session-2.json
│   └── latest-session.json          ← Current session (auto-updated)
├── skills/
│   └── session-tracker/             ← NEW skill
│       ├── SKILL.md
│       └── tracker.py
```

---

## Session JSON Structure

```json
{
  "session_id": "2025-03-07-session-1",
  "start_time": "2025-03-07T10:30:00",
  "last_update": "2025-03-07T14:22:00",
  "status": "active",
  "project": "pickleballbn",
  "branch": "claude/issue-7-demo-fixes",
  "tasks": [
    {"id": "1", "desc": "Fix BottomNav clipping", "status": "completed"},
    {"id": "2", "desc": "Test on preview", "status": "in_progress"}
  ],
  "context": {
    "last_action": "Updated BottomNav.tsx line 45",
    "next_step": "Test preview URL",
    "blockers": [],
    "notes": "User mentioned glassmorphism needs consistency"
  },
  "snapshots": [
    {"time": "10:30", "action": "Session started"},
    {"time": "11:15", "action": "Fixed BottomNav"},
    {"time": "14:22", "action": "Ready for testing"}
  ]
}
```

---

## Commands

| Command | What It Does |
|---------|--------------|
| `/sessions` | List recent sessions |
| `/session current` | Show current session details |
| `/session recover` | Restore last session after crash |
| `/session save` | Manual snapshot |

---

## Session List Output

```
Recent Sessions:

ID                  Start      Status    Project       Branch
2025-03-07-s3       14:00     active    pickleballbn  claude/issue-7
2025-03-07-s2       10:30     ended     pickleballbn  main
2025-03-06-s5       16:45     ended     pickleballbn  claude/issue-5

Last active: 2025-03-07-s3
Working on: BottomNav fixes
Next: Test on preview
```

---

## Recovery After Crash

```
┌─────────────────────────────────────────────────────────────┐
│                    CRASH RECOVERY FLOW                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Computer crashes                                        │
│     ↓                                                       │
│  2. User starts new session                                 │
│     ↓                                                       │
│  3. Claude detects: latest-session.json exists              │
│     ↓                                                       │
│  4. Claude: "I see you had an active session. Recover?"    │
│     ↓                                                       │
│  5. User: "Yes"                                             │
│     ↓                                                       │
│  6. Claude loads:                                           │
│     - What you were working on                              │
│     - Last action taken                                    │
│     - Next steps                                           │
│     - Current branch                                       │
│     - Uncommitted changes                                  │
│     ↓                                                       │
│  7. Continue from where you left off ✅                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Integration with Existing Systems

```
┌─────────────────────────────────────────────────────────────┐
│                 MEMORY SYSTEM INTEGRATION                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Session Tracker ─────┐                                     │
│  (current work)        │                                     │
│                        ├──→ Saves to activeContext.md      │
│  Skills                │    (manual trigger)              │
│  (rules) ──────────────┘                                     │
│                        │                                     │
│  Supabase KB ───────────┘    (periodic sync)               │
│  (infrastructure)                                            │
│                                                             │
│  On crash:                                                  │
│  1. Session Tracker: "You were working on X"               │
│  2. Skills: "Remember to use className"                   │
│  3. Supabase KB: "DEV DB is luhetbx..."                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Auto-Save Triggers

Session state auto-saves when:
- ⏱️ Every 15 minutes
- 📝 After each task completion
- 💬 When user says "save", "checkpoint", "pause"
- 🔀 Before branch switch
- 📤 Before git push

---

## Quick Commands Implementation

```bash
# List sessions
alias sessions="cat ~/.claude/.session-log/sessions.json | jq -r '.[] | [.id, .start, .status, .project] | @tsv'"

# Show current session
alias current-session="cat ~/.claude/.session-log/latest-session.json | jq '.'"

# Recover last session
alias recover-session="cat ~/.claude/.session-log/latest-session.json"
```

---

## Example Session Recovery Dialogue

```
User: (starts new session after crash)

Claude: I detected you had an active session that may have
        crashed. Here's what I found:

        Session: 2025-03-07-s3
        Project: PickleballBN
        Branch: claude/issue-7-demo-fixes
        Last action: Updated BottomNav.tsx line 45
        Next step: Test on preview URL
        Tasks completed: 1 of 2

        Would you like to:
        1. Resume this session
        2. Start fresh
        3. View full details

User: 1

Claude: Resuming session...
        - Branch: claude/issue-7-demo-fixes
        - Completed: BottomNav clipping fix
        - In progress: Testing preview

        Ready to continue. Test preview now?
```

---

## File Locations

```
~/.claude/.session-log/
├── sessions.json              ← Master list
├── latest-session.json         ← Current (auto-updated)
├── archive/                   ← Past sessions
│   ├── 2025-03/
│   └── 2025-02/
└── .session-index             ← Quick lookup
```

---

## Summary

| Before | After |
|--------|-------|
| Crash = all context lost | Crash = recover from latest snapshot |
| "What was I working on?" | `/sessions` shows recent work |
| Manual memory only | Auto-save every 15 min |
| No session history | Full session log |
| Can't resume after crash | `/session recover` restores all |

**Yes, you'll be able to list sessions and recover after crashes.**
