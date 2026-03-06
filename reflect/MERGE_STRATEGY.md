# The 100+ Feature Branches Problem

**Your current issue:** Fixes stuck in branches, never merged to main.

---

## The Problem

```
┌─────────────────────────────────────────────────────────────┐
│                 CURRENT BROKEN FLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  claude/issue-1  ─┐                                          │
│  claude/issue-2  ─┤                                          │
│  claude/issue-3  ─┤                                          │
│  ...            ─┼──→ All deployed to preview (DEV)         │
│  claude/issue-99 ─┤     BUT NOT MERGED!                     │
│  claude/issue-100─┘                                          │
│                                                             │
│  main branch ← STALE, missing all fixes                     │
│                                                             │
│  Result:                                                    │
│  - 100+ branches with unmerged code                         │
│  - Can't test fixes together                                │
│  - main doesn't have the "good" code                        │
│  - Each fix is isolated                                     │
│  - Merge conflicts will be NIGHTMARE                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Why This Happens

1. **No merge cadence** - "I'll merge later" becomes "never merge"
2. **Fear of breaking main** - Want everything perfect before merging
3. **Feature branch addiction** - Every fix = new branch
4. **No integration testing** - Each fix tested in isolation

---

## Solution: Regular Merge Cadence

```
┌─────────────────────────────────────────────────────────────┐
│                    HEALTHY FLOW                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  claude/issue-1  ──┐                                        │
│  claude/issue-2  ──┤                                        │
│  claude/issue-3  ──┼──→ Merge to main DAILY                │
│                     │   → Test on preview                  │
│                     │   → Fixes integrated together         │
│                     │   → Delete merged branches            │
│                                                             │
│  Result:                                                    │
│  ✅ main has all the latest fixes                           │
│  ✅ Fixes tested together                                   │
│  ✅ No merge conflicts (small, frequent merges)             │
│  ✅ Clean branch list                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Recommended Workflow

### Option 1: Daily Merge (Recommended)

```bash
# At end of each work day:
git checkout main
git pull origin main

# Merge all completed issue branches
for branch in claude/issue-*; do
  git merge origin/$branch
done

# Push to main
git push origin main

# Delete merged branches
git branch -d claude/issue-*

# Clean remote branches
git push origin --delete claude/issue-*
```

### Option 2: Per-Issue Merge (Safest)

```
Complete fix → Test preview → Merge to main immediately → Delete branch
```

**Rule:** Don't start next fix until current fix is merged.

### Option 3: Weekly Integration Batch

```
Monday-Friday: Work on fixes in branches
Saturday: Merge all completed fixes to main
Sunday: Delete merged branches, start fresh Monday
```

---

## The "Fix Stuck in Preview" Recovery Plan

If you already have 100+ branches:

```bash
# Step 1: Create integration branch
git checkout main
git checkout -b integration/batch-march-2026

# Step 2: Merge all issue branches
for branch in $(git branch -r | grep "claude/issue-"); do
  git merge ${branch#origin/} || echo "Conflict: $branch"
done

# Step 3: Fix conflicts (one time instead of 100 times)
# Resolve all conflicts in this batch

# Step 4: Test integration branch preview
git push origin integration/batch-march-2026

# Step 5: If tests pass, merge to main
git checkout main
git merge integration/batch-march-2026
git push origin main

# Step 6: Clean up
git branch -d claude/issue-*
git push origin --delete claude/issue-*
```

---

## Quick Commands

### See all branches that need merging
```bash
git branch -r | grep "claude/issue-" | wc -l
```

### See what's in a branch but not in main
```bash
git log main..origin/claude/issue-XXX --oneline
```

### Merge multiple branches at once
```bash
git checkout main
git merge origin/claude/issue-1 \
  origin/claude/issue-2 \
  origin/claude/issue-3
```

### Delete all merged branches
```bash
git branch -d $(git branch --merged | grep "claude/issue-")
```

---

## Rule to Add to Skills

Add to `pickleballbn/SKILL.md`:

```markdown
## 🔄 MERGE CADENCE (CRITICAL)

**Rule: Merge to main DAILY, not never.**

| Frequency | What |
|-----------|------|
| **Daily** | Merge completed fixes to main |
| **Per fix** | Merge immediately after testing |
| **Never** | Don't let fixes pile up in branches |

**After merge:**
1. Test on preview (main branch deployment)
2. Delete merged branches
3. Start fresh

**Don't let 100+ branches accumulate!**
```

---

## The Key Insight

| Wrong Thinking | Right Thinking |
|----------------|----------------|
| "I'll merge when everything is perfect" | "Merge small, merge often" |
| "This branch might break main" | "Test on preview, then merge" |
| "I need all 100 fixes before merging" | "Merge as you go, integrate continuously" |
| "Branches are safe keeping places" | "Unmerged branches are technical debt" |

---

## Summary

| Problem | Solution |
|---------|----------|
| Fixes stuck in 100+ branches | Merge to main DAILY |
| Can't test fixes together | Integration branch or frequent merges |
| Merge conflicts will be nightmare | Small, frequent merges = easy conflicts |
| main is stale | Keep main fresh with constant merges |

**Merging is not a "final step". It's a DAILY habit.**
