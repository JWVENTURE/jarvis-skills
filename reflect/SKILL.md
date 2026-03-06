---
name: reflect
description: Auto-learn from session corrections. Scans conversation for patterns like "never do X", "always do Y", updates skill files and commits to Git. Use keyword: reflect, learn, update skill
user-invocable: true
---

# JARVIS Reflex Skill - Self-Improving Memory

**Goal:** Correct once, learn forever. Every session makes JARVIS smarter.

---

## How It Works

1. **Scan Conversation** - Look for correction patterns
2. **Classify by Confidence** - High/Medium/Low signals
3. **Update Skills** - Apply learnings to relevant skill files
4. **Git Commit** - Version control every learning

---

## Correction Patterns to Detect

| Pattern | Example | Confidence |
|---------|---------|------------|
| **Never do X** | "Never use Xano anymore" | HIGH |
| **Always do Y** | "Always use Supabase for backend" | HIGH |
| **Don't forget** | "Don't forget to run lint before commit" | HIGH |
| **I prefer** | "I prefer className over style" | MEDIUM |
| **Remember** | "Remember Chia doesn't like popups" | MEDIUM |
| **Next time** | "Next time, add more padding" | MEDIUM |
| **Good job on** | "Good job on the glassmorphism" | LOW (success pattern) |

---

## Confidence Levels

### HIGH (Apply Immediately)
- Explicit prohibitions ("never", "don't", "stop")
- Explicit requirements ("must", "always", "required")
- Direct corrections from user

### MEDIUM (Review Before Apply)
- Preferences ("I prefer", "I like")
- Suggestions ("should", "could", "better")
- Style choices

### LOW (Log for Review)
- Observations
- Success patterns to reinforce
- Ideas for future sessions

---

## Skill Update Flow

```
1. Detect signals in conversation
   ↓
2. Match to relevant skill files
   ↓
3. Propose changes (with natural language)
   ↓
4. User approval (Y / modify / skip)
   ↓
5. Update skill file
   ↓
6. Git commit with learning message
   ↓
7. Push to GitHub (optional)
```

---

## Example Learning Session

**Conversation:**
```
User: "Why did you use Xano again? I told you we only use Supabase!"
Claude: "Sorry, let me fix that..."
```

**Reflex Extracts:**
- Signal: "Never use Xano, only Supabase"
- Confidence: HIGH
- Target Skill: `pickleballbn` or `tech-stack`

**Skill File Updated:**
```markdown
## Deprecated Technologies
- ❌ Xano - replaced by Supabase
- ❌ Stripe - not available in Brunei
```

**Git Commit:**
```
feat(learn): Deprecate Xano, enforce Supabase-only backend

Session: 2025-03-07-reflex-setup
Signal: User correction "Why did you use Xano again"
Confidence: HIGH
```

---

## Target Skills for PickleballBN

| Skill | What It Learns |
|-------|----------------|
| `pickleballbn` | Project-specific rules, Chia's preferences |
| `tech-stack` | Approved/deprecated technologies |
| `code-style` | Naming, formatting, linting rules |
| `branding` | Colors, fonts, logo usage |
| `workflow` | Branch naming, commit patterns, PR flow |

---

## Manual Trigger

```
/reflect
```

Or with specific skill:
```
/reflect pickleballbn
```

---

## Automatic Mode (Session End Hook)

In `~/.claude/settings.json`:
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

## Toggle Commands

| Command | Action |
|---------|--------|
| `reflect on` | Enable auto-learning on session end |
| `reflect off` | Disable auto-learning |
| `reflect status` | Show current mode |

---

## Git Integration

All learnings are committed to:
```
~/.claude/skills/ (private) or
https://github.com/JWVENTURE/jarvis-skills (shared)
```

**Commit Message Format:**
```
feat(learn): [Brief learning summary]

Session: [session-id]
Signal: [what user said]
Confidence: HIGH/MEDIUM/LOW
Target: [skill-name]
```

---

## Safety Rules

1. **NEVER delete existing rules** - only add or modify
2. **Preserve formatting** - maintain markdown structure
3. **Ask before HIGH confidence changes** - show diff first
4. **Log LOW confidence** - add to "Review Later" section
5. **Git rollback** - if learning breaks something, revert commit

---

## Review Later Section

At bottom of each skill file:
```markdown
---

## Pending Review (Low Confidence Signals)

- [ ] Observation from [date]: [note]
- [ ] Suggestion from [date]: [note]
```

---

## Example Skill File Structure

```markdown
---
name: pickleballbn
description: PickleballBN project rules, client preferences, brand guidelines
---

# PickleballBN Project Rules

## Tech Stack (LOCKED)
- Backend: Supabase ONLY
- Frontend: React Native + Expo
- Styling: NativeWind className= (NEVER style={})

## Brand Colors (NON-NEGOTIABLE)
- Midnight Blue: #002c72
- Chartreuse: #dfff03
- Cyan: #01f9fb

## Client Preferences
- Chia prefers minimal popups
- "Professional" not "cute" design
- Mobile-first UI

## Deprecated (NEVER USE)
- ❌ Xano
- ❌ Flutter
- ❌ Stripe
- ❌ Old colors (#1F5070, #C7F61E, #3DC7E3)

---

## Pending Review

- [ ] 2025-03-07: User mentioned wanting dark mode toggle (LOW)
```

---

## Commands for Shell Scripts

**reflect** (manual):
```bash
claude mcp clay apply "Reflect on this conversation and update skills"
```

**reflect-on** (enable auto):
```bash
echo "reflect" > ~/.claude/.reflect-mode
```

**reflect-off** (disable auto):
```bash
rm -f ~/.claude/.reflect-mode
```

**reflect-status**:
```bash
if [ -f ~/.claude/.reflect-mode ]; then
  echo "Reflect: AUTO (enabled)"
else
  echo "Reflect: MANUAL (disabled)"
fi
```
