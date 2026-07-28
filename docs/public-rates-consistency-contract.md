# Public Rates Page ↔ Q3 Direct-Link Page — Consistency Contract v1

**The two pages are one document at two depths.** The direct-link page
(`wolfpackdata/wp-rates-page` → `intake.wolfstrategyllc.com/rates_2026Q3/`, noindex) is
the detailed, quarter-stamped source of truth for all pricing. The public page
(`wp-website/rates/`, indexed, evergreen) is derived from it. **Consistency means: every
fact the public page states matches the current direct-link page exactly. Depth may
differ; facts may not.** Anything not on the delta list below is, by definition, supposed
to match.

The upstream repo is read-only from this repo's sessions (local checkout:
`c:\wp\wp-rates-page`). The two repos are **not connected** — no automation links them;
sync is a prompted, manual port (see §3).

---

## 1. The mirror set — must match the direct-link page exactly, wherever shown

- Hourly rate ($175/hr), 4-hour minimum, <10 hrs/wk, billed on delivery, bonus-hours
  ratio (2 per 15), pro-rated upgrade right.
- Tier names (Base / Focus / Solo), monthly prices ($13,400 / $16,200 / $18,100),
  commitments (20 / 25 / 30+ hrs/wk), contract lengths (1 / 2 / 3 months), effective
  rates ($155 / $150 / $140), save percentages (10 / 15 / 20), featured-tier choice
  (Focus, "Most popular") and "Best rate" badge (Solo).
- Coaching pack prices and math (Single $135 · 3-Pack $365 · 6-Pack $690 · 9+1 $1,080),
  every-6th-free, never-expires, nonrefundable.
- The coupon **fact** (Focus/Solo include a shareable 25%-off coaching coupon, terms
  apply) — the public page states it in one line; only the depth differs.
- Terms values that the public page shows: no added fees/taxes · ACH −2% ·
  2-yr grandfathering · ≥90-day rate-change notice · no-contract hourly · 30-day project
  notice · `fin@wolfstrategyllc.com`. (Net 7 dropped from the public page — see D10.)
- The booking calendar URL for 30-minute-call CTAs:
  `https://calendar.app.google/zHNd1NA9wzb4VRLw5` — the Q3 page's current link, mirrored
  here 2026-07-28 (#32; supersedes `WUQnihH9GEEJRMARA`, #8). ℹ️ Google periodically
  regenerates share URLs for the **same** calendar (Ry, 2026-07-28), so a URL difference
  between pages is benign — old intro-call URLs keep resolving to the same booking page.
  Still mirror the Q3 page's current URL on each sync so the pair stays textually
  consistent. The `13EANJ…` link is the separate **45-minute tutoring calendar** — never
  use it for 30-minute-call CTAs. (The Q3 page also once shipped a third, wrong link —
  `wp-rates-page#21`.)
- Nav structure follows the Q3 page for sections both pages carry — e.g. both dropped the
  "Terms" nav link on 2026-07-28 (ruled by Ry; the terms sections themselves stay) and
  renamed "Coaching" → "AI Coaching". Nav items for Q3-only sections (Portfolio — D9) are
  omitted here; the public-only "Engagements" item stays.
- Contact email `main@wolfstrategyllc.com`, LinkedIn URL.
- Wolfpack Advantage list content; About-Ryan facts (titles, track-record numbers,
  credentials); credential stats strip.
- Brand tokens: navy `#000B29`, coral `#F95954` (rationed), Roboto/Montserrat, 4px
  radius, the surface/line palette.

## 2. The delta list — intentional, enumerated differences (everything else matches)

| # | Public page difference vs. Q3 page | Why |
|---|-----------------------------------|-----|
| D1 | Indexed (+ canonical, OG tags); Q3 is `noindex, nofollow` | The page is meant to be found |
| D2 | Evergreen URL `…/rates/` + "last reviewed" line; no version stamp or quarter in URL/headline | Brief: evergreen, not quarter-stamped |
| D3 | Hero copy: transparency posture ("Know the rate before the call." — Ry's draft-1 wording, 2026-07-23) instead of the two-products catalog opener | Cold reader; the posture is the hook |
| D4 | New "context before numbers" framing section + **standard-engagements / custom-quote note** | Brief directives |
| D5 | **No kickoff-retainer amounts** (incl. the hourly "$525 kickoff" line) and **no rate-ladder bar chart** | Ruled: monthly prices yes, itemization no |
| D6 | Process section reframed as "the call" — what it is / isn't — and promoted; retainer language softened | The call is the conversion goal |
| D7 | **No intake-form links anywhere**; coaching CTA is the calendar | Book-first funnel (intake sent after booking) — matches `ai-coaching/` |
| D8 | Coupon bridge compressed to a one-line perk; $50-invoice-credit mechanics omitted | Deal mechanics read transactional to strangers |
| D9 | **No application-screenshot portfolio grid** and no placeholder button; proof = hero stats + compact About | Proof lives on the upcoming Applications page; dead buttons spend trust |
| D10 | Terms condensed to the trust-bearing subset (§1); retainer-due-in-full, coaching-billing mechanics, **and the Net-7 line** omitted (Net-7 drop ruled by Ry in draft-1 feedback, 2026-07-23) | Match depth to what the page shows |
| D11 | **No phone number** in contact | Indexed page; scrape/spam exposure |
| D12 | About Ryan trimmed to ~2 paragraphs | Compact-credibility ruling |

## 3. Sync workflow (Ry's stated process: update Q3 first, then prompt the port here)

When the direct-link page changes, a session in this repo:
1. Diff the current `c:\wp\wp-rates-page\index.html` (and css) against the last-synced
   state — `git -C c:\wp\wp-rates-page log` identifies what changed.
2. Port **every changed fact in the mirror set** (§1) into `rates/index.html`.
3. For changes touching a delta (§2): apply the *fact* at the public page's *depth*
   (e.g. a new tier price ports; a new retainer amount doesn't — D5).
4. A change that fits no rule = a new ruling → ask Ry, then **record it here** as a new
   D-row or mirror-set line. This contract only works if it stays current.
5. Update the public page's "last reviewed" date (hero kicker + footer) whenever a sync
   lands. When the Q3 page is superseded (e.g. `rates_2027Q1`), update the upstream URL
   references here and in `CLAUDE.md`.

## 4. Upstream flags — for the future `wp-rates-page` session prompt

A handoff prompt will be authored **after Ry approves a good version of the public page**
(not before), telling the `wp-rates-page` session:
- A downstream public derivative exists at `wp-website/rates/` under this contract; the
  repos are not connected, and its own workflow doesn't change — except that after any
  content change lands, **Ry prompts the wp-website session to sync** (§3). The prompt
  should tell that session to remind Ry of the downstream sync when content changes merge.
- **Known upstream inconsistencies to reconcile on its next update:**
  - The Q3 page links the coaching intake form twice ("Start with the 2-minute intake" /
    "skip the call") — this predates the **book-first** funnel decision (intake sent after
    booking) that both `ai-coaching/` and the public rates page follow.
  - ✅ **Resolved 2026-07-28:** the Q3 page's booking CTAs no longer point at the
    45-minute tutoring calendar (`13EANJ…`) — wp-rates-page#32/#34 moved them to the
    intro calendar (`zHNd1NA9wzb4VRLw5`), and the public page mirrors it
    (`wp-website#32`). The `ai-coaching/` pages remain on `WUQnihH9GEEJRMARA` — a prior
    URL of the **same** intro calendar, so equivalent — deliberately untouched (Ry,
    2026-07-28).
  - Ry's call on when to reconcile both.
