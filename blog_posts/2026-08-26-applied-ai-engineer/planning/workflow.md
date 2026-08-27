# Workflow — A Fish Called Engineer

Phase: 3 — **parked.** Draft is finished and sitting in Wix; Ry is holding it until the
timing is right to post. Nothing is blocked and nothing is late — do not chase it.

| | |
|---|---|
| Folder          | `blog_posts/2026-08-26-applied-ai-engineer/` |
| GitHub issue    | wolfpackdata/wp-website#256 |
| Notion content  | https://app.notion.com/p/3c8c70e5c7b481528c74fe8fdb577007 (Blog Post 11) |
| Notion LinkedIn | https://app.notion.com/p/3c8c70e5c7b481078997c3c1abce7807 |
| Notion task     | https://app.notion.com/p/3c8c70e5c7b481f3b294f2a1dc54f012 |
| Wix draft ID    | **`c896b105-e86a-4526-83c2-cdaf4427ce3a`** — pushed 2026-08-26 5:42 PM PT, `UNPUBLISHED` |
| Live URL        | (unset) |
| Slug            | `a-fish-called-engineer` — **Ry, 2026-08-26** |
| Cover           | `cover.jpg`, 1200 x 675, 184 KB — supplied by Ry 2026-08-26; master `planning/fish called engineer image 2.png` (1672 x 941) |

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
- **`LLM arrived in '22`** — Ry made this correction in the ledger rather than in `post.md`,
  so Claude applied it to the post on 2026-08-26. It now reads *LLMs arrived*.
- **Blog Post 11, not 10.** `Blog Post 10: Analyzing the Cost of Claude for Organizations`
  already exists in the Content DB at `Idea`.
- **Notion `Platform`** is `Website`, not the skill's `WP Blog` — the live schema has no
  such option. Same finding as Blog Post 9; the skill is still stale on this point.

## A re-push is a PATCH, never another POST

**`PATCH /blog/v3/draft-posts/c896b105-e86a-4526-83c2-cdaf4427ce3a`.** A `POST` creates a
second post. The PATCH is partial, so a retitle, excerpt change or cover swap is a two-field
patch; send a rebuilt body only when the body changed, and hash the live body against a
fresh build first in case Ry has edited the draft in the dashboard.

| Resolved at push time | |
|---|---|
| Cover media | `e00ee6_0b19933917a9420992f073615b508e06~mv2.jpg` — uploaded from the develop raw GitHub URL after a sha256 check against the local file; Wix reports 1200 x 675 |
| `AI engineering` | `1e614466-776a-4b7e-9fa8-5da9e3eee0f3` — existing |
| `engineering leadership` | `cc7c1304-6a3f-4aa3-b6f6-4518ee1ef4ed` — existing |
| `snarky` | `5660cc31-982b-46e5-8aad-e6fe424f9bb7` — **created by this push** |
| `editorial` | `b03581ab-7d16-46bb-b492-11de1546c7c0` — **created by this push** |
| `HR` | `1f3f8482-4dad-4983-ac8e-88a1fc9fc0dd` — **created by this push** |
| `positioning` | `b0bfa4ca-032e-4c7d-914f-2c0fb6127216` — created by the reframe patch |
| ~~`job hunting`~~ | `3e792d68-9a62-4e78-aace-68da5446e285` — created by the first push, then **orphaned by the reframe.** Still exists in the blog's taxonomy at `postCount: 0`. Left in place deliberately; deleting a tag is a taxonomy action for Ry, not a tidy-up |
| Author | `e00ee638-af7f-4aac-aa2b-c99d795ecf78`, the converter default |
| Destinations | Two, both Ry's call: the AI Command case study (`/wolfpack-ai-command/`) and the portfolio (`/portfolio/`). **No intro-call CTA** — this is the only post here without one, and it is deliberate |

**The body was read back and verified after the push**, not assumed: `GET
…?fieldsets=RICH_CONTENT` was compared paragraph by paragraph against the built payload —
171 nodes, six headings, the nine-item list, the blockquote, both links, the NOAA link, the
italic *toothfish*, every em dash, curly quote and `résumé`. Nothing was dropped or mangled.

## Outstanding

All Ry's:

- **Proofread and publish** in the Wix dashboard. The draft's preview path already reads
  `/post/a-fish-called-engineer`, which happens to match the `seoSlug` here only because the
  title derives to the same string — README fidelity limit 3 still applies in general.
- **LinkedIn subpost** — no `raw-linkedin-post.md` exists; the LinkedIn Content row is at
  `Idea`.
- **Share / boost.**

Then Phase 3 bookkeeping here: Content row → `Published` + URL + date, task to-dos, and
**the Web Property Map — this one now needs it.** The post carries two `intake.` links
(`/wolfpack-ai-command/` and `/portfolio/`), which is a new Wix → GitHub link path and an
explicit staleness trigger. Record the edge after publication, verified against the live
page rather than against `post.md`.

## Log

- 2026-08-26 — **Parked at Ry's call.** The draft is complete and correct in Wix; he is
  holding publication for timing. **A future session should not read the unset Live URL as
  a stalled workflow** — the post is done, the trigger is Ry deciding to ship it. When he
  does, Phase 3 resumes from the Outstanding list above, and the Web Property Map edge is
  the item most easily forgotten.

- 2026-08-26 — **Reframe: the speaker is a consultant, not an applicant** (#271). Ry will
  not publish a post announcing that he is personally job hunting; he runs a consulting
  practice and the same observations hold for a business positioning what it sells. **The
  industry critique is untouched** — title literalism, ATS matching, the toothfish conceit,
  every joke. Four edits, and that is the whole list:

  | Line | Change |
  |---|---|
  | 20 | `navigating the technology job market` → `watching how the technology market files what I sell`. *Files* now hands straight off to *"Apparently, I am Chilean sea bass."* |
  | 80 | prefixed `The stock question follows:` — the dialogue survives verbatim but belongs to the market, not to an interviewer in a room |
  | 164 | `recruiter` → `recruiters`. Addressing the profession is commentary; addressing *your* recruiter is a pipeline |
  | 8 | tag `job hunting` → `positioning` |

  **The third person was deliberately left alone** — *"every person who applies"*, *"a person
  can have spent years…"*, *"excluding candidates"*. The critique being about the hiring
  market is the point; only the first person moved. Ry's own edits at L74, L140 and L190
  reached git for the first time in the same commit, preserved exactly.

  **Draft patched, not re-posted:** `PATCH /blog/v3/draft-posts/c896b105-…` with
  `richContent` + `tagIds` only. Title, excerpt, cover, `seoSlug` and `memberId` all
  survived the partial update, as the README says they do. Still `UNPUBLISHED`. The draft
  had been carrying both the old framing *and* three of Ry's edits that were made after the
  first push, so this patch closes both gaps at once.

- 2026-08-26 — **Phase 2 complete: pushed to Wix as an unpublished draft.** Cover, both
  CTAs and the `LLMs` fix landed first (#261). `POST /blog/v3/draft-posts` returned
  `c896b105-e86a-4526-83c2-cdaf4427ce3a`, `UNPUBLISHED`, 171 nodes, 5 minutes to read,
  cover 1200 x 675, six tags of which four were created by this push. Body verified by
  reading the draft back. **Nothing published.**

- 2026-08-26 — **Cover and CTAs.** Ry supplied the hero (a police lineup of five faceless
  men in five different work outfits — the same person, five job titles) and asked for two
  subtle CTAs. `cover.jpg` derived at 1200 x 675 from the 1672 x 941 master, which is
  exactly 16:9 so nothing was cropped; **rebuild from the master rather than re-encoding
  `cover.jpg`.** Real `cover_alt` written from the image. CTA 1 lands after the
  *cognitive infrastructure* sentence → `/wolfpack-ai-command/`; CTA 2 closes the post →
  `/portfolio/`. Ry's `LLMs` correction was applied here — he had made it in this ledger
  rather than in `post.md`.

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
