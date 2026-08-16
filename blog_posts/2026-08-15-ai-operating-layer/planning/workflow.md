# Workflow — An AI Operating Layer for Streamlining Project Delivery

Phase: 2 — draft in hand, **push deliberately not made**

| | |
|---|---|
| Folder          | `blog_posts/2026-08-15-ai-operating-layer/` |
| GitHub issue    | wolfpackdata/wp-website#196 |
| Notion content  | https://app.notion.com/p/3bec70e5c7b481dbbe75d5d1bac184f5 (Blog Post 7) |
| Notion LinkedIn | https://app.notion.com/p/3bec70e5c7b48156ab99f601cbb3aae1 |
| Notion task     | https://app.notion.com/p/3bec70e5c7b481969071d68ca7b436c8 (8. Launch the … blog post) |
| Wix draft ID    | **(unset — never pushed)** |
| Live URL        | (unset) |
| Slug            | `ai-operating-layer-for-project-delivery` |
| Cover           | `cover.jpg`, 1200 x 675, 49 KB — the case study's shield hero, downscaled |

## Why this one skipped a phase boundary

Ry asked for the post **end to end in one session**, using verbatim copy from the case study
rather than a fresh draft, and explicitly said not to publish to Wix yet. So Phase 1 and the
authoring half of Phase 2 both happened on 2026-08-15, and there is **no `raw-blog-post.md`** —
the body went straight into `post.md`. `planning/copywriter-brief.md` was written alongside it
and is a record of the constraints plus the spec for a redraft, not a handoff anybody acted on.

**Everything from the push onward is untouched.** No payload was built, nothing was uploaded to
the Wix Media Manager, no tags were created, and no draft exists in the dashboard.

## Before the next session pushes this

- **There is no draft ID.** The next push is `POST /blog/v3/draft-posts`, not a `PATCH`.
  Record the returned ID in the table above and commit it in the same session — the SetMaster
  post (#147) is the worked example of what happens when nobody does.
- **`project management` is a new Wix tag.** `AI engineering` already exists (created by the
  five-projects post). Creating a tag is a real Wix entity, so it needs Ry's yes.
- **`featured` is set to `false`** and is a guess. The SetMaster post is the only `true` in
  this folder.
- The case study this post links is **live** — `https://intake.wolfstrategyllc.com/wolfpack-ai-command/`
  was fetched and confirmed 2026-08-15. The root `CLAUDE.md` deployment table does not list it
  and is stale on this point; do not re-derive the answer from that table.
- **The push is Ry's call, not a leftover chore.** He asked for the post without publishing it.

## Open questions for Ry — the Phase 2.4 batch, unasked

Collected rather than drip-fed, in the order the push needs them:

| | |
|---|---|
| Tags | `AI engineering` (exists) + `project management` (**new — needs approval**). Or drop the second |
| `featured` | Currently `false` |
| Slug | `ai-operating-layer-for-project-delivery`. It is the URL and the Wix draft preview will show a title-derived path instead, so confirm it in the dashboard |
| Excerpt | **Ry's copy** (2026-08-15, #201), and the case study's `og:description` is the same sentence. Nothing guards that pair — change both or neither |
| `date` | `2026-08-15` |
| LinkedIn | `raw-linkedin-post.md` is written and is Ry's to post. It points at the profile link rather than pasting a URL, matching the five-projects draft |

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
