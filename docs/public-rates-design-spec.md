# Public Rates Page — Design & Content Spec v1

**Responds to:** [public-rates-design-brief.md](public-rates-design-brief.md) (Ry's strategy brief — authoritative where they'd conflict)
**Companion doc:** [public-rates-consistency-contract.md](public-rates-consistency-contract.md) (what mirrors the Q3 page vs. what intentionally differs)
**Status:** Planning approved rulings baked in · no code written yet
**Target:** `rates/` in this repo → `https://wolfpackdata.github.io/wp-website/rates/` (Wix links to it, same pattern as the ROI calculator)

---

## 1. Thesis

The direct-link Q3 page closes a deal already in motion. This page's only job is to make
a **30-minute conversation feel like the obvious, safe next step** — and it does that by
being the rates page with nothing to hide. Transparency is the hook; the call is the ask.
The sale happens on the call, not on the page.

Success metric (from the brief): **fewer, better calls.** A good-fit visitor books feeling
informed; a bad-fit visitor self-selects out before taking a calendar slot.

## 2. Rulings ledger (all decided — do not re-litigate at build time)

| # | Ruling | Decision |
|---|--------|----------|
| R1 | Phone number | **Dropped.** Contact = email + LinkedIn + calendar CTA only. |
| R2 | Coupon bridge | **Compressed.** 25% shareable coaching coupon stated as a Focus/Solo perk; the $50-invoice-credit mechanics stay on the Q3 page. |
| R3 | Public home | **github.io path**, Wix links to it (Ry repoints Wix himself). |
| R4 | Folder / URL | **`rates/`** (renamed from `rate-page-public/`). Evergreen — no quarter in the URL. |
| R5 | Project tier depth | **Monthly prices shown.** Each tier: name, monthly $, hrs/wk, contract length, effective $/hr, save %. **Dropped:** kickoff-retainer amounts and the bar-chart rate ladder. |
| R6 | Coaching depth | **Exact pack prices**, all four packs — low-ticket transparency models the posture. |
| R7 | Proof content | **Compact credibility only.** About-Ryan block + hero credential stats. No application-screenshot grid — proof lives on the upcoming "Business Applications built" page; link it from here once it exists. |
| R8 | Terms depth | **Condensed trust terms.** Keep: Net 7, no added fees/taxes, ACH −2%, 2-yr rate grandfathering, 90-day change notice, no-contract hourly, 30-day project out, billing-questions email. Drop: retainer-due-in-full, coupon math, coaching billing mechanics. |
| R9 | Funnel | **One CTA: book the call** (`https://calendar.app.google/13EANJ63HKqMc76z6`). **No intake-form links anywhere** — coaching is book-first; the intake is sent after booking (matches the approved `ai-coaching/` page, deliberately diverges from the Q3 page's two intake links). |
| R10 | Dating | **Evergreen.** No version stamp in headline/URL/framing. Quiet *"rates last reviewed: \<Month YYYY\>"* line instead (hero kicker + footer). |

## 3. Page architecture (in order)

Every section must stand alone reasonably well — the brief assumes the page gets linked,
screenshotted, and read out of context.

### 3.1 Sticky nav
Same pattern as the Q3 page. Brand → `https://www.wolfstrategyllc.com`. Links:
**Engagements · How it works · Coaching · Terms** (no Portfolio — R7). Coral CTA: **Book a call**.

### 3.2 Hero
- Kicker (mono `.k` voice): `Rates & engagement guide · last reviewed <Month YYYY>`
- H1, the posture itself. Directional copy:
  > **Every rate we charge is on this page.**
- Lede: no "starting at," no quote theater — read the numbers, then spend thirty unbilled
  minutes on your problem. One coral CTA (the calendar). Optional ghost CTA → `#coaching`.
- Credential stats strip ports from the Q3 hero (20 yrs data & code · 10 yrs COO · 3+ yrs
  building with AI · outcomes over activity · …) — this is most of the page's proof budget (R7).

### 3.3 Context before numbers (new section — brief directive)
Short framing block **ahead of the first price**. Tight — framing, not a hero-heavy landing
page. Contents:
- Who this is for: teams that need analytics/automation/AI systems built (projects), and
  working professionals who want AI in their actual workflow (coaching).
- What an engagement looks like: reserved weekly time, a collaborative SOW, visible work.
- **Standard-engagements note (verbatim intent):** the rates below are standard
  engagements; **larger or unusual scopes are custom-quoted.** (Preserves negotiating room
  without undermining the transparency posture.)

### 3.4 Projects — standard engagements (`#engagements`)
Section lede carries the rate-curve rationale (voice: where a number has a rationale, show
the rationale): *one curve — the more time you block off, the less each hour costs; the
discount is already built into every tier.*

- **Hourly rail** — $175/hr · no contract · 4-hour minimum · under 10 hrs/wk · billed on
  delivery. Perks: 2 bonus hours per 15 booked; upgrade to any tier anytime, pro-rated.
  (The "$525 kickoff" line is retainer mechanics — stays on the Q3 page, R5.)
- **Three tier cards** (per R5, each card):
  - Project · Base — $13,400/mo · 20 hrs/wk · 1 month · effective $155/hr · save 10%
  - Project · Focus — $16,200/mo · 25 hrs/wk · 2 months · effective $150/hr · save 15% — **featured** (coral border + "Most popular" badge, as on Q3)
  - Project · Solo — $18,100/mo · 30+ hrs/wk · 3 months · effective $140/hr · save 20% — "Best rate" badge
  - Tier one-liner feet keep the Q3 spirit (proving ground / sweet spot / full throttle).
- **No** ladder bar chart, **no** kickoff-retainer rows (R5).
- Close with the custom-quote reminder if it didn't land in 3.3.

### 3.5 The call (`#process`) — the conversion engine
Promoted and reframed from the Q3 process section. Two beats:
1. **What the 30 minutes is:** unbilled; you describe the problem, I listen; you leave
   knowing exactly what working together would look like. Then: proposal & SOW iterated
   together transparently → price/deliverables/timeline finalized together ("there's
   always a conversation to be had") → time gets blocked and work begins. (Soften the Q3
   "retainer comes in" step — retainer mechanics are off this page.)
2. **What it isn't:** no pitch deck, no pressure — the prices were already on the page.
   *(This line is the whole strategy in one sentence — keep it.)*
Coral CTA repeat.

### 3.6 The Wolfpack Advantage
Port the check-list from the Q3 page (custom web applications, agentic dev environment,
isolated client data + DPA, reusable AI skills, live ROI dashboards, evidence over
consultant theater, collaborative SOW, radical Notion visibility, weekly working sessions).
The `wolfpack-advantages.png` collage may port with it (already public on the Q3 URL).
Trim only if the page runs long — the list is proof, and proof budget is thin here (R7).

### 3.7 AI Coaching (`#coaching`)
- Same positioning lede as Q3 (45-min 1:1 video sessions, no contract, no prerequisites).
- **All four packs, exact prices** (R6): Single $135 · 3-Pack $365 (≈$122/session, save
  10%) · 6-Pack $690 ($115/session, save 15%) · 9+1 $1,080 ($108/session, save 20%).
  Every 6th session free; packs never expire; nonrefundable.
- **Compressed coupon perk** (R2), one line inside this section (no standalone bridge):
  *Focus and Solo project clients get a shareable 25%-off coaching coupon (terms apply).*
- **CTA = the calendar link** (R9). No intake link, no "skip the call" note.

### 3.8 About Ryan (compact — R7)
Photo + name + roles line + a trimmed bio (~2 short paragraphs max: the operator-with-an-
engineering-skillset arc, the $300K→$30M and $20k-MRR receipts, Cornell OR&IE). LinkedIn
link. No superlatives — the numbers are the adjectives.

### 3.9 Billing & terms, condensed (`#terms`)
"The fine print, in plain sight" framing survives — on a public page it's the proof of the
hero's claim. Single condensed group (R8): Net 7 · no added fees or taxes · ACH takes 2%
off · rates grandfathered 2 years for active clients · ≥90 days' notice before any rate
change · hourly has no contract · ending a project takes 30 days' notice · questions
welcome → `fin@wolfstrategyllc.com`.

### 3.10 Contact / final CTA
"Bring us the problem" framing from Q3. Coral CTA (calendar) + `main@wolfstrategyllc.com`
+ LinkedIn. **No phone (R1), no intake note (R9).**

### 3.11 Footer
Wordmark · *rates last reviewed \<Month YYYY\>* · link to wolfstrategyllc.com.

## 4. What is banned (the not-salesy contract)

No urgency, scarcity, or countdowns · no "book before rates change" (the 90-day-notice
term makes it dishonest anyway) · no lead-capture forms, email gates, or popups · no
newsletter or contact-form fork (one CTA — brief) · no obfuscated "starting at" pricing ·
no unattributed hype quotes or superlatives · no disabled/placeholder buttons (the Q3
portfolio placeholder does **not** port) · no dark-pattern anything.

## 5. Design system

- Inherits the Q3 page's system (`wp-rates-page/css/rates.css` is the pattern library):
  navy `#000B29` ground, 4px radius cards, Roboto 700 headings / Montserrat body, mono
  `.k` kicker labels, `--surface`/`--line` tokens.
- **Coral `#F95954` discipline** — own CSS file (`rates/css/rates.css`) carries a header
  comment enumerating every allowed use, kept true (same convention as `ai-coaching/`).
  Planned allowance: nav CTA, featured tier (border + badge), the three section CTAs
  (call section, coaching, contact), link hover, focus ring. Nothing else.
- Where coral is a fill, text on it is **navy, never white** (AA).
- 16px minimum body font (iOS zoom), `scroll-behavior: smooth`, sticky nav.

## 6. Head / SEO (indexed — unlike both sibling intake-domain pages)

- `<title>`: `Rates & Engagement Guide — Wolfpack Data & Strategy` (no quarter/version).
- Meta description: transparency posture + the two offerings, ~155 chars.
- **No robots meta** (indexable). Canonical: `https://wolfpackdata.github.io/wp-website/rates/`
  — revisit the canonical if the page later moves behind a custom domain (Web Property
  Map governs; one Pages custom domain per repo).
- OG/Twitter tags: title, description, `og:image` (logo or a purpose-made card — decide at
  build), `og:url` = canonical.
- **No external requests**: fonts + images self-hosted in `rates/` (copy font files and
  needed images from `wp-rates-page`, read-only source at `c:\wp\wp-rates-page`).

## 7. Build & ship checklist (for the implementation session)

1. Build `rates/index.html` + `rates/css/` + `rates/fonts/` + `rates/img/` per this spec.
2. Verify: real browser open; phone width via the **390px-iframe trick** (per CLAUDE.md —
   headless Chrome fakes overflow below ~492px); AA contrast on navy; every link works;
   zero external requests; each section reads sensibly in isolation.
3. Fill in the real "last reviewed" date at ship time (both hero kicker and footer).
4. Update this repo's `CLAUDE.md` (new `rates/` section) and the **Web Property Map**
   (new public URL; also touches the map's open rates-consolidation items) — then tell Ry
   the map was updated, per standing instruction.
5. Ry repoints/creates the Wix link himself (R3) — not ours to do.
6. After Ry approves a good version: author the **handoff prompt for the `wp-rates-page`
   session** (see consistency contract §4) — the two repos are not connected.
