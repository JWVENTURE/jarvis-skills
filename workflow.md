---
name: workflow
description: Git workflow, branch naming, worktree rules, Cloudflare deployment
---

# Workflow Rules - PickleballBN

## Worktree Usage (LOCKED)
- ✅ Use `EnterWorktree` tool ONLY
- ❌ NEVER use raw `git worktree add`
- **Reason:** Status line visibility for user

## Cloudflare Auto-Build Requirements (CRITICAL)
Cloudflare Pages **ONLY** auto-builds branches matching:
```
claude/issue-[number]-[description]    ✅ AUTO-BUILDS
claude/review-[description]            ✅ AUTO-BUILDS
feature/anything                       ❌ SKIPPED
```

**Worktree naming follows branch naming** - when using `EnterWorktree`, the branch is created with the worktree name. Must use `claude/issue-*` or `claude/review-*` prefix.

Session ID suffixes OK: `claude/issue-49-design-I4AZt` ✅

⚠️ **If session assigns wrong branch name**: Flag to user BEFORE pushing implementation code. Do NOT silently push to wrongly named branch.

## Git Workflow
1. Development happens on `claude/issue-*` branches
2. Push triggers Cloudflare preview build
3. Test on preview URL
4. Post "ship it" on GitHub Issue
5. GitHub Actions handles merge to main/master

## Commit Messages
```
feat: Add [feature] for [component]
fix: Resolve [issue] in [component] (closes #XX)
docs: Update [document]
```

## Pre-Commit Checklist
- `npm run lint` - Must pass
- `npm run build` - Must pass
- No console.log left in production code
- No unused imports (TypeScript strict mode)

## Deployment Targets (IMPORTANT)
| Branch | Deployment | When to Update |
|--------|-----------|----------------|
| `main` | `pickleballbn-dev.pages.dev` | DEV environment - PRIMARY for testing |
| `master` | `pickleballbn.pages.dev` | PROD environment - LIVE site |
| `claude/issue-*` | Preview URLs | Temporary testing only |

**Key:** When user says "main is outdated", they mean the DEV deployment (`pickleballbn-dev.pages.dev`) needs updating. Preview builds are temporary; MAIN is the persistent DEV environment users actually test on.

## Post-Merge Workflow
After merging PR to `main`:
1. ✅ **Return to feature branch** - Stay on `claude/issue-*` to continue work
2. ✅ Update local `main` via `git pull`
3. ✅ Cloudflare auto-builds `pickleballbn-dev.pages.dev`
4. ❌ DON'T switch to `main` and work there

## User Feedback Patterns

### "Missing X" or "X doesn't have Y"
**Why:** User reports incomplete data - think COMPREHENSIVELY
**How to apply:** When user says "billing info missing", they mean ALL billing-related fields (names, address, etc.), not just what was initially mentioned. Think holistically about what data should be present.
**Source:** Session 2026-04-08, user said "the profile account also dont have the billing info"

### "When does X happen?" / "Where does Y occur?"
**Why:** User values precise understanding of flow timing and location
**How to apply:** Be specific about WHEN (pre-payment vs post-payment) and WHERE (email link vs redirect URL) things happen. Ambiguity here wastes time.
**Source:** Session 2026-04-08, user asked "so when i enter as guest, when is the detection whether i am a membber or not?"

### "Main is outdated" / "Preview is updated but..."
**Why:** User wants MAIN dev deployment updated, not just preview
**How to apply:** When working on features, remember to merge to `main` for DEV deployment. Preview builds are for temporary testing only.
**Source:** Session 2026-04-08, user said "preview is updated, the main is still outdated"

---

## Pending Review
