# Workflow — Consolidation Under Pressure

Phase: 4 — published, link placement outstanding

| | |
|---|---|
| Folder          | `blog_posts/2026-08-15-consolidation-under-pressure/` |
| GitHub issue    | wolfpackdata/wp-website#211 |
| Notion content  | https://app.notion.com/3bec70e5c7b481d6a989d58078f983b3 (Blog Post 8) |
| Notion LinkedIn | https://app.notion.com/3bec70e5c7b481f88a39f5d371af4db5 |
| Notion task     | https://app.notion.com/3bec70e5c7b4811089f1ee8b102919c3 |
| Notion LinkedIn task | https://app.notion.com/3bec70e5c7b4818c93fac31fb42dd836 |
| Wix draft ID    | **`ad404772-7e42-4108-a157-60efe0267d67`** — pushed 2026-08-15, published 2026-08-15 10:24 PM PT |
| Live URL        | **<https://www.wolfstrategyllc.com/post/consolidation-under-pressure-music-gear>** |
| Slug            | `consolidation-under-pressure-music-gear` |
| Cover           | `cover.jpg`, 1200 x 675, 226 KB — Ry's supplied hero art, downscaled |

## The cover is supplied art — there is no generator

The master is
`case_studies/consolidation_under_pressure/planning/consolidation-under-pressure-hero.png`
— 1337 x 752 RGBA, 2,202,468 bytes — **supplied by Ry on 2026-08-15** and committed
with this round. The filename as supplied was `consolidation under pressure hero.png`,
with spaces; it was **renamed on commit** to match this repo's asset naming, and the
original is left untracked in the main checkout for Ry to delete.

**Unlike the other two case-study covers, there is no `build_hero.py`.** The
financial model and AI Command heroes are both composed by a committed generator and
the standing instruction there is *rebuild rather than retouch*. Here the committed
PNG **is** the master, and the art appears nowhere else in the repo — this case
study's own hero is a text hero with stat tiles and no image. **Retouching means
asking Ry for new art.** There is nothing to re-run.

`cover.jpg` was derived from that master with:

```python
from PIL import Image
src = Image.open(r'case_studies/consolidation_under_pressure/planning/consolidation-under-pressure-hero.png')
img = src.convert('RGB').resize((1200, 675), Image.LANCZOS)
img.save(r'blog_posts/2026-08-15-consolidation-under-pressure/cover.jpg', 'JPEG', quality=88, optimize=True, progressive=True)
```

## Rulings applied

| | |
|---|---|
| Title | The case study's `h1`, **verbatim** — the #119 rule. No colon, so unquoted |
| Slug | Confirmed by Ry 2026-08-15. Deliberately does not follow the title |
| Body | Lifted verbatim from **the PAGE**, never the vendored `.md` — that file has been stale since #197. Passage map, every cut and every punctuation deviation in `planning/source-notes.md` |
| Numbers | Only the page's vetted meta-description set: **2016–2026 as digits**, and **forty-three / thirty-one as the page's own words** inside a verbatim lift. **The map's event count appears nowhere** — design plan **D-009** is open with Ry (brief says 41, dataset holds 42) |
| Tags | `music technology` + `case study` + `financial modeling`, all existing, Ry's pick 2026-08-15 |
| `featured` | `false`, Ry's call |
| Excerpt | The page's `og:description`, **verbatim** — and deliberately not the same wording as the hero standfirst the post opens on. The page carries both |
| Destinations | Two: the case study, then the intro call. The report's 82 source links are citations, and `transaction-map.html` is `noindex` and reached from the report only |

## Open flags for Ry

- **The verbatim `#about` lift carries two spelled-out structural counts** — *"the
  other twelve"* rows without a primary source, and *"the seven places the record is
  thin."* They are counts of the report's **evidence structure**, not market figures,
  and they sit inside Ry's own sentence. If that reads as one count too many, **drop
  the whole paragraph rather than edit it** — editing it forks his copy, which is the
  one thing this post is built to avoid.
- **The root `CLAUDE.md` says the case study has "Eleven numbered parts."** The page
  labels its sections **Part zero … Part nine** plus two appendices, so that line
  does not describe the page. An earlier draft of *The Full Version* inherited the
  count and it was removed on verification. **Flagged, not fixed here** — correcting
  `CLAUDE.md` is a separate change.

## Log

- 2026-08-15 — Phases 1–2 authoring in one session (#211), the same shape as the AI
  Command post (#196/#210). Issue filed; the Notion trail already existed, created by
  an earlier session, and was flipped to **AI Processing / Drafting** at the start of
  work. `post.md` and `raw-linkedin-post.md` lifted verbatim from the page,
  `copywriter-brief.md` and `source-notes.md` written alongside, cover derived from
  Ry's supplied art. Converter dry-run clean — one bulleted list, two items, no #208
  orphans. An **independent verification pass caught a derived part count** ("eleven
  parts") sourced from the stale root `CLAUDE.md` rather than the page; it was removed
  from the post and the brief, and the enumeration that survives is verifiable line by
  line against the page. Same pass tightened the deviation record: the two Pattern
  headings take a terminal full stop as bullet leads, the colon closure recurs in the
  LinkedIn draft, and the `#about` lift's *"reproduced here in full"* was cut because
  "here" changes referent once the copy leaves the page. **Push pending.**
- 2026-08-15 — **Pushed to Wix as an unpublished draft.** `POST /blog/v3/draft-posts` returned
  `ad404772-7e42-4108-a157-60efe0267d67`, status `UNPUBLISHED`, 51 rich-content nodes, 3 minutes
  to read. Cover imported from the feature branch's raw GitHub URL after a byte-for-byte hash
  check, stored as `e00ee6_73dcac5cba66431fab45c0572be10cd0~mv2.jpg` (1200 x 675). All three tags
  existed; none created. The draft was read back and matches what was sent field by field —
  title, excerpt, `seoSlug`, all three tag IDs, cover id/dimensions/altText, `featured: false`,
  `memberId`, both outbound links, the one bulleted list at 2/2 items, every em dash intact, and
  not one node id rewritten. A subagent's first POST attempt was blocked by the local permission
  classifier; the send was made from the main session, and listing drafts confirmed the blocked
  attempt created nothing. The draft preview path is title-derived
  (`/post/consolidation-under-pressure`) — the README's third fidelity limit; `seoSlug` is stored
  correctly, so confirm the final URL in the dashboard before publish. The pre-send inspection
  also surfaced a pre-existing converter bug — bold wrapped around a link is dropped (#212) — so
  the CTA arrives unbolded here exactly as on every previously pushed post.
- 2026-08-15 — **Ry retitled the draft in the Wix dashboard** to *"New Case Study:
  Consolidation Under Pressure"* (draft `editedDate` 10:22 PM PT) and the retitle was
  mirrored back into `post.md` in the same evening's sync commit, so the pair cannot
  drift and a future re-push cannot revert it. **This deliberately departs from the
  #119 h1-verbatim rule — Ry's call, as that rule's owner**; the title is now quoted
  in the front matter because it carries a colon. The slug is untouched. Because the
  dashboard was edited directly, **hash the live body against a fresh build before any
  body re-push** (README, "Re-pushing an edited post").
- 2026-08-15 — **Ry reported publishing the post, but the publish did not register.**
  At sync time (~10:35 PM PT) the draft still reads `status: UNPUBLISHED` with
  `hasUnpublishedChanges: true`, `GET /blog/v3/posts/{id}` returns `POST_NOT_FOUND`,
  and the published-posts list holds 7 posts, this one absent — four consistent
  signals. The retitle *did* save (`changeOrigin: MANUAL_SAVE`), which reads like a
  save that was mistaken for a publish, or a publish flow that did not complete.
  **Flagged to Ry to re-publish from the dashboard; nothing was published from here**
  per the standing rule. Phase stays 3 until the publish is confirmed, and the Phase 3
  bookkeeping (content row → `Published`, post URL, Web Property Map edge) waits with
  it.
- 2026-08-16 — **Published, and the previous entry resolves as a race.** The live page
  stamps `datePublished` 2026-08-16T05:24:02Z — **2026-08-15 10:24 PM PT**, two minutes
  after the probes that read `UNPUBLISHED`. Ry clicked publish on seeing the flag and
  confirmed the fix the next morning with the live URL. Verified live: HTTP 200, the
  retitled `<title>`, and the `seoSlug`-derived path
  `/post/consolidation-under-pressure-music-gear` (the title-derived preview path never
  became the URL — the README's fidelity limit behaved as documented). Body links on
  the live page: the case study and the intro calendar, exactly the two destinations.
  Phase 3 bookkeeping run the same morning: content row → `Published` with URL and
  date, the blog task's last two to-dos checked and the task closed `AI Done`, and the
  Web Property Map given the new Wix → intake edge. The LinkedIn task stays
  `In progress` — the draft is written; posting, visual, and sequencing are Ry's.

<!--
Phase values, in order:
  1 — intake
  2 — awaiting copywriter draft
  2 — draft in hand, pushing
  3 — draft in Wix, awaiting Ry's proofread and publish
  4 — published, link placement outstanding
  done
-->
