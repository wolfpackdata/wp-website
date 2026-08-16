# Creative brief — "Consolidation Under Pressure" case study

**To:** creative director + web development team
**From:** Wolf Strategy
**Deliverable:** a published case study built from two existing, finished pages
**Status of the content:** final and frozen. This is a re-skin and a re-frame, not a rewrite.

---

## 1. What you are getting

Two self-contained HTML files. Each is a single file with all CSS and JS inline, no build
step, no dependencies, no external requests.

| File | What it is | Live reference |
| --- | --- | --- |
| `ma-landscape-report.html` | The full report — ~11 sections, 7 tables, 4 custom figures, ~6,000 words | https://claude.ai/code/artifact/d513bb1a-bec8-41eb-9abe-fb4880a295eb |
| `ma-transaction-map.html` | A standalone full-width interactive timeline of 41 transactions | https://claude.ai/code/artifact/eb61290e-d70d-4fdd-ab30-adf424895fcd |

The report embeds a compact version of the map and links out to the standalone one.
**Both roles must survive in your build.**

Source of record for the prose is `01-ma-landscape-2016-2026.md` in the same directory —
use it if you need the copy as plain text.

---

## 2. The job

Turn these into a **case study** in your studio's visual identity: your palette, your
typefaces, your spacing and layout language, your motion. Add whatever case-study framing
you normally use — a cover, a problem/approach/outcome intro, credits, a results section.

The existing design is a deliberately utilitarian "consultancy document" treatment. **You are
not being asked to preserve any of its aesthetic decisions.** Replace the amber/graphite
palette, the serif-body/grotesk-heading pairing, the margin rail, all of it. What you are
being asked to preserve is the **content and the behavior**.

---

## 3. Hard constraints

### 3.1 Copy is frozen

Every word ships as written. That includes the parts that look like they could be trimmed:

- All figures **and their currency parentheticals** — `$8.2bn (≈€7.5bn)`, `€200m (≈$236m)`.
  The dual-currency treatment is a deliberate editorial standard; both values appear
  everywhere a monetary figure appears. Do not drop, round, or reformat either side.
- All **footnotes, captions, confidence labels, and methodology notes.** The "Confidence
  levels", "Known gaps", "Confidence note" and "Note on comparability" blocks are the
  credibility of the document. They are not filler.
- The **full source list** and every inline source link.
- Section numbering and the sequence of sections.

If a line seems to fight your layout, change the layout. Come back to us before changing a
word — some sentences are worded precisely because of what can and cannot be claimed from
the underlying evidence.

### 3.2 Structure and formatting retained

- **Section order and hierarchy** as-is: Executive summary → Two shocks → Deal record →
  Three deals → Five patterns → Value migration → Two disruptions → Implications → Watch list
  → Methodology → Sources.
- **All 7 tables keep all their columns**, including the narrow **`Src`** gutter — a single
  link glyph per row, pointing at the press release or filing that row is drawn from. 31 of
  43 rows are linked; the other 12 show a muted dash meaning "no primary source verified."
  **That distinction is load-bearing and must remain visually legible.** Style the glyph
  however you like; do not merge, hide, or drop the column.
- The **callouts, pull quotes, and bordered note blocks** are distinct from body copy and
  from each other. Two note variants exist — neutral and warning — and the difference is
  meaningful.
- Wide content (tables, the map) must scroll **inside its own container**. The page body must
  never scroll horizontally.

### 3.3 The standalone map's behavior must survive

This is the piece most likely to be lost in a rebuild. Spec in §4. Reproduce the behavior;
restyle it freely.

### 3.4 Theme handling

The pages currently render correctly in three states: explicit light, explicit dark, and
"system" (where only `prefers-color-scheme` applies). If you ship a single committed look
instead, that is fine — but paint every color and the page background explicitly so the page
never inherits its host's ground.

### 3.5 Accessibility floor

- Every source link keeps an accessible name (`title` + `aria-label`), because the visible
  label is an icon.
- Visible keyboard focus states throughout.
- Respect `prefers-reduced-motion` for any motion you add.
- Data marks keep ≥3:1 contrast against their surface; body text meets WCAG AA.

### 3.6 If you republish to the same Artifact hosting

A strict CSP blocks all external hosts: no font CDNs, no external stylesheets, no remote
images, no fetch/XHR. Inline the CSS and JS, embed fonts and images as data URIs, keep the
page under 16 MB. If you are hosting it yourself, ignore this.

---

## 4. Map behavior spec

The standalone map is the interactive centerpiece. Its behavior:

**Layout**
- Horizontal axis is time, **2014.0 → 2026.9**, linear, with gridlines and labels at each year.
- Four horizontal **lanes**: Macro & regulatory · Software & platform · Hardware manufacturing ·
  Retail & marketplace. Alternating lane tints. Lane name pinned at the left of each band.
- Each of the **41 events** is a dot at its announcement date, in its lane, with a short label.

**Responsive width — this is the point of the standalone version**
- Plot width = `max(1600px, containerWidth − 190px)`. It measures the viewport and **spreads
  to fill the tab**; on a wide monitor events separate and need fewer stacked rows, so it reads
  better than the embedded copy. It never compresses below 1600px — it scrolls instead.
- Re-renders on window resize (debounce ~140 ms).

**Collision-free label packing — do not hand-place labels**
- Events sort by date. Each label sits to the **right** of its dot, flipping to the **left**
  when dot + label would exceed the plot's right edge.
- Each event is assigned the **lowest vertical track** within its lane where its label span
  does not overlap an already-placed span (with an ~8px gutter). Lane height grows to fit the
  tracks used.
- This is why the map survives a resize and a palette change: nothing is positioned by hand.
  **If you rebuild it, keep a real packing pass.** Hand-placed labels will collide the first
  time someone changes a font or a viewport width.

**Encoding**
- Dot **fill** encodes disclosed deal value as an **ordered, sequential scale** — five steps:
  ≥$1bn · $500–999m · $100–499m · <$100m · undisclosed.
- Keep it **sequential in one hue, light→dark** (or dark→light in a dark theme). Do **not**
  convert it to a categorical or rainbow palette — the variable is magnitude, and a
  non-ordered palette makes it unreadable.
- "Undisclosed" is the **absence** of a value, not the smallest value: it reads as an unfilled
  ring, visually outside the ramp.
- Every dot carries a thin ring so the palest step stays visible against the lane tint.
- Dot **size is uniform.** Size carries no meaning; readability of the labels is the priority.
- A legend is always present.

**Macro bands**
- Two shaded spans behind the lanes: the **pandemic demand surge** (2020.20–2022.00) and the
  **2025 tariff regime** (2025.25–2026.75), each labeled in a reserved strip above the lanes.
- These are macro shocks, not transactions — they must read as clearly different from dots.

**In the report**, the same map appears at fixed width inside a horizontal scroller, with a
visible **"Open full width ↗"** affordance to the standalone page. Keep both.

---

## 5. What is yours to decide

Everything not listed above. Explicitly including:

- Palette, typography, type scale, spacing system, grid, and page composition
- Cover treatment, section transitions, scroll behavior, motion and micro-interaction
- How the case study frames the work — intro, approach, outcome, credits
- Whether the margin rail survives, and how sections are numbered or marked
- Photography, illustration, texture, and any brand furniture you add
- Whether the map's chrome (header, legend placement, footnote) is restyled or rebuilt

---

## 6. Two traps that already bit us

Worth knowing before you refactor the layout:

1. **CSS grid `1fr` has an implicit `min-width: auto`.** The map is 1780px wide inside a
   scroll container. In a `grid-template-columns: 1fr` track it forces the track to 1780px and
   stretches the whole page, squeezing every text column into a strip. Use `minmax(0, 1fr)`
   and put `min-width: 0` on the flex/grid ancestors between the track and the scroller.
2. **Cascade order beats media queries at equal specificity.** A `.rail{display:none}` placed
   *after* a `@media (min-width:1000px){ .rail{display:block} }` wins at every width. Because
   `display:none` removes the grid item entirely, the body content then falls into the narrow
   annotation column. Same-specificity base rules go **before** their media queries.

---

## 7. Acceptance checklist

- [ ] Word-for-word copy match against `01-ma-landscape-2016-2026.md`, including every
      currency parenthetical, caption, footnote and confidence note
- [ ] All 7 tables present with all columns; `Src` gutter intact; 31 links + 12 dashes
- [ ] Every source link opens in a new tab, `rel="noopener"`, with an accessible name
- [ ] Map: all 41 events, correct lanes, correct dates
- [ ] Map: resize the window — labels re-pack with **zero collisions** at every width
- [ ] Map: deal-value scale is sequential and ordered; undisclosed reads as unfilled
- [ ] Map: opens full width in its own tab, and is linked from the report
- [ ] Page body never scrolls horizontally at any viewport width
- [ ] Light and dark both legible; no color defined only inside a media query
- [ ] Keyboard focus visible throughout; `prefers-reduced-motion` respected

---

## 8. Notes on the content, for framing

Useful if you are writing the case-study wrapper. The report's argument, in one line: **music
revenue is at an all-time high and the companies that build the instruments captured none of
it** — and the 2024–26 wave of distress traces to two macro shocks (a pandemic demand spike
that reverted, and 2025 tariffs), not to a product or competitive failure.

The visual anchors, in order of strength: the **transaction map**; the **three outsider-buyer
deals** shown as entry-price → exit-price dumbbells (Masimo −$680m, Etsy −$170m, Sonova
pending); the **Reverb ownership diagram** (2019 Etsy →$275M→ Reverb; 2025 Etsy →$105M→ Servco
Pacific + Creator Partners, where Servco Pacific owns Fender); and the **revenue meters**
comparing global recorded music to the entire US music-products industry.

All figures are public-source and dated 11 August 2026. Currency conversions use disclosed
annual-average rates. If the case study is published later than Q4 2026, flag it — several
"watch list" items will have resolved and the page should say as of when it was true.
