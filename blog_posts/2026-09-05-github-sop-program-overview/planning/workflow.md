# Workflow — The Wolfpack GitHub SOP: A Program Overview

Phase: 2 — **two drafts in hand, nothing pushed to Wix** (Ry's instruction). Awaiting his
pick between them, plus a cover and the batched Phase 2 answers.

| | |
|---|---|
| Folder          | `blog_posts/2026-09-05-github-sop-program-overview/` |
| GitHub issue    | wolfpackdata/wp-website#281 |
| Notion content  | https://app.notion.com/p/3d2c70e5c7b481c9a193df16e616c892  (Blog Post 12) |
| Notion LinkedIn | https://app.notion.com/p/3d2c70e5c7b481638070ff98f7930380 |
| Notion task     | https://app.notion.com/p/3d2c70e5c7b48106863ee6c135c93be3 |
| Wix draft ID    | **(unset — nothing has been pushed)** |
| Live URL        | (unset) |
| Slug            | `github-sop-program-overview` (draft 1) / `nobody-reads-the-sign` (draft 2) — **provisional, Ry settles** |
| Cover           | **missing.** Both drafts name `cover.jpg`; none supplied or described |

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

**Draft 1 is in `post.md` because it is what Ry asked for first, not because it has won.**
Promoting draft 2 is a file copy; its front matter travels with it, and nothing in this
ledger assumes which one ships. Its title and slug deliberately differ from draft 1's.

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

## Outstanding

Claude's, once Ry answers:

- **Which draft ships**, and whether the other stays in `planning/` as a record or is deleted.
- The batched Phase 2 question: tags, `featured`, slug, excerpt, `date`, cover, and whether
  the post wants a CTA at all.
- The Wix push, and **recording the returned draft ID in the table above.**
- **`Add CTAs` is unchecked on the task** and is the one to-do of Claude's still open —
  neither draft carries a CTA, and whether the post wants one is Ry's call.
- Renaming the Notion rows and the task if Ry picks draft 2, whose title differs.

Ry's:

- **The cover.** Both drafts name `cover.jpg` and the converter hard-errors until it lands,
  which is the intended loud failure — `--list-images` will not run before then.
- Proofread and publish, the LinkedIn subpost, share / boost.
- Then Phase 3 bookkeeping. The Web Property Map needs nothing unless a CTA adds an
  `intake.` link.

## Log

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

Next session: the trigger is Ry picking a draft, plus a cover and his answers to the
batched question. The Notion trail is still owed and comes first. The push is the
five-step procedure in blog_posts/README.md — and the returned draft ID goes in the
table above before anything else happens.
-->
