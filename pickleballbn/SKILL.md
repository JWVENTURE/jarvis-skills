---
name: pickleballbn
description: PickleballBN project rules - tech stack, brand colors, client preferences, workflow, design standards. Auto-updates via /reflect skill.
user-invocable: true
---

# PickleballBN Project Skill

**Client:** Racquet & Co (Chia Kok Yin)
**Budget:** BND 8,000
**Project:** Sports venue booking platform (3 venues: Lamunin, Bandar, Tutong)

---

## 🚨 LOCKED TECH STACK (Never Change)

| Component | Technology | Status |
|-----------|------------|--------|
| Backend | **Supabase PostgreSQL** | ✅ LOCKED |
| Frontend | **React Native + Expo** | ✅ LOCKED |
| Styling | **NativeWind (className=)** | ✅ LOCKED |
| Auth | **Supabase Auth** | ✅ LOCKED |
| Payments | **CyberSource (Baiduri)** | ✅ LOCKED |

### ❌ DEPRECATED (Never Use)
- Xano (replaced by Supabase)
- Flutter/Dreamflow (not using)
- Stripe (not available in Brunei)
- Firebase (replaced by Supabase)
- `style={}` prop (use `className=`)

---

## 🎨 BRAND COLORS (NON-NEGOTIABLE)

**Source:** `branding/pickleballbn/COLOR_PALETTE_REFERENCE.md`
**See also:** `/brands` skill for all JW Ventures family brands

### Primary Colors
| Color | Hex | RGB | Tailwind | Usage |
|-------|-----|-----|----------|-------|
| **Midnight Blue** | `#002c72` | `rgb(0, 44, 114)` | `bg-midnight` | Primary brand, headers, backgrounds |
| **Chartreuse Yellow** | `#dfff03` | `rgb(223, 255, 3)` | `bg-chartreuse` | Primary accent, CTAs, highlights |
| **Cyan/Aqua** | `#01f9fb` | `rgb(1, 249, 251)` | `bg-cyan` | Secondary, links, icons |

### Extended Palette (USE THESE TOO!)
| Color | Hex | RGB | Tailwind | Usage |
|-------|-----|-----|----------|-------|
| **Chambray** | `#3c6691` | `rgb(60, 102, 145)` | `bg-chambray` | Blue shade, muted elements, info |
| **Sushi** | `#7ca135` | `rgb(124, 161, 53)` | `bg-sushi` | Green accent, success states |
| **Rock Blue** | `#a0b8d0` | `rgb(160, 184, 208)` | `bg-rock-blue` | Light blue, backgrounds, disabled |
| **Key Lime Pie** | `#b0d31c` | `rgb(176, 211, 28)` | `bg-keylime` | Yellow-green, hover states |
| **Killarney** | `#466d50` | `rgb(70, 109, 80)` | `bg-killarney` | Dark green, secondary accent |

**IMPORTANT:** Use ALL brand colors when appropriate. Don't limit to just primary 3.

### ❌ OLD WRONG COLORS (Never Use)
- ~~#1F5070~~ (old navy)
- ~~#C7F61E~~ (old lime)
- ~~#3DC7E3~~ (old cyan)

---

## ♿ WCAG COMPLIANCE (Mandatory)

All UI must meet WCAG 2.1 AA standards:

### Color Contrast Requirements
| Element | Minimum Contrast | Goal |
|---------|------------------|------|
| Normal text | 4.5:1 | ✅ AA |
| Large text (18pt+) | 3:1 | ✅ AA |
| UI components | 3:1 | ✅ AA |
| Graphics | 3:1 | ✅ AA |

### Verified Contrast Combinations
| Foreground | Background | Ratio | Pass? |
|-----------|------------|-------|-------|
| White `#FFFFFF` | Midnight `#002c72` | 12.6:1 | ✅ AAA |
| Chartreuse `#dfff03` | Midnight `#002c72` | 8.5:1 | ✅ AAA |
| Cyan `#01f9fb` | Midnight `#002c72` | 6.8:1 | ✅ AAA |
| White `#FFFFFF` | Chambray `#3c6691` | 6.2:1 | ✅ AAA |
| White `#FFFFFF` | Killarney `#466d50` | 5.8:1 | ✅ AAA |

### Accessibility Rules
1. **Never use color alone** to convey information (add icons/text labels)
2. **Focus indicators** must be visible (3:1 contrast)
3. **Touch targets** minimum 44x44px (WCAG AAA: 24x24px)
4. **Form errors** must be announced (ARIA)
5. **Images** need alt text (decorative: alt="")

---

## 👁️ NO COLOR VIBRATIONS (Visual Comfort)

**What to avoid:** Colors that vibrate/hum when placed together (causes eye strain, migraines)

### Problematic Combinations (NEVER USE)
| Foreground | Background | Issue |
|-----------|------------|-------|
| Bright red | Bright blue | Extreme vibration ❌ |
| Chartreuse on white | Too bright, eye strain | ❌ |
| Cyan on white | Insufficient contrast + vibration | ❌ |
| Pure red `#FF0000` | Pure green `#00FF00` | Color blindness + vibration ❌ |

### Safe Combinations
| Foreground | Background | Safe? |
|-----------|------------|-------|
| Chartreuse `#dfff03` | Midnight `#002c72` | ✅ |
| Cyan `#01f9fb` | Midnight `#002c72` | ✅ |
| White `#FFFFFF` | Any dark brand color | ✅ |
| Dark text on Sushi `#7ca135` | ✅ |
| Dark text on Key Lime `#b0d31c` | ✅ |

### Rule
When in doubt: **put dark colors on light, or light colors on dark. Never bright-on-bright.**

---

## 🪟 GLASSMORPHISM CONSISTENCY

All glassmorphism must follow the same pattern:

### Standard Glass Card
```tsx
// Light mode glassmorphism
<View className="bg-white/70 backdrop-blur-xl border border-white/20 rounded-2xl p-4 shadow-lg">
  {/* content */}
</View>
```

### Dark Mode Glass Card
```tsx
// Dark mode glassmorphism
<View className="bg-midnight/80 backdrop-blur-xl border border-white/10 rounded-2xl p-4">
  {/* content */}
</View>
```

### Glassmorphism Rules
| Element | Value | Usage |
|---------|-------|-------|
| Background opacity | 70-80% | `bg-white/70` or `bg-midnight/80` |
| Blur | `xl` (24px) | `backdrop-blur-xl` |
| Border opacity | 10-20% | `border-white/10` or `border-white/20` |
| Border radius | `xl` (16px) or `2xl` (24px) | `rounded-xl` or `rounded-2xl` |
| Shadow | `lg` | `shadow-lg` |

### Where to Use Glassmorphism
- ✅ Cards (booking cards, venue cards)
- ✅ Modals and sheets
- ✅ Navigation bars
- ✅ Floating action buttons
- ✅ Overlays

### Where NOT to Use
- ❌ Large full-screen backgrounds (performance)
- ❌ Text-heavy content (readability)

---

## 👤 CLIENT PREFERENCES (Chia)

| Preference | Detail |
|------------|--------|
| Design Style | Professional, not "cute" |
| Popups | Minimal - user prefers direct action |
| Communication | Direct, technical, no fluff |
| Mobile | Mobile-first UI is priority |
| Desktop | Desktop is secondary concern |
| Overall Aesthetic | Clean, premium, modern |

---

## 📋 WORKING PROTOCOLS (NON-NEGOTIABLE)

### ALWAYS Verify Before Assuming
- ❌ "I assume this column exists"
- ❌ "This should work based on..."
- ❌ "Probably" or "should be" without checking
- ❌ "Task is blocked - needs business decision" (without checking code)
- ✅ READ the actual schema/file FIRST
- ✅ CHECK `supabase/migrations/*.sql` before declaring blockers
- ✅ CHECK database columns before querying
- ✅ VERIFY with user when unclear

**User feedback:** "never assume, i dont like that.. when working with me always verify first"
**User correction (2026-03-29):** "have you check existing system logic? i think thi is resolve" - Task #235 example: claimed blocked, but `purchase_credits()` RPC already supported both credit types

### Investigation Order
1. **Check migrations first** - `supabase/migrations/*.sql` contains ACTUAL implementation
2. Check RPC functions - they show what's really possible
3. Documentation describes intent, code shows reality
4. Only then declare something as "blocked" or "needs decision"

---

## 🏢 JW VENTURES BRANDING (Contracts & Invoices)

**⚠️ IMPORTANT:** JW Ventures has its own brand colors - NOT PickleballBN colors!
**See:** `/brands` skill for complete JW Ventures family brand reference

### JW Ventures Brand Colors (for contracts/invoices only)
| Color | Hex | Usage |
|-------|-----|-------|
| **Olive/Sage Green** | `#8B9A6A` | Primary, headers, branding |
| **Charcoal** | `#333333` | Secondary, text |
| **White/Cream** | `#FFFFFF` | Accent, backgrounds |

### ⚠️ DO NOT confuse brands:

| Document/Product | Brand | Primary Color |
|------------------|-------|---------------|
| JW Ventures contracts/invoices | JW Ventures | Olive `#8B9A6A` |
| PickleballBN app/website | PickleballBN | Midnight Blue `#002c72` |
| UniPlay platform | UniPlay | Navy `#0A2240` |
| MeterAI products | MeterAI | Purple `#4B0082` |

### JW Ventures Company Information
```
Company: JW Ventures
Registration: P30000657
Address: No.30 Simpang 94, Kampong Pancha Delima, Jalan Muara
Email: H.jabbar@jwventures.group
Website: www.jwventures.group
Bank: Bank of China (HK) Brunei
Account: 052-120-2-004785-8
SWIFT: BKCHBNBB
Owner: Haji Awang Jabbar bin Haji Awang Tengah
```

### Document Design Standards

| Element | Specification |
|---------|---------------|
| Font | Professional sans-serif (Arial, Calibri) |
| Primary Color | Olive Green `#8B9A6A` (JW Ventures branding) |
| Accent Color | White/Cream highlights |
| Layout | Clean, spacious, professional, premium |
| Tables | Light grid, alternating row colors (#F0F0F0) |
| Headers | Color-coded with Olive Green background |
| Signatures | Side-by-side layout for contracts |
| Footer | "JW Ventures \| P30000657 \| Bandar Seri Begawan \| H.jabbar@jwventures.group" |

### Document Types
1. **Work Order** - Both signatures (JW Ventures + Client)
2. **Invoice** - JW Ventures signature only
3. **Quote** - JW Ventures signature only
4. **Contract** - Both signatures

### Document Types
1. **Work Order** - Both signatures (JW Ventures + Client)
2. **Invoice** - JW Ventures signature only
3. **Quote** - JW Ventures signature only
4. **Contract** - Both signatures

### Premium Design Elements
- Generous white space
- Clear hierarchy with font sizes
- Color-coded headers for sections
- Professional tables with borders
- Consistent footer on all pages
- Center alignment for title/headers
- Right alignment for amounts/prices

---

## 🔄 WORKFLOW RULES

### 🚨 MERGE CADENCE (CRITICAL - DON'T LET FIXES PILE UP!)

| Frequency | What |
|-----------|------|
| **Per Fix** | Complete fix → Test preview → Merge to main → Delete branch |
| **Daily** | Merge all completed fixes to main before ending day |
| **Never** | Don't let 100+ branches accumulate unmerged! |

**Rule of thumb:** If you have >5 unmerged branches, you're falling behind.

**Why:** Fixes stuck in branches = can't test together = merge hell later

### Branch Naming (Cloudflare Auto-Build)
```
claude/issue-[number]-[description]    ✅ Triggers build
claude/review-[description]            ✅ Triggers build
feature/*                              ❌ SKIPPED
```

### Linting (Before Every Commit)
```bash
cd src/magicpatterns
npm run lint          # MUST pass before commit
npm run build         # Verify build works
git commit            # Only if lint passes
```

### Git Workflow
```
Feature Branch (claude/issue-*)  →  main (staging)  →  master (production)
        ↓                               ↓                        ↓
   pickleballbn-dev                 pickleballbn-dev          pickleballbn-prod
      DEV DB                           DEV DB                    PROD DB
```

---

## 📁 IMPORTANT PATHS

| Path | Purpose |
|------|---------|
| `CLAUDE.md` | Project instructions for AI |
| `.memory-bank/pickleballbn/activeContext.md` | Current session state |
| `branding/pickleballbn/COLOR_PALETTE_REFERENCE.md` | Official colors |
| `supabase/migrations/` | Database migrations |
| `src/magicpatterns/` | Web prototype |

---

## 🧠 SHARED MEMORY ARCHITECTURE (Git)

**Source of truth:** `.memory-bank/pickleballbn/` (committed to git)

### Files and Roles
| File | What it Stores | How to Use |
|------|----------------|------------|
| `activeContext.md` | Current session state | **Read at session start**, update during work, refresh at wrap |
| `systemPatterns.md` | Technical patterns | Add reusable implementation patterns and conventions |
| `progress.md` | Completed work timeline | Append notable completed items (features, migrations, fixes) |
| `techStack.md` | Tech decisions + constraints | Record locked choices, versions, and “never use” items |
| `decisionLog.md` | Key decisions + rationale | Log decisions with *why* (trade-offs, constraints) |

### How each IDE uses it
- **Claude Code**: reads `activeContext.md` at session start (standard protocol)
- **Cursor**: same files, but you must explicitly prompt “read `activeContext.md` first”
- **Trae**: same as Cursor (explicit prompt needed)

**Rule:** If context feels “missing”, re-open `activeContext.md` before doing work.

## 🗄️ DATABASE ENVIRONMENTS

| Environment | Project ID | Purpose |
|------------|-----------|---------|
| DEV | `luhetbxmnfxylgkrvagh` | Testing, prototype |
| PROD | `zolxejafzbxgcmimarsz` | Live app |

**Cloudflare Pages Auto-Switch:**
- `master` branch → PROD database
- All other branches → DEV database

---

## 🏟️ VENUES

| Venue | Location | Courts | Status |
|-------|----------|--------|--------|
| Lamunin | Lamunin | 6 | ✅ Primary - Complete |
| Bandar | B.S.B. | 3 | ✅ Active |
| Tutong | Tutong | 3 | ✅ Active |

---

## 💰 PRICING REFERENCE

| Service | Typical Price |
|---------|---------------|
| Domain Transfer | BND 100 |
| DNS Configuration | BND 50 |
| Domain Registration (.com) | BND 15/year |
| SSL Setup | BND 50 |

---

## 🚨 COMMON MISTAKES TO AVOID

1. ❌ Using wrong colors → Always check `COLOR_PALETTE_REFERENCE.md`
2. ❌ Wrong branch names → Must start with `claude/issue-*` or `claude/review-*`
3. ❌ Skipping lint → Run `npm run lint` before every commit
4. ❌ Pushing to master → Only for production deployment
5. ❌ Using Xano → Supabase only
6. ❌ Using `style={}` → Use `className=` with NativeWind
7. ❌ Forgetting to test preview → Always test Cloudflare preview before "ship it"
8. ❌ Poor color contrast → Ensure WCAG AA (4.5:1 for text)
9. ❌ Color vibrations → Never use bright-on-bright combinations
10. ❌ Inconsistent glassmorphism → Follow the standard pattern
11. ❌ Not using extended palette → Use all 8 brand colors when appropriate
12. ❌ Unprofessional documents → Follow JW Ventures branding guidelines
13. ❌ Skipping image analysis → Always use z.ai vision tool to analyze images first
14. ❌ Fixing without planning → Analyze → Plan → Execute
15. ❌ Deploying untested code → Test thoroughly before deploying preview
16. ❌ Using Puppeteer when user requests "fireclaw"/Firecrawl → User explicitly wants Firecrawl MCP tools

---

## 🗄️ DATABASE SAFETY (CRITICAL - LEARNED THE HARD WAY)

**User experienced "chaos" from accidental database reset - ALWAYS BACKUP FIRST!**

### Before ANY Database Modification:
1. **Create backup** to `backups/` directory
2. **Use Supabase MCP plugin** for migrations (never write raw SQL directly)
3. **Test in DEV first**, never touch PROD directly

### Migration Verification Pattern (Task #166 Lesson)
**Problem:** Migration `20260315_fix_slots_player_counting.sql` was created but NEVER applied to DEV or PROD

**Rule:** Always verify migration was actually applied
```
# Check if migration exists in applied migrations
supabase migrations list --project-ref {PROJECT_ID}

# Compare with local migration files
ls supabase/migrations/*.sql
```

**Detection:** Check `list_migrations` output - if migration file exists locally but not in list, it wasn't applied!

### DEV/PROD Divergence Pattern (Task #166)
**Problem:** Functions had different signatures on DEV vs PROD
- DEV: `get_available_slots_for_venue(UUID, DATE, BOOLEAN)` - had player counting
- PROD: `get_available_slots_for_venue(UUID DEFAULT NULL, DATE, BOOLEAN)` - had scheduled breaks but hardcoded `current_players = 0`

**Solution:** Dynamic column detection pattern
```sql
-- Check if column exists before querying
SELECT EXISTS(
  SELECT 1 FROM information_schema.columns
  WHERE table_name = 'venues' AND column_name = 'allow_bookings_when_closed'
) INTO v_has_column;

-- Use dynamic SQL based on result
IF v_has_column THEN
  EXECUTE format('SELECT column FROM venues WHERE id = $1') USING p_id INTO v_row;
ELSE
  EXECUTE format('SELECT column, DEFAULT FROM venues WHERE id = $1') USING p_id INTO v_row;
END IF;
```

### DROP FUNCTION Syntax (Task #166 Lesson)
**Problem:** `DROP FUNCTION IF EXISTS get_available_slots_for_venue(UUID DEFAULT NULL::UUID...)` → syntax error
**Fix:** PostgreSQL doesn't allow DEFAULT values in DROP FUNCTION signature

**Correct:**
```sql
DROP FUNCTION IF EXISTS get_available_slots_for_venue CASCADE;
```

### Always Test DEV → PROD
| Step | Environment | Action |
|------|-------------|--------|
| 1 | DEV | Apply migration first |
| 2 | DEV | Test with actual data (not schema check) |
| 3 | DEV | Verify output (e.g., `current_players: 1, available_spots: 3`) |
| 4 | PROD | Only after DEV verified |

### Backup Location
```
C:\uniplay-development\backups\
```

### Backup Format (JSON)
```json
{
  "backup_date": "YYYY-MM-DD",
  "backup_time": "Description of what backup protects",
  "project_id": "luhetbxmnfxylgkrvagh",
  "project_name": "pickleballbn-dev",
  "summary": {
    "venues": N,
    "courts": N,
    "bookings": N
  },
  "restore_instructions": {
    "critical_tables": ["venues", "courts", "bookings", "user_profiles"]
  }
}
```

### Commands (Use Supabase MCP)
| Action | Tool |
|--------|------|
| Apply migration | `mcp__supabase__apply_migration` |
| Run SQL | `mcp__supabase__execute_sql` |
| List tables | `mcp__supabase__list_tables` |
| Check migrations | `mcp__supabase__list_migrations` |

---

## 🔧 DATABASE KNOWN ISSUES (In Progress)

### Scheduled Breaks Feature (2026-03-27)
| Item | Status | Details |
|------|--------|---------|
| `venues.scheduled_breaks` column | ✅ EXISTS | Verified via information_schema (jsonb type) |
| `get_available_slots_for_venue` uses breaks | ❌ BUG | Does NOT read scheduled_breaks column |
| Frontend (VenueOperatingHours.tsx) saves breaks | ❓ UNKNOWN | Needs verification |
| Required: Filter slots during scheduled breaks | 🟡 TODO | Update RPC + verify frontend |
| Required: Side panel "Venue Management" menu | 🟡 TODO | Add "Venue Management" → "Venue Settings" |

**Related Files:**
- `supabase/functions/get_available_slots_for_venue` - RPC to update
- `src/magicpatterns/src/hooks/useVenueLogo.ts` - isVenueOpen() function (has break logic)
- `src/magicpatterns/src/components/admin/VenuesOperatingHours.tsx` - Admin UI

---

## 🤖 MULTI-AGENT WORKFLOW (User Expectation)

**User expects systematic, plan-driven execution with parallel agent coordination.**

### When User Requests Feature Work
**User expectation:** "plan everything with super power skill including implementation and e2e test, use multi agents in parallels , independent or depedent supervised by you base on our plan"

**Required workflow for new features:**
1. **Brainstorming skill** - Design the feature first (ask clarifying questions, propose approaches)
2. **Create implementation plan** - With E2E tests included
3. **Multi-agent parallel execution** - Independent/dependent as planned
4. **Supervised coordination** - Follow the plan systematically

### Workflow Pattern
1. **Create tasks** via `TaskCreate` with clear subjects and descriptions
2. **Track progress** via `TaskUpdate` (in_progress → completed)
3. **Parallel execution** via `Agent` tool for independent workstreams
4. **Supervised coordination** - Always follow written plans systematically

### When to Use Agents
| Scenario | Approach |
|----------|---------|
| Independent file changes | Parallel agents (one per file/feature) |
| Sequential dependencies | Single agent, then next |
| Large refactors | Break into tasks, coordinate agents |

### Example Pattern
```
1. TaskCreate for each component
2. Agent 1: Component A
3. Agent 2: Component B (parallel if independent)
4. Review and integrate results
5. TaskUpdate all tasks to completed
```

**Never skip planning and jump straight to execution** - the user expects structured work.

---

## 📝 SESSION WRAP PROTOCOL

When ending session:
1. Update `activeContext.md` with current status
2. Commit changes with descriptive message
3. Push to branch
4. Post progress on GitHub Issue (if applicable)

---

## 🧪 SMOKE TESTING TOOLS (User Preference)

**When user requests "fireclaw" or "Firecrawl":**
- ✅ USE: Firecrawl MCP tools (`mcp__firecrawl*` or available browser MCPs)
- ❌ DON'T: Puppeteer MCP (`mcp__puppeteer__*`) - user didn't ask for this

**User language cues:**
- "fireclaw" → Firecrawl MCP
- "smoke test" → User wants to verify preview themselves
- "test with X" → Use tool X specifically

**Why:** User explicitly chose Firecrawl for smoke testing. Using wrong tool breaks trust.

---

## 💳 CYBERSOURCE SECURE ACCEPTANCE (Phase 1)

### Test Credentials (Sandbox)
| Property | Value |
|----------|-------|
| Environment | TEST (`ebc2test.cybersource.com`) |
| Merchant ID | `950051292_test001` |
| Profile Name | `baiduri` |
| Profile ID | `6707F8D1-76C2-4BC1-87FF-7130B42E83DC` |
| Access Key | `026d06d4998b3b76bfc64120264ca6a9` |
| Secret Key | `fbdfd1e1e5c44ac1a5a62d315afd65702f18e4bd3c58461a9baabb49463b334b1dfc6f3604da44a792458033f342138d6bc366a29e6b404f899a5acc924cc5d85e38715523c1479cb51889f8b5ad326c0bd3333ca39948d0b534b64782f6e8d3c2c4d2ccb9084128b7aa8422a8e2ad8979db2646f6424eefa23022b4f5db0922` |

### Return URLs (DEV)
| Event | URL | Notes |
|-------|-----|-------|
| Success | `https://pickleballbn-dev.pages.dev/payment-success` | ✅ Configured |
| Failure | *(Not needed)* | User stays on CyberSource hosted page for errors |
| Cancel | `https://pickleballbn-dev.pages.dev/cart` | ✅ Configured |

### ⚠️ CRITICAL: Failure URL NOT Required
**User stays on CyberSource hosted page when payment fails** - error messages are displayed there. User can retry or cancel from hosted page. Only success and cancel redirects are needed for Phase 1.

### Environment Variables (Supabase Edge Functions)
```bash
CYBERSOURCE_ACCESS_KEY=026d06d4998b3b76bfc64120264ca6a9
CYBERSOURCE_SECRET_KEY=fbdfd1e1e5c44ac1a5a62d315afd65702f18e4bd...
```

---

## 🎟️ LOYALTY PROGRAM ARCHITECTURE

### System Components
| Component | Table | Purpose |
|-----------|-------|---------|
| Points Balance | `loyalty_points` | User balances, tier status, booking count |
| Transaction History | `loyalty_transactions` | Audit trail of all point activity |
| Award Function | `award_loyalty_points()` | Core function to add points |
| Triggers | `award_points_on_booking()` | Fires on booking confirmed/completed |
| Settings | `app_settings.loyalty_settings` | Enable/disable, points per booking |

### Function Behavior
```sql
-- Points awarded when booking status = 'confirmed'
INSERT INTO bookings (..., status = 'confirmed', ...)
  → Trigger: award_points_on_booking()
  → Function: award_loyalty_points()
  → Result: +10 points, +1 booking_count
```

### Known Gotchas
| Issue | Detail |
|-------|--------|
| **Guest bookings** | `user_id = NULL` → No points (by design) |
| **Transaction logging** | Fixed 2026-03-29 - was missing, now creates audit trail |
| **Valid transaction_type** | 'earn', 'redeem', 'expire', 'admin_adjust', 'bonus' (NOT 'earned'!) |
| **Tier progression** | Bronze → Silver (10) → Gold (25) → Platinum (50) bookings |

### Settings (app_settings)
```json
{
  "loyalty_settings": {
    "enabled": true,
    "pointsPerBooking": 10,
    "redemptionRate": 100
  }
}
```

### Debugging Loyalty Issues
1. Check triggers exist: `SELECT * FROM information_schema.triggers WHERE trigger_name LIKE '%loyalty%'`
2. Check settings: `SELECT * FROM app_settings WHERE setting_key = 'loyalty_settings'`
3. Verify function: `SELECT pg_get_functiondef(oid) FROM pg_proc WHERE proname = 'award_loyalty_points'`
4. Test booking: Create test booking with `user_id` (not guest) and `status = 'confirmed'`
5. Check records: `SELECT * FROM loyalty_points WHERE user_id = '<user_id>'`

---

## 🔄 AUTO-LEARNING (via /reflect)

This file is **auto-updated** by the reflect skill when:
- You correct a mistake ("never do X")
- You express a preference ("I prefer Y")
- A pattern is identified across sessions

**Last Learning:** [Updated 2026-03-29 - Task #139: Loyalty transaction logging bug fixed + systematic debugging patterns]

**Git History:** View commit history to see how JARVIS learned over time.

---

## Pending Review (Low Confidence Signals)

_Added by reflect skill for future review_

- [ ] 2026-03-26: Vision tool workaround - use Read tool first (uploads to CDN), then built-in 4_5v analyze_image
- [ ] 2026-03-26: CRON_SECRET not needed for Phase 1 MVP - can add automated cleanup later
- [ ] 2026-03-26: Database backup before ANY modification (learned from "chaos" of accidental reset)
- [ ] 2026-03-26: Multi-agent workflow expectation - use TaskCreate/TaskUpdate + Agent tools
- [x] 2026-03-29: **VERIFIED** - Migration patterns work! Task #166 completed successfully using:
  - Migration verification (checked list_migrations, found old migration wasn't applied)
  - DEV → PROD testing order (tested on DEV first, verified output, then applied to PROD)
  - DROP FUNCTION CASCADE syntax (fixed DEFAULT parameter error)
  - Dynamic column detection (handled schema drift between DEV/PROD)
