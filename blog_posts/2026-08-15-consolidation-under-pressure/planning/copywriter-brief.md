# Copywriter brief — the Consolidation Under Pressure post

**For:** the person writing the post. **Not** the post itself, and not a draft to
polish. Everything here is raw material and constraints — with one large exception,
spelled out immediately below, which is that most of the sentences are not yours to
write.

**Deliverable:** one post, target **700 words**, hard cap **900**, at
`blog_posts/2026-08-15-consolidation-under-pressure/post.md`, plus a LinkedIn
version at `raw-linkedin-post.md`.

> **Read this before section 1.** This brief was written in the same session as the
> draft it describes. The instruction was to lift verbatim copy from the case study
> rather than reinvent it, so there was no copywriter handoff and no
> `raw-blog-post.md` — the body went straight into `post.md`. The brief is
> therefore a **record of the constraints the draft was built under and the spec for
> redrafting it**, not a handoff that was acted on. It is written in the second
> person anyway, because the next person to touch this post will be redrafting
> rather than reading history.

---

## 1. Hard constraints

- **The title is the case study's `h1`, verbatim:** *Consolidation Under Pressure*.
  Repo rule, set 2026-08-04 (#119) — one piece of work, one name. Not the `<title>`
  tag, which carries the subtitle and a `· Case Study` suffix meant for the tab and
  the SERP. The slug is set explicitly and does not follow the title.
- **The excerpt is the page's `og:description`, verbatim.** Verify it against the
  HTML; do not improve it. Note that it is *not* the same wording as the hero
  standfirst the post opens on — the page carries both forms, and so does the post.
- **Lifting is the job.** The body is verbatim from
  `case_studies/consolidation_under_pressure/index.html`. Paraphrasing a lifted
  paragraph into your own phrasing is the failure mode, not the craft.
  **Cutting whole sentences from a lifted passage is allowed** and is how the
  numbers policy gets enforced; every cut is recorded in
  `planning/source-notes.md`. **Reflowing structure is allowed** — an HTML card
  list into bullets, an `h3` into a bolded bullet lead. **Rewording is not.**
  Connective tissue between lifts must be minimal and explicitly recorded as
  original.
- **The page's prose is Ry's**, after three review passes — #197, #200 and #206 —
  that rewrote sentences for evidentiary correctness and cut a quarter of the
  defensive language. Nothing guards this post against the page. `verify_copy.py`
  guards the *page* against its vendored source; it has never seen the blog folder.
  **Change the case study first, then re-lift. Never the reverse.**
- **Never lift from the vendored `.md`.** `planning/01-ma-landscape-2016-2026.md`
  and the upstream `dj-gear-study` markdown are both now behind the page in the
  places #197 corrected. The PAGE is the source.
- **The case study's evidence rules carry over in full.** No results section, no
  invented outcome, no testimonial, and **no client named** — the anonymisation is
  *"a music-technology manufacturer"* and it is lifted exactly, never loosened,
  never sharpened. There is no instrumented result behind this document and the post
  must not imply one.
- **Two links in the whole post**, and no third: the case study, and the intro call.

---

## 2. The numbers policy — the sharp edge of this post

The case study is a numbers document, and `planning/verify_copy.py` checks every
numeric token on the page against the vendored source, plus the `Src` column
arithmetic, the source links' accessible names and the map dataset. **Nothing
guards a number copied into a blog post.** It arrives undated, unlinked, and drifts
on its own. So:

- **The only numerals allowed anywhere in the body or the excerpt** are the window
  **2016–2026**, **43** (transactions) and **31** (of them primary-sourced). These
  are the page's own meta-description set — the vetted, public-facing numbers. Lift
  them in the page's phrasing (the `#about` block spells them: *Forty-three*,
  *Thirty-one*).
- **No other numeral, anywhere.** No deal value, no percentage, no year of any
  individual event, no era date, no market size, no currency figure, no FX rate.
  **If a passage you want carries one, cut that sentence or choose another
  passage.** Most of the cuts recorded in `source-notes.md` are exactly this.
- **Never cite the transaction map's event count, in any form.** The brief says 41,
  the dataset holds 42, and design-plan **D-009 is open with Ry**. A post that picks
  a side gets it wrong, in a place nothing checks. Describe the map; never count it.
- **Do not recompute, round, sum or derive anything.** Lift or omit. There is no
  third option.
- **Spelled-out counts of the report's own structure are fine inside a verbatim
  lift** — *ten years*, *eighteen months*, *two shocks*, *three eras*, *five
  patterns*. They describe the document, not the market. **The report's part count
  is not one of them:** the page labels its sections *Part zero … Part nine* plus
  two appendices, so any bare count reads wrong, and the "eleven parts" in the root
  `CLAUDE.md` is not sourced from the page. The draft carries no part count at all. The draft
  also carries two counts of the report's *evidence* structure inside the `#about`
  lift — *the other twelve* unsourced rows, *the seven places the record is thin* —
  and flags them in `source-notes.md`. If that ever reads as one count too many, drop
  the whole paragraph rather than editing his sentence.

---

## 3. The subject, in plain description

A ~6,000-word public-source market-intelligence report on M&A in music gear and pro
audio, 2016–2026, written for the executive committee of an anonymised
music-technology manufacturer and reproduced on the site in full. Numbered parts
labelled **Part zero through Part nine** plus two appendices, eight data tables,
four rendered figures, 43 cited transactions with a source
column that distinguishes the 31 primary-sourced rows from the 12 that are not, and
an interactive transaction map that ships twice — embedded at fixed width in the
report, and full width in a `noindex` standalone page.

The argument, in the order the report makes it: music revenue is at a high while the
gear industry is flat and taxed; two macro shocks — a pandemic demand spike that
reverted, and the tariffs — sit underneath the recent distress; the decade's deals
split into three eras; three transactions define the category; five patterns run
through the record; and the money migrated to platforms and rights-holders while
hardware sat at the least monetizable point in the chain.

Source, not copy. **The post does not tour all of that** — see section 4.

---

## 4. Suggested outline, with word budgets

Adjust the split, not the total. **The post's only job is to make someone read the
case study.** A taste, not a summary — the AI Command post ran ~1,150 words and this
one has to be visibly shorter.

| § | Section | Words | Must contain |
|---|---|---:|---|
| 1 | Open on the hook | 100 | The hero standfirst verbatim — it is the strongest sentence pair on the page — then ONE short original paragraph saying this is an abbreviated taste of a much longer report, linked at the end. Do not enumerate the contents; §5 does that |
| 2 | The paradox | 200 | Lifted from `#paradox`: the two diverged industries, the popular framing being wrong in two of its three clauses, the value-migration paragraph, and the bifurcation counter-signal. The page's one pull quote (from §06) belongs here — it is the paradox in one line |
| 3 | The two shocks | 150 | The framing prose from `#shocks`, **not the figures**: the demand spike, "the problem is the shape, not the size", the cohort-not-a-run-rate line, the sponsor-leverage passage, and the closing discipline paragraph about not attributing software damage to a hardware duty |
| 4 | What the deal record shows | 170 | The `#about` block — this is where the vetted counts live and where the client anonymisation is lifted — plus the three-eras line and two of the five patterns as bullets |
| 5 | The full version + CTA | 90 | One or two sentences on what the full report contains, the case study link, a short Wolfpack plug (lift the `#start` close), then the intro-call button |

**If only one thing survives a cut, it is §3's discipline paragraph** — *attribute
the hardware damage to tariffs; treat the software link as reasoning from
adjacency*. It is the sentence that tells a reader what kind of document the case
study is, which is the entire pitch.

---

## 5. CTAs

- **Inline link:** exactly one — *Read the case study*, pointing at
  `https://intake.wolfstrategyllc.com/consolidation-under-pressure/`.
- **Closing CTA:** the 30-minute intro call,
  `https://calendar.app.google/zHNd1NA9wzb4VRLw5`, labelled **Work With Wolfpack**
  (matching the financial model and AI Command posts; the page's own button reads
  *Contact Wolfpack*).

**Both URLs are the page's own.** The case study URL comes from its
`<link rel="canonical">` and `og:url`; the call URL matches both of its CTAs and the
current intro-call URL per #32.

**The case study is live.** Verified 2026-08-15 by fetching that URL: it returns the
report with the matching `h1` and standfirst. Trust the URL, not the root
`CLAUDE.md` deployment table — that table is a record kept by hand and it has been
stale before (it was stale for the AI Command case study on the same day).

No intake-form link, no rates link, no portfolio link, no résumé download, and **no
link to `transaction-map.html`** — see the traps.

---

## 6. Traps

- **Never hard-wrap a list item.** The converter joins wrapped lines inside a
  paragraph but **not** inside a bullet (#208), and it fails silently: a two-line
  bullet becomes a one-item list plus an orphan paragraph, with a plausible node
  count and no warning. Three wrapped items become three lists each numbered `1.`.
  Hard-wrap prose freely; keep every bullet on one source line.
- **Do not fork Ry's copy.** The single most expensive mistake available here. A
  lifted paragraph you "tightened" is now a second wording of his sentence, with
  nothing anywhere able to see the two have diverged. If a sentence has to go, cut
  it whole and record the cut.
- **Do not link the transaction map.** `transaction-map.html` is `noindex`, carries
  no Open Graph block, and is deliberately reached from the report and nowhere else.
  A blog post pointing traffic straight at it defeats that in one line.
- **Do not carry a source link.** The report's 82 citations are citations. This post
  has two destinations and they are both listed above.
- **Do not count the map's events.** See the numbers policy. D-009 is open.
- **Do not name a company.** The draft names none, deliberately — it keeps the post
  clear of the numbers policy and of any accidental characterisation of a live
  business. Part Four's three transactions are the reason to click through.
- **Do not re-add a figure "because it's only one number."** The whole policy exists
  because one number is exactly how it starts, and the case study's numeric surface
  is guarded precisely so that this one is not.
- **Do not summarize all eleven parts.** A post that does is a worse case study, not
  a better post.
- **No tables, no nested lists, no raw HTML** — the converter does not support them.
  No hand-authored blank paragraphs either; spacing is inserted at payload assembly
  and a manual one arrives doubled.

---

## 7. The cover image

`cover.jpg`, 1200 × 675, 226 KB, in the post folder.

A luminous blue-violet circuit-tree at night on a dark desert plain: trunk and
branches drawn as glowing circuitry, the canopy grown out of music-gear forms —
mixing consoles, speaker cones, synth and drum-machine panels, waveform readouts,
vinyl records — with fine constellation lines threading the branches. `cover_alt` is
written, is in the front matter, and carries no figures.

**This is SUPPLIED ART from Ry (2026-08-15), and it is unlike the other two
case-study covers in two ways that matter.**

1. **There is no generator and no rebuild path.** The financial model and AI Command
   heroes are both composed by a committed `build_hero.py` and the standing
   instruction is *rebuild rather than retouch*. This one has no such script. The
   master is the committed source PNG at
   `case_studies/consolidation_under_pressure/planning/consolidation-under-pressure-hero.png`
   (1337 × 752), and `cover.jpg` is a downscale of it. **Retouching means asking Ry
   for new art** — there is nothing to re-run.
2. **The art appears nowhere else in the repo.** The other two covers are their case
   study's own hero, so the reader meets the same image on both surfaces. This case
   study's hero is a text hero with stat tiles and no image, so the tree exists only
   as this post's cover. That is fine — but it means a future change to the case
   study page will never surface here, and a change here will never surface there.

**Considered and rejected:**

- `case_studies/case-study-assets/img/og-consolidation-under-pressure.png` — the
  finished social card (1200 × 627). It has the title text baked into it, so as a
  blog cover it would print the headline twice in the feed, once as art and once as
  the post title.
- `case_studies/consolidation_under_pressure/planning/card/map-capture.png` — the
  transaction-map capture (1932 × 842) built by `planning/card/capture_map.py` as the
  **inset for that card**, at a size that reads as texture in a 360 px LinkedIn tile.
  Wrong in role, and unreadable as a cover: at cover scale it is four lanes of small
  dots with labels no reader can resolve, and it invites exactly the question the
  post is forbidden to answer — how many events are on it.

---

## 8. The LinkedIn version

**Target ~300 words**, at `raw-linkedin-post.md`. Same lift discipline, same numbers
policy, same evidence rules — none of them relax because the surface is a feed.

It opens on the hook (the standfirst's first two sentences), carries the paradox and
the pull quote, both shocks, and the method passage that holds the counts, then ends
on **a question to the reader** followed by *"Read the full case study linked in the
Wolfpack profile."* — the profile-link convention the other two LinkedIn drafts here
follow, rather than pasting a URL in the body. **No hashtags**, matching every other
LinkedIn draft in this repo.

**It is Ry's to post**, and the HTML comment at the bottom says so, along with the
case study URL for if he would rather paste it after all.

---

## 9. Source files, if you want to go deeper

| Topic | File |
|---|---|
| Front matter schema, converter limits, push procedure | `blog_posts/README.md` |
| Passage-by-passage provenance, every cut, the redaction check | `planning/source-notes.md` |
| The case study itself — **the source for every lift** | `case_studies/consolidation_under_pressure/index.html` |
| Design plan and decisions ledger, incl. **D-006** (one destination) and **D-009** (the event count) | `docs/consolidation-case-study-design-plan.md` |
| The numeric-surface guard on the page | `case_studies/consolidation_under_pressure/planning/verify_copy.py` |
| The original research report and the case study brief | `case_studies/consolidation_under_pressure/planning/01-ma-landscape-2016-2026.md`, `02-case-study-brief.md` |
| Case study folder conventions and voice notes | `case_studies/README.md` |
| The social card and its map inset | `social-cards/build_cards.py`, `case_studies/consolidation_under_pressure/planning/card/capture_map.py` |
| The worked example this post's shape follows | `blog_posts/2026-08-15-ai-operating-layer/` |
