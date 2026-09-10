# Workflow — How to Restrict What Your IC Can Touch

Phase: 3 — **draft in Wix, awaiting Ry's proofread and publish.** The Wix draft is
`UNPUBLISHED`.

| | |
|---|---|
| Folder          | `blog_posts/2026-09-10-restrict-what-your-ic-can-touch/` |
| GitHub issue    | wolfpackdata/wp-website#302 |
| Notion content  | https://app.notion.com/p/3d7c70e5c7b481f9981be563e41933fa  (Blog Post 13) |
| Notion LinkedIn | https://app.notion.com/p/3d7c70e5c7b4810d8fe3ef9b3b4ad894 |
| Notion task     | https://app.notion.com/p/3d7c70e5c7b481ce8e13e51ac32f0004 |
| Wix draft ID    | **`bb47b919-8bed-404d-8098-e06cff4ead34`** — pushed 2026-09-10 12:45 PM PT, `UNPUBLISHED` |
| Live URL        | (unset) |
| Slug            | `how-to-restrict-what-your-ic-can-touch` — `seoSlug` set; Wix reports the same path in the draft's `url` |
| Cover           | `cover.jpg` 1600×900, **generated** by `planning/hero/build_hero.py` (Pillow + numpy, deterministic — two consecutive runs produced the same sha256) |

## How this one differs from the standard Phase 1

Ry asked, in one session, for the post to be written **end to end** by Claude — post, hero
image, and the Wix draft — after a single batch of questions. So there is **no copywriter
and no copywriter brief**. The intake material is `planning/source-notes.md`: Ry's prompt,
his seven answers, and the research into his own guardrail practice that the post draws on.

- Skill §2.3 ("do not edit the prose") does not bind here — there is no copywriter draft to
  protect. It reverts to report-never-correct on the next post that has one.
- The hero is **generated, not supplied**. `planning/hero/build_hero.py` is the master —
  rebuild rather than retouch. No `hero-original.png` exists because there is no original
  outside the script.
- Ry's seven answers, recorded because they are rulings for this post: (1) IC = independent
  contractor, and the AI counts as one; (2) first person; (3) sandbox repos and dev databases
  stay in as **general advice** even though they are not Wolfpack's own practice; (4) the two
  PAT rotations may be mentioned, anonymously; (5) under 1,500 words; (6) generated hero;
  (7) links and tags as proposed. Plus: **no British spellings.**

## Facts about the copy

- **1,495 words** in the body (front matter excluded), six sections plus a one-paragraph
  checklist. Wix reports 6 minutes to read.
- **American spelling** checked by grep against a list of common British variants; no hits.
- Every claim about Wolfpack's own practice is traced in `source-notes.md`. The two items
  Ry chose to keep as general advice are framed as "what to ask for," and the only
  first-person claim near them ("in my own tools … a dry run") is true of `bql apply`.
- **Two outbound links + one CTA:** the "New Clients" post
  (`/post/working-with-wolfpack`) and the 30-minute intro call. **No `intake.` link**, so
  publishing creates no new Wix → GitHub edge and the Web Property Map needs no entry.
- **The GitHub SOP overview post is deliberately not linked yet.** Ry approved linking it
  *once it is live*; it is still a draft (`154a9527-…`). When it publishes, that link is a
  `post.md` edit plus a body PATCH to the draft ID above.

## A re-push is a PATCH, never another POST

**`PATCH /blog/v3/draft-posts/bb47b919-8bed-404d-8098-e06cff4ead34`.** A `POST` creates a
second post. The PATCH is partial, so a retitle, excerpt change, or cover swap is a
two-field patch; send a rebuilt body only when the body changed, and hash the live body
against a fresh build first in case Ry has edited the draft in the dashboard.

| Resolved at push time | |
|---|---|
| Cover media | `e00ee6_c751d976d7e54bc09d387a1795c4fbdc~mv2.jpg` — uploaded from the feature branch's raw GitHub URL after a sha256 match against the local file; Wix reports 1600 × 900 |
| `governance` | `4ebddc6b-bc34-45c3-8a34-93b199f139c6` — existing |
| `AI safety` | `24a87803-28a8-4e7e-b6b0-98f6ab47ad25` — existing |
| `engineering leadership` | `cc7c1304-6a3f-4aa3-b6f6-4518ee1ef4ed` — existing |
| `client engagement` | `e5a1a81d-8c55-451e-bfe2-193f7a6f819e` — existing |
| Author | `e00ee638-af7f-4aac-aa2b-c99d795ecf78`, the converter default |
| `featured` | false |
| Tags created | **None** — all four existed |

**The body was read back and verified after the push** (`GET …?fieldsets=RICH_CONTENT`)
and fingerprinted against the built payload: 65 top-level nodes (58 paragraphs including
the 32 spacers, 7 headings), 8,281 characters of text, djb2 `1545603733`.

## Outstanding

Claude's:

- Nothing on the post itself. `Add CTAs` is checked: the intro call is the CTA and Ry
  approved it as the only one.
- **Follow-up owed when the GitHub SOP overview post goes live:** add its link (see above).

Ry's:

- **Proofread and publish** in the Wix dashboard.
- **LinkedIn subpost** — no draft exists; the LinkedIn Content row is at `Idea`.
- **Share / boost.**

Then Phase 3 bookkeeping here: Content row → `Published` + URL + date, task to-dos. No Web
Property Map entry is owed (no `intake.` link).

## Log

- 2026-09-10 — **Phases 1 and 2 in one session.** Ry's prompt and seven answers recorded in
  `source-notes.md`; research into `wp-github-sop`, `wp-codex-init`, `wp-codex-sop`,
  `wp-bql`, and `wp-notion-team` done by a read-only subagent. Issue #302 filed (acceptance
  criteria derived). Notion trail: Blog Post 13 row at `Drafting`, LinkedIn row at `Idea`
  with `Promotes` set, launch task created **first** at `Not started` and flipped to
  `AI Processing` before the writing began. Post written by Claude (1,495 words, American
  spelling), hero generated by the committed script (deterministic, verified), converter
  validated, all 47 converter tests pass. Cover uploaded after a sha256 match; no tags
  created; `POST /blog/v3/draft-posts` returned `bb47b919-8bed-404d-8098-e06cff4ead34`,
  `UNPUBLISHED`, 6 minutes to read, cover 1600 × 900. Body verified by fingerprint.
  **Nothing published.**

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
No Web Property Map entry is owed. A re-push is a PATCH to the draft ID above, never
another POST. When the GitHub SOP overview post is live, link it from section 5 or the
checklist via post.md + PATCH.
-->
