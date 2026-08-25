# Workflow — What Every New Client Gets When Working with Wolfpack

Phase: 3 — draft in Wix, awaiting Ry's proofread and publish

| | |
|---|---|
| Folder          | `blog_posts/2026-08-25-new-client-expectations/` |
| GitHub issue    | wolfpackdata/wp-website#253 |
| Notion content  | https://app.notion.com/p/3c7c70e5c7b48172a13ac0481b2f6d0b (Blog Post 9) |
| Notion LinkedIn | https://app.notion.com/p/3c7c70e5c7b4818ca44cd1817d30b7b6 |
| Notion task     | https://app.notion.com/p/3c7c70e5c7b4817c89c3ea88925897e9 |
| Wix draft ID    | **`7034284f-fd91-46d3-8ee5-aea8b523a25c`** — pushed 2026-08-25 4:03 PM PT, `UNPUBLISHED` |
| Live URL        | (unset) |
| Slug            | `working-with-wolfpack` (Ry, 2026-08-25; preferred over the proposed `what-every-new-client-gets` as evergreen) |
| Cover           | `cover.jpg`, 1200 x 675, 116 KB — supplied by Ry 2026-08-25; master `planning/Wolfpack analytical data layer landscape hero.png` (1672 x 941) |

## How this one differs from the standard Phase 1

Ry's instructions arrived **inside the transcript** (`source-transcript.srt`, its last two
minutes) and in chat, and they reshape the deliverables:

- Instead of a brief alone, Phase 1 produced a **verbatim-heavy first draft**
  (`first-draft.md`) — Ry's transcript sentences reordered into an outline, fillers
  removed, grammar deliberately not corrected — plus a **client-lens critique** of it
  (`draft-feedback.md`) that deliberately does **not** rewrite it.
- The draft hands off to a **human copywriter**, whose finished `raw-blog-post.md` +
  `raw-linkedin-post.md` land in the post folder and trigger Phase 2 as usual.
  `copywriter-brief.md` carries the outline, word budgets, constraints, and traps.
- **No Wix work of any kind happened in Phase 1**, per Ry.

## Decisions and flags

- **HBO / Time Warner** cleared for publication by Ry, 2026-08-25 ("HBCU" in the
  transcript is a mis-transcription of HBO). All transcription corrections tabled in
  `source-notes.md`.
- **BigQuery cost fact-checked 2026-08-25** at Ry's in-transcript request: no $100 storage
  floor exists; $50–$100/month is a conservative ceiling. Draft keeps the hedge; the
  "lowest level of storage" rationale was dropped. Sources in `source-notes.md`.
- **Notion Platform option:** the blog-workflow skill says to use `WP Blog`, but the live
  Content DB schema has no such option (options: Website, LinkedIn Personal, …). Live
  space wins — the row uses **`Website`**, matching Blog Posts 1–8. Flagged for Ry: the
  skill is stale on this point.
- Standing constraints for the post are in `copywriter-brief.md` §1 (no invented outcomes,
  no links to noindex pages, AI Command never implies PM replacement, one CTA).

## A re-push is a PATCH, never another POST

**`PATCH /blog/v3/draft-posts/7034284f-fd91-46d3-8ee5-aea8b523a25c`.** A `POST` creates a
second post. The PATCH is partial, so a retitle, excerpt change or cover swap is a two-field
patch; send a rebuilt body only when the body changed, and hash the live body against a
fresh build first in case Ry has edited the draft in the dashboard.

| Resolved at push time | |
|---|---|
| Cover media | `e00ee6_8326e52a04934f79b1f94f4734606b97~mv2.jpg` — uploaded from the branch's raw GitHub URL after a byte-for-byte check; Wix reports 1200 x 675 |
| `AI engineering` | `1e614466-776a-4b7e-9fa8-5da9e3eee0f3` — existing |
| `project management` | `1e4b5fb4-5cd1-48f7-a802-e8f092631aaa` — existing |
| `client engagement` | `e5a1a81d-8c55-451e-bfe2-193f7a6f819e` — **created by this push** (Ry approved) |
| `AI safety` | `24a87803-28a8-4e7e-b6b0-98f6ab47ad25` — **created by this push** (Ry approved) |
| `featured` | `false` |
| Excerpt | Claude's proposal, approved by Ry 2026-08-25; derived from the post's own claims, no new facts |
| Author | `e00ee638-af7f-4aac-aa2b-c99d795ecf78`, the converter default |
| Destinations | Three, all Ry's call: the intro call (`calendar.app.google/zHNd1NA9wzb4VRLw5`), the AI Command case study (`/wolfpack-ai-command/`, placed after that section's last paragraph), and the portfolio (`/portfolio/`, last line) |

**The body is Ry's final copy, verbatim** — `raw-blog-post.md` is his file, and `post.md`'s
body differs from it only by the two CTA lines he asked for. Claude's `first-draft.md`
and `draft-feedback.md` are Phase 1 artifacts he drew on; nothing from them was applied
by Claude. A verbatim check (draft minus H1 vs. post.md body minus the two CTA lines)
passed before the push, and the four em dashes survived the payload.

## Outstanding — all Ry's

- **Proofread and publish** in the Wix dashboard. The preview URL shows the title-derived
  path; the `seoSlug` `working-with-wolfpack` becomes the real path on publish (README
  fidelity limit 3).
- **LinkedIn subpost** — no `raw-linkedin-post.md` exists yet; the LinkedIn Content row is
  at `Idea`.
- **Share / boost.**
- Then Phase 3 bookkeeping here: Content row → `Published` + URL + date, task to-dos,
  Web Property Map edge (this post links two `intake.` pages, so it is a new Wix → GitHub
  link path).

## Log

- 2026-08-25 — Phase 1 done (#253). Transcript moved into `planning/`, first draft +
  feedback + brief + source notes written, BigQuery pricing verified, issue filed, Notion
  trail created (Blog Post 9 row, LinkedIn row, launch task — task at `In progress`,
  `Outline` checked). Cover still missing. **No Wix work**, per Ry — next trigger is the
  copywriter's `raw-blog-post.md` landing in the folder.

- 2026-08-25 — **Phase 2, pushed to Wix as an unpublished draft.** Ry's final draft landed as
  `planning/What Every New Client Gets When Working With Wolfpack.md` (Claude fixed only the
  CTA link, Wix contact page → intro calendar, on his instruction; zero copy corrections
  were needed), renamed to `raw-blog-post.md`. Batched question answered: cover supplied,
  four tags (two new), slug `working-with-wolfpack`, proposed excerpt approved. Two CTAs
  added on Ry's instruction. `POST /blog/v3/draft-posts` returned
  `7034284f-fd91-46d3-8ee5-aea8b523a25c`, `UNPUBLISHED`, 179 nodes, 7 minutes to read,
  cover 1200 x 675, six lists intact at 4/7/5/5/2/8 items, three links. **Nothing
  published.**

<!--
Phase values, in order:
  1 — intake
  2 — awaiting copywriter draft
  2 — draft in hand, pushing
  3 — draft in Wix, awaiting Ry's proofread and publish
  4 — published, link placement outstanding
  done

Phase 2 note for whoever gets there: read the Notion task first (Ry's standing
instruction), then the batched question set in the skill §2.4 — this post additionally
needs the cover resolved (nothing exists) and the slug confirmed. The draft-feedback
items Ry accepts may come back as copywriter revisions; do not apply them yourself.
-->
