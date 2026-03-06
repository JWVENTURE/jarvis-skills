# Linting Workflow - Prevent Bad Code

**Goal:** Never commit broken code. Lint first, commit second.

---

## The Problem

```
❌ WRONG FLOW:
Write code → Commit → Push → CI fails → Fix → Commit again

Time wasted:
- Waiting for CI
- Fixing errors found by CI
- Multiple commits for same fix
- Breaking main for others
```

---

## The Solution

```
✅ RIGHT FLOW:
Write code → Run lint → Fix errors → Commit → Push → CI passes

Benefits:
- Fast feedback (30 sec vs 5 min)
- CI becomes safety net, not gatekeeper
- Clean commits
- No broken code in main
```

---

## Commands

### Before EVERY Commit

```bash
cd src/magicpatterns
npm run lint          # Check for issues
npm run build         # Verify build works
git commit            # Only if both pass
```

### What Each Command Does

| Command | What It Checks | Time |
|---------|---------------|------|
| `npm run lint` | Code quality, syntax, unused vars, patterns | ~30 sec |
| `npm run build` | Code actually compiles | ~10 sec |
| `git commit` | Save changes | Instant |

---

## Linting Rules (What Gets Caught)

| Category | Example |
|----------|---------|
| **Syntax** | Missing brackets, typos |
| **Unused** | `const x = 5` but never used |
| **Imports** | Importing files that don't exist |
| **Types** | Wrong type for variable |
| **Patterns** | Anti-patterns in code |

---

## When to Run Lint

| Situation | Run Lint? |
|-----------|-----------|
| Before commit | ✅ YES (mandatory) |
| Before push | ✅ YES |
| After fixing bug | ✅ YES |
| Just saving file | ❌ No (waste of time) |
| Experimenting | ❌ No (not committing) |

---

## Common Lint Errors

```
❌ 'x' is assigned a value but never used
   Fix: Remove unused variable or use it

❌ Missing semicolon
   Fix: Add semicolon

❌ Import '../../file' does not exist
   Fix: Fix path or remove import

❌ Type 'string' is not assignable to type 'number'
   Fix: Use correct type
```

---

## VS Code Integration (Optional)

Install ESLint extension for real-time feedback:

```json
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "eslint.validate": ["javascript", "typescript"]
}
```

This shows errors as you type, before you even run lint.

---

## CI is Safety Net, Not First Line

```
┌─────────────────────────────────────────────────────────────┐
│                    DEFENSE IN DEPTH                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. VS Code ESLint → Real-time errors (instant)             │
│  2. npm run lint → Before commit (30 sec)                   │
│  3. CI Lint → On push (5 min)                               │
│                                                             │
│  Best case: Catch at #1 (instant fix)                       │
│  Good case: Catch at #2 (quick fix)                         │
│  Safety net: Catch at #3 (doesn't block others)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Rule:** If CI fails, you failed at steps 1 and 2. That's embarrassing.

---

## Quick Reference Card

```
┌──────────────────────────────────────┐
│   BEFORE COMMITTING CODE             │
├──────────────────────────────────────┤
│                                      │
│   cd src/magicpatterns               │
│   npm run lint      ← MUST PASS      │
│   npm run build     ← MUST PASS      │
│   git commit                       │
│                                      │
│   If lint fails:                    │
│   → Fix errors                      │
│   → Run lint again                  │
│   → Only commit when passes         │
│                                      │
└──────────────────────────────────────┘
```

---

## Why Bother?

| Scenario | Without Lint | With Lint |
|----------|--------------|-----------|
| Typos in code | CI fails, everyone blocked | Caught in 30 sec |
| Unused imports | Bloated code | Removed automatically |
| Wrong types | Runtime crashes | Caught before run |
| Bad patterns | Tech debt accumulates | Enforced good practices |

---

## Summary

| Step | Command | Pass Required? |
|------|---------|----------------|
| 1 | `npm run lint` | ✅ YES |
| 2 | `npm run build` | ✅ YES |
| 3 | `git commit` | Only after 1 & 2 pass |

**Don't skip lint. It saves time, not wastes it.**
