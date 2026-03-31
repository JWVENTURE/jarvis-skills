---
name: workflow
description: JARVS workflow protocols - image analysis, planning, multi-agent execution, testing before deployment. Keywords: workflow, plan, execute, test, deploy, preview, smoke
user-invocable: true
---

# JARVIS Workflow Protocols

**Core Principles:** Analyze first, plan thoroughly, execute intelligently, test before deploy.

---

## 🔍 RULE 1: Always Check Images Using Built-in Z.AI

**MANDATORY:** When user attaches an image, ALWAYS analyze it FIRST using vision tools.

### Built-in Vision Tool (z.ai GLM Vision)

```
Tool: mcp__glm-zai-vision__analyze_image
Use: Image URL or local file
Purpose: Analyze screenshots, UI, code screenshots, errors
```

### Image Verification Protocol

```
┌─────────────────────────────────────────────────────────────┐
│                    WHEN USER SENDS IMAGE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. STOP everything                                       │
│     ↓                                                       │
│  2. Use mcp__glm-zai-vision__analyze_image tool            │
│     ↓                                                       │
│  3. Quote what you see in the image                       │
│     ↓                                                       │
│  4. Explain what it means                                  │
│     ↓                                                       │
│  5. ONLY THEN proceed with any action                      │
│                                                             │
│  ❌ DON'T: Assume, guess, or skip analysis                 │
│  ✅ DO: Always analyze with vision tool first              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Prompt for Image Analysis

```
"Describe in detail the layout structure, color style, main components,
and interactive elements of the website in this image to facilitate
subsequent code generation by the model. [Add your specific questions]"
```

---

## 📋 RULE 2: Always Analyze and Plan First

**Before ANY fix or enhancement:** Analyze → Plan → Execute

### Planning Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                 ANALYZE → PLAN → EXECUTE                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ANALYZE                                                │
│     • Read the code/file                                    │
│     • Understand the problem                                │
│     • Identify dependencies                                 │
│     • Check related files                                   │
│     ↓                                                       │
│  2. PLAN                                                   │
│     • Create step-by-step plan                              │
│     • Identify independent tasks                           │
│     • Identify dependent tasks                             │
│     • Estimate complexity                                   │
│     ↓                                                       │
│  3. GET APPROVAL (if complex)                              │
│     • Show plan to user                                    │
│     • Explain approach                                     │
│     • Confirm before executing                             │
│     ↓                                                       │
│  4. EXECUTE                                                │
│     • Use multi-agent system                               │
│     • Execute based on dependencies                        │
│     • Monitor progress                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### When to Plan

| Situation | Need Planning? |
|-----------|---------------|
| Simple bug fix (1-2 lines) | ⚠️ Quick plan OK |
| New feature | ✅ Full plan required |
| Refactoring | ✅ Full plan required |
| Multiple files | ✅ Full plan required |
| UI changes | ✅ Full plan required |
| Database changes | ✅ Full plan required |
| Unknown scope | ✅ Full plan required |

### Plan Template

```
## Analysis
**Issue:** [Description of problem]
**Root Cause:** [What's causing it]
**Affected Files:** [List files involved]

## Plan
**Phase 1:** [Task 1]
- [ ] Step 1.1
- [ ] Step 1.2

**Phase 2:** [Task 2] (depends on Phase 1)
- [ ] Step 2.1
- [ ] Step 2.2

**Dependencies:**
- Task 2 depends on Task 1
- Task 3 can run in parallel with Task 1

**Estimated Effort:** [Time/Complexity]
```

---

## 🤖 RULE 3: Auto-Invoke Code Review After Completing Work

**CRITICAL:** After completing ANY significant code changes, ALWAYS invoke code review BEFORE asking user to test.

### When to Auto-Invoke Review

**MANDATORY after:**
- ✅ Completing a feature implementation
- ✅ Fixing a bug or issue
- ✅ Making database changes
- ✅ Finishing multi-file changes
- ✅ Before creating PR
- ✅ Before merging to main

### Review Skills to Auto-Invoke

```
┌─────────────────────────────────────────────────────────────┐
│              AFTER COMPLETING CODE CHANGES                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. IMPLEMENTATION COMPLETE                                │
│     → All code changes made                                 │
│     → Files modified                                        │
│     ↓                                                       │
│  2. AUTO-INVOKE REVIEW SKILL                                 │
│     → Skill: superpowers:code-review                       │
│     OR → Skill: superpowers:verification-before-completion  │
│     ↓                                                       │
│  3. REVIEW COMPLETE                                         │
│     → Address any issues found                             │
│     → Make recommended fixes                                │
│     ↓                                                       │
│  4. THEN ASK USER TO TEST                                  │
│     → "Reviewed and ready for testing"                     │
│     → Provide preview URL or test instructions              │
│                                                             │
│  ❌ FORBIDDEN: "Done, please test" (without review)         │
│  ✅ CORRECT: "Code reviewed, ready for testing"             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### How to Invoke Review (CORRECT METHOD)

```
# STEP 1: Get git SHAs
BASE_SHA=$(git rev-parse HEAD~1)
HEAD_SHA=$(git rev-parse HEAD)

# STEP 2: Read the code-reviewer template
# Location: .claude/plugins/cache/claude-plugins-official/superpowers/5.0.6/skills/requesting-code-review/code-reviewer.md

# STEP 3: Dispatch code-reviewer subagent via Agent tool
# Fill placeholders: {WHAT_WAS_IMPLEMENTED}, {PLAN_REFERENCE}, {BASE_SHA}, {HEAD_SHA}, {DESCRIPTION}
```

**❌ FORBIDDEN (Wrong Methods):**
- `Skill: superpowers:code-review` - Does not exist
- `Skill: superpowers:code-reviewer` - Does not exist
- Direct Agent invocation without template - Lacks context

**User Correction:** "you are using the wrong or old deprecated command" (2026-03-31)

### Why This Matters

**User Feedback:** "I wish you knew how and when to invoke those commands"

Without code review:
- Bugs slip through to user testing
- User finds issues AI should have caught
- Lost trust from "saying it's done" when it's not

With code review:
- Fresh eyes on the code
- Different model may catch bugs implementer missed
- Higher quality before user sees it
- User receives more polished work

Without code review:
- Bugs slip through to user testing
- User finds issues AI should have caught
- Lost trust from "saying it's done" when it's not

With code review:
- Fresh eyes on the code
- Different model may catch bugs implementer missed
- Higher quality before user sees it
- User receives more polished work

---

## 🤖 RULE 5: Use Multi-Agent for Execution

**After planning:** Use multi-agent system to execute tasks intelligently.

### Multi-Agent Strategy

```
┌─────────────────────────────────────────────────────────────┐
│              MULTI-AGENT EXECUTION STRATEGY                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INDEPENDENT TASKS → execute_parallel                       │
│    ↓          ↓          ↓                                  │
│  Task A      Task B     Task C     (run simultaneously)      │
│                                                             │
│  DEPENDENT TASKS → execute_sequential                       │
│    → Task A (must complete first)                           │
│    → Task B (depends on Task A)                             │
│    → Task C (depends on Task B)                             │
│                                                             │
│  MIXED → Use agent to decide execution mode                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Multi-Agent Commands

```bash
# Parallel execution (independent tasks)
Agent: execute_parallel
- Task A
- Task B
- Task C

# Sequential execution (dependent tasks)
Agent: execute_sequential
- Step 1
- Step 2
- Step 3

# Auto execution (agent decides)
Agent: auto_execute
- Analyze dependencies
- Execute optimal strategy
```

### Task Classification

| Type | Execution | Example |
|------|-----------|---------|
| **Independent** | Parallel | Fix unrelated bugs in different files |
| **Dependent** | Sequential | Build → Test → Deploy |
| **Mixed** | Auto | Complex feature with mixed dependencies |

---

## 🧪 RULE 6: CAPTURE LOGS BEFORE CLAIMING "FIXED"

**CRITICAL:** NEVER claim anything is "fixed" without capturing and analyzing console/data logs FIRST.

### The "Lying" Problem

**User Feedback:** "how can i work with a liar?" / "you are lying to me, why?"

This happens when:
- You claim "fixed" without proper verification
- The bug still exists when user tests
- You wasted time because you didn't investigate properly

### Verification Protocol (MANDATORY)

```
┌─────────────────────────────────────────────────────────────┐
│              BEFORE CLAIMING "FIXED"                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CAPTURE ACTUAL DATA                                    │
│     → Run Playwright test with console logging             │
│     → Use browser dev tools to see network requests         │
│     → Check database RPC returns actual values              │
│     → Screenshot the BEFORE and AFTER states               │
│                                                             │
│  2. ANALYZE THE LOGS                                       │
│     → Read the console output YOURSELF                      │
│     → Identify the ACTUAL values vs EXPECTED values        │
│     → Find WHERE the data flow breaks                       │
│                                                             │
│  3. VERIFY THE FIX                                         │
│     → See the BEFORE values → apply fix → see AFTER values  │
│     → Confirm the numbers changed correctly                 │
│     → ONLY THEN say "I've made changes, please test"        │
│                                                             │
│  ❌ FORBIDDEN: "It's fixed" / "That should work"           │
│  ✅ CORRECT: "Modified X, logs show Y changed. Please test" │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Example: Field Mapping Bug

**What happened (WRONG):**
```
Me: "Applied migration, player counts now 0/4. Fixed!"
User: "Courts still show 'booked' ❌"
Me: (lost trust because I didn't verify)
```

**What should have happened (CORRECT):**
```
Me: "Applied migration. Let me capture console logs..."
     (Run Playwright test, see logs)
Me: "Logs show '0/16 slots, 0/4 players → booked'
     RPC returns available=true but frontend reads is_available=undefined.
     Root cause: Field mapping mismatch.
     Fixing useBookings.ts line 463..."
     (Verify with test again)
Me: "Logs now show '16/16 slots, 0/4 players → available' ✓
     Please verify at [preview URL]"
```

### Playwright Console Logging Template

```typescript
// CAPTURE ALL CONSOLE MESSAGES
page.on('console', msg => {
  allLogs.push(msg.text());
  console.log(`[BROWSER CONSOLE] ${msg.text()}`);
});

// CAPTURE NETWORK REQUESTS (for debugging)
page.on('request', req => {
  console.log(`[REQUEST] ${req.method()} ${req.url()}`);
});

page.on('response', res => {
  console.log(`[RESPONSE] ${res.status()} ${res.url()}`);
});
```

### When to Use Cloudflare vs Local

| Situation | Use | Why |
|----------|-----|-----|
| Quick verification | Local (localhost:5173) | Faster iteration |
| Final verification | Cloudflare preview | Production environment |
| Database RPC testing | Cloudflare preview | Uses real DB connection |

**User preference:** "if using cloudflare is slow for testing use local"

---

## 🚀 RULE 7: Test Before Deploy Preview

**MANDATORY:** Before ANY preview deployment, test first and ensure end-to-end workflow works.

### Pre-Deploy Testing Checklist

```
┌─────────────────────────────────────────────────────────────┐
│               BEFORE DEPLOYING PREVIEW                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CODE QUALITY                                           │
│     [ ] Run npm run lint (MUST pass)                        │
│     [ ] Run npm run build (MUST succeed)                    │
│     [ ] Check for TypeScript errors                         │
│                                                             │
│  2. LOCAL TESTING                                           │
│     [ ] Test the feature locally                            │
│     [ ] Verify UI renders correctly                         │
│     [ ] Check all interactions work                         │
│     [ ] Test edge cases                                     │
│                                                             │
│  3. WORKFLOW TESTING                                        │
│     [ ] Test complete user flow                            │
│     [ ] Verify data flow end-to-end                         │
│     [ ] Check database operations                           │
│     [ ] Verify auth/access works                            │
│     [ ] Test error handling                                 │
│                                                             │
│  4. SMOKE TEST CHECKLIST                                    │
│     [ ] Page loads without crashes                         │
│     [ ] Primary action works                                │
│     [ ] No console errors                                   │
│     [ ] Data displays correctly                             │
│                                                             │
│  ✅ ONLY THEN deploy preview                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### What "Smoke Test" Means

**Smoke test** = Quick verification that the core functionality works, NOT full testing.

**User does smoke test:**
- ✅ Open preview URL
- ✅ Check main feature works
- ✅ No obvious crashes/errors
- ✅ Looks correct visually

**AI does BEFORE smoke test:**
- ✅ Run linting
- ✅ Run build
- ✅ Test locally
- ✅ Verify workflow
- ✅ Check for obvious bugs

---

## 🚀 RULE 5: Preview Deployment is for Smoke Test Only

**Preview deployment purpose:** User verification, NOT AI saying "it's done".

### Deployment Mindset

| Phase | Who Does What | Purpose |
|-------|---------------|---------|
| **Pre-deploy** | AI: Test everything | Ensure it works before user sees it |
| **Deploy** | AI: Push to trigger preview | Make available for user |
| **Smoke test** | User: Quick verification | User checks it works |
| **Fix if needed** | AI: Address smoke test issues | Fix any problems found |
| **Ship** | User: "ship it" or approval | Final sign-off |

### What to Say When Deploying

❌ **WRONG:**
```
"Deployed to preview! Everything should be working."
```

✅ **RIGHT:**
```
"Deployed to preview for smoke testing.

Preview URL: https://xxx.pages.dev

Please test:
- [ ] Main feature works
- [ ] UI displays correctly
- [ ] No console errors

Let me know if you find any issues."
```

---

## 🔧 RULE 8: Testing vs Production Code

**PRINCIPLE:** Code that's good for testing may be bad for production (and vice versa).

### Testing-Friendly Features (Keep During Dev)

| Feature | Why Good for Testing | Remove for Production |
|---------|---------------------|----------------------|
| Signature verification disabled | Can test without real CyberSource callbacks | ❌ Payment fraud risk |
| OTP codes in logs | Can verify OTP was generated correctly | ❌ Security vulnerability |
| Test email fallback | Prevents crashes during testing | ❌ Wrong for real users |
| Debug console.logs | See what's happening | ❌ Performance/log cost |

### Production-Required Features (Apply Before Go-Live)

| Feature | Why Required | When to Apply |
|---------|--------------|--------------|
| Signature verification enabled | Prevents payment fraud | Production deployment |
| Remove OTP from logs | Security best practice | Production deployment |
| Fix venue credit bug | Correct accounting | Production deployment |
| Remove test fallbacks | Real data only | Production deployment |

### Workflow

```
┌─────────────────────────────────────────────────────────────┐
│              TESTING vs PRODUCTION WORKFLOW                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. DEVELOPMENT & TESTING                                   │
│     → Keep testing-friendly features                         │
│     → Debug with verbose logging                             │
│     → Smoke test freely                                      │
│     ↓                                                       │
│  2. CREATE PRODUCTION CHECKLIST                             │
│     → Document all required patches                          │
│     → File: docs/PRODUCTION_DEPLOYMENT_CHECKLIST.md         │
│     ↓                                                       │
│  3. PRODUCTION DEPLOYMENT                                   │
│     → Apply security patches                                 │
│     → Remove test fallbacks                                  │
│     → Enable production features                             │
│     → Deploy to live environment                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Production Checklist Template

**Always create** `docs/PRODUCTION_DEPLOYMENT_CHECKLIST.md` when building features that have different dev/prod requirements.

**Template structure:**
```markdown
# Production Deployment Checklist - [Feature Name]

## 🔴 CRITICAL (Must Fix Before Production)
1. Enable signature verification
2. Remove sensitive data from logs
3. Fix accounting bugs

## 🟡 IMPORTANT (Should Fix)
1. Remove test fallbacks
2. Add error monitoring

## ✅ VERIFICATION
- [ ] Smoke test passed
- [ ] Code review completed
- [ ] Production checklist applied
```

### User Preference

**User quote:** "if we do those fixes now will it be difficult for us for testing and debugging especially monitoring, maybe we patch it when moving to production?"

**Decision:** Keep testing-friendly code during development. Create production checklist. Apply patches only when deploying to live.

**Why this works:**
- Faster iteration during development
- Easier debugging with verbose logs
- Security properly applied before production
- No "works on my machine" issues

---

## 📊 Complete Workflow Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPLETE JARVIS WORKFLOW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. IMAGE RECEIVED                                             │
│     → Use z.ai vision tool to analyze                           │
│     → Quote what you see                                       │
│     → Explain meaning before proceeding                         │
│                                                                  │
│  2. TASK ASSIGNED                                               │
│     → Analyze the codebase                                      │
│     → Read related files                                       │
│     → Identify root cause                                      │
│     → Check dependencies                                       │
│                                                                  │
│  3. CREATE PLAN                                                 │
│     → Break down into steps                                     │
│     → Identify independent vs dependent tasks                  │
│     → Estimate complexity                                       │
│     → Get user approval if complex                              │
│                                                                  │
│  4. EXECUTE PLAN                                               │
│     → Use multi-agent for parallel/sequential                   │
│     → Monitor progress                                         │
│     → Verify each step                                         │
│                                                                  │
│  5. PRE-DEPLOY TEST                                            │
│     → Run linting (npm run lint)                               │
│     → Run build (npm run build)                                │
│     → Test locally                                              │
│     → Verify end-to-end workflow                                │
│                                                                  │
│  4.5 AUTO-INVOKE CODE REVIEW (CRITICAL)                        │
│     → Skill: superpowers:code-review                       │
│     → OR: superpowers:verification-before-completion  │
│     → Review completed code for issues                         │
│     → Address any problems found                              │
│     → Ensure quality before user testing                         │
│                                                                  │
│  5.5 CAPTURE LOGS AND VERIFY FIX (CRITICAL)                    │
│     → Run Playwright test WITH console logging                 │
│     → Read ACTUAL console output YOURSELF                       │
│     → Compare BEFORE vs AFTER values                            │
│     → ONLY say "fixed" AFTER seeing correct values             │
│                                                                  │
│  6. DEPLOY PREVIEW                                             │
│     → Push to trigger Cloudflare preview                        │
│     → Provide preview URL                                      │
│     → Request smoke test from user                             │
│                                                                  │
│  7. SMOKE TEST RESULTS                                         │
│     → User tests and reports back                              │
│     → Fix any issues found                                     │
│     → Repeat until user approves                               │
│                                                                  │
│  8. SHIP                                                        │
│     → User says "ship it" or approves                           │
│     → Merge to main/master                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚨 Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Skip image analysis | Might misunderstand the issue | Always use z.ai vision first |
| Claim "fixed" without logs | User loses trust when bug still exists | Capture logs → Analyze → Fix → Verify → Show user |
| Fix without planning | Might miss dependencies | Analyze → Plan → Execute |
| Execute everything sequentially | Wastes time on independent tasks | Use multi-agent parallel when possible |
| Deploy without testing | User finds bugs immediately | Test thoroughly before deploy |
| Say "it's deployed" without context | User doesn't know what to test | Provide URL + smoke test checklist |
| Assume it works | Haven't actually verified | Test locally first |

---

## ✅ Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                    JARVIS WORKFLOW RULES                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. 🖼️  IMAGE → Use z.ai vision tool FIRST               │
│  2. 📋 PLAN → Analyze and plan before fixing              │
│  3. 🤖 AGENTS → Multi-agent parallel/sequential execute   │
│  4. 🔍 REVIEW → Use Agent tool with template (not Skill)   │
│  5. 🧪 LOGS → Capture logs BEFORE claiming "fixed"          │
│  6. 🧪 TEST → Test thoroughly BEFORE deploying preview     │
│  7. 🚀 DEPLOY → Preview is for USER smoke test             │
│  8. 🔧 PROD → Keep test-friendly code, patch for production │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Commands Reference

| Command | Purpose |
|---------|---------|
| `mcp__glm-zai-vision__analyze_image` | Analyze images/screenshots |
| `/plan` or `/analyze` | Create execution plan |
| `Agent: execute_parallel` | Run independent tasks together |
| `Agent: execute_sequential` | Run dependent tasks in order |
| `Agent: auto_execute` | Agent decides execution strategy |
| `Agent: general-purpose` | Code review via superpowers:requesting-code-review template |
| `npm run lint` | Check code quality |
| `npm run build` | Verify build works |

**Code Review Template Location:**
`.claude/plugins/cache/claude-plugins-official/superpowers/5.0.6/skills/requesting-code-review/code-reviewer.md`

---

**Every session follows these rules. Future Claude sessions will automatically know them.**
