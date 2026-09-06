# Public Rates Page ↔ Q3 Direct-Link Page — Consistency Contract v1

**The two pages are one document at two depths.** The direct-link page
(`wolfpackdata/wp-rates-page` → `intake.wolfstrategyllc.com/rates_2026Q3/`, noindex) is
the detailed, quarter-stamped source of truth for all pricing. The public page
(`wp-website/rates/`, indexed, evergreen; canonical public URL
`intake.wolfstrategyllc.com/rates_public/` since 2026-07-28 — spec R12) is derived from
it. **Consistency means: every
fact the public page states matches the current direct-link page exactly. Depth may
differ; facts may not.** Anything not on the delta list below is, by definition, supposed
to match.

The upstream repo is read-only from this repo's sessions (local checkout:
`c:\wp\wp-rates-page`). The two repos are **not connected** — no automation links them;
sync is a prompted, manual port (see §3).

---

## 1. The mirror set — must match the direct-link page exactly, wherever shown

- Hourly rate ($135/hr), 4-hour minimum, <10 hrs/wk, billed on delivery, bonus-hours
  ratio (2 per 15), pro-rated upgrade right. **The rail's placement and label mirror too**
  (2026-09-06): it sits **below** the tier grid and its caption, labelled
  **BASE RATE W/O CONTRACT** — spec R17.
- Tier names (Base / Focus / Solo), monthly prices ($10,800 / $12,400 / $13,500),
  commitments (20 / 25 / 30+ hrs/wk), contract lengths (1 / 2 / 3 months), effective
  rates ($125 / $115 / $105), save percentages (10 / 15 / 20), featured-tier choice
  (Focus, "Most popular") and "Best rate" badge (Solo). ⚠️ The save percentages are
  **Ry's round numbers**, not recomputed arithmetic — mirror them as printed.
- Coaching pack prices and math (Single $99 · 3-Pack $269 · 6-Pack $499 · 10-Pack $799),
  every-6th-free, never-expires, nonrefundable. (The fourth card is the **10-Pack** since
  2026-09-06; the "9 + 1 bonus" framing is gone from both pages.)
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
- The coaching section's closing two-button row (added upstream 2026-07-28,
  `wp-rates-page#39`/#40): the **second** button is a navy-ghost link to the
  **AI ROI Calculator**, labeled *"Calculate what AI is worth to you."* The **first**
  button differs by design (D7: calendar CTA here, intake CTA there) and stays first and
  primary; the ROI button's label/ghost style/second position, and its target — the
  calculator's canonical public URL
  `https://intake.wolfstrategyllc.com/roi-calculator/` (moved to the intake domain by Ry,
  2026-07-28; the source still lives in this repo's `roi-calculator/`) — mirror exactly.
  The Q3 page's skeptic-nudge line above the row does **not** port (D13).
  (Ported via #46; nudge dropped via #50.)
- Nav structure follows the Q3 page for sections both pages carry — e.g. both dropped the
  "Terms" nav link on 2026-07-28 (ruled by Ry; the terms sections themselves stay) and
  renamed "Coaching" → "AI Coaching". Nav items for Q3-only sections (Portfolio — D9) are
  omitted here; the public-only "Engagements" item stays. **`Pilot project` is the FIRST nav
  item on both pages** since 2026-09-06 — spec R16.
- **The pilot project section.** History first, because it keeps getting mis-told: the pilot
  landed on the Q3 page as a full-width band *below* the tiers on **2026-08-18** (issue
  `wp-rates-page#42`, PR `#43`, merged `bc5d510`) and was ported here the same day (#238). On
  **2026-09-06** that band was **replaced on both pages** by a `#pilot` **section above the
  tiers** — upstream `wp-rates-page#50`, ported here as #283. Ry's sequencing ruling holds and
  this round went **Q3-first again**, so the pilot stays a **mirror-set item, not a delta**.
  ⚠️ **Status at 2026-09-06 (remove when it clears):** `wp-rates-page#50` is open, awaiting the
  Admin merge (the session's bypass was refused), and `ai-coaching-intake#97` redeploys it. Until
  both land, `wp-rates-page` `main` (`1736e7a`) and the live `/rates_2026Q3/` still carry v1.0.0 —
  `$175/hour` and the `$5,000` band. **A sync session in that window reads PR #50's head
  (`8de9244`), not `main` and not the live page**; this repo's `develop` already carries the
  mirrored v2.0.0 facts (#292).
  ℹ️ *The 2026-09-06 planning pass mis-read the repo state and asserted that `#42` never
  landed and the Q3 page carried no band. It landed and was live at `/rates_2026Q3/`; the
  sequencing claim recorded here was always true, and the correction is recorded so the misread
  is not "fixed" back in.*

  **The six facts that must match exactly:** the **$500 kickoff fee** · it **covers the first
  6 hours** · **$85 / hour after that**, billed once at the end · **30 calendar days** ·
  **10–20 hours per week is the recommendation** · the worked example, **≈ $2,900** billed at
  the end for 10 hrs/week — kept as the 4-week approximation by Ry's ruling on wp-website#296
  (2026-09-06; he wants the example under $3,000), never recomputed to 30 days.
  **Placement is mirrored too**: `#pilot` immediately before the
  projects section (the first pricing on the page), `Pilot project` as the first nav item, and a
  single **navy-ghost** CTA — *"See the pilot project"* — linking
  `https://intake.wolfstrategyllc.com/pilot-project/`. Never coral: the ration in
  `rates/css/rates.css` is a closed enumerated list and it is full. Public-page depth notes:
  spec R15/R16.

  **Removed from the mirror set on 2026-09-06** — the **$5,000 fixed fee**, the
  **two-to-three-week calendar window**, and the **two included systems** (Wolfpack AI Command
  and the BQL Analytics Provisioner). None of the three is a fact about the offer any more.
  The section **lists no inclusions at all** (Ry's instruction), states **no total pilot price**
  (`≈ $2,900` is the only figure of that shape and it is explicitly an example), and names **no
  post-pilot rate and no fence** — day 31 is negotiated on the call.

  ⚠️ **THE NO-HOURS RULE IS RETIRED — 2026-09-06, Ry's call. Do not reinstate it.** Until that
  date this contract required both pages to state no hours, no weekly commitment and no
  effective hourly rate for the pilot, and to close on the disarm sentence *"a pilot buys a
  scoped outcome rather than reserved time, so it sits off the rate curve above."* **The rule
  and the sentence are dead together** — retired, not weakened. The $85/hr, the 6 covered
  hours and the 10–20 hrs/week recommendation all publish deliberately, on a page whose base
  rate ($135/hr) is printed further down, and Ry made that call knowing exactly what the
  arithmetic looks like. His
  reason, verbatim: *"I realize this is a big change that offers a big discount, that is why I'm
  making it and putting it up top."* Neither half carries over to any page, and neither may be
  re-derived from the numbers and restated as a live rule.
- Contact email `main@wolfstrategyllc.com`, LinkedIn URL.
- Wolfpack Advantage list content; About-Ryan facts (titles, track-record numbers,
  credentials); credential stats strip.
- Brand tokens: navy `#000B29`, coral `#F95954` (rationed), Roboto/Montserrat, 4px
  radius, the surface/line palette.

## 2. The delta list — intentional, enumerated differences (everything else matches)

| # | Public page difference vs. Q3 page | Why |
|---|-----------------------------------|-----|
| D1 | Indexed (+ canonical, OG tags); Q3 is `noindex, nofollow` | The page is meant to be found |
| D2 | Evergreen URL (canonical `…/rates_public/`, github.io `…/rates/` — spec R12) + "last reviewed" line; no version stamp or quarter in URL/headline | Brief: evergreen, not quarter-stamped. ⚠️ **The *"rates last reviewed"* line is public-page-only** — it lives in this page's hero kicker and footer, and the Q3 page carries a **version stamp** (`v2.0.0 · Effective Q3 2026`) in the same two slots instead. A sync instruction that says to move the line "on both pages" is describing this page only; on the Q3 page the equivalent act is the version bump. Currently **September 2026** here (moved from August 2026 by the 2026-09-06 sync) |
| D3 | Hero copy: transparency posture ("Know the rate before the call." — Ry's draft-1 wording, 2026-07-23) instead of the two-products catalog opener | Cold reader; the posture is the hook |
| D4 | New "context before numbers" framing section + **standard-engagements / custom-quote note** | Brief directives |
| D5 | **No kickoff-retainer amounts**: the Q3 page's flat **$1,500** per-tier retainer rows and its hourly **"kick off for $500 — covers your first 4 hours"** line have no counterpart here, so those facts stay **Q3-only**. ⚠️ That $500 is the **hourly** kickoff covering **4** hours — not the pilot's $500 kickoff covering **6**; the two figures collide and are different offers. | Ruled: monthly prices yes, itemization no. **The rate-ladder half of this delta RETIRED 2026-09-06**: the bar chart was deleted from the Q3 page (`wp-rates-page#50`), so the two pages converge there and there is nothing left to diverge from. Its caption survives upstream as `.tiers__caption`, which this page also carries |
| D6 | Process section reframed as "the call" — what it is / isn't — and promoted; retainer language softened | The call is the conversion goal |
| D7 | **No intake-form links anywhere**; coaching CTA is the calendar | Book-first funnel (intake sent after booking) — matches `ai-coaching/` |
| D8 | Coupon bridge compressed to a one-line perk; $50-invoice-credit mechanics omitted | Deal mechanics read transactional to strangers |
| D9 | **No application-screenshot portfolio grid** and no placeholder button; proof = hero stats + compact About | Proof lives on the upcoming Applications page; dead buttons spend trust. **Resolved 2026-08-05 — see D15:** that page shipped, and the public page now links it rather than rebuilding a grid. The grid itself is still banned here |
| D10 | Terms condensed to the trust-bearing subset (§1); retainer-due-in-full, coaching-billing mechanics, **and the Net-7 line** omitted (Net-7 drop ruled by Ry in draft-1 feedback, 2026-07-23) | Match depth to what the page shows |
| D11 | **No phone number** in contact | Indexed page; scrape/spam exposure |
| D12 | About Ryan trimmed to ~2 paragraphs | Compact-credibility ruling |
| D13 | **No skeptic-nudge line** (*"Skeptical of AI hype? Good — run your own numbers."*) above the coaching CTA row — the Q3 page keeps it | Ruled off the public page by Ry, 2026-07-28 (#50) |
| D14 | The two "Two ways to work with Wolfpack" path cards **are navigation** — heading and image both link to that path's section (`#engagements` / `#coaching`) — a public-only affordance (spec R13) | The framing section is public-only (D4), so its cards have no Q3 counterpart to diverge from; navigation, not a fact — nothing in the mirror set moves |
| D15 | A closing `#work` section with a navy-ghost **"See recent projects"** button linking `…/portfolio/` (spec R14) — public-only; the Q3 page has no counterpart | **This is how D9 resolves.** D9 dropped the Q3 application-screenshot grid because "proof lives on the upcoming Applications page"; that page shipped 2026-08-05, so the public page links it instead of rebuilding a grid. A link, not a fact — nothing in the mirror set moves, and the Q3 grid stays as it is |
| D16 | **The Q3 portfolio grid's buttons do not port** (added 2026-09-06): upstream, two application tiles gained a navy-ghost `btn--sm` *"Read the case study"* link and the dead portfolio placeholder became a live navy-ghost button to `…/portfolio/` (`wp-rates-page#50`, spec R18). This page has **no application grid to hang them on** — it reaches the portfolio through its own closing `#work` section instead (D15) | D9 bans the screenshot grid here, so a change *inside* that grid has no public-page counterpart. Not a fact about pricing — nothing in the mirror set moves. The button styling is worth recording anyway: it went **navy-ghost, never coral**, and dropped the Q3 coral ration 9 → 8, matching the ghost discipline R14 set here |

## 3. Sync workflow (Ry's stated process: update Q3 first, then prompt the port here)

When the direct-link page changes, a session in this repo:
1. Diff the current `c:\wp\wp-rates-page\index.html` (and css) against the last-synced
   state — `git -C c:\wp\wp-rates-page log` identifies what changed.
2. Port **every changed fact in the mirror set** (§1) into `rates/index.html`.
3. For changes touching a delta (§2): apply the *fact* at the public page's *depth*
   (e.g. a new tier price ports; a new retainer amount doesn't — D5).
4. A change that fits no rule = a new ruling → ask Ry, then **record it here** as a new
   D-row or mirror-set line. This contract only works if it stays current.
5. Update **this page's** *"rates last reviewed"* date (hero kicker + footer) whenever a sync
   lands — **September 2026** as of the 2026-09-06 pilot/reprice sync. The line is
   public-page-only (D2): the Q3 page's counterpart is its version stamp, so a sync never
   "moves the last-reviewed line on both pages". When the Q3 page is superseded (e.g. `rates_2027Q1`), update the upstream URL
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
