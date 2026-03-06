# JARVIS Reflect Skill - Self-Improving Memory

**"Correct once, learn forever."**

---

## What It Does

JARVIS analyzes each conversation for corrections and patterns, then updates skill files automatically.

| Problem | Solution |
|---------|----------|
| "I just told you this yesterday!" | Skills persist across sessions |
| Repeating the same corrections | Learn from each correction |
| Forgetting preferences | Client choices remembered forever |
| Inconsistent code style | Style rules enforced automatically |

---

## Quick Start

### Check Status
```bash
reflect-status
```

### Enable Auto-Learning
```bash
reflect-on
```

### Disable Auto-Learning
```bash
reflect-off
```

---

## Files Created

```
~/.claude/skills/
├── reflect/
│   ├── SKILL.md           # Main skill definition
│   ├── reflect.sh         # Session end hook (Linux/Mac)
│   ├── reflect-toggle.ps1 # Toggle script (Windows)
│   ├── reflect-on.bat     # Enable auto-learning
│   ├── reflect-off.bat    # Disable auto-learning
│   ├── reflect-status.bat # Check status
│   └── README.md          # This file
└── pickleballbn/
    └── SKILL.md           # PickleballBN project rules (auto-updated)
```

---

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    SESSION FLOW                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. User: "Never use Xano again, only Supabase"            │
│     ↓                                                       │
│  2. Claude fixes the code                                   │
│     ↓                                                       │
│  3. [Session ends]                                          │
│     ↓                                                       │
│  4. Reflect detects correction signal                      │
│     ↓                                                       │
│  5. Updates pickleballbn SKILL.md:                         │
│     "❌ Xano - deprecated, use Supabase"                    │
│     ↓                                                       │
│  6. Git commits: "feat(learn): Deprecate Xano"             │
│     ↓                                                       │
│  7. Next session: Already knows!                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Learning Signals

| Signal | Confidence | Example |
|--------|------------|---------|
| **never** | HIGH | "Never use style={}" |
| **always** | HIGH | "Always run lint first" |
| **don't** | HIGH | "Don't forget to test" |
| **prefer** | MEDIUM | "I prefer minimal UI" |
| **remember** | MEDIUM | "Remember Chia hates popups" |
| **good job** | LOW | Success pattern |

---

## Example: What Gets Learned

**Conversation:**
```
User: "Why did you use the old colors? Use #002c72 not #1F5070"
Claude: "Sorry, fixing..."
```

**Skill Updated:**
```markdown
## ❌ OLD WRONG COLORS (Never Use)
- ~~#1F5070~~ (old navy) - Use #002c72 instead
```

**Git Commit:**
```
feat(learn): Enforce correct Midnight Blue color

Signal: "Why did you use the old colors"
Old: #1F5070 → New: #002c72
Confidence: HIGH
```

---

## Skills That Auto-Learn

| Skill | What It Learns |
|-------|----------------|
| `pickleballbn` | Project rules, Chia's preferences, brand colors |
| `tech-stack` | Supabase only, React Native, no Xano |
| `code-style` | className not style, linting rules |
| `workflow` | Branch naming, commit messages, PR flow |

---

## Viewing Learned History

```bash
# See what was learned
cat ~/.claude/.reflect.log

# See git history of learnings
cd ~/.claude/skills
git log --oneline
```

---

## Manual Learning (Without Auto Mode)

If auto-learning is disabled, use the `/reflect` command at the end of a session:

```
/reflect
```

This will:
1. Scan the conversation
2. Show detected signals
3. Ask for confirmation
4. Update skills
5. Commit to git

---

## Safety Features

| Feature | Protection |
|---------|------------|
| **Never delete** | Only adds/modifies, never removes rules |
| **Git rollback** | Revert commit if learning is wrong |
| **Review first** | Shows changes before applying |
| **Low confidence** | Logs for review instead of auto-applying |

---

## Setup Session End Hook (Optional)

For fully automatic learning, add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStop": [
      {
        "type": "shell",
        "command": "reflect-auto"
      }
    ]
  }
}
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Not learning | Run `reflect-on` to enable |
| Learning wrong things | Check `~/.claude/.reflect.log` and revert git commit |
| Skills not found | Check `~/.claude/skills/` directory exists |

---

## Inspiration

Based on: https://www.youtube.com/watch?v=-4nUCaMNBR8

**Video:** "Self-Improving Skills in Claude Code" by Developers Digest

---

## Version History

| Date | Change |
|------|--------|
| 2025-03-07 | Initial setup for JARVIS / PickleballBN |
