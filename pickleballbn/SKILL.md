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

---

## 📝 SESSION WRAP PROTOCOL

When ending session:
1. Update `activeContext.md` with current status
2. Commit changes with descriptive message
3. Push to branch
4. Post progress on GitHub Issue (if applicable)

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

## 🔄 AUTO-LEARNING (via /reflect)

This file is **auto-updated** by the reflect skill when:
- You correct a mistake ("never do X")
- You express a preference ("I prefer Y")
- A pattern is identified across sessions

**Last Learning:** [Updated 2026-03-26 - CyberSource Secure Acceptance: Failure URL NOT needed]

**Git History:** View commit history to see how JARVIS learned over time.

---

## Pending Review (Low Confidence Signals)

_Added by reflect skill for future review_

- [ ] 2026-03-26: Vision tool workaround - use Read tool first (uploads to CDN), then built-in 4_5v analyze_image
- [ ] 2026-03-26: CRON_SECRET not needed for Phase 1 MVP - can add automated cleanup later
