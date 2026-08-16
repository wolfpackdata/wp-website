# Design plan — "Consolidation Under Pressure" case study

**Folder:** `case_studies/consolidation_under_pressure/`
**Public URL:** `https://intake.wolfstrategyllc.com/consolidation-under-pressure/`
**Built:** 2026-08-11 (#172) · **Deployed:** 2026-08-15 (`ai-coaching-intake#74`), from
`develop 64fa14d`, both pages
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

### Round two — Ry's review, 2026-08-15 (#195)

Nine changes. Four of them are evidentiary and are the reason the round exists; the rest are
presentation. The through-line of the four: **the page was claiming more than its sources
carry**, and every fix is a step down in strength rather than a new claim.

| # | Decision | Why |
|---|---|---|
| **D-023** | ~~D-011's "the tiles carry no invented outcome" was thought to cover the evidentiary surface~~ **It did not.** The tiles were clean; the *prose* was not | Ruled by Ry. The build round policed the one place a case study usually overclaims — the stat tiles — and never audited the argument for the same fault. Four separate passages asserted causation, market position or accounting facts the sources do not support. **The lesson generalises: an outcome ration on the tiles is not an evidence policy for the document** |
| **D-024** | **Purchase price minus sale price is a "headline purchase-to-sale consideration gap", never a loss.** The Pattern 1 table's column is renamed, and an `.rtable__note` states what the number is not | Ry. The gap and the loss differ by orders of magnitude in the one case where both are public: Etsy's $170m gap against the **$5.1m loss on sale** its FY2025 10-Q records. Masimo's ~$680m is the same kind of number, and **Sonova has no exit price, so it has neither a gap nor a loss** — the old table asserted one anyway. The three-loss conclusion is gone from the exec summary, Pattern 1, the dumbbell figcaption and the Era 3 card |
| **D-025** | **A transaction timeline establishes sequence, not cause.** Part Two no longer says "nearly every failure traces to one of two macro events", and no longer rules out product or competitive factors | Ry. The claim was doing two illegitimate things at once: inferring causation from a chronology, and treating the absence of a competing explanation in the sources as the absence of the factor. Part Two now says what the record shows and, explicitly, how far it does not reach |
| **D-026** | **The Native Instruments diagnosis is withdrawn**, and so are the product-status assertions | Ry. "A balance-sheet failure" was a finding the sources do not contain: no administrator's report, filing or management statement in them identifies a cause, and NI is a private German company with no published accounts. "Kontakt remains the industry-standard sampler and Traktor a top-tier DJ platform" needed adoption or market-share data that does not exist in these sources either — the methodology already says no such series exists, so the page was contradicting its own appendix. The section is now *"an insolvency, and an estate broken up three ways"*, and it names what it cannot say |
| **D-027** | The same correction was applied **where the identical fault recurred outside the named sections** — Part Seven's "the industry's leading AI-audio asset", the exec summary's "balance-sheet failure", the implications' "the arithmetic that ended Soundwide", the aside titled "The strongest evidence that the products were fine" | Not asked for line by line, and done anyway: a page that fixes an unsupported superlative in Part Four and leaves the same superlative standing in Part Seven has not been corrected, it has been patched. Flagged to Ry rather than assumed |
| **D-028** | **The pandemic-spike figures are marked press-reported at the point of use**, and the unquantified software "step-change" is gone | Ry. The guitar percentages and the 16m first-time-buyer estimate were flagged only in the appendix, four sections later. The page now says at the figures that the coverage does not name the survey, its sample, whether the count is US or global, or whether it covers guitars or all instruments. The software claim had no series at all and could not be repaired, so it was cut |
| **D-029** | **`.rtable` gets real cell padding and a column hairline**; `.dtable` deliberately does not | Ry: the tables were "difficult to read and not recognizable as tables". Two faults with one cause — a component that borrowed `.dtable`'s habits without noticing `.dtable` is a *figure* of four numbers, where this is a 43-row register with prose in two of five columns. At 11px padding a two-line cell spaced its own lines further apart than it sat from the row above, and with no column edge the rows read as indented paragraphs. Padding is now larger than the text's leading, and the hairline is the one the sheet already uses. No new hue, no new weight |
| **D-030** | **The page's inline spacing styles are gone**; `.k + .section__title` and `.plainlist`'s margins moved into the shared sheet | The vertical-rhythm ruling (#182, 2026-08-15) landed after this page was built, and the page had been carrying twenty inline `margin-top` declarations — the same failure mode as the hand-authored `<br>`s that prompted #182, in another costume. The geometry and swatch styles on the figures stay inline: those are **data**, not spacing decisions |
| **D-031** ⚠️ | **The trim came to 6.8% net, not 10%** — a ~13% cut of the original prose, against roughly 500 words added by D-024 through D-028 | The two instructions in this round pull opposite ways: correcting an overclaim costs words, because saying what you cannot support takes longer than asserting it. Everything cut was restatement — a duplicated Src explainer, a callout restating the pull quote three lines above it, the "money in gear" table whose four figures were all already on the page, the "money in music" table folded to a sentence, the source list's redundant trailing domains. **What was not cut: any figure, any source, any caveat, any of the eleven implications.** Reaching 10% net from here means cutting evidence or recommendations, which is Ry's call, not mine |
| **D-032** | **`verify_copy.py`'s premise is updated, its numeric check is not** | The prose is no longer frozen, so a guard that implied it was would send the next session to "restore" copy Ry deliberately cut. The figure check is the half that still holds, and it passed unchanged through the whole round — every numeric token in the source is still on the page after a 13% prose cut |

### Round three — the map's palette and three cuts, 2026-08-15 (#199)

Four changes. One is a design ruling with consequences past this page; three are cuts.

| # | Decision | Why |
|---|---|---|
| **D-033** | **Hue may encode a category inside a figure.** Three conditions, all required: the variable is genuinely categorical, the hue is **redundant** with something already in the figure, and it touches neither the coral ration nor the navy chrome nor a magnitude scale. Declared in `case-study.css` with a measured contrast ratio, never inline in a page. Recorded in `docs/site-brief.md` §1.6 | Ry asked for the map to be "more colorful and interesting, within the page styling", and the sheet's own escape hatch says an accent may be added *here, with a written justification*. So it is written down as a rule rather than taken as a licence. **This extends `wolfpack-ai-command`'s D-015 rather than breaking it** — that one put hue in a committed image so the sheet stayed hue-free, which a chart drawn in HTML cannot do. Both say hue is figure content; only the storage differs |
| **D-034** | **The lane is the hue; the deal value stays neutral.** Ring = which lane (`--map-l0`…`l3`), fill = how big (`--fig-ramp-1`…`4`), on the same dot | The map has exactly two variables and only one of them can take hue. Lane is a *name*; value is a *magnitude*. Colouring the value as well would leave the figure with two categorical-looking scales and no readable magnitude — which is the failure the ramp was built to avoid in the first place (`docs/site-brief.md` §1.5). **The redundancy condition is satisfied by construction:** a lane is already identified by vertical position and by a name printed inside it, so a reader who cannot separate the teal from the amber reads the figure exactly as well as before |
| **D-035** | **Bands and gridlines were painting *under* the lanes, and now do not** | Not asked for, and found while tinting the lanes. Everything in the figure is absolutely positioned in one stacking context, so paint order was document order and an opaque lane surface hid whatever crossed it — a band spanning all four lanes was being drawn as stripes through the two lanes that had no background. Survivable while half the lanes were transparent; not once all four carry a tint. The layers are now named in the sheet (0 lanes, 1 bands and gridlines, 2 events, 3 labels) |
| **D-036** | **The year axis runs along the top as well as the bottom** | Ry. The plot is 1600px at its narrowest and four lanes deep, so dating an event in the first lane meant tracking to the far edge of the figure and then all the way down |
| **D-037** | **Three cuts: the 145% figure out of "Cut the tail" (now "High tariffs"), the "Rebuild deal capability" implication, the "Tariff schedule changes" watch row** | Ry, no reason given and none needed. Both figures survive elsewhere on the page, so `verify_copy.py` check 1 is untouched; the watch row carries no `Src` cell, so the 43 / 31 / 12 arithmetic is untouched. The watch table's accessible caption moved from "Eight open questions" to "Seven" in the same edit — **a count stated in a `visually-hidden` caption is exactly the kind of fact that goes stale silently**, because nothing on screen contradicts it. The implications list is now ten and renumbers itself |

**D-010's "ten tables" is now eight**, and has been since #195 folded two of them away
(D-031). `CLAUDE.md` was still saying ten and now says eight. Recorded here rather than
edited into D-010, because the ledger is a record of what was decided when.

**The rose is not a coral drift.** `--map-l3 #E08BB4` is a desaturated rose on a near-black
figure ground; `#F95954` is the accent. The two render together in the same viewport — nav CTA
above, map below — and do not read as the same colour. **The ration is still six**, and the
sheet, the brief and this ledger all say so, because "there is pink in the map now" is the
shape of a future session concluding otherwise.

### Round four — editorial restraint, 2026-08-15 (#205)

Two thesis corrections and a defensive-language trim. **The round after #195 is the mirror of
#195**, and the pair is the actual lesson: that round fixed a page claiming more than its sources
carry, and the fix left the page *announcing* its own carefulness. Correcting an overclaim and
performing rigour are two different things, and the second one costs credibility too — it reads
as a writer expecting to be cross-examined rather than one making an argument.

| # | Decision | Why |
|---|---|---|
| **D-038** | **The hero no longer excludes what the body says is not excluded.** *"two economic shocks, not a product problem, explain the wreckage"* → *"two economic shocks sit underneath much of the distress"* | Ry. The hero was the one place on the page still asserting the claim #195 removed everywhere else: Part Two says a timeline cannot rule out product or competitive factors, and Part Four says the same about Native Instruments. **A page whose hero contradicts its own Part Two is worse than either version alone** — a reader who notices stops trusting both. Not replaced with "may have contributed to"; the thesis is still stated as a thesis. `og:description` and the meta description carried the same claim and moved with it |
| **D-039** | **"Scale is a liability, expect conglomerates to break up" → "what has failed is unrelated ownership, not breadth"** | Ry, and the report's own Pattern 5 was the counter-evidence: Audiotonix and Focusrite have assembled broad audio portfolios over the same decade and are still buying. The old claim — *"every large diversified owner in this report that assembled breadth has since sold it"* — was **false against the page's own signal-chain table**. The corrected version keeps every strategic implication and gains one: **operating adjacency is the variable**, not size. Bose dropped out of the example list, because an audio company divesting a division is not an outsider exiting and lumping the two was part of the original error |
| **D-040** | **"The endpoint is four to six vertically integrated groups" → "One plausible endpoint is…"**, and *"There is no stable middle"* stays | Ry. Framing the destination as conditional is enough; once the sentence opens as a plausible endpoint the closing line reads inside that frame. Softening the punch line as well would have cost the voice for no gain in accuracy |
| **D-041** | **~127 words of cautionary prose removed**, against ~480 words of in-body hedging — about a quarter. **No limitation, confidence level, source distinction or known gap was removed** | Ry's test, adopted verbatim as the rule: *does this sentence stop a reasonable executive reader from making a materially incorrect inference?* Keep if yes; cut if it mainly signals that the author is rigorous. What went: the label *"correctly stated"*; *"Read those three figures as reported, not as measured"* (the substance stays, one sentence shorter); the label *"The honest limit of this argument"*; *"It is evidence about demand for the assets, and about nothing else"*; *"survey data, not panel data"* where the confidence note four sections earlier already says it; *"not yet evidence for it"* after *"being tested in public"* already implies it; and *"Both figures are press-reported, not company-confirmed"* on two figures **already prefixed "reported" and already listed in the Confidence levels appendix** — triple-marked |
| **D-042** | **The two consecutive Native Instruments epistemic paragraphs are merged into one**, 126 words to 92 | *"What this report can and cannot say about why"* followed by *"Two things this report explicitly does not claim"* made the same move twice in a row. All four substantive points survive: the chronology is documented, no source states a cause, product/customer/competitive factors are not excluded, and no category-level adoption or share series exists. **One paragraph of restraint reads as discipline; two consecutive ones read as anxiety** |
| **D-043** | **The consideration-gap note is kept, and kept prominent** — trimmed by twelve words, not compressed | Ry, explicitly. It is the one caution on the page that is load-bearing *financially*: without it a reader takes $170m and $680m for losses. The only clause cut was *"so for Sonova no gap and no loss exist yet"*, which the table now states in its own cell (*"None established — no exit price"*) |
| **D-044** ⚠️ | **One cut went a step past what was strictly required:** *"and no comparable series for software sales exists in these sources at all"*, from the pandemic-figures paragraph | It guarded an inference about a claim that no longer exists — #195's D-028 already cut the software "step-change". The nearest live claim is the sponsor-pricing aside, which rests on insolvency reporting rather than on a software volume series. Flagged rather than assumed: it is one sentence, and putting it back is one edit |
| **D-045** | **The hero art is supplied, not generated, and the committed PNG is the master.** `planning/consolidation-under-pressure-hero.png` — 1337×752, RGBA, added by Ry 2026-08-15, tracked from #213 and renamed out of its spaces in #214 | This folder's other two case studies both ship a `build_hero.py` and carry *rebuild rather than retouch*. This one has nothing to re-run, so the rule inverts: **the file is the artifact of record and must never be lost or "regenerated"**, and everything derived from it records a *derivation* command rather than a rebuild command. Written down because the missing generator otherwise reads as an omission against a convention stated twice in `CLAUDE.md` — the next person goes looking for a script that has never existed. Its aspect is 1.7779, so a 16:9 derivative crops nothing; it is RGBA, so any JPEG derivative must flatten first |
| **D-046** ⚠️ | **The hero is not on the case study page, and was not put there.** It reaches the public only as the blog post's `cover.jpg` | The page ships no hero figure and gained none. Adding one is a page edit plus a re-copy into `ai-coaching-intake`, which is a publishing decision rather than a tidy-up — **Ry's call, open.** Noted here so the gap between "the case study has hero art" and "the case study page shows hero art" cannot be mistaken for an oversight |

**Net word count moved almost not at all** — 7,331 to 7,239, 1.3%. That is the honest shape of the
round: ~127 words of hedging out, ~64 words back in for D-039, which needed *more* words to say the
narrower and more defensible thing. **A restraint pass is not a length pass**, and #195's D-031
already showed the same arithmetic running the other way.

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

## 4a. Verification re-run, 2026-08-15 (#195)

| Check | Result |
|---|---|
| Horizontal overflow, **all four case studies**, at 320 / 390 / 768 / 1024 / 1440 | `scrollWidth − clientWidth = 0`, and `scrollTo(99999,0)` leaves `scrollX = 0`, everywhere. The AI Command page is in the sweep because it also uses `.rtable` |
| Map label collisions | **0**, at every width, on both pages; still 42 events across 19 tracks |
| `Src` gutter | 43 cells, 31 links + 12 dashes, unchanged through the rewrite |
| Copy vs. the source `.md` | all 186 numeric tokens still present after a ~13% prose cut |
| `verify_copy.py` · `check_meta.py` | clean |

**Headless Edge produced no output at all on this machine during this round** — the binary
returns nothing, `--version` included. Chrome's headless mode works and the sweep was run
there. Worth knowing before assuming a verification script is broken: check the browser.

## 4b. Verification re-run, 2026-08-15 (#199)

Chrome again, for the reason above.

| Check | Result |
|---|---|
| Horizontal overflow, **all pages on the shared sheet**, at 320 / 390 / 768 / 1024 / 1440 | `scrollWidth − clientWidth = 0`, `scrollX = 0`, no element extending past the viewport outside a declared scroller |
| Map label collisions | **0**, on both pages, at 390 / 1440 / 1600 / 2200 |
| Lane encoding, read back from **computed style** | 4 distinct ring hues, 4 distinct label inks, 4 distinct lane names, 4 distinct tints; every lane and all 42 events carry `data-lane`; 0 events missing it |
| Deal value still neutral | the only five dot fills are `transparent`, `#FFFFFF`, `#C3C9D4`, `#98A0AE`, `#6E737E` — the ramp, unchanged, no hue |
| Layer order | `band: 1  grid: 1  lane: 0  event: 2` — bands and gridlines above the lane surfaces (D-035) |
| Year axis | 13 labels top and 13 bottom, 2014–2026, top strip entirely above lane 1, bottom strip entirely below lane 4 |
| `verify_copy.py` · `check_meta.py` | clean; 186 numeric tokens, 43 Src cells (31 + 12), 42 map events, 12 pages PASS |

**The `.rtable`-adjacent sweep flagged `setmaster3-case-study` at 320 and 390** and it is not a
regression: `scrollWidth − clientWidth = 0` on the document, the flagged table sits inside that
page's own `.trow` scroller, and that page loads `sm3-case.css`, which this round never
touched. The probe's exclusion list knew about `.rtable` and `.dtable` and not about `.trow`.

## 5. Open items

1. **D-006 needs Ry's ruling** — whether a citation counts against the destination policy.
   Everything else on this page is settled by an existing rule; this one is not.
2. **D-008 and D-009 are flagged word/number changes.** The brief says to come back before
   changing a word, and there was no way to ask mid-build. Both are one line each and both
   are reversible.
3. **D-031: the trim landed at 6.8% net against a 10% aim.** Going further means cutting
   evidence, the eleven implications, or the watch list. Ry's call.
4. **D-027 went slightly beyond the named sections** to fix the same fault where it recurred.
   If that was unwanted, the three extra edits are individually revertible.
5. **The upstream source has now diverged.** `wolfpackdata/dj-gear-study`'s
   `01-ma-landscape-2016-2026.md` still carries the pre-review prose, including the three
   "losses", the categorical causal claim and the Native Instruments diagnosis. **The
   corrections in #195 are corrections of fact, not of house style**, so the upstream document
   is now wrong in the same four places this page used to be. Worth porting back.
6. ~~**Not deployed.**~~ **Deployed 2026-08-15** at `/consolidation-under-pressure/`
   (`ai-coaching-intake#74`), from `develop 64fa14d`, both pages. `case-study-assets/` needed
   **no copy** — the intake's own #73 had re-copied it whole an hour after #200 merged, so the
   lane hues, `map.js` and the social card were already sitting there unreferenced. That is the
   re-copy-whole rule paying for itself, and it was verified rather than assumed: all 27 tracked
   asset files were copied over the deployed ones and `git status` came back empty. **The other
   two case studies are untouched by this deploy**, having already taken the shared-sheet
   restyle in #73.
   - **One correction landed with it.** The intake's log entry (10) described the CSS it carried
     as `#182` and `#195` only; it also carried `#199`/`#200`. Nothing caught it because neither
     change touches the other two deployed pages. Corrected in the intake's entry (11) rather
     than by editing the old entry.
7. ⚠️ **The Web Property Map is now stale** — a new page and a new public URL went live on
   2026-08-15 and the Notion page has not been updated. `CLAUDE.md`'s standing rule is to tell
   Ry rather than silently edit it, so this is the telling.
8. **The report is dated 11 August 2026 and says so.** Several Part Nine watch-list items
   will resolve; the closing fine print already tells the reader to read it as of its issue
   date, which is the brief's own instruction for a later publication.
