---
name: code-style
description: Code patterns, testing conventions, and workflow rules for PickleballBN
---

# Code Style - PickleballBN

## 🧪 Testing Tools (APPROVED)

### Testing Stack
| Tool | Purpose | Location |
|------|---------|----------|
| **Playwright** | Local E2E tests, fast feedback | `src/__tests__/smoke/` |
| **Firecrawl** | Production validation | `supabase/functions/smoke-test-firecrawl/` |
| **Supabase MCP** | Direct API/RPC testing | `execute_sql` tool |

### Testing Commands
```bash
# Run smoke tests (Playwright)
npm run test:smoke

# Run against production (Firecrawl)
npm run test:smoke:prod

# Run both (unified report)
npm run test:smoke:all

# Debug mode
npm run test:smoke:debug
```

---

## 📋 Console Log Capture (REQUIRED)

**User feedback:** "what about the console logs?" → User values debugging visibility.

### Why Capture Console Logs?
- Debug test failures quickly
- Catch Supabase API errors
- Detect missing API keys
- Find network issues
- Track React warnings

### Implementation
```typescript
import { setupConsoleCapture, getConsoleSummary, formatConsoleSummary } from './console-utils';

// In test
test('my-test', async ({ page }) => {
  const getLogs = setupConsoleCapture(page, 'my-test');

  // ... test code ...

  // Report console summary
  const summary = getConsoleSummary(getLogs());
  console.log(`  ${formatConsoleSummary(summary)}`);
});
```

### Console Log Features
- **Capture:** All browser console (error, warning, info, log, debug)
- **Detect:** Supabase errors, network errors, missing API keys, CORS
- **Save:** To `playwright-report/console-logs/` per test
- **Format:** Emojis for quick scanning (❌ error, ⚠️ warning, ℹ️ info)

### Console Issues Detected Automatically
```typescript
import { detectCommonIssues } from './console-utils';

const issues = detectCommonIssues(logs);
// Returns: { missingAPIKeys, networkErrors, supabaseErrors, corsErrors }
```

---

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

## 📊 Testing Roadmap

| Phase | Status | What |
|-------|--------|------|
| 1 | ✅ Complete | Smoke tests (Playwright + Firecrawl, console capture) |
| 2 | ⬜ TODO | E2E user journeys (Browse → Book → Pay → Confirm → Check-in) |
| 3 | ⬜ TODO | API testing (RPC functions via Supabase MCP) |
| 4 | ⬜ TODO | Visual regression (Percy, Chromatic) |
| 5 | ⬜ TODO | Performance (Lighthouse CI, Core Web Vitals) |
| 6 | ⬜ TODO | Accessibility (Axe-core, WCAG AA) |

---

## Pending Review (Low Confidence Signals)

- [ ] _None yet_

---

## Technical Lessons Learned (2026-03-31)

### ICS File Generation - Timezone Handling (CRITICAL)

**Issue:** ICS files using UTC 'Z' suffix cause 8-hour offset for Brunei (GMT+8) users.

**Incorrect:**
```typescript
const formatICSDate = (date: Date) => {
  return date.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
};
```

**Correct:**
```typescript
const formatICSDate = (date: Date) => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');
  return `${year}${month}${day}T${hours}${minutes}${seconds}`; // NO 'Z' suffix
};
```

**Why:** Calendar apps treat 'Z' as UTC, converting to local time. For Brunei (GMT+8), this shows 8 hours wrong.

---

### Race Condition Prevention - User Linking (CRITICAL)

**Issue:** When guest completes payment, link booking to existing user BY PHONE. But if booking already linked to different user, data corruption occurs.

**Incorrect:**
```typescript
const { exists, userId } = await checkExistingUser(supabase, phone);
if (exists && userId) {
  await supabase.from('bookings')
    .update({ user_id: userId })
    .eq('reference', booking.reference);
}
```

**Correct:**
```typescript
const { exists, userId } = await checkExistingUser(supabase, phone);
if (exists && userId) {
  // Check if already linked to different user
  if (existingBooking.user_id && existingBooking.user_id !== userId) {
    console.warn('[Payment Callback] Booking already linked to different user. Skipping link.');
  } else {
    await supabase.from('bookings')
      .update({ user_id: userId })
      .eq('reference', booking.reference);
  }
}
```

**Why:** Prevents data integrity issue where two guests with same phone number could claim each other's bookings.

---

### Code Review Protocol (CRITICAL)

**Rule:** Always request code review via `superpowers:requesting-code-review` before claiming completion.

**Evidence from this session:**
- Reviewer found 3 Critical, 3 Important, 3 Minor issues
- Without review, these bugs would have shipped to production
- Fixed 2 Critical (ICS dates, race condition) and 1 Important (timezone) before claiming complete

**Process:**
1. Get BASE_SHA and HEAD_SHA
2. Dispatch code-reviewer subagent with context
3. Act on feedback (fix Critical, fix Important, note Minor)
4. Only then claim completion

**Files Modified This Session:**
- `BookingSuccessScreen.tsx` - ICS date parsing + local time
- `payment-callback/index.ts` - Race condition check
