---
name: code-style
description: Code patterns, testing conventions, and workflow rules for PickleballBN
---

# Code Style - PickleballBN

## E2E Testing Patterns (Playwright + Supabase)

### Serial Mode for Shared Resources

**When E2E tests operate on shared database state, ALWAYS use serial mode:**

```typescript
// Add at top of test file (after imports)
test.describe.configure({ mode: 'serial' });
```

**When to use:**
- Tests using same `venue_id`
- Tests using same `court_id`
- Tests booking same time slots
- Tests operating on same JSONB arrays (e.g., `scheduled_breaks`)

**Why:** Parallel workers cause race conditions → second test can't see first test's writes → flaky failures

**Files where this was applied:**
- `scheduled-breaks.spec.ts` — same venue's JSONB array
- `cash-payment.spec.ts` — Court 1 at specific slots (20:00, 21:00)
- `guest-booking-display.spec.ts` — Court 1 conflicts
- `role-access.spec.ts` — syntax fix also applied

**Result:** 56/56 passed, 0 flaky (33.1s)

---

## Pending Review (Low Confidence Signals)

- [ ] _None yet_
