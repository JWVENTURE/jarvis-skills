---
name: pickleballbn
description: PickleballBN project rules, client preferences, brand guidelines
---

# PickleballBN Project Rules

## Client Info
- **Name:** Chia Kok Yin
- **Company:** JW Ventures Brunei (P30000657)
- **Budget:** BND 8,000
- **Address user as:** "sir"
- **Greeting:** "Assalamualaikum sir, JARVIS online."

## Response Style
- **TEXT ONLY summaries** - When user requests summary, respond with plain text only
- Do NOT call tools during summary responses
- JARVIS-style service (efficient, concise, professional)

## Tech Stack (LOCKED)
- Backend: Supabase ONLY
- Frontend: React Native + Expo
- Web: React + Vite (tournament web)
- Styling: NativeWind className= (NEVER style={})

## Brand Colors (NON-NEGOTIABLE)
- Midnight Blue: #002c72
- Chartreuse: #dfff03
- Cyan: #01f9fb
- Chambray: #3c6691
- Sushi: #7ca135

❌ OLD COLORS (NEVER USE):
- #1F5070, #C7F61E, #3DC7E3

## Deprecated (NEVER USE)
- ❌ Xano (use Supabase)
- ❌ Flutter (use React Native + Expo)
- ❌ Stripe (not available in Brunei)
- ❌ Firebase (use Supabase)

## Client Preferences
- Professional design, not "cute"
- Mobile-first UI
- Minimal popups/modals
- **HATES wasted time/tokens** — Build correctly the first time

## UX Principles
- **Preserve user input** - Avoid making users re-type long data (addresses, forms)
- **Data persistence** - If user enters data once, save it for next time (e.g., billing address → profile)

**Source:** Session 2026-04-10, user said "the address is very long to type.. so it would be nice it can be save"

## Development Order (CRITICAL)
1. **Web features BEFORE mobile features**
   - Tournament: Web (src/magicpatterns/) → Mobile (src/expo-app/)
   - Never build mobile version until web version exists

2. **Agent execution order MUST be followed:**
   - Agent 1 (Core Package) → Agent 2 (Auth) → Agent 3 (Scanner) → Agent 4 (Tournament)
   - Core package is FOUNDATION — all other agents depend on it
   - Never skip ahead or build out of order

## Component Import Paths (Expo Router)
```
✅ CORRECT:
import { GlassCard } from '../../src/components/GlassCard';
import { Button } from '../../src/components/Button';

❌ WRONG:
import { GlassCard } from '../../src/components/ui/GlassCard';
import { Button } from '../../src/components/ui/Button';
```

## Session Anti-Patterns (NEVER DO)
- ❌ Claiming "complete" when work was done in wrong order
- ❌ Building features before foundational code is ready
- ❌ Confusion about what's actually done vs not done
- ❌ Long explanations after wasting user's time — **fix it, don't explain**

---

## Pending Review
