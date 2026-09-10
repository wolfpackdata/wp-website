# Workflow — The Wolfpack GitHub SOP: A Program Overview

Phase: 3 — **draft in Wix, awaiting Ry's proofread and publish.** Draft 1 shipped; the
Wix draft is `UNPUBLISHED`.

| | |
|---|---|
| Folder          | `blog_posts/2026-09-05-github-sop-program-overview/` |
| GitHub issue    | wolfpackdata/wp-website#281 |
| Notion content  | https://app.notion.com/p/3d2c70e5c7b481c9a193df16e616c892  (Blog Post 12) |
| Notion LinkedIn | https://app.notion.com/p/3d2c70e5c7b481638070ff98f7930380 |
| Notion task     | https://app.notion.com/p/3d2c70e5c7b48106863ee6c135c93be3 |
| Wix draft ID    | **`154a9527-96d5-483c-b4c2-a5a5511e342f`** — pushed 2026-09-10 9:41 AM PT, `UNPUBLISHED` |
| Live URL        | (unset) |
| Slug            | `github-sop-program-overview` — draft 1 shipped 2026-09-10; `seoSlug` set. The dashboard preview path reads `/post/the-wolfpack-github-sop-a-program-overview` (title-derived, README fidelity limit 3) |
| Cover           | `cover.jpg` 1600×900, derived from Ry's `planning/hero-original.png` (1672×941, generated 2026-09-10, prompt in `planning/hero-prompt.md`) |

## How this one differs from the standard Phase 1

Ry supplied a **finished report** written in another session, dropped at
`blog_posts/github-sop-program-overview.md`, and asked for two drafts off it — one using
the whole report verbatim, one a five-minute read in the tone of the `applied-ai-engineer`
post. So there is **no copywriter and no copywriter brief**; Claude wrote both drafts at his
direction. Their absence from `planning/` is the shape of the request, not an omission.

- **The report is preserved byte-for-byte** at `planning/source-report.md`. The loose root
  copy was moved, not copied — `blog_posts/` holds one folder per post and nothing else.
- **No `source-notes.md`.** The report *is* the source, and it is already here whole.
- **No Wix work of any kind**, per Ry. Phase 2 stops after the drafts.
- Skill §2.3 ("do not edit the prose") does not bind here — there is no copywriter draft to
  protect. It reverts to report-never-correct on the next post that has one.

## The two drafts

| | Draft 1 — `post.md` | Draft 2 — `planning/draft2-five-minute-read.md` |
|---|---|---|
| Working title | *The Wolfpack GitHub SOP: A Program Overview* | *Nobody Reads the Sign* |
| Length | 2,545 words, ~11 min | 1,044 words, ~4.5 min |
| Converter | 155 nodes, 16 headings, 2 bulleted + 1 ordered list | validated, 35 KB payload |
| Voice | The report's — third person, declarative, reference-shaped | `applied-ai-engineer`'s — first person, short paragraphs, one running analogy |
| Relation to source | Whole report, wording preserved | The argument only; six inventories cut |

**Draft 1 shipped on 2026-09-10** — Ry supplied the cover and called `post.md` ready. Draft 2
stays in `planning/` as a record of the alternative; it was never pushed anywhere.

### What "verbatim" survived, and the three things that could not

1. **The six tables are gone; their wording is not.** The converter does not support tables
   (`blog_posts/README.md`), so every row became a labelled paragraph or a one-line bullet.
   This is the whole of the "reorganize" step.
2. **Eleven links were removed.** The report links `wolfpackdata/wp-github-sop` as its source
   of truth and each of the ten rules to a `docs/sop/*.md` path. **That repository is
   PRIVATE** — verified 2026-09-05 via `gh repo view --json visibility`. Every one of those
   links would 404 for a reader. The rules keep their numbers and their text.
3. **The "Part I" / "Part II" spine was flattened.** A document structure, not a blog one.

Both drafts carry **no outbound links at all** as a result. That is a fact worth knowing
before Phase 3: there is no `intake.` link, so publishing creates **no new Wix → GitHub edge**
and the Web Property Map needs no entry — unless a CTA is added.

## Flagged for Ry, not acted on

- **The private repo is the one real decision here.** The post describes the internals of a
  private repository in some detail — 36 repositories, the hook suite, the failure log. The
  report was written for "technical partners and clients", so publishing it is clearly the
  intent; the links were the only part that could not survive contact with a public reader.
  **If `wp-github-sop` is ever made public, the ten rules should get their links back.**
- **Title, slug, excerpt and tags are provisional.** Draft 1's excerpt is the report's opening
  sentence (280 characters — long for a feed preview; the `applied-ai-engineer` post shipped
  348 by Ry's call, so this is within precedent).
- **Three or four of the four tags may not exist in the Wix blog.** `AI engineering` exists;
  `engineering leadership` exists; `governance` and `process` have not been checked. Read the
  tag list before creating any — `POST /blog/v3/tags` returns `409 ALREADY_EXISTS` rather than
  the existing tag.
- **Backticked names render as plain body copy on Wix.** `main`, `develop`,
  `fixed-on-develop`, `github-gitflow` and the rest lose their monospace: Ricos has no inline
  code decoration and Wix strips `FONT_FAMILY` on save. A verified fidelity limit, not a
  converter bug. Draft 1 uses roughly thirty of them. They read fine in context; **bold is the
  option that survives** if the distinction matters to him.
- **"The Applied AI Engineer"** in draft 1's *How the work was divided* is the report's own
  third-person phrasing for Ry. In a first-person blog post under his byline it reads oddly.
  Left as written — changing it is a voice call, not a mechanical one.
- **Draft 2 is 4.5 minutes at 230 wpm**, 5.2 at 200. Called a five-minute read either way.

## A re-push is a PATCH, never another POST

**`PATCH /blog/v3/draft-posts/154a9527-96d5-483c-b4c2-a5a5511e342f`.** A `POST` creates a
second post. The PATCH is partial, so a retitle, excerpt change or cover swap is a two-field
patch; send a rebuilt body only when the body changed, and hash the live body against a
fresh build first in case Ry has edited the draft in the dashboard.

| Resolved at push time | |
|---|---|
| Cover media | `e00ee6_0b0acc5f4f8c4a4b8e5f1c6bdab1d5f1~mv2.jpg` — uploaded from the feature branch's raw GitHub URL after a sha256 check against the local file; Wix reports 1600 × 900 |
| `AI engineering` | `1e614466-776a-4b7e-9fa8-5da9e3eee0f3` — existing |
| `engineering leadership` | `cc7c1304-6a3f-4aa3-b6f6-4518ee1ef4ed` — existing |
| `governance` | `4ebddc6b-bc34-45c3-8a34-93b199f139c6` — **created by this push** |
| `process` | `e7e67495-c9ff-4c46-9b4e-2bf7f49c2f7f` — **created by this push** |
| Author | `e00ee638-af7f-4aac-aa2b-c99d795ecf78`, the converter default |
| `featured` | false |
| Destinations | **None.** The post carries no links at all (see above) — no CTA, no `intake.` link, so the Web Property Map needs no entry |

**The body was read back and verified after the push**, not assumed: `GET
…?fieldsets=RICH_CONTENT` was fingerprinted (top-level node count, per-type counts, total
text length, and a djb2 hash of every text run) and matched the built payload exactly —
155 nodes, 16 headings, 2 bulleted + 1 ordered list.

## Outstanding

Claude's:

- **`Add CTAs` is still unchecked on the task.** The post shipped to Wix with no CTA and no
  link of any kind. If that is the decision, Ry checks it (or says so and Claude does); if he
  wants one, it is a body PATCH — the draft ID above — plus a `post.md` edit, and the Web
  Property Map then needs the edge once published.

Ry's:

- **Proofread and publish** in the Wix dashboard.
- **LinkedIn subpost** — no `raw-linkedin-post.md` exists; the LinkedIn Content row is at
  `Idea`.
- **Share / boost.**

Then Phase 3 bookkeeping here: Content row → `Published` + URL + date, task to-dos. The Web
Property Map needs nothing unless a CTA adds an `intake.` link before publication.

## Log

- 2026-09-10 — **Phase 2 complete: pushed to Wix as an unpublished draft.** Ry supplied the
  hero (generated 2026-09-10; original and prompt committed under `planning/`), called
  draft 1 ready, and the placeholder `cover_alt` was replaced with a description of the
  image. Cover uploaded from the branch's raw URL after a sha256 match; two tags created
  (`governance`, `process`); `POST /blog/v3/draft-posts` returned
  `154a9527-96d5-483c-b4c2-a5a5511e342f`, `UNPUBLISHED`, 155 nodes, 10 minutes to read,
  cover 1600 × 900. Body verified by fingerprint against the built payload. Front matter
  shipped as it stood on 2026-09-05 (title, slug, excerpt, four tags, `featured: false`,
  `date: 2026-09-05`) — Ry's "ready" taken as the answer to the batched question; each is a
  two-field PATCH if he wants it changed. **Nothing published.**

- 2026-09-05 — **Phase 1 and both drafts (local only).** Ry's root-level report moved to
  `planning/source-report.md`; folder created; `post.md` assembled as draft 1 with the tables
  reorganized and the eleven dead links removed; `planning/draft2-five-minute-read.md`
  written to the `applied-ai-engineer` tone. Converter validated on cover-less copies of
  both — draft 1 at **155 nodes**, 16 headings, `seoSlug` correct; draft 2 clean. All 47
  converter tests pass. Issue #281 filed with derived acceptance criteria. Notion trail
  created — Blog Post 12 row at `Drafting`, LinkedIn row at `Idea`, launch task at
  **`In progress`** with `Outline`, `Write` and `Add content` checked and a comment posted.
  `Add CTAs` deliberately left unchecked. The linked project *Wolf Pack Blog July
  development* was already `In progress`, so no cascade was owed. **Nothing pushed to Wix,
  nothing published.**

<!--
Phase values, in order:
  1 — intake
  2 — awaiting copywriter draft
  2 — draft in hand, pushing
  3 — draft in Wix, awaiting Ry's proofread and publish
  4 — published, link placement outstanding
  done

Next session: the trigger is Ry handing back the live URL (Phase 3). Content row →
Published + URL + date; task → check Proofread and Publish; ledger → live URL, Phase 4.
No Web Property Map entry is owed unless a CTA was added first. A re-push is a PATCH to
the draft ID above, never another POST.
-->
