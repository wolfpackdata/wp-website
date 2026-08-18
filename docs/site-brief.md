# Site brief — wolfstrategyllc.com

**This is the authoritative site brief.** The `web-design-language` skill reads it before any
CSS work in this repo and **refuses to run without it**. It supplies every concrete value —
palette, accent ration, type, space, destinations — which is what lets the skill itself carry
rules and no values at all.

- **The skill and its reasoning:** [`wolfpackdata/wp-web-sop`](https://github.com/wolfpackdata/wp-web-sop)
  — `.claude/skills/web-design-language/SKILL.md` for the rules, `docs/rules-ledger.md` for
  why each exists and what it cost to learn. **`X-n` references below point at that ledger.**
- **The empty form this was filled from:** `docs/site-brief-template.md` in the same repo.

> **Keeping it true.** This brief is only useful while it matches the stylesheets. When a
> value here changes, change it in the sheet in the same PR — and the reverse. A brief that
> has quietly drifted from the CSS is worse than no brief, because it will be trusted.

Values read from this repo as of **2026-08-09**. Anything **computed** rather than read from
source is marked †; anything still open is marked ⚠️ and carries follow-up work in §12.

---

## 0. Identity

| Field | Value |
|---|---|
| Site / brand name | Wolf Strategy LLC / Wolfpack Data & Strategy |
| Repo | `wolfpackdata/wp-website` |
| This brief lives at | *n/a — reconstructed, never lived in that repo* |
| Brief last reviewed | *n/a* |

### 0.1 Stylesheet architecture

**Eight built stylesheets, two visual systems.**

| Sheet | Applies to | Palette | Why it differs |
|---|---|---|---|
| **Master** — the Wolfpack system, expressed in `rates/css/rates.css` as the pattern library | `rates/`, `ai-coaching/`, `hire/`, `portfolio/`, `github/`, `case_studies/`, `sm3-.../sm3-case.css` | §1–§2 | — |
| `sm3-specific-pages/sm3-assets/css/sm3-landing.css` | `setmaster3/` — the product page | Its own — [§11](#11-page-specific-surfaces) | It **is** SetMaster's surface, not a page about SetMaster |

There is no single master *file* — the Wolfpack system propagates by derivation
(`rates.css` → `coaching.css`/`hire.css` → `portfolio.css` → `github.css`; `sm3-case.css` →
`case-study.css`), with each sheet re-declaring the same eleven tokens. That is a legitimate
architecture for a no-build-step site, but it means **the master palette lives in seven
copies with nothing enforcing agreement.** See §11's note.

**The distinction this site draws, and it is the clean example:** `sm3-case.css` and
`sm3-landing.css` sit in the same folder and describe the same product. The case study wears
Wolfpack navy because *"it is a portfolio document… linked from both `hire/` pages, so it
wears the same chrome they do."* The landing page wears near-black because *"it is a product
surface."* They must never be merged — *"a single sheet holding both palettes is how an accent
ration gets spent by accident."*

## 1. Palette

### 1.1 System hues

| Role | Value | Contrast vs. ground | Permitted scope |
|---|---|---|---|
| Ground | `#000B29` | — | — |
| Primary text | `#FFFFFF` | **19.4:1** † | Unrestricted |
| Secondary / muted | `#BFC2CA` | **10.9:1** † | Unrestricted — passes AA and AAA for body text |
| Dimmest text | `#808594` | **5.3:1** | **Labels only** — annotated in every `:root` |
| Surface | `#0A1435` | — | Raised panels; **absent from `github.css`** |
| Surface 2 | `#101B3F` | — | as above |
| Hairline | `#222E52` | — | — |

† **Computed, not sourced.** The stylesheets state only the `--faint` ratio. The other two
were calculated here (WCAG 2.x relative luminance) because the template asks for them and a
blank cell invites a guess later. **Method validated against the one known value:** the same
calculation reproduces `--faint` as **5.28:1**, matching the source's stated 5.3:1.

⚠️ One number I could not reconcile: the sheets state **5.8:1** for ground-on-accent, and the
same method gives **6.1:1**. Both pass comfortably, so nothing is at risk — but the source's
figure is kept below rather than silently "corrected", since I do not know what tool produced
it. Worth a re-measure if anyone is near it.

### 1.2 The rationed accent

| Field | Value |
|---|---|
| Accent | `#F95954` |
| Ground-colored text on an accent fill | **5.8:1** — passes |
| White text on an accent fill | **fails AA** — stated in all six stylesheet headers |
| Therefore, text on an accent fill is | the ground navy, never white |

### 1.3 Palette exception

| Exception | Spec | Placements | May not share space with |
|---|---|---|---|
| The RML mark's orange→violet sun | `resume_design/header-footer-spec.md` §5 | Exactly one — the music page's Music & Creative Technology section | An accent fill (so no accent CTA sits in that section) |

### 1.4 Figure ground

| Field | Value |
|---|---|
| Shows screenshots or data figures? | **Yes** — case studies carry spreadsheet and dashboard captures |
| Renders its own data tables meant to match them? | **Yes** — `.dtable` |
| Mat background | `#0A0A0A` |
| Panel inside the frame | `#141414` *(SM3 case study only, as `--app-panel`)* |
| Row stripe | `#1A1A1A` |
| Emphasized row | `#23262E` *(generic case studies only, as `--fig-lift`)* |
| Border | `#2A2A2A` |
| Text | `#E6E6E6` |
| Dim text | `#9C9C9C` |
| **Scoped to** | `.shot`, `.ph`, `.dtable`, **`.figframe`** (generic) · `.shot`, `.trow` (SM3 case study) — never page chrome, never page type |

**`.figframe` joined the scope 2026-08-11 (#172)**, for the reason the ground was created.
A chart drawn in HTML is the alternative to a screenshot *of* a chart, so it stands exactly
where a captured image would stand; the rule the scope encodes is "anything standing where a
captured image would". The same PR drew the line on the other side: `.rtable`, the long-form
report table, is built from the **navy system**, because a table the reader reads is the
document's body rather than a figure, and a page whose body is mostly near-black slabs stops
looking like this site.

### 1.5 The sequential ramp *(added 2026-08-11, #172)*

An **extension of the figure ground's neutral axis, not a new hue.** Four ordered steps, dark
to light on a dark surface, for a single variable that is a *magnitude* — currently the
transaction map's disclosed deal value. A categorical palette would make a magnitude
unreadable, and a magnitude is exactly what this site's one chart encodes.

| Token | Value | Contrast vs. `--fig-row #1A1A1A` | Encodes |
|---|---|---|---|
| `--fig-ramp-1` | `#6E737E` | **3.6:1** | < $100m |
| `--fig-ramp-2` | `#98A0AE` | 6.6:1 | $100–499m |
| `--fig-ramp-3` | `#C3C9D4` | 10.6:1 | $500–999m |
| `--fig-ramp-4` | `#FFFFFF` | 16.7:1 | ≥ $1bn |

Measured against `--fig-row`, the **lighter** of the two lane surfaces a mark can land on;
the darker one is the easy case. Step 1 is the binding constraint and sits above the 3:1
floor for data marks on purpose — a 0.66rem dot is a small mark, and the headroom is what
survives a lane tint changing later. **Widen the ramp at the light end, never the dark one.**

**The fifth state is not a step.** "Undisclosed" is drawn as an unfilled ring, visually
outside the ramp, because an absent value is not a small one — bucketing it as the bottom
step would be a claim the sources do not make.

**Direction is not on this ramp and takes no colour at all.** A metric up or down is carried
by the glyph (▲ ▼ ▬) and by weight. That is the semantic-pair rule holding: a green and a red
are atomic, and neither half earns its way in alone.

**Two instantiations, five values shared.** `case-study.css`'s `--fig-*` ramp and
`sm3-case.css`'s `--app-*` ramp agree byte-for-byte on `#0A0A0A`, `#1A1A1A`, `#2A2A2A`,
`#E6E6E6`, `#9C9C9C` and differ only in their fifth slot — `--fig-lift #23262E` (an
emphasized table row) versus `--app-panel #141414` (a panel inside the product frame).

That is the generalization recorded in `case-study.css`'s header actually visible in the
values: the generic figure ground **is** the SM3 product surface with the semantic pair
stripped out. It is also, incidentally, five more strings living in two places with nothing
guarding them — see §9.

**Sanity check passes:** delete every screenshot and data table from this site and all eight
values become unused.

### 1.6 The four lane hues *(added 2026-08-15, #199)*

**The one place this site spends hue on data.** The transaction map's lane — macro, software,
hardware, retail — is a *category*, and §1.5's ramp is the wrong tool for a category the way a
categorical palette is the wrong tool for a magnitude. So the map now runs both encodings on
the same mark: **the dot's ring is its lane, the dot's fill is its value**, and they never swap.

| Lane | Hue | vs. `#1A1A1A` | Ink (42 event labels) | vs. `#1A1A1A` |
|---|---|---|---|---|
| Macro & regulatory | `--map-l0` `#E2B04A` | 8.7:1 | `--map-l0-ink` `#E3CDA3` | 11.2:1 |
| Software & platform | `--map-l1` `#7EA6F6` | 7.2:1 | `--map-l1-ink` `#BCCDF2` | 10.9:1 |
| Hardware manufacturing | `--map-l2` `#5FC2A6` | 8.1:1 | `--map-l2-ink` `#ABD9CA` | 11.2:1 |
| Retail & marketplace | `--map-l3` `#E08BB4` | 7.1:1 | `--map-l3-ink` `#EFC0D6` | 10.9:1 |

Each lane also carries a `-tint` (its surface wash, 0.07–0.08 alpha) and a `-line` (the
hairline to the next lane, 0.32 alpha). Ratios are measured against `#1A1A1A`, which is
lighter than any surface these actually land on, so every number is a floor.

**Three conditions, and they are the ruling, not the palette.** A figure may spend hue when:

1. the variable is **genuinely categorical** — a name, not a quantity;
2. the hue is **redundant** with something already in the figure (a lane is identified by
   vertical position *and* by a name printed inside it), so a reader who cannot separate two
   of the hues loses nothing — nothing here is the sole carrier of any fact;
3. it touches **neither the coral ration nor the navy chrome nor a magnitude scale**.

**This is not the [`wolfpack-ai-command`] D-015 ruling, and the two do not conflict.** That one
put hue in a *committed image* so the sheet stayed hue-free. This one puts hue in the *sheet*,
because a chart drawn in HTML has nowhere else to put it — which is why the conditions above
are narrow and written down. Both say the same thing: **hue is figure content, never chrome.**

**The rose is not coral.** `#E08BB4` is a desaturated rose on a near-black figure ground;
`#F95954` is the accent, and the two appear on screen together (nav CTA above, map below)
without reading as the same colour. **The coral ration is still six.** "There is pink in the
map now" is the shape of a future session concluding otherwise.

**The macro bands stay neutral.** A band is a shock, not a lane; a fifth hue there would read
as a fifth category. Same for the time axis, which every lane shares.

## 2. The accent ration

⚠️ **There is no site-level ration count.** See §11, F-1.

| Field | Value |
|---|---|
| **Ration count** | *per page — no site default* |
| Site-level rule | The *pattern* is site-level: enumerated in the stylesheet header, closed list, count ratchets down only |

| Page | Count | Last moved | Enumeration |
|---|---|---|---|
| `rates/` | **7** | **2026-07-22** (#3) — never moved since | nav CTA · featured tier (border + badge) · call-section CTA · coaching ghost CTA · contact CTA · link hover · focus ring. **Ruling X-3** — the shipped sheet also lists a hero CTA (8th). Hero kicker is deliberately **not** accent here, unlike the Q3 page |
| `ai-coaching/` | **8** — ruled 2026-08-09 | **2026-07-22** (#3) — never moved since | nav CTA · hero kicker · hero solid CTA · contact solid CTA · 24/7 support bridge band · price-band left border · link hover · focus ring. **See the note below** |
| `hire/` | 8 | 2026-07-30 (set at build) | nav CTA · hero CTA · hero contact-line rule · availability status dot · IN PREPARATION chip · closing contact CTA · link hover · focus ring |
| `portfolio/` | 6 | **2026-08-04** | nav CTA · closing intro-call button *(was hero CTA until #130 — moved, not duplicated)* · hero rule · IN PREPARATION chip *(live but unused)* · link hover · focus ring |
| `case_studies/` | 6 | **2026-08-04** (#92) — set at build, never moved | nav CTA · hero rule · pull-quote rule · closing CTA · link hover · focus ring. **The refusal list grew 2026-08-11 (#172); the count did not** — a ~6,000-word report brought source-link glyphs, a five-step deal-value scale, two macro bands, highlighted table rows, part numbers, era cards and an "open full width" affordance, and not one of them became coral |
| `github/` | **3** | **2026-08-07** | button fill · link hover · focus ring. The smallest — *"what a page with one link should cost"*. Was 4 until #158 took the hero rule with the standfirst it underlined |
| `pilot-project/` | **5** | **2026-08-18** (#236) — set at build | nav CTA · hero CTA · closing CTA · link hover · focus ring. **Not the price** — the biggest number on the page is carried by type size, which is the ration's own refusal of stat values applied to the one page where a number is the offer |

⚠️ **`ai-coaching/` could not be counted from its own header — now ruled at 8.**
It states the ration in prose rather than as a numbered list, and the prose was genuinely
ambiguous: *"the solid CTAs (hero + contact)"* and *"the two accent bands"* each read as
either **one** entry or **two** — **6 prose items** or **8 actual placements**.

**Ruled 8 by Ry, 2026-08-09: one entry per distinct placement.** That is how every *numbered*
sheet on the property already counts — `hire.css` lists nav CTA, hero CTA and closing CTA as
three separate entries — so this makes `coaching.css` consistent with its siblings and
countable. **Follow-up in `wp-website`: renumber that header comment as a list.**

This is ledger finding **V-3** with a concrete cost attached, and the argument for L-099
(cross-reference the ration at each use site, `/* accent use 2 of 6 */`) — `sm3-case.css`
does this and is auditable by grep; `coaching.css` does not and is not.

**History of the counts, recovered from git 2026-08-09.** `rates.css` and `coaching.css` both
had their ration comment written on **2026-07-22** (#3) and **neither has been touched
since** — so the `rates/` 7-vs-8 discrepancy is **original, not drift**: the shipped sheet
enumerated 8 from day one while the spec planned 7, and the two simply never agreed. Nothing
grew. `portfolio/` and `github/` both moved *down*, with dates. `sm3-landing.css` is the only
sheet on the property to have moved a count *up* (§11) — which is what corrected the ratchet
rule (X-5).

**Nothing else.** The refusals actually on the record:

> Not a section heading, not an app name, not a figure (`portfolio.css`). Not a job title,
> not a date, not a skill chip, not a timeline band (`hire.css`). Not a stat value, not a
> subhead, not a sidebar label, not a table row (`case-study.css`).

## 3. Type

| Field | Value |
|---|---|
| Heading family / weight | Roboto 700 |
| Body family | Montserrat 400/500/600 |
| Mono / label family | `ui-monospace, "Cascadia Mono", "Roboto Mono", Consolas, monospace` |
| Body size | **16px** — floor honored; comment in all six sheets: *"never smaller: 16px stops iOS zooming on focus"* |
| Body line-height | 1.6 |
| Heading line-height | 1.15 |
| Type scale ratio | *none declared* — sizes are set per element |

### 3.1 The small-label voice

| Field | Value |
|---|---|
| Has one? | Yes — `.k` |
| Family · size · tracking · case · color | mono · `0.86rem` · `0.14em` · uppercase · `--faint` |
| What it is for | *"the 'engineering document' voice"* — kickers, contact lines, stats |

Present in five of six sheets; **deleted from `github.css`** along with the kicker it served
(#158) — an instance of L-080, every rule serving a deleted element leaves with it.

## 4. Space

| Field | Value |
|---|---|
| Measure | `1100px` |
| Gutter | `24px` |
| Base spacing unit | ⚠️ **cannot fill** — never named. See §11, F-3 |
| Radius | `4px` |
| Second radius | `12px`, `github.css` only — *"the card only — a 4px corner reads as a button"* |

Section rhythm: deliberately not specified (X-4).

## 5. Density policy

**Scope question — credible claim or atmosphere?** **Credible claim**, unambiguously. Every
page here exists to be believed: rates that can be checked, work that can be opened, a résumé
that can be verified. The policy applies at full strength; there is no mood-driven page on
this property.

| # | Category | On this site |
|---|---|---|
| a | Real evidence | Screenshots of software that exists — eight shipped applications, plus anonymized client-work captures in the case studies |
| b | Honestly-rendered data structure | The career timeline (real concurrency), the expertise matrix, `.dtable`, the tier cards |
| c | Typographic hierarchy | Everything else |
| d | Icon from the site's own system | **None yet** — see §5.1. Permitted as of ruling X-7, 2026-08-09 |

**Nothing else.** Ban honored in full and named at source: no metaphor imagery, stock
photography, "my journey" devices, animated counters, parallax. Animation adds: no typewriter
effects, no scroll-jacking, no entrance animations on body text.

| Exception | Justification |
|---|---|
| *none* | |

### 5.1 Icon system

**Does this site have one?** **Not yet — approved and in progress.** Ruling **X-7**
(Ry, 2026-08-09) narrowed the ban from *decorative icons* to *off-the-shelf or stock
iconography*, on the grounds that what makes stock bad is anonymity, not decoration.

Tracked as [wp-website#166](https://github.com/wolfpackdata/wp-website/issues/166) and the
Notion task *Incorporate custom icons into wolfpack website*.

| Field | Value |
|---|---|
| **Provenance** | **Self-produced by Ry**, from scratch |
| Grid / weight / corner treatment | ⚠️ **Ry** — not yet defined |
| Format | **Inline SVG taking `fill: currentColor`** — the treatment the GitHub mark already uses in `github/css/github.css`, so an icon inherits its colour and there is no second value to keep in sync with the AA rule |
| **Count** | **0 today.** Four proposed for round one |
| Count last moved | *n/a — set has not shipped* |
| Are any rendered in the accent? | **Proposed: no.** Several pages are at a spent ration, and an accent icon would have to be added to that page's enumeration in the same PR |

**Proposed round-one set** — two atomic pairs, both doing semantic work:

| # | Icon | Where | What a reader loses without it |
|---|---|---|---|
| 1 | Application marker | `portfolio/` | The page mixes two kinds of evidence; today they are distinguished only by card shape |
| 2 | Case-study marker | `portfolio/` | *(pair with 1 — both or neither)* |
| 3 | Windows | `setmaster3/` | Which build is theirs, at a glance. Functional, not decorative |
| 4 | macOS | `setmaster3/` | *(pair with 3 — two equal platforms, per the ration note in §11)* |

⚠️ **Not yet ruled by Ry** — the set, the count, and the production spec. `github/` is
excluded by design (two strings on the page, #158).

## 6. Destination policy

| Field | Value |
|---|---|
| **Copy posture** | **Transparency — site-wide** (ruled by Ry, 2026-08-09). Named at source on `rates/` — *"the rates page with nothing to hide; transparency is the hook, the call is the ask"* — and the same posture is visible on four independent pages: the not-salesy contract bans urgency, scarcity, gates and dark patterns; `github/` is explicitly *"not to funnel people"*; the case studies name no client and invent no testimonial; and the ban on *"book before rates change"* is checked against the 90-day-notice term. Urgency and scarcity are banned **outright** here, not merely when false |
| Default destinations per page | **1** — the "book-first" rule |
| What counts as site chrome | The header wordmark's link to the company home page (precedent set #126) |
| Adding one requires | A written ruling, recorded in the page's design plan or the rulings ledger |
| Subordination rule | Navy-ghost, never the accent; never displaces the primary CTA |

| Page | Count | Prohibitions, and the harm each prevents |
|---|---|---|
| `portfolio/` | 1 + 1 subordinate | SetMaster 3 product page (D-015, Ry 2026-08-17) — navy-ghost, one size down, in the tile whose product it is. **Never link `hire/`** — those carry a time-sensitive "actively seeking a role" claim; linking from a client-facing page tells every prospect he is job-hunting. **The harm is the résumés, not `noindex`** (D-003, scope-corrected same day) |
| `github/` | 1 | Stricter: **no `mailto:` in the footer**, uniquely in the repo — *"that is precisely how a not-a-contact-page becomes a contact page"* |
| `rates/` | 1 + 3 subordinate | ROI calculator (R11), portfolio (R14), and the pilot project (R15, 2026-08-18 #238), all navy-ghost, all individually ruled. R15 differs in kind from the other two: it is a **mirror-set** item under the consistency contract rather than a public-page-only delta, because the pilot landed on the Q3 direct-link page first (`wp-rates-page#42`) |
| `pilot-project/` | 1 + 3 subordinate | The rate card and the AI Coaching page, both navy-ghost buttons, plus an **inline text** link to `/wolfpack-ai-command/` on the blurb of one of the two included systems (S-12). The case-study link is navigation within the work, the reading portfolio D-014 settled — but it is written down here because it is the count's third, and three is one more than any other page carries. **Linked from both rates pages since 2026-08-18** (#238 / `wp-rates-page#42`), which resolved the open question; nothing else links it |

**Navigation strategy (X-8): user-first and intuitive is the default; one-way is an
exception that must name its reason.**

Link graph read from every `index.html` on 2026-08-09 (self-canonicals, assets, and
`github.com` targets excluded):

| Pair | Direction | Reason on record? | Verdict |
|---|---|---|---|
| `rates/` → `portfolio/` | One-way | **Yes** — spec R14 / contract D15. *Amended 2026-08-17:* the original reason was that a link back would be `portfolio/`'s second destination, and that specific argument is now spent — D-015 gave it one. The pair stays one-way on the **other** ground, which was always the stronger one: `portfolio/` cut its rates coda by Ry's explicit decision (portfolio D-011), so a rates link there is a reversal, not a gap | ✅ **Legitimate exception, on a re-stated reason** |
| `setmaster3/` ↔ `setmaster3-case-study/` | **Bidirectional** | — | ✅ **Not a gap** — they link both ways already |
| `portfolio/` → all three case studies | One-way | **Yes, deferred rather than rejected.** `portfolio-page-design-plan.md` §7 proposed the return link and **deliberately did not build it**: editing the case study means re-deploying `case_studies/` alongside `portfolio/`, *"doubling the round's deploy surface, which is a cost Ry should choose rather than absorb"* | ⚠️ **A deferral on cost grounds, not a design decision.** Still open |
| `portfolio/` → `setmaster3/` | One-way | **Yes** — D-015, Ry 2026-08-17. `setmaster3/` is a product surface for DJs and carries no consultancy framing at all (§11), so a link back would drag the wrong audience into the wrong page | ✅ **Legitimate exception** |
| `hire/` → 4 case studies + `setmaster3/` | One-way, outbound-only | **Yes** — D-003 in reverse. Nothing may link *to* `hire/`, and `hire/` linking *out* to indexed pages is the harmless direction | ✅ **Legitimate exception** |
| `hire/` ← nothing | One-way, inbound-only | **Yes** — D-003. The résumés are deliberately linked from nothing | ✅ **Legitimate exception** |
| **`roi-calculator/` ← 3 pages, → nothing** | **Dead end** | **No** | ⚠️ **The clearest gap on the property.** `rates/`, `ai-coaching/`, and the ops-fin-model case study all link *into* it; it links back to **nothing at all** — no nav, no return path, no onward step. A reader who follows it is stranded |

⚠️ **Ry, 2026-08-09:** site-wide nav consistency is planned but not yet done — page content
came first. So some existing one-way pairs on this property are **gaps rather than
decisions**, and this table is incomplete until that pass happens. See the open items.

## 7. Indexability and assets

| Field | Value |
|---|---|
| Default robots posture | Indexed |
| Deliberately `noindex` | `hire/` (two differently-framed résumés indexed side by side reads badly); `github/` (thin content that would compete with `/portfolio/` for the same queries) |
| External requests | **Zero** — verified by grep for absolute URLs, `@import`, `url(https:…)` |
| Fonts / images self-hosted | Yes, per folder |
| **Build architecture** | **Static, no build step** — the repo's defining property. Four Python scripts build *inputs* (résumés, images, blog payloads), none produces a page. This is what makes the copy-assets-in rules correct here |
| Folder shape default | **Self-contained**; shared assets only when pages ship as one deploy unit (`hire/`, `case_studies/`) |

### 7.1 Audience — per page *(field added during this exercise; see §11, F-4)*

| Page | Audience | Indexed? | What this audience makes the page exclude |
|---|---|---|---|
| `rates/` | Clients | Indexed | Kickoff-retainer amounts, rate-ladder chart, intake links |
| `ai-coaching/` | Clients, coaching specifically | Indexed | Intake links (book-first) |
| `hire/` | Hiring managers | **noindex** | Nothing — carries the full résumé |
| `portfolio/` | **Both at once** | Indexed | **All résumé apparatus** — timeline, experience bullets, expertise matrix, education, downloads. Work evidence reads the same to both audiences; career narrative does not |
| `case_studies/` | Founders, SMB directors, operating executives | Indexed | Client names, invented testimonials, **and any claimed outcome** — the stat tiles carry build, artifact and method facts only |
| `…/transaction-map.html` | as above, arriving from the report | **noindex** | Everything except one figure and the route back |
| `github/` | Anyone sent the link | **noindex** | Everything except a heading and a button |
| `pilot-project/` | A prospect who balked at the monthly tiers | **noindex** | **Hours, weekly commitment, and any effective hourly rate** — the fee prices a scoped outcome and the rate curve prices reserved time, so publishing hours here would contradict `/rates_public/` arithmetically. Also: the once-per-client limit (enforced on the call), and any measured outcome |
| `roi-calculator/` | Consideration-stage clients | Indexed | — a tool, not a funnel page |
| `setmaster3/` | **Product users** — DJs | Indexed | Wolfpack consultancy framing entirely. It is the product's own surface (§11) |
| `setmaster3-case-study/` | Clients / hiring managers | Indexed *(flipped from `noindex` 2026-08-04)* | The product-user framing — it is a portfolio document about the product |
| `blog_posts/` | Mixed / inbound | *Wix, not this repo* | ⚠️ Outside the deploy table — authored here, published to Wix |

## 8. Verification

| Field | Value |
|---|---|
| Breakpoints measured at | 320 / 390 / 768 / 1024 / 1440 — `scrollWidth − clientWidth = 0` |
| Phone-width capture | Headless Edge/Chrome clamps to **~492px** and crops, faking overflow. Workaround: 390px `<iframe>` in a wider host page |
| Renders with JS disabled | **Required.** Hidden state scoped to a `.js` class only the script adds |
| Reduced motion | `prefers-reduced-motion: reduce` bypasses everything; where smooth scroll is a primary nav path, the jump and its hover affordances are disabled too |

## 9. Strings guarded by a machine check

| String set | Copies live in | Guard | Fails loudly if its anchor moves? |
|---|---|---|---|
| Project names + blurbs | `eng_only.yaml` / `eng_music.yaml`, `portfolio/index.html`, both `hire/` pages — **3 HTML copies** | `verify_facts.py` check 6 | **Yes** — reports *"the markup changed, and this check is now silently guarding nothing"* on zero matches |
| Figures (spans, dollar amounts) | Both YAMLs | check 2 vs. `FIGURES` | — |
| Facts appearing on both résumés | Both YAMLs | check 3 vs. `SHARED` | — |
| Contact block | Built `.docx` | check 5 | — |
| **The master palette — 11 tokens** | **7 stylesheets**, each re-declaring them | ❌ **NONE** | — |
| The figure ground — 5 of 6 values | `case-study.css` (`--fig-*`) and `sm3-case.css` (`--app-*`) | ❌ **NONE** | — |
| Booking calendar URL | `rates/`, `hire/` ×2, `ai-coaching/`, plus the upstream `wp-rates-page` | ❌ **NONE** — governed by a written contract, not a check | — |
| **The music-gear report's copy** — every figure, caption, footnote and confidence note | `dj-gear-study`'s `docs/strategy/01-ma-landscape-2016-2026.md`, vendored into `case_studies/consolidation_under_pressure/planning/`, and that page's HTML | ✅ **`planning/verify_copy.py`** *(added 2026-08-11, #172)* | **Yes** — every structural check asserts it found its anchor before asserting the anchor is right |

The guard is **directional**: a page may show a subset of the résumé's projects, never a
string the résumé lacks.

⚠️ **The three unguarded rows are the largest duplication on this property**, and by this
section's own rule (*any string in more than one artifact gets a machine guard, or it will
diverge*) they are the gap. They currently agree — which is the only reason it has not bitten,
and precisely the silence L-038 warns about. The calendar URL has already drifted once
historically (a third, wrong link shipped on `wp-rates-page#21`).

## 10. Deliberately not specified

| What | Why |
|---|---|
| **Copy voice** | The voice guide was **deleted** (#150, 2026-08-06) — *"not good enough to be binding"*. Copy is judged by Ry against no written spec. Non-binding tone reference points (added 2026-08-15) live in `case_studies/README.md` §Voice |
| Section rhythm / vertical scale | X-4 |
| Density quantity | X-1 |
| Deploy mechanics | X-2 — they live in `wp-website/CLAUDE.md` |
| Type scale ratio | No ratio is declared; sizes are set per element. Not reverse-engineered, for the same reason as section rhythm |
| Icon *style* | Deliberately open — X-7 constrains **provenance and count**, not appearance. Ry is producing them |

---

## 11. Page-specific surfaces

### Surface: SetMaster 3 landing page

| Field | Value |
|---|---|
| Stylesheet | `sm3-specific-pages/sm3-assets/css/sm3-landing.css` |
| Pages using it | `sm3-specific-pages/setmaster3/` → `intake.wolfstrategyllc.com/setmaster3/` |
| **Why it is a separate surface** | *"This page wears SetMaster 3's own surface because it is a product surface."* The case study beside it is a portfolio document and wears Wolfpack navy |
| Ground · panel · row · border | `#0A0A0A` · `#141414` · `#1A1A1A` · `#2A2A2A` |
| Text · secondary · dim | `#E6E6E6` · `#9C9C9C` · `#6B6B6B` *(4.9:1 — labels and meta only)* |
| Radius scale | `6px` / `4px` — differs from the master's flat `4px` |
| Brand accent | `--brand-purple #9B5CFF` — section eyebrow labels and the wordmark numeral |
| **Inherited from the master unchanged** | Structure, spacing, type scale, button shapes, reveal behaviour, footer — *"so the two pages are recognisably the same hand"*. Roboto 700 / Montserrat, because the repo already carries the files |

**Accent ration for this surface** — counted separately, and split by *how* the color is used:

| # | Where | Fill or on-ground? |
|---|---|---|
| 1 | Nav Download button | Fill |
| 2 | Windows Download button | Fill |
| 3 | macOS Download button | Fill |
| 4 | Live release status dot | Fill |
| 5 | Hero stat values | Text |
| 6 | Link hover | Text |
| — | Focus rings — `--accent-blue`, *"the application's focus colour and it stays that here"* | — |

| Field | Value |
|---|---|
| Count | **4 fills + 2 text/border**; blue is focus-only; purple is eyebrow labels + wordmark numeral |
| Text on an orange fill | `#0A0A0A` — **8.4:1**. White is **2.9:1** and fails |
| Last moved | **2026-08-05, grew 3 → 4 fills.** macOS shipped as a signed `.dmg` (v3.0.4) and the install band gained a second real download. *"Two equal platforms with one orange button between them would have made the ration a lie about the product rather than a discipline"* |

**Semantic color pairs:**

| Pair | What it encodes | Appears where |
|---|---|---|
| `--out #FF4FD8` / `--in #4DE8E8` | Out Track / In Track | **`sm3-case.css` only.** Cut from the landing page 2026-08-05 with the transition-row table; both variables and every rule reading them came out together |

> Both halves left together and *"if a future band pictures a transition row again, they come
> back TOGETHER: magenta without cyan means the Out/In semantic was borrowed as a decorative
> colour."*

**A note this exercise surfaced:** the master palette has no single home — seven sheets each
re-declare the same eleven tokens, and nothing checks that they agree. They currently do
agree, which is the only reason this has not bitten. By §9's own rule (*any string in more
than one artifact gets a machine guard*), the master palette is the largest unguarded
duplication on this site.

## 12. Rulings on this brief — all resolved 2026-08-09

| # | Question | Ruling |
|---|---|---|
| **O-1** | Live brief or worked example? | **Live brief — this file.** `wp-web-sop` keeps the template-validation findings and a pointer here, so there is exactly one authoritative copy of the values |
| **O-2** | `ai-coaching/`'s ration — 6 or 8? | **8 — one entry per distinct placement**, matching every numbered sheet on the property. *Follow-up: renumber `coaching.css`'s header as a list* |
| **O-3** | Round-one icon set | **The `portfolio/` pair only** — application + case-study markers. One surface, one enumeration. The `setmaster3/` platform marks follow once the production spec is settled |
| **O-4** | One-way pairs — gaps or decisions? | **`roi-calculator/` is a gap** and needs a return path. `rates/` → `portfolio/` and the `hire/` inbound-only rule are legitimate exceptions; `setmaster3/` ↔ its case study was never a gap (already bidirectional); the `portfolio/` return link is a recorded deferral on deploy cost |
| **O-5** | Guard the unguarded duplications? | **All three, one script** — a `check_tokens.py` in the style of `check_meta.py` |
| **O-6** | Copy posture — one page or site-wide? | **Site-wide transparency.** Urgency and scarcity are banned outright here, not merely when false |
| **O-7** | Missing "ration set at" dates | **Recovered from git**, no ruling needed. `rates.css` and `coaching.css` both 2026-07-22 (#3), untouched since; `case-study.css` 2026-08-04 (#92) |

### Follow-up work these rulings create

| Work | Issue | From | Status |
|---|---|---|---|
| This brief, moved in | — | O-1 | ✅ **done** |
| Renumber `coaching.css`'s ration as an 8-entry list | [#167](https://github.com/wolfpackdata/wp-website/issues/167) | O-2 | Open |
| Give `roi-calculator/` a return path | [#168](https://github.com/wolfpackdata/wp-website/issues/168) | O-4 | Open |
| `check_tokens.py` — the three unguarded duplications | [#169](https://github.com/wolfpackdata/wp-website/issues/169) | O-5 | Open |
| The `portfolio/` icon pair | [#166](https://github.com/wolfpackdata/wp-website/issues/166) | O-3 | Open |

⚠️ **Three of the values in this brief are known-unguarded until #169 lands** — the master
palette, the figure ground, and the calendar URL. Until then, the brief and the stylesheets
agree by inspection only.
