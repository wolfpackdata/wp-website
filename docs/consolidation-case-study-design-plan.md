# Design plan — "Consolidation Under Pressure" case study

**Folder:** `case_studies/consolidation_under_pressure/`
**Public URL:** `https://intake.wolfstrategyllc.com/consolidation-under-pressure/`
**Built:** 2026-08-11 (#172) · **Deployed:** not yet
**Source material:** `wolfpackdata/dj-gear-study`, `docs/strategy/` — the report
(`ma-landscape-report.html`), the standalone map (`ma-transaction-map.html`), the prose
source of record (`01-ma-landscape-2016-2026.md`) and the creative brief
(`02-case-study-brief.md`). The last two are vendored into `planning/` here; see D-019.

---

## 1. What was asked for

A finished report and a finished interactive figure, rebuilt as a case study in this site's
visual identity. The brief freezes two things and opens everything else:

**Frozen** — every word, every figure with both currency parentheticals, every caption,
footnote, confidence label and methodology note, the full source list, the section order,
all seven tables with all their columns including the `Src` gutter, and the transaction
map's *behaviour*.

**Open** — palette, typography, spacing, grid, composition, cover, motion, the case-study
framing, whether the margin rail survives, and how the map's chrome is styled.

The existing design was a deliberately utilitarian amber-and-graphite consultancy document
in a serif body face with a sticky margin rail. The brief is explicit that none of its
aesthetic decisions need survive. None did.

## 2. Decision ledger

IDs are stable and are never renumbered. A superseded entry is struck through and annotated
in place. Entries marked ⚠️ are calls made without a ruling from Ry and are the ones to
read first.

| # | Decision | Why |
|---|---|---|
| **D-001** | It is a **case study in `case_studies/`**, not a standalone artifact, and it wears the Wolfpack navy | "Your studio's visual identity" is this site's, and `case_studies/` is the folder that owns long-form client-facing documents. It inherits that folder's whole convention set: the shared stylesheet, the six-use coral ration, no new hues, no client named, no invented outcome, the full Open Graph block, and rendering complete with JavaScript off |
| **D-002** | **Public and indexed** | Same reasoning the financial model case study carries. Its audience is founders, directors and operating executives, and being found is the point. Its sibling `transaction-map.html` is `noindex` — see D-020 |
| **D-003** | **The margin rail does not survive.** Part numbers become `.k` kickers in the flow | The brief left this open. Every page in this folder already does wayfinding with a sticky nav and scroll-spy; a second, parallel navigation device is one more thing to keep in sync for no reader benefit. It also sidesteps the cascade-order trap the brief warned about, since there is no rail to hide and un-hide |
| **D-004** | **The figure ground extends to rendered charts** (`.figframe`), joining `.shot`, `.ph` and `.dtable` | The token exists so a captured image sits in a frame of its own visual weight. A chart drawn in HTML is the alternative to a screenshot *of* a chart; the rule the scope encodes is "anything standing where a captured image would stand". `docs/site-brief.md` §1.4 updated in this PR |
| **D-005** | The map's deal-value scale is a **four-step neutral ramp on the figure ground, dark to light**, with "undisclosed" drawn as an unfilled ring outside the ramp | The brief requires an ordered sequential scale in one hue and forbids a categorical palette, because the variable is a magnitude. The sheet forbids new hues. A ramp along the figure ground's own neutral axis satisfies both, and it is an extension of an existing ramp rather than a new colour. Contrast measured against the lighter of the two lane surfaces: 3.6 / 6.6 / 10.6 / 16.7 : 1. "Undisclosed" is the absence of a value, not the smallest one, so bucketing it as the ramp's bottom step would be a claim the sources do not make |
| **D-006** ⚠️ | **A citation is not a destination.** The page carries one destination — the 30-minute intro call — plus 31 in-table source links and 51 source-list links | This fits no existing rule, so by the design skill's own instruction it is a new ruling and Ry has not made it. The argument for it: the destination count governs where the page *sends* a reader as an onward step in the funnel. A source link is provenance — the mechanism by which the document is checkable — and it is the same commitment the site's transparency posture already makes elsewhere. The brief also freezes the source list, so the alternative was not available. **Needs a ruling; if it goes the other way this page cannot exist in this form** |
| **D-007** | **The coral ration stays at six.** Nav CTA, hero rule, pull-quote rule, closing CTA, link hover, focus ring | The count only ever goes down. Fourteen places in the source used its amber accent; none of them became coral here. The refusals are now enumerated in `case-study.css`'s header: not a source-link glyph, not a deal-value step, not a macro band, not a highlighted table row, not a part number, not an era card, not the "open full width" affordance |
| **D-008** ⚠️ | Where the `.md` and the finished HTML say the same thing in different words, **the HTML's wording ships** — it is the later draft and is a superset in every case. Nothing that exists in only one of them was dropped. **One exception, and it is a word change the brief says to ask about first** | The brief names the `.md` as the source of record for prose and the acceptance checklist asks for a word-for-word match against it, but the finished HTML carries captions and clauses the `.md` never had. Carrying both is the only reading that cuts nothing. **The exception:** the HTML's Spotify paragraph ended *"…paid the music industry $8bn (≈€6.9bn) in the twelve months to June 2025, up from $8bn's predecessor figure of $6bn in 2021–22"* — a clause that is not in the `.md` and does not parse. The `.md` has a fact in the same slot: YouTube was *"up from 100m in Feb 2024"*. The page now reads *"…passed 125 million subscribers in March 2025, up from 100m in February 2024, and paid the music industry $8bn (≈€6.9bn) in the twelve months to June 2025."* **Flagged for Ry rather than done silently** |
| **D-009** ⚠️ | The map plots **42 events, not 41**, and both pages say 42 | The brief, and the standalone source page's own subtitle, both say 41. The standalone's dataset actually holds 42 rows; the embedded copy in the report held 41, because it was missing the April 2025 tariff event. So "41" described one of the two copies, and the two had drifted. Dropping a row to make the stated number true would be falsifying the figure. **Flagged** |
| **D-010** | **Ten tables**: the seven from the finished HTML, unchanged and with every column, plus three restored from the `.md` | Three `.md` tables carried facts the finished HTML had dropped when it converted them to stat tiles and figures — US paid subscription accounts (106.5m), US CD revenue ($312.4m, −11.6%), the paid-subscription share (52.4%), US vinyl's +9.3%. "The money in music, 2025" and "The money in gear, 2025" come back as a matched pair because the section is built on the comparison; Pattern 1's table comes back beside its dumbbell figure, the same table-plus-figure pairing the deal record already uses |
| **D-011** | The hero's stat tiles carry **artifact and method facts** — 43 transactions, 31 of 43 primary-sourced, 42 mapped events, 7 known gaps. **There is no results section** | The rule the financial model case study set. There is no instrumented outcome behind this document, and a tile reading "informed a $40m decision" would be the single most damaging thing this page could carry. The brief offered a results section; this folder's convention refuses to invent one, and this `CLAUDE.md` wins. What the wrapper says instead is how much was counted and how much of it can be checked |
| **D-012** | **One map script reading one dataset**, shared by both pages; the only difference is a `data-fill` flag | The source shipped the map twice as two copies of the same 200 lines, and the copies had already drifted by one event (D-009) with nothing able to see it. This is the folder's "one implementation of a shared thing" rule applied to the exact failure it exists to prevent |
| **D-013** | Label widths are **measured with canvas `measureText`**, not estimated from character count | The original used `label.length * 5.75 + 34`. That is a guess about a font, and the label font is `--mono`, a *system* stack whose metrics are unknowable from the build machine — the same trap `github/`'s button label carries. A guess that runs narrow packs two labels into one track and they collide. The character-count estimate is kept only as a fallback for a browser with no 2d context |
| **D-014** | `.rtable` and `.dtable` are `position: relative` | Found by measurement, not by eye. `overflow-x: auto` clips a wide table but does **not** clip an absolutely positioned descendant whose containing block is elsewhere — and with no positioned ancestor, "elsewhere" is the page. `.visually-hidden` is `position: absolute`, and there is one in every unsourced row's Src cell. They took their static position ~640px into the table, escaped every scroller above them, and gave the document 269px of horizontal scroll at 390px wide while every container measured correctly. Documented at length in the stylesheet, because the tell — an ancestor's `overflow: hidden` not fixing it — is the useful part |
| **D-015** | **Direction is a glyph, never a colour pair** (`.trend`, ▲ ▼ ▬) | The source used a green and a red. A semantic colour pair is atomic and neither half earned its way past the no-new-hues rule alone. The arrow was doing the work in the original design too; removing the colour removes nothing and survives a grayscale print and a colour-vision difference |
| **D-016** | The dumbbells distinguish entry, exit and unsold **by shape** — ring, filled disc, dashed ring | Same constraint, same answer. Every mark is also labelled with its own figure at its own position, so shape is a scanning convenience and never the sole carrier |
| **D-017** | The brief's two note variants are `.aside` and `.aside--warn`, differing by a brighter left rule and the label text ("Note" / "Caution") | Reuse over addition: `.aside` already was the bordered note block. A red rule would read as an error state; these are caveats, which is the same reasoning `.status`'s gray chips already carry |
| **D-018** | `.callout` and `.callout--big` added; **`.pull` stays one per page** | The sheet's rule is one pull quote per page — "two pull quotes is shouting". This document has eight lifted lines. `.pull` goes to the one that is the page's thesis ("A phone plus a subscription DAW plus one interface now clears a bar that once required a studio"); the rest are callouts, quieter by every means except size |
| **D-019** | The source `.md` is **vendored into `planning/`** and guarded by `planning/verify_copy.py` | The report's copy now exists in two repos. The site brief's own rule is that any string in more than one artifact gets a machine guard or it will diverge, and the three largest duplications on this property are unguarded precisely because nobody wrote one. Vendored rather than referenced because a check that reaches into a sibling clone reports nothing on most machines. The guard checks every numeric token, the Src arithmetic, link accessibility, the map dataset, and the external-resource stance — and fails loudly if its own anchors move |
| **D-020** | `transaction-map.html` is **`noindex, follow`** and carries no Open Graph block; it is not a row in `check_meta.py`'s table | One figure with no prose is thin content that would compete with the case study for the same queries, and the case study should win those because it explains the figure. `follow` because the link back to the report is worth crawling. A card exists so a page survives being pasted somewhere; the page that gets pasted is the report |
| **D-021** | The social card's inset is **the transaction map**, captured by a generator that ships with it | A card needs a raster and the map exists only as something a browser draws. Redrawing an approximation in Pillow is how a card and the thing it advertises stop being the same picture. `planning/card/capture_map.py` renders the real page and crops the plot out of it; `social-cards/build_cards.py` composes. Both under the repo's standing rule: **rebuild rather than retouch**. At the 360px a LinkedIn Featured tile renders, the inset is texture — and 42 labelled events across four lanes reads unmistakably as a dense research document, where a crop of prose would read as any page of any website |
| **D-022** | The closing block has **one CTA and no second destination**, and its copy describes the shape of the work rather than a result | The book-first rule. It also cannot claim an engagement outcome, per D-011, so what it offers is the method: a dated record with a link on every row, checkable figures separated from unverifiable ones, and the gaps stated |

## 3. What was deliberately not carried over

Recorded because a derived design should say what it refused, not only what it took.

- **The amber accent, on all fourteen of its uses.** Coral is at six and spent (D-007).
- **The green/red direction pair and the cyan/red macro bands** (D-015).
- **The serif body face.** This site is Montserrat and already carries it; adopting a second
  body family would buy nothing the existing stack cannot do, and would mean self-hosting a
  family for one page.
- **The sticky margin rail** (D-003).
- **The `.md`'s production notes** — the two italic lines telling the page builder *"the
  published page carries this as a scrollable transaction map"* and *"…as a diagram"*. They
  describe the page you are looking at.
- **The two `claude.ai/code/artifact/…` URLs** in the `.md`'s front matter. They pointed at
  the pages this one replaces.

## 4. Verification performed, 2026-08-11

Measured, not eyeballed. Method: the real pages rendered in a narrow `<iframe>` inside a
wider host page, per this repo's phone-width workaround — headless Edge clamps its window to
about 492px and then crops, which fakes overflow on any direct "mobile" capture.

| Check | Result |
|---|---|
| Horizontal overflow, both pages, at 320 / 390 / 768 / 1024 / 1440 / 1920 | `scrollWidth − clientWidth = 0` everywhere. **Failed first at 320 and 390** — see D-014 |
| Map label collisions, both pages, at every width above | **0**, against every pair of labels sharing a track |
| Map re-pack on resize | Plot spreads 1804 → 1867 → 2467 → 3067px as the window widens, tracks fall 19 → 18 → 15 → 14, zero collisions at each. Never below the 1600px floor |
| Map dataset | 42 events, 4 lanes, 2 bands, 13 year gridlines, every lane index and value bucket in range |
| `Src` gutter | 43 cells: 31 links + 12 dashes. Every link has `target="_blank"`, `rel="noopener"`, `title` and `aria-label`; every dash has a visually-hidden sentence |
| Copy against the source `.md` | Every one of 186 numeric tokens present. Two were missing on the first pass (Spotify's +12% MAU and +14% revenue) and were restored |
| JavaScript off | 94 table rows, 31 source links, ~7,900 words render; no `.js` class, no dots drawn, the map's static fallback visible |
| External requests | Zero. Grep for `@import`, remote `url(…)`, and absolute `src`/`href` on `script`/`link`/`img`; the only absolute hrefs are the two canonicals |
| Inline `<style>` | None on either page |
| `social-cards/check_meta.py` | 11 pages PASS, including this one |
| `planning/verify_copy.py` | clean |

## 5. Open items

1. **D-006 needs Ry's ruling** — whether a citation counts against the destination policy.
   Everything else on this page is settled by an existing rule; this one is not.
2. **D-008 and D-009 are flagged word/number changes.** The brief says to come back before
   changing a word, and there was no way to ask mid-build. Both are one line each and both
   are reversible.
3. **Not deployed.** `/consolidation-under-pressure/` 404s until the folder and the updated
   `case-study-assets/` are copied into `wolfpackdata/ai-coaching-intake`. Two folders, and
   `planning/` never deploys.
4. **The Web Property Map goes stale on deploy** — a new page and a new URL. Update the
   Notion page in the same round.
5. **The report is dated 11 August 2026 and says so.** Several Part Nine watch-list items
   will resolve; the closing fine print already tells the reader to read it as of its issue
   date, which is the brief's own instruction for a later publication.
