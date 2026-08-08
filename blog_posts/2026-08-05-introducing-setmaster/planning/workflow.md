# Workflow — SetMaster 3 Is Live: The Traktor® Set-Prep Tool I Built for Myself

Phase: 3 — awaiting Ry's proofread and publish

| | |
|---|---|
| Folder          | `blog_posts/2026-08-05-introducing-setmaster/` |
| GitHub issue    | wolfpackdata/wp-website#154 (push) · #136 (authoring) · #146 (outbound links) |
| Notion content  | (unset — post predates the workflow skill) |
| Notion LinkedIn | (unset — post predates the workflow skill) |
| Notion task     | (unset — post predates the workflow skill) |
| Wix draft ID    | `26bf0fe7-d36d-4dde-bb59-09b9291fa2b0` |
| Live URL        | (unset) |
| Slug            | `introducing-the-setmaster-application` |

## This post predates the skill

Written before `wp-blog-writing-workflow` existed (#151), so it never had a ledger and never
had a Phase 1. This file was reconstructed 2026-08-06 from what is in the folder and in git,
per the skill's rule for posts that arrive without one. The gap it closes is the one #147 is
the worked example of: the SetMaster post's markdown was edited to link `/setmaster3/` and
the v3.0.4 tag and the live post carried neither, because no draft ID was recorded anywhere.

**Read this file before any re-push.** A re-push is `PATCH /blog/v3/draft-posts/{id}`, never
another `POST` — a `POST` creates a second post rather than updating this one.

## Body

The published body is the long-format copywriter draft that landed 2026-08-06, kept at
`planning/raw-blog-post.md` and reproduced verbatim in `post.md`. It replaced the 576-word
short version authored under #136, which survives in git history at `46f9e26`. Ry's call,
2026-08-06.

The LinkedIn draft that landed with it is at `planning/raw-linkedin-post.md`, unpushed. It is
Ry's to post.

## Rulings

| | |
|---|---|
| Title | The draft's `h1`, with the trademark mark added |
| Slug | **Unchanged.** Does not follow the new headline, so the planned URL stays put |
| `featured` | `true` |
| Tags | `DJ tools`, `music technology`, carried over from the short version |
| Cover | `sm3-assets/img/a01-track-playlist-matrix.png`, replacing the a02 set-editor capture |
| Excerpt | Assembled from the draft's own opening lines, not written fresh |

## Outstanding

- Ry proofreads the draft in the Wix dashboard and publishes it. Nothing here is public until
  he does.
- **The title mark is the one open question.** Ry chose the draft's `h1` verbatim and also
  chose to apply trademark discipline, and `sm3-specific-pages/README.md` says *every visible*
  Traktor carries the mark — including one in a title. It is marked. A clean title is a
  `{id, title}` patch if he wants it.
- Phase 3 work is owed once the post is live: the Content DB row, the task, and the **Web
  Property Map**, which this post makes stale the moment it publishes — a live Wix post
  linking `intake.wolfstrategyllc.com/setmaster3/` is a new Wix → GitHub link path, one of the
  map's explicit staleness triggers.
- No Notion trail exists for this post. Creating one is a Phase 1 artifact and was not part of
  #154; it is Ry's call whether to backfill it.

## Log

- 2026-08-06 — Ledger written. Hero swapped to the Track-Playlist Matrix capture, body
  swapped to the long-format draft, trademark marks and the unaffiliated line applied, 15
  citation spans stripped. First push to Wix as an unpublished draft (#154).
- 2026-08-06 — Pushed. `POST /blog/v3/draft-posts` returned
  `26bf0fe7-d36d-4dde-bb59-09b9291fa2b0`, status `UNPUBLISHED`, 247 nodes, 8 minutes to read.
  Cover uploaded as media `e00ee6_eb290ffb1bcc47ecb4ac0b6f2bf5a572~mv2.png`. Both tags were
  **new** Wix entities, created by this push: `DJ tools`
  (`287fae4a-5f1d-46c2-943c-1fd47bfd377c`) and `music technology`
  (`97e8df2c-d38a-4126-9dad-8219f06f8e59`).
- 2026-08-06 — One corrective `PATCH`, then verified. The read-back showed the trademark
  disclaimer had lost its `ITALIC` decoration in transit; the patch restored it, and a second
  read-back confirmed all 11 decorated runs, all 247 nodes, both `/setmaster3/` links, and
  every registered mark match `post.md`. **The live body now matches the source of truth
  exactly**, which is what keeps the README's "hash the live body against a fresh build"
  re-push safety check meaningful for this post.

## Notes for the next session

- The draft preview path reads `/post/setmaster-3-is-live-the-traktor-set-prep-tool-i-built-for-myself`.
  That is the **title-derived preview**, the third documented fidelity limit in
  `blog_posts/README.md`, not the real URL. `seoSlug` is stored correctly as
  `introducing-the-setmaster-application`. Confirm in the dashboard before publishing.
- Pushing this post needed a workaround worth knowing: the Wix **code runtime blocks fetches
  to non-Wix hosts**, and routing the payload through Wix's media importer was denied by
  policy, so the 95 KB payload went through `CallWixSiteAPI` as an inline body. Compact JSON
  (`separators=(',',':')`) is 45 KB against 95 KB indented — build it compact if this has to
  be done by hand again, and **read the result back afterwards**, because that is what caught
  the dropped decoration.
