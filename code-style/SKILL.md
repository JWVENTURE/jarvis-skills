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
