# Persistent Learning Setup for JARVIS

**Problem:** Fixes get forgotten when branches merge and get deleted.
**Solution:** Skills live outside project repo, learnings persist forever.

---

## Architecture

```
Project Repo (uniplay-development)          Skills Repo (separate)
├── .git/                                 ├── .git/
├── src/                                  ├── pickleballbn/
├── Branch A (deleted)                    │   └── SKILL.md  ← Lives here!
├── Branch B (deleted)                    ├── reflect/
└── Branch C (active)                      └── tech-stack/
                                               ↑
                            Learnings saved HERE, not in project
```

---

## Two Repos Strategy

### 1. Project Repo (Temporary)
- Contains: Code, features, fixes
- Lifetime: Branch → Merge → Delete
- Purpose: Ship features

### 2. Skills Repo (Permanent)
- Contains: Learnings, rules, patterns
- Lifetime: Forever
- Purpose: Remember everything

---

## Git Setup for Skills

```bash
# Create a separate GitHub repo for skills
cd ~/.claude/skills
git init
git add .
git commit -m "Initial JARVIS skills"

# Connect to GitHub
gh repo create jarvis-skills --private --source=.
git push -u origin main
```

---

## Session Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKING SESSION                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Start feature branch                                    │
│  2. Fix issue / add feature                                 │
│  3. User corrects: "Never do X, always do Y"               │
│  4. Run /reflect                                           │
│  5. Review proposed changes                                 │
│  6. Approve → Updates skills repo                           │
│  7. Push skills (separate from project)                    │
│  8. Continue working                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Sync Skills Across Machines

If you work on multiple machines:

```bash
# On machine A (after learning)
cd ~/.claude/skills
git push

# On machine B (before starting work)
cd ~/.claude/skills
git pull

# Now Machine B knows what Machine A learned!
```

---

## Auto-Sync on Session Start

Add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "shell",
        "command": "git -C ~/.claude/skills pull --quiet"
      }
    ]
  }
}
```

---

## Auto-Sync on Session End

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "type": "shell",
        "command": "reflect-sync"  # Runs reflect + git push
      }
    ]
  }
}
```

Script for `reflect-sync`:
```bash
#!/bin/bash
# Run reflect to learn from session
claude reflect

# Push to GitHub if changes made
cd ~/.claude/skills
if [ -n "$(git status --porcelain)" ]; then
  git add .
  git commit -m "learn: $(date '+%Y-%m-%d %H:%M')"
  git push
fi
```

---

## Benefits

| Problem | Solution |
|---------|----------|
| "I fixed this last month!" | Skills remember forever |
| "Different machine forgot" | Sync via GitHub |
| "Other agent doesn't know" | Shared skills repo |
| "Can't find that fix in git log" | Skills are organized |

---

## Skills vs Codebase: What Goes Where?

| Type | Store In | Example |
|------|----------|---------|
| **Fix** | Project repo | Bug fix in component |
| **Rule** | Skills repo | "Never use Xano" |
| **Feature** | Project repo | New booking screen |
| **Pattern** | Skills repo | "Always lint before commit" |
| **Config** | Project repo | .env files |
| **Preference** | Skills repo | "Chia prefers minimal UI" |

---

## Quick Start Commands

```bash
# Check skills status
reflect-status

# Enable auto-learning
reflect-on

# Sync skills to GitHub
cd ~/.claude/skills && git push

# Pull latest skills from GitHub
cd ~/.claude/skills && git pull
```
