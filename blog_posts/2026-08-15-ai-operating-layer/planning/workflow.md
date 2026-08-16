# Workflow — An AI Operating Layer for Streamlining Project Delivery

Phase: 3 — draft in Wix, awaiting Ry's proofread and publish

| | |
|---|---|
| Folder          | `blog_posts/2026-08-15-ai-operating-layer/` |
| GitHub issue    | wolfpackdata/wp-website#196 |
| Notion content  | https://app.notion.com/p/3bec70e5c7b481dbbe75d5d1bac184f5 (Blog Post 7) |
| Notion LinkedIn | https://app.notion.com/p/3bec70e5c7b48156ab99f601cbb3aae1 |
| Notion task     | https://app.notion.com/p/3bec70e5c7b481969071d68ca7b436c8 (8. Launch the … blog post) |
| Wix draft ID    | **`4c8c192e-cd4a-428b-8e0f-995c4a247909`** — pushed 2026-08-15, `UNPUBLISHED` |
| Live URL        | (unset) |
| Slug            | `ai-operating-layer-for-project-delivery` |
| Cover           | `cover.jpg`, 1200 x 675, 49 KB — the case study's shield hero, downscaled |

## Why this one skipped a phase boundary

Ry asked for the post **end to end in one session**, using verbatim copy from the case study
rather than a fresh draft, and explicitly said not to publish to Wix yet. So Phase 1 and the
authoring half of Phase 2 both happened on 2026-08-15, and there is **no `raw-blog-post.md`** —
the body went straight into `post.md`. `planning/copywriter-brief.md` was written alongside it
and is a record of the constraints plus the spec for a redraft, not a handoff anybody acted on.

The push followed on 2026-08-15, on Ry's separate go-ahead, so Phases 1 and 2 both closed the
same day. **Nothing was published** — the draft sits in the dashboard at `UNPUBLISHED`, and
`--publish` was never used.

## A re-push is a PATCH, never another POST

**`PATCH /blog/v3/draft-posts/4c8c192e-cd4a-428b-8e0f-995c4a247909`.** A `POST` creates a
second post — #147 is the worked example of what happens when the ID lives nowhere. The
`PATCH` is a partial update, so a retitle or a cover swap is a two-field patch. Send a rebuilt
body only when the body actually changed, and hash the live body against a fresh build first,
in case Ry has edited the draft in the dashboard.

| Resolved at push time | |
|---|---|
| Cover media | `e00ee6_a2fce010a5b344f5b1c10981d43c913b~mv2.jpg` — Wix reports 1200 x 675, which is what was sent |
| `AI engineering` | `1e614466-776a-4b7e-9fa8-5da9e3eee0f3` — existing, created by the five-projects post |
| `project management` | `1e4b5fb4-5cd1-48f7-a802-e8f092631aaa` — **created by this push** |
| `featured` | `false` |
| Excerpt | **Ry's copy** (#201), and the case study's `og:description` is the same sentence. Nothing guards that pair — change both or neither |
| Author | `e00ee638-af7f-4aac-aa2b-c99d795ecf78`, the converter default, matching the other posts |

## Three things this push learned

1. **`blog_posts/README.md` was wrong about tags.** It said creating one that already exists
   returns the existing one. It does not — `POST /blog/v3/tags` returns **`409 ALREADY_EXISTS`**,
   and existing tags have to be resolved with `GET /blog/v3/tags`. Corrected in the README in
   the same PR.
2. **The converter silently mangles hard-wrapped list items** (#208). This post had three
   ordered items and seven bullets wrapped across source lines, and every one converted to a
   single-item list plus an orphan paragraph — three lists all numbered `1.`. Caught by reading
   the payload before sending, not by any check. Every list item here is now on one line and
   must stay that way.
3. **The cover uploaded from its raw GitHub URL**, not from base64, after confirming
   byte-for-byte that the URL serves exactly the committed file. `wp-website` is public, so
   `raw.githubusercontent.com/wolfpackdata/wp-website/develop/<path>` is a legitimate route for
   any future asset here, and it sidesteps the Wix media importer a previous push found blocked
   by policy.

## Outstanding — all Ry's

- **Proofread and publish** from the Wix dashboard. Nothing is public until he does;
  `--publish` was never used. **Confirm the slug there** — the draft preview path is
  title-derived (`/post/an-ai-operating-layer-for-streamlining-project-delivery`), which is the
  README's third fidelity limit rather than a mistake. `seoSlug` is stored correctly.
- **Post the LinkedIn subpost** (`raw-linkedin-post.md`), then boost.
- Then Phase 3 bookkeeping: the Content DB row to `Published` with its URL and date, the
  remaining task to-dos, and the **Web Property Map**, which a published post linking
  `intake.wolfstrategyllc.com` makes stale.

Two calls were made on his behalf rather than blocking the push, both cheap to reverse:
`featured` is `false`, and the new `project management` tag was created. Featuring or retagging
is a two-field `PATCH`; the tag is deletable.

## Rulings applied

| | |
|---|---|
| Title | The case study's `h1`, **verbatim** — the #119 rule. No colon, so unquoted |
| Slug | Deliberately shorter than the title, and it does not follow it |
| Body | Mostly verbatim case study copy, per Ry. Passage map in `planning/source-notes.md` |
| Numbers | **None.** Every count on the case study is dated on that page; an undated copy here would drift. The excerpt's *"blistering speed"* is qualitative and voiced as what the system enables — it must never acquire a number |
| Cover | The case study's hero, downscaled — the route the financial model post's cover took |
| Destinations | Two, both already on the case study: the case study itself, and the intro call |

## Rebuilding the cover

The source is generated art, so rebuild rather than retouch. Regenerate the case study hero
with `case_studies/wolfpack-ai-command/planning/hero/build_hero.py`, then:

```python
from PIL import Image
src = Image.open('case_studies/case-study-assets/img/wolfpack-ai-command-shield-hero.jpg').convert('RGB')
src.resize((1200, 675), Image.LANCZOS).save(
    'blog_posts/2026-08-15-ai-operating-layer/cover.jpg',
    'JPEG', quality=88, optimize=True, progressive=True)
```

## Log

- 2026-08-15 — Phase 1 and the authoring half of Phase 2, in one session (#196). Issue filed,
  Notion trail created (Blog Post 7, the LinkedIn row, task 8 under the case study project),
  brief and source notes written, cover built, `post.md` and `raw-linkedin-post.md` written.
  Converter dry-run clean. **No Wix push**, per Ry.
- 2026-08-15 — **Pushed to Wix as an unpublished draft** (#209).
  `POST /blog/v3/draft-posts` returned `4c8c192e-cd4a-428b-8e0f-995c4a247909`, status
  `UNPUBLISHED`, 65 rich-content nodes, 5 minutes to read. Cover uploaded as
  `e00ee6_a2fce010a5b344f5b1c10981d43c913b~mv2.jpg` (1200 x 675). One tag was new
  (`project management`), one existing (`AI engineering`). The draft was read back and matches
  what was sent field by field: title, excerpt, both tag IDs, `seoSlug`, cover dimensions,
  `featured: false`, `memberId`, both outbound links, all three lists at 3/3/4 items, and every
  em dash intact.
  **Blocked and fixed before sending:** the payload's first build had every hard-wrapped list
  item split into a one-item list plus an orphan paragraph (#208). The post's list items were
  unwrapped onto single lines — prose verified character-identical afterwards — and the payload
  rebuilt from 99 nodes to a correct 65.
- 2026-08-15 — Intro gained two framing paragraphs on Ry's instruction (#203): the post is an
  abbreviated summary of the case study, and the system is ready to integrate now, adding value
  in **days, not months**. They sit after the verbatim opener, not above it, and they are the
  **only original prose in the body**. The claim is the offer's estimate, not a measured
  result — guarded in three places now (the HTML comment in `post.md`, the brief's traps, and
  `source-notes.md`).
- 2026-08-15 — Case study **re-deployed** (`ai-coaching-intake#73`), so the live page carries the
  new `og:description`. That deploy also carried the shared `case-study-assets/` forward, which
  restyled the financial model case study too — expected, and recorded in that repo's `CLAUDE.md`.
- 2026-08-15 — Excerpt replaced with Ry's speed-first sentence (#201), and the case study's
  `og:description` changed to the same string in the same PR so the pair stays identical. The
  case study's `<meta name="description">` is a different sentence and was left alone.
  **Consequence:** the deployed case study now carries the old `og:description` until the
  folder is re-copied into `wolfpackdata/ai-coaching-intake`. That is a deploy item on the case
  study, not a gate on this post.
- 2026-08-15 — Corrected mid-session: the issue was filed claiming the case study was not yet
  deployed, sourced from the root `CLAUDE.md` deployment table. Fetching the URL showed the
  page live. The issue carries a correcting comment; the brief, source notes and `post.md`
  were fixed before the branch was committed.

<!--
Phase values, in order:
  1 — intake
  2 — awaiting copywriter draft
  2 — draft in hand, pushing
  3 — draft in Wix, awaiting Ry's proofread and publish
  4 — published, link placement outstanding
  done

Phase 4 note for whoever gets there: the link-placement pass has an unusually short
candidate list for this post. portfolio/ is one-destination and already carries a card for
this case study; the case study itself ends on the intro call and adding a blog link would
be a second destination on a page that has one; rates/ and github/ are out on their own
rules. The live surfaces most likely to be right are the Wix blog index and Wix pages Ry
edits by hand, which are recommendations for him rather than work to do here.
-->
