# JARVIS Memory System - All 3 Layers Working Together

**You already have 3 memory systems. The reflect skill adds a 4th layer. They work TOGETHER.**

---

## Current Memory Systems

| System | Location | Purpose | Update Method |
|--------|----------|---------|---------------|
| **Memory Bank** | `.memory-bank/pickleballbn/` | Deep context, session history | Manual / session wrap |
| **Supabase KB** | `jarvis_knowledge` table | Runtime lookup for all agents | GitHub Action sync |
| **Skills (NEW)** | `~/.claude/skills/` | Behavioral rules, patterns | Auto-learn via /reflect |
| **CLAUDE.md** | Project root | Project instructions | Manual updates |

---

## What Each System Does

### 1. Memory Bank (The "What")
**Files:** `activeContext.md`, `systemPatterns.md`, etc.

```
What it stores:
- What we're working on (current sprint)
- What happened (session history)
- What we decided (decisions log)
- What failed (lessons learned)

Example:
"2026-03-01: Fixed duplicate slug bug in VenueManagementPanel"
"2026-02-28: Laptop crash, recovered from commit f8de8f3e"
```

### 2. Supabase Knowledge Base (The "Where")
**Table:** `jarvis_knowledge`

```
What it stores:
- Infrastructure info (Supabase URLs, Cloudflare config)
- Credentials locations (where to find keys)
- Protocol instructions (how to greet, what to check first)

Example:
"DEV Project ID: luhetbxmnfxylgkrvagh"
"Session start: Greet 'Assalamualaikum sir', check activeContext.md"
```

### 3. Skills (The "How") ← NEW!
**Files:** `pickleballbn/SKILL.md`, `reflect/SKILL.md`

```
What it stores:
- How to code (use className not style)
- What NOT to use (no Xano, no Flutter)
- Client preferences (Chia hates popups)
- Workflow rules (branch naming, lint before commit)

Example:
"❌ Xano - deprecated, use Supabase"
"Always run npm run lint before commit"
```

### 4. CLAUDE.md (The "Rules")
**File:** `CLAUDE.md` in project root

```
What it stores:
- Project-level instructions
- Critical workflows
- Git rules

Example:
"NEVER merge to master without explicit approval"
"Branch MUST be claude/issue-* or claude/review-*"
```

---

## How They Work Together

```
┌─────────────────────────────────────────────────────────────┐
│                    SESSION STARTUP                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Read CLAUDE.md                  ← Project rules        │
│  2. Read activeContext.md            ← What we're doing    │
│  3. Query jarvis_knowledge           ← Infrastructure      │
│  4. Load skills/                     ← How to code         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│                    DURING SESSION                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User: "Never use Xano!"                                    │
│     ↓                                                       │
│  Claude fixes code                                          │
│     ↓                                                       │
│  /reflect triggers                                          │
│     ↓                                                       │
│  Updates skills/pickleballbn/SKILL.md                       │
│     ↓                                                       │
│  [Session ends]                                             │
│     ↓                                                       │
│  Update activeContext.md (Memory Bank)                      │
│     ↓                                                       │
│  Git commits both                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│                    NEXT SESSION                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Skills already knows: No Xano! ✅                          │
│  Memory Bank shows: We fixed it on March 7                 │
│  KB provides: Supabase URLs                                 │
│  CLAUDE.md enforces: Branch naming rules                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Integration Flow

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│   PROJECT REPO                SKILLS REPO                   │
│   (uniplay-development)       (~/.claude/skills)             │
│                                                              │
│   ┌─────────────────┐         ┌─────────────────┐           │
│   │ CLAUDE.md       │         │ pickleballbn/   │           │
│   │ Memory Bank/    │ ←-sync→ │ SKILL.md        │           │
│   │ activeContext   │         │ reflect/        │           │
│   └─────────────────┘         └─────────────────┘           │
│            ↓                           ↓                     │
│            │ GitHub Action              │ Git push          │
│            ↓                           ↓                     │
│   ┌─────────────────┐         ┌─────────────────┐           │
│   │ Supabase        │         │ GitHub          │           │
│   │ jarvis_knowledge│         │ jarvis-skills   │           │
│   └─────────────────┘         └─────────────────┘           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## What Goes Where?

| Type | Store In | Example |
|------|----------|---------|
| **Protocol** | CLAUDE.md | "Session start: greet, check context" |
| **Infrastructure** | Supabase KB | "DEV URL: luhetbx... Supabase" |
| **Session History** | Memory Bank | "Fixed slug bug March 7" |
| **Code Rule** | Skills | "Use className not style" |
| **Client Pref** | Skills | "Chia prefers minimal UI" |
| **Decision** | Memory Bank | "Chose React Native over Flutter" |
| **Deprecated Tech** | Skills | "❌ Xano - use Supabase" |
| **Credential Location** | Supabase KB | "Keys in gcloud secrets" |

---

## Enhanced Wrap Protocol

When ending session, update ALL systems:

```bash
# 1. Run reflect (updates skills)
/reflect

# 2. Update activeContext (memory bank)
# Edit .memory-bank/pickleballbn/activeContext.md

# 3. Commit everything
git add .
git commit -m "session: [summary]"

# 4. Push skills (separate repo)
cd ~/.claude/skills && git push

# 5. Sync to Supabase KB (automatic via GitHub Action)
# Happens when you push to uniplay-development
```

---

## Quick Reference: Update What?

| Situation | Update |
|-----------|--------|
| Fixed a bug | Memory Bank (activeContext.md) |
| User corrected a mistake | Skills (via /reflect) |
| New infrastructure deployed | Supabase KB (add entry) |
| New protocol established | CLAUDE.md |
| Client preference | Skills (pickleballbn/SKILL.md) |
| Decision made | Memory Bank (decisionLog.md) |

---

## The Key Difference

| System | Lifetime | Scope | Update Method |
|--------|----------|-------|---------------|
| **Memory Bank** | Per project | Deep context | Manual |
| **Supabase KB** | Forever | Infrastructure | Manual / GitHub Action |
| **Skills** | Forever | Behavioral rules | **Auto (/reflect)** |
| **CLAUDE.md** | Per project | Project rules | Manual |

**The reflect skill is the ONLY auto-learning system.** It captures corrections that would otherwise be lost.

---

## Example: Complete Memory Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     SESSION SCENARIO                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User: "Why did you use Xano? I told you, Supabase only!"   │
│                                                             │
│  Claude: "Sorry, fixing..."                                 │
│          → Changes code from Xano to Supabase               │
│                                                             │
│  [/reflect triggered]                                       │
│  → Updates skills/pickleballbn/SKILL.md:                    │
│    "❌ Xano - deprecated, use Supabase"                      │
│  → Commits to skills repo                                   │
│                                                             │
│  [Session wrap]                                             │
│  → Updates Memory Bank activeContext.md:                    │
│    "2026-03-07: User corrected Xano usage, fixed"           │
│  → Commits to project repo                                  │
│                                                             │
│  [GitHub Action runs]                                       │
│  → Syncs Memory Bank to Supabase KB                         │
│                                                             │
│  [Next session]                                             │
│  → Skills: "No Xano!" ✅                                    │
│  → Memory Bank: "We had this issue on March 7" ✅           │
│  → Supabase KB: "Project URLs available" ✅                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary

**Your current systems are GREAT. The reflect skill fills ONE gap:**

| Gap | Before | After |
|-----|--------|-------|
| Corrections lost when branch deleted | ❌ | ✅ Skills remember |
| Same mistake across branches | ❌ | ✅ Skills prevent it |
| "I told you yesterday" | ❌ | ✅ Skills learned once |
| Manual update of rules only | ❌ | ✅ Auto-learn via /reflect |

**Everything else stays the same.** Memory Bank, Supabase KB, CLAUDE.md all work as before. Skills just add auto-learning for behavioral rules.
