# Hire pages — design plan

Two long-scroll landing pages that carry **all** of Ryan Hickey's résumé content,
aimed at **hiring managers**, one per résumé variant. Sibling documents to
`public-rates-design-brief.md` / `-spec.md`, which serve the client-facing rates
page; this one serves the candidacy.

| | Page A | Page B |
|---|---|---|
| Source résumé | `ryan-resume-dev/resume_build/content/eng_only.yaml` | `…/eng_music.yaml` |
| Folder here | `hire/ryan-hickey/` | `hire/ryan-hickey-music/` |
| Public URL | `intake.wolfstrategyllc.com/hire/ryan-hickey/` | `…/hire/ryan-hickey-music/` |
| Aimed at | Everyone else | Music-adjacent companies |
| Role line ends | `… · COO · Technical Operator` | `… · COO · Professional Musician` |

Status: **first draft built** (issue #76, branch `feat/76-hire-pages`). Both
pages, the shared stylesheet, the reveal script, and all four downloads exist and
have been verified — see §12. **Not deployed.**

---

## 1. Decisions ledger

Locked with Ry, 2026-07-30. These are settled inputs, not proposals.

| # | Decision | Consequence |
|---|---|---|
| D-001 | **Posture: actively seeking, both IC and leadership.** Hero states availability explicitly: senior IC *or* leadership — AI engineering, data platform, or technical operations. | Hero carries an availability line. The page is time-sensitive and needs editing when Ry lands a role — noted in `hire/README.md`. |
| D-002 | **noindex, direct-link only.** Both pages. | `<meta name="robots" content="noindex, nofollow">` on both; no sitemap entry; no inbound links from `rates/`, `ai-coaching/`, or Wix. Canonical tags point at each page's own intake URL. |
| D-003 | **PDF + DOCX both downloadable.** | New `export_pdf.py` in `resume_build/` (Word COM — confirmed available, v16.0). Four files in `hire/assets/dl/`. |
| D-004 | **Imagery sourced from `wp-rates-page/img/`** plus this repo's résumé design assets. | Eight app screenshots, the wolf mark, the RML mark, two portraits — all copied in. No stock photography anywhere. |
| D-005 | **Phone included** — `415-371-9613` — in both the top and bottom contact blocks. | The page's contact set is a **superset** of the résumé's contact line. §7 records exactly how, so the two artifacts can't drift by accident. |
| D-006 | **RML mark appears in the music page's Music & Creative Technology section only.** | Same Wolfpack chrome on both pages throughout; the RML lockup is one controlled moment, invoking the third-color exception already granted in `resume_design/header-footer-spec.md` §5. |
| D-007 | **URLs are `/hire/ryan-hickey/` and `/hire/ryan-hickey-music/`.** | The repo folder `hire/` mirrors the deploy path exactly, so shipping is one folder copy. |
| D-008 | **`wolfstrategyllc.com` appears at the top as a link and at the bottom as a secondary CTA** (Ry, feedback round 1) — as trust, not as funnel. **Revised round 2:** the bottom CTA moved *out* of the closing block into its own coda band below it. | In the hero contact line, in the closing contact grid, on the eng-only footer wordmark, and — since round 2 — as a single ghost link in the `.softcta` coda section (§4.12). Inside the closing block it had been a fourth button beside two résumé downloads, which read as a peer of the primary CTA rather than below it. It is never coral: the primary CTA stays unambiguously *Contact Ryan*. |
| D-009 | **Music tenure is four spans, not one number** (Ry, feedback round 2). Piano: 36 years of playing and study. Paid performance: since **2003** → 23 years. Studio production/engineering: 20+ years. **Professional DJ: since 2009** → 17 years. | The pages say "36 years at the piano · 23 years paid to perform". The phrase *"a 36-year music career"* is retired — it conflated study with career — as is *"20+ years of DJ performance"*, which predated 2009 by four years. `eng_music.yaml` still carries both and is now the **stale** copy: the résumé needs the same correction on its next build round (§6c). |
| D-011 | **The case studies section carries the published set, in Ry's order, and the `$30M` placeholder is removed.** Order: AI Command → SetMaster 3 → Consolidation Under Pressure → financial model. Both pages, identical markup. Two in-tile CTAs are added to the applications gallery at the same time. Ruling: Ry, 2026-08-17 (#218). | The section had drifted behind reality in two directions at once: it advertised *three* studies while four were published, and it still showed a `Figures in preparation` panel for a study that has had a real hero since #113. **On the removal:** an `IN PREPARATION` chip is a promise, and on a résumé page a reader cannot tell an unwritten case study from an abandoned one — so every card is now something they can open. The `$30M` study is not cancelled; it re-enters as a normal card when it is written. **On the order:** it is Ry's and encodes nothing a script could re-derive, which is why the markup says so in a comment. **On the count strings:** both were removed from the section head — a heading that counts its own children is a fact with no guard on it, and this one had already gone wrong. **On the fourth card's image:** Consolidation Under Pressure is the one case study that ships no hero figure (Ry's ruling, 2026-08-16 — its supplied art is the blog cover), so the card shows the transaction map, the document's signature figure, composed at card width by a generator recorded beside the capture it reads. **On the tile CTAs:** only the two tiles whose system has a published write-up carry one, so their presence is information rather than decoration; they sit *after* `.app__blurb` because `verify_facts.py` check 6 matches name-and-blurb as adjacent siblings and anything between them would unguard a résumé string without failing anything. Coral ration untouched at eight — every new control is navy-ghost — and use 5 is now live-but-unused, the state `portfolio.css` has carried since #113. |
| D-010 | **The music training was taught, and both pages say so** (Ry, feedback round 3). **Ten years of classical piano study with a university professor**; sound engineering learned **from working mentors and paid online programs**. The `.edu-aside` panel — previously eng-only, and previously labeled *"self-taught"* — now runs on **both** pages under **"A second discipline, formally trained."** | *Self-taught* was factually wrong and it undersold the box: it read as a hobby that got serious, when both halves were instructed. Neither fact is anywhere in either YAML, so this is a **second** divergence for the résumé round to absorb (§6c) — and `10 years` is a new figure needing a `FIGURES` entry. |

---

## 2. The concept

**The résumé as a system readout.**

`resume_design/brand-reference.md` §4 already names the brand's voice — *"the
engineering document voice"*: mono labels, quiet grays, one rationed accent. The
concept here is a deliberate escalation of that idea at screen scale, not a
departure from it. The page is a document that behaves like an instrument panel:
the same content a hiring manager would get in a PDF, but paced into sections,
scroll-navigable, and — crucially — **backed by evidence the PDF cannot carry**.

Ry's brief was *"enjoyable to read without coming across as corny."* The
anti-corny discipline is a hard rule, stated once so it can't erode:

> **Every visual element on these pages is one of three things:** (a) real product
> evidence — a screenshot of software that exists; (b) a data structure rendered
> honestly — the career timeline, the skills matrix; or (c) typographic hierarchy.
> **Nothing else.** No metaphor imagery, no decorative icons, no stock
> photography, no "my journey" narrative device, no animated counters, no
> parallax. The restraint is the design.

The three highest-leverage moves, in order of what they buy:

1. **The career timeline** (§4.3) — the single best argument for why this exists
   as a page instead of a document. Six roles spanning 2009→present with real
   concurrency that a linear list flattens into nothing.
2. **The portfolio gallery** (§4.6) — eight shipped applications, each with a
   screenshot. Turns the résumé's longest text section into proof.
3. **The hero slab** (§4.1) — a direct port of the résumé's own header
   composition. The page announces itself as *this specific document*, authored,
   not templated.

---

## 3. Design system

Inherited wholesale from `rates/css/rates.css` and `ai-coaching/css/coaching.css`,
which `resume_design/brand-reference.md` already establishes as the pattern
library. No new tokens.

```
--navy #000B29   --coral #F95954 (rationed)   --white #FFFFFF
--muted #BFC2CA  --faint #808594 (labels only) --surface #0A1435
--surface-2 #101B3F  --line #222E52  --radius 4px  --measure 1100px
Roboto 700 headings · Montserrat 400/500/600 body · mono for kickers/contact/stats
```

**The coral ration, enumerated for this page** — goes in the header comment of
`hire/assets/css/hire.css` and must stay true, same discipline as the other two
stylesheets:

1. the nav CTA (`Contact Ryan`)
2. the hero CTA (`Contact Ryan`)
3. the hero's contact-line bottom rule — the résumé's own coral rule, ported
4. the "Available" status dot in the availability line
5. the case-study `IN PREPARATION` chip border
6. the closing contact CTA
7. link hover
8. the focus ring

Nothing else. Not a section heading, not a job title, not a date, not a skill
chip, not a timeline band. **Where coral is a fill, text on it is navy, never
white** (AA) — carried over unchanged from both existing stylesheets.

**Shared assets, one copy.** Unlike `rates/` and `ai-coaching/` — which are
independent deployments and each carry their own fonts — these two pages ship as
one `hire/` folder, so they share `hire/assets/`. Saves ~330 KB of duplicated
woff2 and ~8 MB of duplicated screenshots, and guarantees the two pages can't
drift stylistically. Pages reference `../assets/…`.

---

## 4. Information architecture

Section order is identical on both pages. **Bold** rows differ between them; §5
is the full delta.

| # | Section | eng-only | eng-music |
|---|---|---|---|
| — | Sticky nav + scroll-spy | ✓ | ✓ |
| 1 | Hero slab — name, role line, availability, contact, CTAs | ✓ | ✓ |
| 2 | Professional Summary | ✓ | **+ music clause** |
| 3 | Career timeline | **6 roles** | **4 roles** |
| 4 | Professional Experience | **6 roles incl. RML + Niceman** | **4 roles** |
| 5 | Core Expertise matrix | **5 groups** | **6 groups** |
| 6 | Selected Applications & Systems | **8 cards** | **7 cards** |
| 7 | Case studies (placeholders) | ✓ | ✓ |
| 8 | **Music & Creative Technology** | — | **✓ (+ RML mark)** |
| 9 | Current Technical Focus | ✓ | ✓ |
| 10 | Education | **2 lines** | **1 line** |
| 11 | Closing contact block | ✓ | ✓ |
| — | Footer | ✓ | ✓ |

### 4.1 Hero slab

A screen-scale port of the shipped résumé header (`header-footer-spec.md` §9),
which is the composition that makes the page read as *authored*:

```
 ┌────────────────────────────────────────────────────────────┐
 │  ▪ wolf mark                                               │
 │                                                            │
 │  RYAN HICKEY                                    ┌────────┐ │
 │  AI Engineer · Data & AI Systems Architect ·    │        │ │
 │  COO · Technical Operator                       │ portrait│ │
 │                                                 │        │ │
 │  ● Open to senior IC or leadership roles —      └────────┘ │
 │    AI engineering, data platform, technical operations     │
 │                                                            │
 │  ryan@… · 415-371-9613 · linkedin · github · SF Bay Area   │
 │ ══════════════════════ coral 3px ════════════════════════  │
 │                                                            │
 │  [ Contact Ryan ]  [ Résumé PDF ]  [ DOCX ]                │
 │                                                            │
 │  ▸ 20+ yrs coding   ▸ $300K→$30M as COO   ▸ $20k MRR built │
 └────────────────────────────────────────────────────────────┘
```

- Name: Roboto 700, uppercase, `letter-spacing: 0.005em`, `line-height: 1.02` —
  the résumé's exact treatment.
- Role line: Montserrat 600, `--muted`, `·` separators in `--faint`.
- Availability line (D-001): mono, uppercase, letterspaced, with a coral dot.
  The only place on the page that speaks in the first person about wanting a job.
- Contact line: mono, `--muted`, with the coral 3px bottom rule — the résumé's
  signature move, ported literally.
- CTAs: `Contact Ryan` is the coral solid and links to
  `https://calendar.app.google/zHNd1NA9wzb4VRLw5` (the current intro-call URL per
  `CLAUDE.md`; new CTAs use the current one). PDF and DOCX are ghost buttons.
- Stat row reuses `.hero__stats` with the `▸` bullet in `--faint`, per
  `brand-reference.md` §4.
- Portrait: `ryan-hickey-portrait.png`, navy-chip framed, `border-radius: 4px`.

The closing contact block (§4.11) is this slab inverted — contact set repeated in
full, same CTAs — so the document opens and closes on the same information, which
is what Ry asked for.

### 4.2 Professional Summary

The YAML's two paragraphs, verbatim, at generous measure (~68ch) and
`font-size: 1.125rem`. No pull-quotes, no highlighted phrases. This is the one
section that should feel like *reading*, and the design's job is to get out of
the way.

### 4.3 Career timeline — the centerpiece

A horizontal band chart, CSS grid, 2009 → 2026+, one row per role. Every value
comes from the YAML `dates` fields; nothing is invented.

```
        2009    2012    2015    2018    2021    2024   now
        │       │       │       │       │       │      │
Wolfpack Data & Strategy                        ▓▓▓▓▓▓▓▓▶  Founder & Principal
Tromml Inc.                                     ▓▓▓▓▓▓▓    Head of Insights
RML Creative LLC                                ▓▓▓▓▓▓▓▓▶  Founder & Producer
Auto SOSS / Shock Surplus       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      COO & Partner
Niceman Music Studio    ▓▓▓▓▓▓▓▓▓▓▓▓                       Founder & Owner
In4mation Insights      ▓▓▓▓▓                              Dir. Marketing Science
```

**Why this is worth building:** the overlaps are the story. Ry was COO of a
company climbing to $30M *while* running a recording studio, and later founded
two LLCs *while* leading analytics at an AI SaaS company. A linear résumé list
destroys that information; a timeline hands it to a reader in one glance. This is
the thing the PDF cannot do.

**Design risk, flagged for Ry's review:** concurrency reads as *operator running
multiple entities* to most hiring managers and as *spread thin* to a few. The
facts are on the résumé either way — the timeline only makes them legible. If Ry
would rather not foreground it, the section drops without affecting anything else.

Bands are `--surface-2` with a 1px `--line` border; the current three carry a
right-pointing terminus instead of a hard edge. **No coral** — the ration is
spent (§3). Bands animate their width in on scroll (§8).

Mobile: below 760px the chart becomes a vertical stack of date-labeled rows. A
horizontally-scrolling gantt on a phone is a bad experience and won't ship.

### 4.4 Professional Experience

Full YAML content — every role, every bullet, verbatim. Each role is a card:
title (Roboto 700) / org (Montserrat 600, `--muted`) / dates (mono, `--faint`,
right-aligned) / bullets with the `▸` marker.

**Preserve the editorial decision the two YAMLs make differently.** `eng_only.yaml`
files RML Creative and Niceman *inside* Professional Experience deliberately —
its own comment explains that a heading would make music *a category of the
candidacy* whereas a work-history entry makes it *a business he runs*.
`eng_music.yaml` gives music its own section. **The pages must not flatten this
into one shared template.** It is the sharpest content decision in the résumé
set and it survives the port intact.

### 4.5 Core Expertise matrix

One card per group, each with a mono uppercase label and its skills as chips
(`--surface-2` fill, 1px `--line`, mono, 0.8125rem). Two columns desktop, one
mobile. eng-only has 5 groups, eng-music has 6 — the grid handles both without
a special case.

### 4.6 Selected Applications & Systems

The `.app` card pattern from `wp-rates-page/css/rates.css` (16:9 `object-fit:
cover` frames, `--surface` cards), with **the résumé's own project prose as the
blurb — not rewritten.** `verify_facts.py` guards that wording; retyping it here
would put a second, unguarded copy into the world.

| Résumé project | Image | Note |
|---|---|---|
| E-commerce Intelligence Platform — Tromml | `app-ecommerce-intelligence.png` | 1693×929 |
| The $30M Data Backbone | `app-data-backbone.png` | 1672×941 |
| Notion–GitHub AI Dev Command Center | `app-notion-system.png` | **543×506 — see below** |
| SetMaster 3 / RML SetMaster 3 | `app-setmaster.png` | 1494×848. **See §6** |
| pdpd | `app-pdpd.png` | 1327×807 |
| BQL Analytics Provisioner | `app-bql.png` | 1536×1024 |
| Time-Trackify | `app-time-trackify.png` | 1387×909 |
| AI Coaching Program & Curriculum *(eng-only only)* | `app-coaching-intake.png` | 1178×826. **See §6** |

**`app-notion-system.png` is 543×506** — near-square and low-resolution. In a
full-width 16:9 cover frame it will go visibly soft. It gets a **half-width card
with a 4:3 frame** instead, which keeps it sharp and reads as an intentional
rhythm break rather than a defect.

### 4.7 Case studies

**As built (2026-07-31): three designed placeholders.** Frames numbered and sized
as though the content were already there, with a mono `IN PREPARATION` chip (coral
1px border, no fill) where the read-more link would go. **Not** "coming soon"
apology copy — a table of contents for work in progress.

| # | Title (Ry's words) | Frame image |
|---|---|---|
| 01 | Developing a proprietary software spine to grow a startup to $30M | `app-data-backbone.png` |
| 02 | How AI-powered transaction-level tracking equates to $M annual ROI | *empty frame* |
| 03 | SetMaster 3 — from problem, to prototype, to a shipped web app | `app-setmaster.png` |

Each frame carried a stable `id` so a future case study could be linked in without
re-cutting the section — and that is exactly what happened, twice: case 02 was
replaced by the published financial model study on 2026-08-04, and the whole
section was rebuilt on 2026-08-17.

**As it stands now (D-011, 2026-08-17, #218): four published studies, no
placeholders.** The design intent above is *spent*, not abandoned — the geometry
it produced is what let every swap since be a one-element change.

| # | Title | Frame image | Links to |
|---|---|---|---|
| 01 | An AI Operating Layer for Streamlining Project Delivery | `case-ai-command.jpg` | `/wolfpack-ai-command/` |
| 02 | SetMaster 3 — from problem, to prototype, to a shipped web app | `app-setmaster.png` | `/setmaster3-case-study/` |
| 03 | Consolidation Under Pressure: M&A in music gear and pro audio, 2016–2026 | `case-consolidation.jpg` | `/consolidation-under-pressure/` |
| 04 | The Model Is Your Business Beacon: a financial model as an operating tool | `case-fin-model.jpg` | `/ops-fin-model-case-study/` |

**The order is Ry's** and follows nothing derivable — not alphabetical, not
chronological, not by publication date. Do not re-sort it.

The `.case__chip` and `.case__shot--empty` devices both survive in `hire.css`,
unused, for the next unpublished study. The section head carries **no count** in
either string, which is what the old *"Three builds"* / *"Two are published; ask
about the third"* pair got wrong: it went stale silently every time a case study
shipped, and by 2026-08-17 it had.

### 4.8 Music & Creative Technology — music page only

`eng_music.yaml`'s dedicated section: RML Creative LLC, Niceman Music Studio LLC,
and the closing line (36 years piano · 20+ years production · 20+ years DJ · the
vendor-ecosystem list).

**The RML mark (D-006).** Placed as the section's own lockup at the head of the
section, ~44px tall, on a navy chip with `border-radius: 4px` — exactly the
treatment `header-footer-spec.md` §5 specifies for the mark on a light ground,
inverted for the dark field. This invokes the standing third-color exception
(the orange→violet sun) and is the **only** place on either page where a color
outside navy/coral appears. Per that same spec it never shares space with a coral
fill — so no coral CTA sits inside this section.

Caveat from `brand-reference.md` §5: the RML PNG is a **recovered raster**, clean
at résumé size and no larger. 44px is well within that; it must not be scaled up.

### 4.9 Current Technical Focus · 4.10 Education

Straight ports. Current Technical Focus keeps its `(2026)` note as a mono kicker.

Education carries a second panel — the music training — **on both pages**
(D-010, round 3), reversing round 1's call that eng-music didn't need it because
the music section already said so. It sits in **its own labeled panel**
(`.edu-aside`), not inside the Cornell card: it is Education content and belongs
in the section, but housed with the degree it read as a footnote to a 2007 B.S.
rather than as the separate lifelong practice it describes (Ry, feedback
round 1).

The two versions are **not** the same paragraph. eng-only's carries the training
*and* the spans, because it is the only place on that page music appears at all;
it also keeps a sentence about real-time systems and signal processing, which is
the whole reason a non-music employer should care. eng-music's carries the
training and points back at the music section for the spans — restating them a
screen below the closing strip would just read as padding.

**Two sentences are shared verbatim** across both panels (Ry's wording, round 4):
the training sentence — *"Sound engineering and composition learned through
mentors, online programs, and practice."* — and the closing one — *"Music and
audio are passions that I will study and explore for the rest of my life."*
Edit them in both files or in neither. That closing line is a deliberate register
shift: it is the one sentence in either panel that a résumé could not have
produced, and it is the only place the music reads as intent rather than
credentials.

### 4.11 Closing contact block + footer

Contact slab inverted (§4.1), full contact set repeated, both CTAs. Footer
follows the site pattern: wordmark left, mono meta right, hairline above —
`RYAN HICKEY · RYAN@WOLFSTRATEGYLLC.COM · WOLFPACK DATA & STRATEGY`, matching
`header-footer-spec.md` §6. Music page swaps the trailing org for
`RML CREATIVE`, which that spec explicitly sanctions.

The closing block holds **three** buttons — book a call, PDF, DOCX. The
consultancy link is not among them; see §4.12.

### 4.12 Secondary CTA — the consultancy coda

A short band between the closing block and the footer (`.section--coda` +
`.softcta`): mono kicker `ALSO`, the name *Wolfpack Data & Strategy*, one line
of what it is, and a single ghost link out to `wolfstrategyllc.com`. Identical
on both pages.

It exists because visiting the consultancy site is a **real but secondary**
goal, and round 1's placement didn't say that. Sitting inside the closing block
as a fourth ghost button, it lined up beside the two résumé downloads and read
as one of them — a wide, oddly-labeled sibling in a row of file downloads
(Ry, feedback round 2). Below the block, in its own quieter frame, the ordering
is legible without a word of explanation.

Rules it keeps: no coral (D-008), one link only, copy stays to a single line,
and it is **not** in the nav — a coda you land on by scrolling past the contact
block, never a destination the page steers you to.

---

## 5. The delta between the two pages

Both pages are generated from their own YAML and share only CSS/JS/assets. The
content differences are real and deliberate:

| Element | eng-only | eng-music |
|---|---|---|
| Role line | `… · COO · Technical Operator` | `… · COO · Professional Musician` |
| Summary ¶1 | no music clause | adds the music-tenure clause (D-009) |
| Core Expertise | 5 groups — incl. **Data & Analytics Engineering** as its own group | 6 groups — data folded into Software Engineering; adds **Music Technology** and **Audio Data & Catalog Engineering** |
| Experience | 6 roles — RML + Niceman filed *inside* the section | 4 roles |
| Music section | none | present, with RML mark and closing line |
| Projects | 8 — includes AI Coaching Program & Curriculum | 7 |
| SetMaster card | "SetMaster 3", vendor names deliberately absent | "RML SetMaster 3", Traktor and Spotify named |
| Education | 2 lines | 1 line |
| Footer org | Wolfpack Data & Strategy | RML Creative |
| Third color | none | RML sun, music section only |

---

## 6. Content conflicts to resolve before build

Three. (a) and (b) were surfaced by pairing the copy against the imagery and
neither blocks the plan; (c) is open and outlives this repo.

**(a) The SetMaster screenshot names vendors the eng-only copy avoids.**
`eng_only.yaml` describes SetMaster without Traktor or Spotify — its header
comment shows this is deliberate framing for a non-music audience ("the
Python/TypeScript application it is, described without the vendor names"). But
`app-setmaster.png` shows a sidebar reading *"Spotify®-Traktor® Comparison
Settings"* and *"RML SetMaster"* in plain sight. **Recommendation:** ship it
as-is. The copy choice is about *framing*, not concealment, and a hiring manager
seeing a real UI is worth more than a tidy abstraction. If Ry disagrees, the fix
is a crop to the main table area — 10 minutes, no code change.

**(b) `app-coaching-intake.png` pictures the intake system, not the curriculum.**
The eng-only résumé's eighth project is *AI Coaching Program & Curriculum*; the
screenshot is the branded intake page. **Recommendation:** title that card
`AI Coaching Program — intake & delivery system` and keep the résumé's curriculum
prose as the blurb, so the caption is honest about what's pictured without
contradicting the résumé.

**(c) RESOLVED in résumé round v2.4 ([#77](https://github.com/wolfpackdata/wp-website/issues/77)) — the résumé said "a 36-year music career" (D-009).** Round 2
corrected the pages; the source YAML was left alone, so the two disagreed and
the résumé was the wrong one. The table below is the record of what was changed;
all three rows landed in `v2.4`, `verify_facts.py`'s `FIGURES` ledger was
re-annotated, the D-010 training sentences were added to both YAMLs and are now
guarded by `SHARED`, and `export_pdf.py` refreshed the four artifacts in
`hire/assets/dl/`. Exact strings, both in
`ryan-resume-dev/resume_build/content/eng_music.yaml`:

| Where | Currently says | Should say |
|---|---|---|
| `eng_music.yaml` Professional Summary ¶1 (~line 40) | `alongside a 36-year music career spanning piano performance, studio production, sound design, and DJ performance` | 36 years at the piano; 23 years paid to perform, since 2003 |
| `eng_music.yaml` Music section `closing:` (~line 315) | `20+ years of DJ performance` | professional DJ since 2009 (17 years) |
| `eng_only.yaml` Education (~line 302) | `Thirty-six years of piano performance and 20+ years of studio production` — no training, no paid-performance span | add the 23 years, the **10 years of classical study with a university professor**, and that the engineering came from mentors and paid programs (D-010) |

Neither YAML mentioned the training at all, so **`eng_music.yaml` took the D-010
facts as well as the D-009 corrections** — before v2.4 the résumé was the only
artifact of the three that still read as though the music were self-taught. Both
Education sections now carry it, and the two sentences Ry wrote verbatim are
guarded by `verify_facts.py`'s `SHARED` set, so they cannot drift apart the way
the tenure facts did.

`verify_facts.py`'s `FIGURES` ledger took the matching edits — `"36 years"` was
annotated *"piano performance and study"* (still correct, but it had to stop
covering the career claim), `"20+ years"` was annotated as also covering *"DJ
performance"* (no longer true), and `23 years`, `10 years`, and `2003` are new
entries. The check reads the YAML, not these pages, so nothing failed while the
drift existed — **that silence is the lesson**, and it is why the fix needed a
tracked task rather than a red build.

---

## 7. Contact information — exact strings

Ry asked for full contact detail at both the top and the bottom. The page set is
a **superset** of the résumé's contact line (D-005: phone added). Recording it
here so the two artifacts can't drift silently.

| Field | Value | On résumé? |
|---|---|---|
| Email | `ryan@wolfstrategyllc.com` | ✓ |
| Phone | `415-371-9613` | ✗ — **page only** (D-005) |
| Website | `wolfstrategyllc.com` | ✗ — **page only** (D-008) |
| LinkedIn | `linkedin.com/in/ryan-hickey-626b2798` | ✓ |
| GitHub | `github.com/wolfpackdata` | ✓ |
| Location | `San Francisco Bay Area` | ✓ |
| Booking | `https://calendar.app.google/zHNd1NA9wzb4VRLw5` | ✗ — page only |

The hero contact line uses a **trailing** separator (`li:not(:last-child)::after`)
rather than a leading one. With a leading `·`, a wrap drops a stray bullet at the
start of the next line; trailing keeps the mark glued to the item it follows.

Email is `mailto:`, phone is `tel:+14153719613`, LinkedIn and GitHub are real
links. Per `CLAUDE.md`, same-domain links open in the same tab; the calendar link
is external and opens in a new tab with `rel="noopener"`.

The `…/13EANJ63HKqMc76z6` calendar is the **45-minute tutoring** link and must
never appear on these pages.

---

## 8. Animation

Ry's constraint was *"if animation tools overcomplicate the build, leave them
out."* No library is needed, so it ships — **~50 lines of vanilla JS, zero
dependencies**, in `hire/assets/js/reveal.js`.

- **Reveal on scroll.** One `IntersectionObserver` at `threshold: 0.15`,
  `rootMargin: 0px 0px -8%`. Elements fade in and rise 12px over 500ms
  `cubic-bezier(.2,.6,.2,1)`, staggered 60ms by index within a section. Observer
  unobserves after firing — nothing re-animates on scroll-back.
- **Timeline bands** (§4.3) draw in by transitioning `transform: scaleX()` from
  the left origin, 700ms, staggered top to bottom.
- **Scroll-spy nav** — same observer marks the active section in the sticky rail.

Two non-negotiables:

1. **`prefers-reduced-motion: reduce` bypasses all of it.** The observer never
   attaches; everything renders final-state. The existing stylesheets already
   honor this and the pattern carries over.
2. **No-JS safety.** JS adds a `.js` class to `<html>` on load; the hidden
   initial state is scoped `.js .reveal { … }`. With JS off or broken, every
   element renders visible. **A résumé that requires JavaScript to be readable is
   a broken résumé** — this is the same failure mode as the v2.1 image-header ATS
   problem in `header-footer-spec.md` §9, and it gets the same treatment.

Explicitly **not** doing: parallax, counters that tick up, typewriter effects,
scroll-jacking, entrance animations on body text. Those are the corny.

---

## 9. PDF + DOCX pipeline (D-003)

Word COM is available on this machine (verified: v16.0), so conversion runs
through the same engine that laid the `.docx` out — highest fidelity available,
no LibreOffice install needed.

**New:** `ryan-resume-dev/resume_build/export_pdf.py`

1. Build both `.docx` as normal (`python build.py`).
2. Open each via `win32com.client` → `Documents.Open` →
   `ExportAsFixedFormat(…, wdExportFormatPDF, …)` with
   `DocStructureTags=True` so the PDF keeps a tagged structure tree — the
   accessibility/parseability property that matters for the same reason
   `ats-guidelines.md` exists.
3. Copy all four artifacts to `hire/assets/dl/` under clean public names.
4. Quit Word in a `finally`, so a failed run can't leave a headless WINWORD
   process holding the file.

**Download filenames.** A hiring manager saves these to a Downloads folder, so
the versioned build name is wrong for the public artifact:

| Source | Public download name |
|---|---|
| `Ryan_Hickey_Resume_eng-only_v2.2.docx` | `Ryan-Hickey-Resume.docx` / `.pdf` |
| `Ryan_Hickey_Resume_eng-music_v2.2.docx` | `Ryan-Hickey-Resume-Music.docx` / `.pdf` |

The rename is scripted in step 3, never done by hand, so the download can't go
stale against a rebuilt résumé. Both `.docx` are already staged; the two PDFs are
the outstanding artifacts.

`verify_facts.py` check 5 reads the `.docx` and is unaffected. **Extending it to
the PDF is worth doing but is out of scope for this round** — flagged in §12.

---

## 10. Files

```
hire/
├── README.md                      ← what this is, how to deploy, D-001 staleness warning
├── assets/
│   ├── css/hire.css               ← one stylesheet, both pages; coral ration in the header comment
│   ├── js/reveal.js               ← IntersectionObserver reveal + scroll-spy
│   ├── fonts/                     ← 14 woff2 (Roboto + Montserrat)   ✓ staged
│   ├── img/                       ← 8 app shots, wolf mark, RML mark, 2 portraits  ✓ staged
│   └── dl/                        ← 2 DOCX ✓ staged · 2 PDF pending §9
├── ryan-hickey/index.html
└── ryan-hickey-music/index.html
```

Design docs live in `docs/` per the convention already set by
`public-rates-design-brief.md` / `-spec.md` / `-consistency-contract.md`.

---

## 11. Deployment

**This repo serves nothing** — GitHub Pages is off (#74, 2026-07-30). These pages
reach the public only by copying `hire/` into `wolfpackdata/ai-coaching-intake`,
which owns `intake.wolfstrategyllc.com`. Same policy as `rates/`, `ai-coaching/`,
and `roi-calculator/`: **this repo stays the source of truth; never edit the
deployed copy; re-copy on change.**

Because the folder here mirrors the deploy path, shipping is one copy of `hire/`
into the intake repo root — the URLs then resolve with no path rewriting.

Follow-ups this creates:

- **The Web Property Map is already stale** — `wp-website` Pages returns 404 as of
  today (#74), which the map does not yet reflect. Shipping these pages will add
  two more URLs to `intake.wolfstrategyllc.com`. Both updates should land in the
  same edit to the map.
- Two new entries in the `CLAUDE.md` canonical-URL table.
- `CHANGELOG.md` entry.
- GitFlow: this needs an issue and a `feat/<issue>-hire-pages` branch off
  `develop` before any of it is committed. Not filed yet — awaiting Ry's go.

---

## 12. Build order

1. `hire/assets/css/hire.css` — tokens, hero slab, section rhythm, cards, timeline, footer.
2. `hire/ryan-hickey/index.html` — full eng-only content from `eng_only.yaml`.
3. `hire/assets/js/reveal.js` + wire it in.
4. `hire/ryan-hickey-music/index.html` — eng-music content, RML lockup, footer swap.
5. `export_pdf.py`; run it; verify all four downloads open.
6. Verify at desktop, tablet, and **true 390px phone width via the iframe method**
   in `CLAUDE.md` (headless Chrome fakes overflow below ~492px — don't trust a raw
   mobile screenshot).
7. Accessibility pass: heading order, contrast on every pair, focus-visible on
   every interactive element, `prefers-reduced-motion` honored, JS-off render.

**Acceptance criteria** — status after the first draft

- [x] Every line of both YAMLs appears on its page. Nothing dropped, nothing invented.
- [x] Project blurbs and experience bullets are **verbatim** from the YAML.
- [x] Coral appears only in the eight places listed in §3.
- [x] Full contact set at both top and bottom of both pages (§7).
- [x] `Contact Ryan` → `calendar.app.google/zHNd1NA9wzb4VRLw5`, everywhere, both pages.
- [x] Both pages carry `noindex, nofollow` and a self-referential canonical.
- [x] Zero external network requests — verified by grep over HTML/CSS: the only
      absolute URLs are the calendar, LinkedIn, GitHub, and the canonicals.
      No `@import`, no `url(https:…)`. Every local asset path resolves.
- [x] Page renders complete and readable with JavaScript disabled — the hidden
      state is scoped to `.js`, which only `reveal.js` adds.
- [x] No horizontal scroll — measured `scrollWidth − clientWidth = 0` on both
      pages at **320 / 390 / 768 / 1024 / 1440 px**.
- [x] All four downloads present, generated by `export_pdf.py`, and opening.
- [x] `verify_facts.py` still passes: *6 roles, 15 figures, 9 shared facts,
      headers consistent, contact block parseable.*

**Known issue — PDF text extraction inserts a space in the LinkedIn URL.**
`pypdf` reads the contact line as `linkedin.com/in/ryan -hickey-626b2798`. The
characters are all present; Word's PDF renderer emits a kerning adjustment that
extractors read as whitespace. The `.docx` is unaffected — `verify_facts.py`
check 5 parses its contact block cleanly. This is the reason the DOCX button is
labeled **“DOCX · ATS”**: PDF for humans, DOCX for the portal. Fixing it means
touching character spacing in the résumé build, which is out of scope for this
round and would need re-verification of both documents.

**Deferred, deliberately**

- Extending `verify_facts.py` to check the exported PDFs (§9).
- A build step that generates the HTML *from* the YAML. Tempting — it would make
  drift structurally impossible — but it means a template engine and a build step
  in a repo whose defining property is *static HTML/CSS/JS, no build step*
  (`CLAUDE.md`). Hand-authored for now; revisit if the résumés change often
  enough to make manual sync a real cost.

---

## 13. Open items for Ry

1. **The career timeline** (§4.3) — foreground the concurrency, or drop the
   section? Recommendation: keep it. It is the strongest thing on the page.
2. **SetMaster screenshot vendor names on the eng-only page** (§6a) —
   recommendation: ship as-is.
3. **Coaching card title** (§6b) — recommendation: retitle to match what the
   screenshot actually shows.
4. **Availability line wording** — D-001 settled the *posture*; the exact
   sentence is a draft until Ry approves it.
5. **Whether to file the GitHub issue now** or after the plan is approved (§11).
