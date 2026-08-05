# SetMaster 3 landing page — design spec

The "hype page." Ry's creative brief, verbatim:

> *"More like if Native Instruments owned SetMaster 3 and had a landing page for
> it, and they were showing its origin story and its awesome functionality."*

- **Page:** `intake.wolfstrategyllc.com/setmaster3/` · **indexed**
- **Audience:** people who might hire Ry first; advanced and technical DJs second.
  **Not beginners** — Ry was explicit. *"It's supposed to be impressive as well."*
- **Depth:** highlights drawn from the case-study material, with *"the history
  just being interesting"* — not a second telling of the case study.
- **Status:** spec. Not built.

---

## 1. The concept

**A product page for software that exists.**

Native Instruments' own product pages work because they are dense, dark, and
photographic in a very specific way: the *interface itself* is the imagery. There
is no metaphor photography, no smiling people, no abstract gradient meaning
"innovation." A knob, a waveform, a browse list. The page looks like the thing.

That is the whole brief, and it produces a hard rule — the same shape as the one
that governs the `hire/` pages, because it prevents the same failure:

> **Every visual element on this page is one of four things:** (a) a screenshot or
> screen recording of SetMaster 3; (b) a screenshot of the SetMaster 2 workbook,
> for the origin story; (c) a data structure rendered honestly — a spec table, a
> release stat; or (d) typographic hierarchy. **Nothing else.** No stock
> photography, no DJ-in-a-club imagery, no vinyl or headphone iconography, no
> waveform decoration that isn't real data, no gradient meshes, no floating
> 3D mockups on angled planes.

The temptation on a DJ-tool page is enormous and every bit of it is corny. The
restraint is the design — and it also happens to be the only option available,
since D-006 forbids shipping a single Native Instruments asset.

**Three highest-leverage moves,** in order of what they buy:

1. **The hero video.** A screen recording of Ry using the app is worth more than
   every word on the page. It is also the one thing here Claude cannot make —
   hence `03-assets-and-capture-list.md` and D-007.
2. **The transition-row explainer.** The one product idea a visitor must
   understand: one row is one transition, out-track left, in-track right. If they
   get that, everything else on the page makes sense. If they don't, the
   screenshots are noise.
3. **The download block.** The page exists to be downloaded from. It is the only
   place orange is allowed to be a fill.

---

## 2. Design system

Ported from `setmaster3/planning/03-ui-design.md` §3 — **the app's real tokens,
not an approximation.** The page and the product must be able to sit side by side
in a screenshot without the difference being visible.

```css
/* Surfaces */
--bg-app:        #0A0A0A;   /* page background */
--bg-panel:      #141414;   /* cards, bands, nav */
--bg-row:        #1A1A1A;   /* inset panels, code blocks */
--bg-row-alt:    #151515;
--border-subtle: #2A2A2A;   /* panel edges only */

/* Text */
--text-primary:   #E6E6E6;
--text-secondary: #9C9C9C;
--text-muted:     #5E5E5E;

/* Signal accents — NI */
--accent-orange: #FF6A00;
--accent-blue:   #3D7BFD;

/* Brand accents — SetMaster */
--brand-magenta: #FF4FD8;   /* OUT track identity */
--brand-cyan:    #4DE8E8;   /* IN track identity */
--brand-purple:  #9B5CFF;   /* wordmark accent, section headings */

/* Type */
--font-ui:   "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, monospace;
```

**Type at web scale.** The app's tokens are sized for a dense 13px data grid and
must not be used literally on a marketing page. The relationship carries; the
scale does not:

| Role | Page | Echoes the app's |
|---|---|---|
| Display | Inter 700, `clamp(2.5rem, 6vw, 4.5rem)`, tight leading | `--type-display` wordmark |
| Section heading | Inter 600, 1.75rem, in a brand accent | `--type-heading` |
| **Label** | Inter 600, 0.6875rem, **uppercase, +0.06em tracking** | `--type-label` — **the signature NI move.** Kickers, stat labels, spec-table headers, button micro-labels. Used generously; it is what makes the page read as an instrument panel |
| Body | Inter 400/500, 1rem–1.125rem, `--text-secondary` | `--type-body` |
| Numerals | `font-variant-numeric: tabular-nums` **everywhere a number appears** | the borderless-grid rule |

4px spacing base. Radii 4px (chips, inputs) / 6px (panels, buttons). **No drop
shadows** except on overlays — elevation is background-lightness steps, per the
app.

### The accent ration

Goes in the header comment of `sm3-assets/css/sm3-landing.css` and must stay
true — same discipline as `rates/css/rates.css` and `hire/assets/css/hire.css`.
Four accents is three more than those pages carry, so the ration matters *more*
here, not less.

**`--accent-orange` — fill allowed, 3 uses:**
1. the primary download button (the page's only solid CTA)
2. the nav download button
3. the live "v3.0.3 · released 2026-07-31" status dot

**`--accent-orange` — as text/border, 2 uses:** stat-tile values in the hero;
focus-ring and link-hover.

**`--brand-magenta` / `--brand-cyan` — 1 use each, always as a pair:** the OUT/IN
column-group identity, wherever a transition row is depicted — the explainer
(§4.3), screenshot captions, and the section-heading rule of the set-editor
feature block. **They are never used decoratively and never appear alone.**
Magenta without cyan is a bug; it means the Out/In semantic was borrowed as a
color.

**`--brand-purple` — section headings and the wordmark lockup only.**

**`--accent-blue` — focus states only.** It is the app's focus color and stays
that here.

**Where an accent is a fill, text on it is `#0A0A0A`, never white.** `#FF6A00`
against white is 2.9:1 and fails AA; against near-black it is 8.4:1.

---

## 3. Trademark and honesty guardrails

These are not stylistic. A public, indexed page carries obligations a local app
does not, so `setmaster3/planning/03-ui-design.md` §1.3 is inherited **and
tightened**:

1. **No Native Instruments asset, ever** — no logo, logotype, icon, product
   screenshot, or bitmap lifted from Traktor® or Rekordbox®. Not in the hero, not
   in an "integrates with" strip, not in the favicon, not in an OG image. The
   brief is *"as if NI owned it,"* which is a statement about typography and
   density, not about borrowing marks.
2. **® on every visible** "Traktor", "Native Instruments", "Spotify" — including
   in `<title>`, meta description, OG tags, alt text, and structured data.
   **"Exportify" renders plain.**
3. **The unaffiliated line ships in the footer, not buried:**
   *"SetMaster 3 is independent fan software and is not affiliated with, endorsed
   by, or sponsored by Native Instruments®, Spotify®, or Exportify. Traktor® is a
   registered trademark of Native Instruments GmbH. Spotify® is a registered
   trademark of Spotify AB."*
4. **No claim of macOS support** until an artifact exists and the checklist passes
   (C-03). The page says what is true, in the download block, in one line.
5. **No invented adoption.** No user counts, no testimonials, no "trusted by," no
   star ratings, no fake press logos. The page has real proof — a public release
   with a sha256, a passing test suite, three years of professional use — and it
   uses that instead.

---

## 4. Information architecture

Eleven bands. Ordered so a visitor who leaves after two screens has still seen
what it is and how to get it.

| # | Band | Ground | Purpose |
|---|---|---|---|
| — | Sticky nav | `--bg-panel`, blurred | Wordmark · anchors · orange download |
| 1 | Hero | `--bg-app` | What it is, the video, both buttons |
| 2 | The two jobs | `--bg-panel` | Set prep and catalog analysis, side by side |
| 3 | The transition row | `--bg-app` | The one idea. The explainer |
| 4 | Set editor in depth | `--bg-panel` | Screenshot-led feature reel |
| 5 | Catalog analysis in depth | `--bg-app` | Matrix + compare, screenshot-led |
| 6 | Origin story | `--bg-panel` | Three panels: spreadsheet → SM2 → SM3 |
| 7 | Built in the open | `--bg-app` | Offline, read-only, no telemetry, tested |
| 8 | **Download** | `--bg-panel`, bordered | The conversion band |
| 9 | Roadmap & honesty | `--bg-app` | Rekordbox® planned; macOS pending; work in progress |
| 10 | Who made this | `--bg-panel` | One authored moment → case study, intro call, site |
| 11 | Footer | `--bg-app` | Trademarks, disclaimer, links |

### 4.1 Sticky nav

Wordmark lockup left: the RML mark (from `setmaster3/docs/design/brand/rml-mark.svg`)
+ **SetMaster 3** re-set in Inter — never a bitmap of a wordmark, per the RML
usage rules. Anchors center, in `--type-label` style. Orange **Download** button
right. Collapses to wordmark + button below 760px; anchors move into a details
disclosure, not a hamburger overlay.

### 4.2 Hero

```
┌──────────────────────────────────────────────────────────────────┐
│  ▪ RML   SETMASTER 3                            [ Download ]     │
├──────────────────────────────────────────────────────────────────┤
│  OFFLINE · LOCAL · YOUR COLLECTION STAYS YOURS                   │
│                                                                  │
│  Set preparation                                                 │
│  for people who prepare.                                         │
│                                                                  │
│  A structured transition editor and a catalog analyzer for        │
│  Traktor® and Spotify®. Runs entirely on your machine.           │
│                                                                  │
│  [ ⬇ Download for Windows ]  [ View on GitHub ↗ ]                │
│  ● v3.0.3 · released 2026-07-31 · 72 MB · free                   │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │                                                            │  │
│  │          [ HERO VIDEO — see A-V1 ]                         │  │
│  │                                                            │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ▸ In pro use since 2023       ▸ 867 tests   ▸ reads Traktor®    │
│                                  passing       strictly read-only │
└──────────────────────────────────────────────────────────────────┘
```

- **Kicker** in `--type-label`, `--text-secondary`. The three words that
  differentiate the product from everything cloud-based.
- **Headline** is two lines, the second in `--text-secondary`. Draft only —
  alternatives in §10.
- **Buttons:** orange solid (OS-detected, §6) + ghost with `--border-subtle`.
- **Status line** in mono, with an orange dot. Version, date, size, price — all
  four facts a technical visitor wants before clicking, given without a click.
  **Generated, never hand-typed**; see §6.4.
- **Stat row** reuses the `▸`-bullet pattern from `hire/`. Values in orange,
  labels in `--type-label`. The tenure stat is **"in pro use since 2023"** (C-07)
  — a year, not a duration, so it never needs updating and never goes stale.
- **The video is the hero's center of gravity.** Until it exists, the frame
  carries the designed placeholder (§9) at the exact final aspect ratio, so the
  hero's composition never changes when the real file lands.

### 4.3 The transition row — the explainer

The most important band on the page and the one most likely to be cut for being
"not marketing." It is marketing: it is the reason a DJ understands why this is
not a spreadsheet.

A single row rendered in the app's own styling — borderless, tabular numerals,
row striping, the OUT group headed magenta and the IN group headed cyan — with
callouts:

```
  ┌─ OUT TRACK ──────────────────┬─ IN TRACK ───────────────────┐
  │ ● magenta group header        │ ● cyan group header          │
  │  Track      T #   Lows  Level │  Track      M #   BPM   Key  │
  │  ─────────────────────────────┼──────────────────────────────│
  │  Nightdrive  3    OUT   HOT   │  Cosmic Dub  2   122   Gbm   │
  └───────────────────────────────┴──────────────────────────────┘
     ▲ where you leave                ▲ where you land
     
     "One row is one transition. Read it left to right."
```

Copy beat, adapted from Ry's own framing: Traktor® and Rekordbox® read
top-to-bottom, one track per row, and notes are hard to read there. SetMaster
reads **left to right** — where you're coming from, where you're going, and every
cue you set yourself for the move between them.

**Build it in HTML/CSS, not as an image.** It is a table; it should be a table.
It stays sharp at every density, it is readable by a screen reader, it costs
nothing to load, and it can't go stale against a UI change the way a screenshot
does.

### 4.4 / 4.5 Feature bands

Alternating image/text rows — screenshot in a 16:9 frame with a 1px
`--border-subtle` and 6px radius, copy beside it, `--type-label` kicker over each.

**Set editor (band 4).** Four beats: the grid and its formatting (RED / YELLOW /
box, exactly as the app names them); **your own emoji palette**; the **mix timer**
— *"so you know how long sections are and how long your whole mix is"*; export to
CSV, XLSX, and Markdown.

#### The flight-to-LA anecdote — ON this page (Ry, 2026-07-31, final)

**Decision history, kept because this flipped twice.** Round 3 planned it. Draft 1
of the copy cut it, on the reasoning that the flight was SetMaster 2 and its
payoff depends on a performance view SM3 has not rebuilt. **Ry overruled that:
which version it was does not matter to this particular story.**

He is right, and the cut was over-cautious. The anecdote's subject is **the
workflow** — prepare somewhere, play somewhere else, and the notes carry across.
That workflow is what SetMaster 3 does. The version number is an artifact of the
telling, not the point of it, and the aside never claims a feature.

**The copy, ~45 words, three sentences, beside the set-editor screenshot:**

> Prepped on a plane to a Los Angeles gig. Found transitions worth adding to an
> already-finished set, and locked them in well enough to play them that night.
> During the set, switched back to read the notes from that afternoon.

**Two guardrails it keeps:**

1. **It names no version and no feature.** "Switched back" is what happened; it
   does not assert a performance view, so nothing here contradicts band 9's
   Perform Mode line or the honesty discipline behind it.
2. **It is not styled as a testimonial.** §3.5's ban stands. A testimonial is a
   stranger vouching; this is the maker describing his own use. The distinction
   is real but thin, so protect it in the styling: **no quotation-mark graphic, no
   avatar, no star rating, no attribution card.** Mono, `--text-secondary`, no
   border. If it starts looking like a pull quote, it has crossed the line.

It earns the space because it is the only thing on the page showing **preparation
and performance as one artifact**, which is the product's actual argument and is
invisible in a feature list.

**Ry's *"beyond just a fancy spreadsheet"* line still stays off this page.** It
answers an objection a case-study reader forms; on a product page, raising the
comparison is the only thing that would plant it.

**Catalog analysis (band 5).** Three beats: compound filter and sort across the
whole collection, of a kind Traktor® itself cannot do; the Spotify®↔Traktor®
comparison that turns *what you've been listening to* into *what you don't own
yet*; notes on the comparison that **survive every re-run**.

**One honest framing rule, carried from the repo:** catalog analysis is the
optional half. The page must **never present Traktor® as a prerequisite** — the
repo states this as a binding rule and it applies to marketing copy at least as
much as to UI copy. Band 4 comes before band 5 for exactly this reason, and band
5 opens by saying the tool works fine without it.

### 4.6 Origin story

Ry's constraint: *"the history just being interesting."* Three panels, ~70 words
each, horizontal on desktop and stacked on mobile:

| | 2023 → | ~2024 → | 2026 |
|---|---|---|---|
| **The spreadsheet** | Google Sheets, then Excel. One row per transition. Built on planes between gigs — and used in professional sets from the start. | | |
| **SetMaster 2** | | VBA and Python behind the workbook. The Traktor® collection becomes queryable data. | |
| **SetMaster 3** | | | Specified first, then rebuilt as an offline web app. |

**Dates resolved by C-07/C-08**, with one caveat: **2023 and 2026 are stated and
sourced; the middle year is derived** from Ry's *"used it for like a year"* before
SM2. If he doesn't confirm ~2024, the panels drop the year row and lead with the
names — which reads fine and removes the only soft fact on the page.

**Do not write "Windows and macOS" in the SM3 panel** (C-03). The panel describes
the rebuild, not the shipping platforms.

The strongest line in this band is *"used in professional sets from the start."*
It is the fact that separates this from a side project, and it belongs in the
first panel, not the last.

Closing line links to the case study: *"The full story: the specification, the
port, the tests, and what is still unfinished."* This is the page's **only** link
to the case study and it lives here, not in the nav.

### 4.7 Built in the open

Four claim cards, `--type-label` heading + one sentence, each one true and
checkable:

| Card | Claim |
|---|---|
| **Offline by design** | Local backend, browser UI on `localhost`. No cloud, no accounts, no telemetry, no external calls. |
| **Read-only, always** | Your `collection.nml` is opened strictly read-only and never modified. |
| **Tested** | 867 automated tests across the pipeline, the app, and the UI. The pipeline is verified byte-identical to its predecessor on real data. |
| **Open source** | Public repo, MIT-licensed, sha256 published with every release. |

The test figure is 206 backend + 624 frontend unit + 37 end-to-end, as of v3.0.3.
It moves every round, so it is one of the values declared once and read from a
single source per §6.4 — not typed into four cards.

### 4.8 Download band — the conversion moment

Full spec in §6. Visually: a bordered `--bg-panel` band, the orange button
centered and oversized, the platform table below it, and the "no Python, no Node,
no terminal" line — which is the single most reassuring sentence available for
the technical-but-not-developer audience this page is aimed at.

### 4.9 Roadmap & honesty

Deliberately included, and it is the band that separates this from a hype page
that overclaims. Three lines, `--type-label` status chips:

- `PLANNED` — **Rekordbox® collection import.** No timeline.
- `IN PROGRESS` — **macOS build.** Written and structurally verified; not yet
  built or tested on a Mac.
- `DEFERRED` — **Perform Mode** and the natural-language filter bar.

Framing sentence: *"SetMaster 3 is actively developed and played with in real
gigs. This is what is next, and what is not ready."*

The Perform Mode line gains one clause now that the case study has established why
it matters: *"specified and waiting, not abandoned."* The workbook had a
performance view; this version has not rebuilt it yet, and saying so is the same
discipline as the macOS line.

### 4.10 Who made this

The page's one authored moment (see `00-overview.md` §9, item 5). A short block —
portrait, two sentences, three links: the case study, the intro call
(`calendar.app.google/zHNd1NA9wzb4VRLw5`), and `wolfstrategyllc.com`. Ghost
buttons; **no orange** — the download stays the page's only solid CTA.

Both the intro call and the main-site link come straight from the transcript.

### 4.11 Footer

Wordmark, the trademark and disclaimer block (§3.3), repo link, license, version.
Mono, `--text-muted`, hairline above.

---

## 5. Deliberately not on this page

- **Pricing / tiers.** It is free and there is nothing to price.
- **A comparison table against other DJ tools.** And specifically **no Lexicon
  mention** — see `01-case-study-outline.md` §9.
- **Testimonials, user counts, "trusted by."** None exist (§3.5).
- **A newsletter or email capture.** The funnel is book-first; the CTA is the call.
- **Traktor®/Rekordbox® logos** in an "integrations" strip (§3.1).
- **The Anthropic-portfolio framing.** It belongs on the case study, aimed at
  employers; on a product page it is a non sequitur to a DJ.

---

## 6. The download component (D-005)

The transcript's ask: *"two buttons, one to go to the public repo in a new tab and
another one just to download in one click. But I guess they'll have to choose
Windows or Mac, and which Mac."*

### 6.1 The constraint

The public repo's latest release, `v3.0.3` (2026-07-31), carries **one** asset:
`SetMaster3-3.0.3-windows-x64.zip` (72 MB). There is **no macOS artifact** — the
`.command` launchers and `build-macos.sh` exist and are structurally fixed, but no
build has ever been run on a Mac, and the repo says so in its changelog.

So the "which Mac" question (arm64 vs x64) is not yet live. The component is built
to handle it, and today it resolves to a truthful unavailable state.

### 6.2 Behavior

```
                    ┌─────────────────────────────┐
   platform detect  │  navigator.userAgentData    │
   (progressive)    │  .platform → fallback UA    │
                    └──────────────┬──────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
    Windows                      macOS                  Linux / unknown
        │                          │                          │
  ┌─────────────┐          ┌───────────────┐         ┌────────────────┐
  │ ⬇ Download  │          │ macOS build   │         │ Choose your    │
  │ for Windows │          │ coming soon   │         │ platform ▾     │
  │  72 MB      │          │ [ Watch repo ]│         │ (full table)   │
  └─────────────┘          └───────────────┘         └────────────────┘
        └──────────────── [ View on GitHub ↗ ] ───────────────┘
```

- **Windows** → the orange button links **directly to the release asset URL**.
  One click, one file, no interstitial. That is the transcript's ask, satisfied.
- **macOS** → the primary slot renders a `--bg-row` panel, not a disabled orange
  button. Copy: *"The Mac build is not ready yet. It is written, and it is waiting
  on a Mac to build and verify it. Watch the repository and it will appear here."*
  With a ghost **Watch the repo** button. A grayed-out button that does nothing is
  worse than an honest sentence.
- **Linux / unknown / no JS** → the full platform table, which is also always
  present further down the band for anyone downloading for a different machine
  than the one they're browsing on. This is a real case and the reason the table
  is never *only* behind detection.

### 6.3 No-JS behavior is the base case

The band is authored in HTML as the **platform table with every option visible**.
JavaScript's only job is to *promote* the matching row into the primary slot. With
JS off, disabled, or broken, the visitor sees a complete, working download table.
Nothing is hidden by default and revealed by script.

This is the same rule the `hire/` pages apply to their reveal animation, for the
same reason: **a download page that requires JavaScript to offer a download is
broken.**

### 6.4 Keeping the version honest

Version, date, size, and asset URL appear in at least four places (nav, hero
status line, download band, structured data). Hand-maintaining them across a
release is how a page ends up advertising v3.0.3 a year later.

**Rule:** they are declared **once**, in a `data-*` block or a small inline JSON
object at the top of the page, and every appearance reads from it. Updating the
page for a new release is a one-object edit.

**Deliberately not doing:** fetching `api.github.com/repos/…/releases/latest` at
runtime. It would keep itself current, and it violates the no-external-requests
rule every page in this repo keeps — plus it makes the download band depend on a
third-party API being up. Flagged here because it is the obvious suggestion and
the answer is no.

**Follow-up this creates:** a release of SetMaster 3 now has a downstream step —
update this page. That belongs in the `setmaster3` repo's release checklist, not
just here, or it will be forgotten exactly once and then permanently.

---

## 7. SEO (indexed — D-003)

The only page in this folder that gets any of this.

- `<title>` — **SetMaster 3 — offline DJ set preparation and catalog analysis for
  Traktor®** (~70 chars)
- Meta description, ~155 chars, leading with *offline* and *free*.
- Self-referential canonical: `https://intake.wolfstrategyllc.com/setmaster3/`
- OG + Twitter card. **The OG image is a real screenshot** with a title bar
  composited over it — 1200×630, self-hosted. Not a stock graphic, not a mockup.
- **`SoftwareApplication` JSON-LD**: name, applicationCategory
  `MultimediaApplication`, operatingSystem `Windows`, softwareVersion, downloadUrl,
  `offers` with `price: 0`, license, author. `operatingSystem` lists **Windows
  only** until the Mac artifact ships — the structured data cannot claim what the
  page won't (C-03).
- The public repo's `homepage` field points here. Highest-value inbound link
  available, and it is currently empty.
- Real `alt` text on every screenshot describing *what the screen shows*, not
  "screenshot of SetMaster 3."
- ~~No sitemap entry for the case study, it is noindex.~~ **The case study went
  indexed on 2026-08-04** (D-003 revised), so it belongs in a sitemap on the same
  terms as this page. Note this repo has no sitemap at all today, so there is
  nothing to add it to yet.

---

## 8. Motion and performance

- **Reveal on scroll:** one `IntersectionObserver`, fade + 12px rise, 500ms,
  60ms stagger, unobserve after firing. Same ~50-line vanilla pattern as
  `hire/assets/js/reveal.js` — **reuse it, don't rewrite it.** No libraries.
- **`prefers-reduced-motion: reduce` bypasses everything**, including video
  autoplay. The observer never attaches; everything renders final-state.
- **Video rules, all non-negotiable:** `muted`, `playsinline`, `preload="none"`,
  a real `poster` frame, visible controls. The hero video may autoplay-loop
  **only** if it is silent, under 15 seconds, and reduced-motion-aware; every
  other video is click-to-play. No video ever plays audio without a click.
- **Budget: ≤ 6 MB total, hero video excluded from first paint.** Screenshots are
  `loading="lazy"` below the fold, sized with explicit `width`/`height` to hold
  layout, and served as WebP with a JPEG fallback.
- **Zero external requests.** Fonts (Inter, JetBrains Mono) self-hosted as woff2
  in `sm3-assets/fonts/`. Video self-hosted in `sm3-assets/video/`. This is why
  §3 of the capture list caps video length — a YouTube embed would solve the
  weight problem and break the rule.

---

## 9. Placeholder contract (D-007)

Every media slot ships as a **designed placeholder at the exact final aspect
ratio**, so dropping the real file in changes nothing about the layout.

A placeholder is: a `--bg-row` panel, a 1px dashed `--border-subtle`, a centered
`--type-label` caption naming what goes there and its target dimensions, and a
mono asset id (`A-V1`, `A-02`…) matching `03-assets-and-capture-list.md`. Never
a gray box, never a "coming soon," never a stock image standing in.

**The page must look deliberate with every placeholder still in it** — that is the
test. It is also the same pattern the `hire/` pages used for their case-study
frames, which is the proof it works.

---

## 10. Headline options

| # | Headline | Reads as |
|---|---|---|
| 1 | *Set preparation for people who prepare.* | Confident, a little exclusive, matches "not for beginners." **Recommended.** |
| 2 | *Your catalog, finally queryable.* | Leads with catalog analysis — the wrong half first (§4.5). |
| 3 | *One row. One transition.* | Leads with the core idea; needs the subhead to carry all the context. |
| 4 | *The tedious part, automated.* | Ry's own framing. Truest to the thesis, weakest as a hero. |

---

## 11. Voice

Added after the case study was drafted, because writing it exposed that this spec
described the page's *look* in detail and its *voice* not at all. The house style
is [`docs/ryan-blog-tone.md`](../../docs/ryan-blog-tone.md), and its §8 says
explicitly that landing pages inherit the mechanics.

**Carries over unchanged, and it is a lint pass, not a preference:**

- **Zero em dashes and en dashes.** The single most reliable tell of off-voice
  copy in this repo. Use a period, a comma, or a colon.
- **Zero exclamation points. Zero rhetorical questions.** No *"So what does that
  mean for your sets?"* The page tells, it does not ask.
- **No contractions.** "is not", "does not", "it is". Three violations were caught
  in this spec's own draft copy after the case study was written, which is the
  argument for having this section at all.
- **Quotation marks only around language held at arm's length**, never for
  emphasis.
- **Reject list:** hype, magic, seamless, revolutionary, game-changing, unlock,
  supercharge, cutting-edge, empower, synergy, "leverage" as a verb, "10x".
  A DJ-tool page will reach for most of these unprompted.
- **Numbers specific and hedged**, never rounded up for effect. "about 7,000",
  not "10,000+".
- **Every strong claim followed immediately by its limit.** Band 9 is this rule
  scaled up to a whole section, which is why it stays.

**Adapts for a page rather than a post:** "you" appears earlier and more often
than in a blog post, because a landing page is already direct address. Role
naming still applies in the hero.

**The reversal (§4.1) is the device to use for section intros.** Two sentences,
parallel openings, negative first. The case study produced one that belongs on
this page, in band 3 above the transition-row explainer:

> The problem is not having too little music. The problem is getting from an idea
> in your head to the tracks that fit it.

**One rule that does not carry over.** The tone guide's 350-to-1,200-word length
is scoped to blog posts. It does not govern this page, and it does not govern the
case study either, which runs to about 2,700 words by design.

**Where the two pages differ in voice.** The case study is first person: Ry
narrating what he did. **This page is not.** It is a product page, and it speaks
about SetMaster 3 in the third person until band 10, which is the one authored
moment and the only place "I" is allowed. Mixing them is the fastest way to make
the landing page read like a personal blog post with a download button on it.

---

## 12. Open items for Ry

All nine claim conflicts are closed (`04-claims-ledger.md` §2). Remaining:

1. **Headline** (§10) and the hero kicker.
2. **Does the page name Ry at all** beyond band 10? (`00-overview.md` §9.5)
3. **Video count and length** (§8, and `03-…` §3) — the critical-path blocker, and
   the only thing here Claude cannot produce.
4. **The SM2 year in the origin band** (§4.6) — confirm ~2024 or drop the year row.
5. **Is band 9 (Roadmap & honesty) welcome on a hype page?** Recommendation: yes,
   emphatically. It is what makes the other ten bands believable, and this
   audience is technical enough to notice its absence. The case study's
   *What Is Not Finished* section is the same argument at length, and it is the
   strongest section in the piece.
6. ~~Confirm the anecdote cut~~ — **CLOSED.** Ry reinstated it (§4.4): which
   version the story used does not matter to it. The aside names no version and
   no feature.
