# Source notes — Consolidation Under Pressure

Everything in this post came from one place: the case study at
`case_studies/consolidation_under_pressure/index.html`, as it stood at commit
`64fa14d` — *"fix(case-studies): narrow two overclaimed theses and cut a quarter
of the defensive language (#206)"*, the last of Ry's three review passes.

The instruction for this post was the same one the AI Command post ran under:
**lift verbatim copy from the case study rather than reinvent it.** So this is not
a post *about* the report written from notes. It is the report's own argument, cut
to a taste, in its own words.

## Why the no-fork rule bites harder here

Two reasons, and they compound.

**The page is guarded and this post is not.** `planning/verify_copy.py` checks
every numeric token in the vendored source `.md` against the page, plus the `Src`
column arithmetic, the source links' accessible names, the map dataset and the
external-request stance. It has never seen this file and never will. A number
copied into a blog post arrives undated, unguarded, and drifts on its own — which
is why the numbers policy below is the sharpest constraint on the piece.

**The page's prose is Ry's, and the upstream markdown is now wrong.** #197, #200
and #206 rewrote sentences for evidentiary correctness and cut restatement.
Passages that exist in `planning/01-ma-landscape-2016-2026.md` and not on the page
are *expected*; the root `CLAUDE.md` says so, and it says the upstream
`dj-gear-study` `.md` is now wrong in the places #197 corrected. **The PAGE is the
source for this post. Never the vendored `.md`, and never the upstream one.**

Consequence: **change the case study first, then re-lift.** A lifted paragraph
re-edited here silently forks his copy, and nothing anywhere would see the gap.

## Passage map — `post.md`

Every row is verbatim from the page unless it says otherwise. "Cut" always means
whole sentences removed, never sentences rewritten.

| Post passage | Case study source | Treatment |
|---|---|---|
| Opening paragraph | `.hero__stand` | Verbatim, whole. (The front-matter `excerpt` is the *other* wording of the same idea — the page's `og:description`, verbatim. The two differ on the page and both are carried unchanged.) |
| "What follows is a taste…" | — | **Original copy.** The only original paragraph in the body — see below |
| H2 *Music has never been bigger. Gear has never been harder.* | §01 `#paradox` h2 | Verbatim |
| "Two industries share a customer…" | §01 prose 1 | Verbatim sentence 1. **Cut:** "The 2025 full-year results for both:" — carries a year and introduces a stat block the post does not carry |
| "The popular framing…" | §01 *What actually happened* | Verbatim sentence 1. **Cut:** the remaining four sentences — every one carries a market figure (the growth-year count, the vinyl and CD figures, the retail decline, the tariff bill) |
| "The dynamic is not decline but value migration…" | §01 closing prose | Verbatim, whole paragraph, no cuts |
| Pull quote "A phone plus a subscription DAW…" | §06 `.pull` | Verbatim. **Lifted out of order** — §06 is the demand-side explanation of the same paradox, and this is the page's one pull quote |
| "Gear is not uniformly dead…" | §01 `.aside` *The counter-signal, which matters* | Verbatim sentences 1 and 3. **Cut:** sentence 2 (the NAMM decade percentages) |
| H2 *The two economic shocks that produced the distress* | §02 `#shocks` h2 | Verbatim |
| "Lockdowns plus stimulus payments…" | §02 Shock 1, prose 1 | Verbatim sentence 1. **Cut:** sentences 2–3 (the peak year, the guitar-sales percentages, the first-time-buyer estimate) and the whole caveat paragraph after them |
| "The problem is the shape, not the size…" | §02 Shock 1, prose 3 | Verbatim. **Cut:** "Instruments and plugins are durable; a buyer acquired in 2020 is not in the market again in 2022." — two year numerals |
| "Every major sponsor entry…" | §02 `.aside--warn` | Verbatim, with **punctuation deviation 1 of 4 — all four itemized below**: the material after the colon in sentence 1 (the two dated sponsor entries) is cut and the colon closed to a full stop. Sentences 2–3 whole |
| "The second shock was the tariffs." | — | **Original.** The page's own h3 for this shock carries the year, so it could not be lifted |
| "There was no real volume growth anywhere in the US channel." | §02 `.callout--big` | Verbatim sentence 2. **Cut:** sentence 1 (year) |
| "A duty on imported goods…" | §02 closing prose | Verbatim, whole paragraph, no cuts. This is the passage that makes the post's evidentiary stance visible |
| H2 *What the deal record shows* | §00 `#summary` h2 | Verbatim |
| "A market-intelligence report on mergers and acquisitions…" | `#about` prose 1 | Verbatim, with **punctuation deviation 2 of 4**: the trailing clause "and reproduced here in full" cut and the sentence closed at "…manufacturer." Sentence 2 whole. Carries the client anonymisation by shape — *"a music-technology manufacturer"* — exactly as written |
| "The method is the part worth looking at…" | `#about` prose 2 | Verbatim, whole. **This is where the post's only vetted counts live**, in the page's own spelled-out phrasing |
| "The decade splits cleanly…" | §03 `#record` opening prose | Verbatim |
| "The last of the three eras is the correction:" | — | **Original** six-word connective |
| "demand reverts, tariffs land, a regulator intervenes…" | §03 era-3 `.card` body | Verbatim, with "Demand" lower-cased at the join to the connective above |
| "Two of the five patterns the report reads out of that record:" | — | **Original** connective |
| Bullet — *Distress has replaced auction…* | §05 Pattern 3 h3 + prose | h3 verbatim with the "Pattern 3 · " prefix dropped **and a terminal full stop added** (deviation 3 of 4); first sentence verbatim. **Cut:** the second sentence (the retailer's maturity dates and the four-year count) |
| Bullet — *Consolidation runs along the signal chain…* | §05 Pattern 5 h3 + prose | h3 verbatim with the prefix dropped **and a terminal full stop added** (deviation 4 of 4); the paragraph verbatim, whole |
| H2 *The Full Version* | — | Post convention, from the AI Command post. Not from the page |
| "The full report carries the deal record in three eras…" | — | **Original.** Describes the page's structure, and **carries no part count** — see the note under this table |
| "Wolfpack builds that kind of evidence base…" | `#start` `.close__lede` 2 | Verbatim, whole paragraph |
| CTA label *Work With Wolfpack* | — | Post convention, matching the financial model and AI Command posts. The page's own button reads *Contact Wolfpack* |

**Cut from the close:** `.close__lede` paragraph 1 (*"This document exists because
a leadership team needed the deal record in one place…"*). Cut for length only; the
`#about` lift already carries the commissioning shape, and the plug reads back to
the report description above the link.

**No part count.** An earlier draft of *The Full Version* opened *"The report runs
eleven parts"*. That count is **derived and wrong**: the page labels its sections
**Part zero … Part nine**, and "eleven" traces to a line in the root `CLAUDE.md`,
not to the page. It was removed rather than corrected — zero-indexed labelling makes
any bare count confusing, and the enumeration that follows is verifiable without one.
The stale `CLAUDE.md` line is flagged in `planning/workflow.md`, not fixed here.

## Punctuation-level deviations — the complete list

Four in `post.md`, one more in the LinkedIn draft. **Every one is cut-induced**: a
sentence lost material and had to close, or a heading became a bullet lead. **None
is a rewording** — no word of Ry's is changed, reordered or substituted anywhere in
either file, and each remaining fragment is a strict prefix or a whole sentence of
his.

1. **§02 `.aside--warn`** — "Every major sponsor entry in music software happened at
   or immediately after the peak**:**" → the two dated sponsor entries after the
   colon are cut for the numbers policy, and the colon closes to a full stop.
2. **`#about` prose 1** — "…written for the executive committee of a
   music-technology manufacturer **and reproduced here in full.**" → the trailing
   clause is cut and the sentence closes at *manufacturer*. **Reason is not the
   numbers policy but a deictic that changes referent off the page:** on the case
   study "here" is the page, and the claim is true; in a post that says four
   paragraphs earlier that it is an abbreviated version, the same words are false.
   A prefix cut, not a rewrite. The following sentence is kept unchanged — its "it"
   still resolves to the report.
3. **§05 Pattern 3 h3** → bulleted lead, "Pattern 3 · " prefix dropped and a
   terminal full stop added (the page's h3s carry none).
4. **§05 Pattern 5 h3** → same treatment.
5. **LinkedIn, the hook** — the standfirst's clause after the em dash promoted to
   its own sentence: leading "and" dropped, "two" capitalised.

The colon closure at 1 **recurs in the LinkedIn draft**, inside the same reused
lift, and is the same deviation rather than a sixth one. Counting deviations across
both files: five distinct, six occurrences.

## Original prose, in full

Four passages, all short, all listed above. Together they are under 90 words:

1. **"What follows is a taste. This post is an abbreviated version of a much longer
   market-intelligence report on M&A in music gear and pro audio, 2016–2026 — the
   deal record, the shocks underneath it, and the patterns in what changed hands.
   The full report is linked at the end."** — the framing the AI Command post
   carries in the same position, for the same reason: the report has no cause to
   say this about itself. It deliberately does **not** enumerate the contents; *The
   Full Version* already does, and saying it twice makes the post read like it is
   apologising for being short.
2. **"The second shock was the tariffs."**
3. **"The last of the three eras is the correction:"**
4. **"Two of the five patterns the report reads out of that record:"**

Plus the sentence describing the report's structure ("The full report carries the
deal record in three eras…") and the closing question in the LinkedIn draft.
Nothing else in either file is mine.

## Passage map — `raw-linkedin-post.md`

Same discipline, same cuts, and it reuses the same lifts: the standfirst hook, the
popular-framing sentence, value migration, the pull quote, the cohort passage, the
sponsor-leverage passage, the channel line, and the method passage — that last one
**minus its final sentence** ("The methodology names the seven places the record is
thin"), cut for length.

Two things there are not in `post.md`:

- **"Two economic shocks sit underneath much of the distress of the last eighteen
  months."** — the standfirst's clause after the em dash, promoted to its own
  sentence: the leading "and" dropped and "two" capitalised. That is **deviation 5**
  in the list above. Note also that **deviation 1, the colon closure in the
  sponsor-leverage lift, recurs here** inside the same reused passage — the LinkedIn
  draft is not free of the post's deviations, it inherits one of them.
- **"So I built the document I wanted to read."** and the closing question are
  **original**.

## Deliberately left out

- **Every market figure on the page.** Recorded-music and retail revenue, vinyl and
  physical growth, subscriber counts, the tariff rates and the tariff bill, export
  declines, deal values, the purchase-to-sale consideration gaps, subscription
  pricing, every AI-adoption percentage. The report states all of them with a source
  link; a blog post states them with nothing. See the numbers policy below.
- **The three transactions in focus** (Part Four) — the DJ platform and the
  regulator, the marketplace round trip, the insolvency and the three-way split.
  These are the reason to click through, and leaving them out also means **the post
  names no company at all**, which keeps it clear of both the numbers policy and any
  accidental characterisation of a live business.
- **Three of the five patterns**, and the whole of Part Eight's ten implications.
- **The transaction map.** Described in one clause in *The Full Version*, never
  counted, and never linked — `transaction-map.html` is `noindex` and is reached
  from the report, not from a feed.
- **The eight data tables, the four rendered figures, the confidence levels, and
  the seven known gaps** (which survive only as a count, inside the `#about` lift).
- **The 82 source links.** They are citations on that page, not destinations here.

## The numbers policy, as applied

The only numerals in the body and the excerpt are **2016–2026** (once, in the
framing paragraph), and **43** and **31** — which appear the way the page's `#about`
block writes them, spelled out as *Forty-three* and *Thirty-one*. These three are
the page's own meta-description set: the vetted, public-facing counts.

Inside that same verbatim lift, two further spelled-out counts survive — *the other
twelve* rows without a primary source, and *the seven places the record is thin*.
They are counts of the report's own evidence structure rather than market figures,
they are in Ry's sentence, and cutting them would have meant rewriting his
paragraph. **Flagged here rather than assumed:** if that reads as one count too
many, the fix is to drop the whole `#about` paragraph, not to edit it.

Structural counts elsewhere — *ten years*, *eighteen months*, *three eras*, *five
patterns*, *eleven parts*, *two shocks*, *two years*, *three ways* — are spelled out
and describe the document or the shape of an argument, not the market.

**Nothing is recomputed, rounded, summed or derived.** Every figure is lifted or
omitted.

**The transaction map's event count appears nowhere, in any form.** The brief says
41, the dataset holds 42, and design-plan D-009 is open with Ry. A post that picks a
side gets it wrong, and it would be wrong in a place nothing checks.

## Facts checked at write time

- **Case study `h1`:** *Consolidation Under Pressure* — the post's title, verbatim,
  per the repo rule set in #119 (`index.html` line 68).
- **Excerpt:** byte-for-byte the page's `og:description` (line 22). It is
  deliberately *not* the same wording as the hero standfirst the post opens on —
  the page carries both, and so does the post.
- **Canonical URL:** `https://intake.wolfstrategyllc.com/consolidation-under-pressure/`
  from the page's own `<link rel="canonical">` (line 15) and `og:url` (line 20).
  **Verified live 2026-08-15** by fetching it: it returns the report, `h1` and
  standfirst matching. It also matches the root `CLAUDE.md` deployment table
  (deployed 2026-08-15, `ai-coaching-intake#74`).
- **Intro-call URL:** `https://calendar.app.google/zHNd1NA9wzb4VRLw5`, matching both
  of the page's CTAs (nav, line 49; close, line 1204) and the current URL per #32.
- **Two links in the whole post**, and they are these two.

## Redaction check

**Nothing held back.** The only source is a page that is already published, from a
public repo, and whose own basis line reads *Public sources only* — every figure on
it is drawn from a filing, a trade-association report, a regulator's case register
or the trade press, and it states that it contains no confidential information. The
client is anonymised by shape on the page and the post lifts that phrasing exactly:
*"the executive committee of a music-technology manufacturer."*

The post is *narrower* than the page in one respect — it names no company at all —
but that is an editorial choice under the numbers policy, not a redaction of
anything sensitive.
