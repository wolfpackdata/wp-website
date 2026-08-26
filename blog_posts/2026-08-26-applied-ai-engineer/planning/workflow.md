# Workflow — A Fish Called Engineer

Phase: 2 — draft in hand and assembled locally, **not yet pushed to Wix** (Ry's instruction)

| | |
|---|---|
| Folder          | `blog_posts/2026-08-26-applied-ai-engineer/` |
| GitHub issue    | wolfpackdata/wp-website#256 |
| Notion content  | https://app.notion.com/p/3c8c70e5c7b481528c74fe8fdb577007 (Blog Post 11) |
| Notion LinkedIn | https://app.notion.com/p/3c8c70e5c7b481078997c3c1abce7807 |
| Notion task     | https://app.notion.com/p/3c8c70e5c7b481f3b294f2a1dc54f012 |
| Wix draft ID    | **(unset — nothing has been pushed)** |
| Live URL        | (unset) |
| Slug            | `a-fish-called-engineer` — **Ry, 2026-08-26** |
| Cover           | **missing.** `post.md` names `cover.jpg`; Ry is building the hero in parallel |

## How this one differs from the standard Phase 1

Ry handed over a **finished post**, not source material, and explicitly cut the
middle of the workflow:

- **No outline, no copywriter brief, no source notes.** There was no transcript and no
  copywriter — `blog-toothfish-applied-ai__draft2.md` *is* the post. Their absence from
  `planning/` is an instruction, not an omission; do not write them retroactively.
- **`draft2.md` is used verbatim** apart from a punctuation/spelling/grammar pass Ry
  authorized in the same message. The original is preserved verbatim (git normalizes its CRLF line endings, nothing else) at
  `planning/draft2-source.md` so the edit is diffable.
- **This overrides skill §2.3 ("do not edit the prose") for this post only.** Ry granted the
  edit scope directly. It does not generalize — the next post reverts to report-never-correct.
- **No Wix work of any kind**, per Ry. Phase 2 stops after `post.md`.
- The empty `blog-toothfish-applied-ai__draft1.md` was deleted; it was 0 bytes.

## The edit pass — everything Claude changed

Punctuation, spelling, and grammar only. Nothing was added, cut, or reworded for tone.

**One change that is not punctuation, and is the important one:**

- The NOAA sentence carried a **leaked AI citation token** —
  `cite`+`turn655560search12` — pasted in from whatever tool drafted that line. It would
  have shipped as literal garbage in the middle of a paragraph. Claude verified the
  underlying claim against NOAA Fisheries, which states *"Patagonian and Antarctic
  toothfish, also referred to as Chilean sea bass, are harvested in and beyond waters
  subject to CCAMLR's measures"*, and replaced the token with a real link on the words
  *"NOAA will confirm"* →
  <https://www.fisheries.noaa.gov/permit/antarctic-marine-living-resource-program>.
  (`fishwatch.gov/profiles/patagonian-toothfish` is dead — it 301s to a generic
  sustainable-seafood topic page. Do not use it.)

Punctuation and typography:

- Straight quotes and apostrophes normalized to typographic throughout. The draft mixed
  them — `"Manager"` straight, `“just use Claude”` curly, in the same post.
- `--` → em dash, in the *cognitive infrastructure* aside.
- `"Manager".` → `“Manager.”` — period inside the quotes.
- `"Co-Founder",` → `“Co-Founder,”` — comma inside the quotes.
- `[That was an actual recruiter suggestion].` → period inside the brackets.
- `the forgotten 2022's` → `2022s` — no apostrophe in a plural year.
- Comma added after *"In an industry obsessed with abstraction"*.
- `I'm sorry, recruiter, even if I change…` → em dash after *recruiter*, which was a comma
  splice.
- `The boundaries aren't fuzzy, **the boundaries are gone**.` → em dash, same reason.
- `…what I am doing **now**:` → `.` The colon promised a title and delivered a sentence
  about fish.
- Double blank lines collapsed to single. (Harmless to the converter, but see the spacing
  rule in `blog_posts/README.md` — blank paragraphs are inserted at payload assembly and a
  hand-authored one arrives doubled.)

Grammar:

- `do not fit at all into one box` → `do not fit into one box at all` — misplaced adverb.
- `why well-founded robust guardrails amplify the AI's value, and not diminish it` →
  `why well-founded, robust guardrails amplify the AI's value rather than diminish it`.

Deliberately **not** changed, so a later session does not "fix" them:

- Both headings that end in a period, and the comma splice in
  *"Tools change, skill sets evolve, titles are just words."* — his voice, and the triad is
  the joke.
- *"Nice to meet me."*, *"Leaky or undirected AI use (cough, vibe coding, cough…)"*, and the
  other deliberate fragments in the problem list.

## Flagged for Ry, not acted on

- **The three back-ticked lines** in *We Are Optimizing Humans for Search Results*
  (`` `Head of Insights & Analytics` becomes `Data Engineering Leader` ``, and the two
  after it) **will render as plain body copy on Wix.** Ricos has no inline-code decoration
  and Wix strips `FONT_FAMILY` on save — a verified fidelity limit, not a converter bug.
  If the visual distinction matters, bold is the option that survives. Left as authored.
- **Title, slug, excerpt and tags are settled — Ry, 2026-08-26.** Title *A Fish Called
  Engineer*, slug `a-fish-called-engineer`, excerpt is the opening prose through *"Same
  fish, better title."* verbatim with the bold markers stripped (348 characters — long for
  a feed preview, and Wix may truncate it; his call).
- **Four of the six tags do not exist in the Wix blog yet** — `snarky`, `editorial`, `HR`,
  and `job hunting`, all approved by Ry in the same message. `AI engineering` and
  `engineering leadership` exist. Creating a tag is a real entity in the blog's taxonomy
  and **`POST /blog/v3/tags` returns `409 ALREADY_EXISTS` rather than the existing tag**,
  so read the tag list first and only create the four.
- **`LLM arrived in '22`** — reads like a typo for *LLMs*. Ry's own sentence, flagged rather
  than changed.
- **Blog Post 11, not 10.** `Blog Post 10: Analyzing the Cost of Claude for Organizations`
  already exists in the Content DB at `Idea`.
- **Notion `Platform`** is `Website`, not the skill's `WP Blog` — the live schema has no
  such option. Same finding as Blog Post 9; the skill is still stale on this point.

## Outstanding

Claude's, once Ry answers:

- Whether the post wants a CTA at all. Everything else from the batched Phase 2 question
  is answered; `featured` stays `false`.
- The Wix push, and **recording the returned draft ID in the table above.**

Ry's:

- **The cover.** `post.md` names `cover.jpg` and the converter hard-errors until it lands,
  which is the intended loud failure — `--list-images` will not run before then.
- Proofread and publish, the LinkedIn subpost, share / boost.
- Then Phase 3 bookkeeping: Content row → `Published` + URL + date, task to-dos, and the
  Web Property Map only if the published post ends up linking an `intake.` page. **As
  written it links none** — its one outbound link is the NOAA citation — so there is no new
  Wix → GitHub edge to record unless a CTA is added.

## Log

- 2026-08-26 — **Ry's revision pass.** He edited `post.md` in place — eleven prose changes
  of his own, including the Steely Dan genre analogy, the *"Change the résumé and re-apply"*
  line, and a rewritten close to *Real problems arrive as…* — and set the title, slug,
  excerpt and tags. Claude touched **only** the front matter plus the typographic
  normalization of the straight quotes and apostrophes his new sentences introduced
  (`"Change the résumé…"`, `"jazzy rock"`, `"engineer"`, `I'm`, `'22`), keeping the file
  consistent with the pass below. **No other prose was touched.** Re-validated: 167 nodes,
  six headings, list and blockquote intact. Still nothing pushed to Wix; still no cover.

- 2026-08-26 — **Phases 1 and 2 (local only).** Ry's two root-level drafts reorganized into
  this folder; empty `draft1.md` deleted, `draft2.md` preserved at
  `planning/draft2-source.md`. `post.md` assembled with front matter and the edit pass
  above. Converter validated on a cover-less copy: **165 nodes**, six headings, the
  nine-item bulleted list and the blockquote intact, `seoSlug` correct. Issue #256 filed.
  Notion trail created — Blog Post 11 row at `Drafting`, LinkedIn row at `Idea`, launch task
  at `In progress` with `Outline` and `Write` checked and a comment posted. **Nothing pushed
  to Wix, nothing published.**

<!--
Phase values, in order:
  1 — intake
  2 — awaiting copywriter draft
  2 — draft in hand, pushing
  3 — draft in Wix, awaiting Ry's proofread and publish
  4 — published, link placement outstanding
  done

Next session: the trigger is Ry's cover landing plus his answers to the batched question.
Read the Notion task first (his standing instruction). The push is the five-step procedure
in blog_posts/README.md — and the returned draft ID goes in the table above before anything
else happens.
-->
