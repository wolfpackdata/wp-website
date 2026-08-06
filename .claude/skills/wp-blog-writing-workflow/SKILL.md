---
name: wp-blog-writing-workflow
description: Run a Wolfpack blog post from a raw prompt or transcript through to a published Wix post and the site links that should point at it. Use when Ry hands over links and ideas for a new post, when a copywriter's draft lands in a post folder, when he gives back a live URL after publishing, or when he asks where on the site a post should be linked. Four phases across separate sessions, resumed from a committed ledger.
---

# The Wolfpack blog writing workflow

Four phases, days apart, each starting in a fresh session with no memory of the last.
**A committed ledger is what makes that work** — read it first, always.

| Phase | Trigger | Ends with |
|---|---|---|
| **1 — Intake** | Ry hands over a prompt, transcript, links, ideas | A copywriter brief, a Notion trail, a GitHub issue |
| **2 — Draft push** | A copywriter draft appears in the post folder | An unpublished Wix draft, ID recorded |
| **3 — Post-publish** | Ry gives back the live URL | Notion and the Web Property Map current |
| **4 — Link placement** | After Phase 3, or on request | Ranked recommendations for where to link it |

## First move, every session: find the phase

```bash
ls blog_posts/*/planning/workflow.md
```

Read the ledger for the post in question. It names the phase. If Ry names a post with no
ledger, it predates this skill — write one from what exists in the folder before doing
anything else.

**Never guess the phase from the conversation.** Ry saying "push it to Wix" when the ledger
says Phase 1 means the copywriter draft has not landed yet, and the right response is to say
so rather than to push a brief to the blog.

---

## The ledger

`blog_posts/<folder>/planning/workflow.md`, committed. Every phase reads it and writes it.

```markdown
# Workflow — <post title>

Phase: 2 — awaiting copywriter draft

| | |
|---|---|
| Folder          | `blog_posts/2026-08-07-example/` |
| GitHub issue    | wolfpackdata/wp-website#160 |
| Notion content  | https://app.notion.com/p/<id>  (Blog Post 7) |
| Notion LinkedIn | https://app.notion.com/p/<id> |
| Notion task     | https://app.notion.com/p/<id> |
| Wix draft ID    | (unset) |
| Live URL        | (unset) |
| Slug            | example-post-slug |

## Log
- 2026-08-07 — Phase 1 done. Brief at `planning/copywriter-brief.md`. Cover supplied by Ry.
```

**The Wix draft ID is the single most important line.** `blog_posts/README.md` warns that a
push without it creates a *second* post rather than updating the first. The SetMaster post
(#147) is the worked example of what happens when it lives nowhere: its markdown was edited
to link `/setmaster3/` and the v3.0.4 tag, and the live post carries neither, because nothing
recorded that a re-push was owed.

---

## Phase 1 — Intake

Ry supplies a long prompt, a transcript, links, and ideas, plus either a hero image, a
description of one he will make, or nothing yet. Turn that into a brief a **copywriting agent
that cannot see this session** can work from.

### 1.1 Redaction check, before writing anything

**`wp-website` is a public repo.** Everything committed to `planning/` is world-readable the
moment it merges. Source transcripts routinely carry things that should not be: client names,
rates, unannounced work, private strategy.

Read the source material for those before writing. **Anything you cannot confidently clear,
stop and ask Ry** — do not paraphrase it into safety and do not quietly drop it, because a
dropped fact is one the copywriter then cannot use.

### 1.2 The folder

```
blog_posts/YYYY-MM-DD-slug/
  cover.jpg                      # if Ry supplied one; .jpg for photographic or composed
  planning/
    workflow.md                  # the ledger
    copywriter-brief.md          # the deliverable of this phase
    source-notes.md              # Ry's raw links and ideas, cleaned
```

Folder name is dated by intended publish date. **The folder name is not the URL** — that
comes from the `slug` front matter key, set in Phase 2.

If Ry described a cover he will supply later, record the description in the brief's cover
section and mark the file missing in the ledger. If he described one to be generated, note it;
two posts here ship a committed generator under `planning/` rather than a retouched image, and
that is the pattern to follow.

### 1.3 The brief

Follow [`references/copywriter-brief-template.md`](references/copywriter-brief-template.md).
The worked example this skill is derived from is
`blog_posts/2026-08-05-five-projects/planning/copywriter-brief.md`.

Three properties matter more than the section list:

- **It is raw material and constraints, never prose to polish.** A brief containing draft
  sentences gets those sentences back, lightly edited. Say what must be true, not how to say
  it.
- **It does not dictate voice.** The repo's tone guide was removed 2026-08-06 (#150) because
  the copywriting agent already writes in Ry's voice. Supply facts, structure, constraints,
  and traps. Nothing about sentence construction.
- **It is self-contained.** The copywriter cannot see this session, so every path is written
  out and every fact appears in the brief rather than being pointed at. The source-file table
  at the end is for going deeper, not for filling gaps you left.

The section that does the most work is the **outline with per-section word budgets**. Give a
total, split it across sections, and say what each section must contain.

### 1.4 The GitHub issue

Use **`create-github-issue`**. Label `enhancement` (a post is new content) unless the post is
purely documentation of existing work. Title it `feat(blog): …`.

### 1.5 Notion

Verify identity first (**SOP rule A6**): `notion-fetch` on id `self` must return **Main**
(`39cd872b-594c-817a-8412-00023f0d7dc8`). Any other identity is a hard stop — do not write,
tell Ry.

**Two Content DB entries**, both from the default `New content` template
(`375c70e5-c7b4-8006-810f-e011a60f6a65`), data source
`collection://375c70e5-c7b4-80a4-adf4-000b7ef88033`:

| | Post row | LinkedIn row |
|---|---|---|
| `Content name` | `Blog Post N: <title>` | `LinkedIn: <title>` |
| `Content type` | `Blog article` | `Social post` |
| `Platform` | `WP Blog` | `LinkedIn Personal` |
| `Status` | `Drafting` | `Idea` |

Read `N` from the database — the existing rows are numbered in sequence. Relate both to the
project, and to the task once it exists.

> Some older rows read `Platform: Website` for blog posts. `WP Blog` is the option that exists
> for this; use it. Do not retro-fix old rows as a side effect of creating a new one.

**One task**, via **`notion-create-task`**. Name it `Launch the <title> blog post`,
`Task type: Marketing`, **`Priority` left empty**, related to the project, the product, and
both Content DB rows. Body carries the eight default to-dos, in order:

```markdown
- [ ] Outline
- [ ] Write
- [ ] Proofread
- [ ] Add content
- [ ] Add CTAs
- [ ] Publish
- [ ] LinkedIn subpost
- [ ] Share / boost
```

Ownership, which the skill needs to know and the task does not state: **outline, add content,
and add CTAs are Claude's**; **write** is the copywriter's; **proofread, publish, LinkedIn
subpost, and share / boost are Ry's.**

**This is why the task does not reach `AI Done` for days.** The completion gate requires every
checkbox checked, and four of them are Ry's. Every phase below ends at **`In progress`** with a
comment naming what is outstanding. `AI Done` comes only when Ry has published and boosted and
the last box is checked. Do not shortcut this by dropping his to-dos, and do not mark the task
done because Claude's share is finished.

### 1.6 Ship it

Branch → PR → squash-merge to `develop` per **`github-gitflow`**. Then tell Ry: the brief's
path, anything the source material could not answer, and anything held back at 1.1.

**End state:** ledger at Phase 2. Task at `In progress`, `Outline` checked, comment posted.

---

## Phase 2 — Draft push

Triggered by the copywriter's markdown landing in the folder — by convention
`raw-blog-post.md` and `raw-linkedin-post.md`.

### 2.1 Read the Notion task first

Ry's standing instruction. The task may carry comments, a changed title, or to-dos checked
since Phase 1 that change what the push should do.

### 2.2 Assemble `post.md`

Front matter per the schema in [`blog_posts/README.md`](../../../blog_posts/README.md), body
from the copywriter's draft. **Two rules that are not obvious:**

- **A post that has a case study takes the case study's title, verbatim** — its `h1`, not its
  `<title>` tag, which carries a subtitle and a `· Case Study` suffix. Retitling never touches
  the slug. A title with a colon must be quoted.
- **Never hand-author blank paragraphs for spacing.** `space_blocks()` inserts them at payload
  assembly, so a manual one arrives doubled.

### 2.3 Do not edit the prose

**Report, never correct.** Ry's call, 2026-08-06. If something reads wrong, say so and name
the line; the fix is the writer's or Ry's. The post is single-authored and stays that way.

This includes tone. There is no checklist to run — the guide was removed (#150).

### 2.4 One batched question

Everything the push needs, asked **once**, not drip-fed:

- Tags — which, and any new ones to create (tag creation is a real Wix entity, not a label)
- `featured` — true or false
- Slug — confirm, since it is the URL and the draft preview will not reflect it
- Excerpt — approve or supply
- `date`
- The cover, if still missing
- CTA targets, if the brief left any open

### 2.5 Push

The five-step procedure in `blog_posts/README.md`: `--list-images`, `--list-tags`, upload
images for `media.json`, create tags for `tags.json`, build `payload.json`, `POST` to
`/blog/v3/draft-posts`. `media.json`, `tags.json`, and `payload.json` are gitignored build
artifacts.

**Record the returned draft ID in the ledger and commit it.** This is not optional.

**Re-pushing an edited post:** `PATCH /blog/v3/draft-posts/{id}` is a partial update, so a
retitle or a cover swap is a two-field patch. Send a rebuilt payload only when the body changed,
and check first whether anyone has edited the draft in the Wix dashboard — a rebuilt body
overwrites theirs. Hash the live body against a freshly built payload; identical means safe.

**End state:** ledger at Phase 3, draft ID recorded. Task at `In progress`, `Add content` and
`Add CTAs` checked, comment naming what is outstanding. Tell Ry the draft is in the dashboard
awaiting his proofread and publish.

---

## Phase 3 — Post-publish

Triggered by Ry handing back the live URL.

1. **Content DB post row** → `Status: Published`, `Post URL`, `Publish date`.
2. **Task** → check `Proofread` and `Publish`; comment. Still `In progress` while the LinkedIn
   subpost and the boost are outstanding.
3. **Ledger** → live URL, Phase 4.
4. **Web Property Map** — [the Notion page](https://app.notion.com/p/3a5c70e5c7b48156be95db3a256a8250).
   **A published post that links an `intake.` page is a new Wix → GitHub link path, which is one
   of the map's explicit staleness triggers.** Fetch the live post, list its outbound links, and
   add the edge and a dated entry under *Maintaining this page*. Do not record a link the
   published post does not actually carry — verify against the live page, not against `post.md`.

---

## Phase 4 — Link placement

Read the published post, then find where on the site it belongs. **The constraints below kill
most obvious suggestions, which is the point of doing this with a method rather than by feel.**

Candidate surfaces: `rates/`, `ai-coaching/`, `portfolio/`, `case_studies/`,
`sm3-specific-pages/`, `hire/`, and the Wix pages.

**Three standing rules, all from `CLAUDE.md`:**

- **`portfolio/` has exactly one destination on the entire page: the 30-minute intro call.** No
  second destination without asking Ry. A blog link is a second destination.
- **Nothing indexed may link the `hire/` pages**, and they are `noindex` by design. A blog post
  linking them undoes it in one step.
- **The coral ration on `rates/`, `portfolio/`, and the case studies is fully spent.** A new CTA
  there is navy-ghost or it does not ship.

Also: **Wix is out of scope for edits** — it is hand-edited by Ry, and the API has no
theme-typography surface. Recommend Wix placements as instructions for him, not as work to do.

For each recommendation give the **surface, the exact anchor point, why the post is relevant
there, and whether it should be a hyperlink in existing copy or a CTA.** Rank them. Prefer
turning an existing sentence into a link over adding a new block — a page that gains a block
per post decays.

Deliver in chat. Offer to file an issue for the ones Ry wants; do not file one unprompted.

**End state:** when Ry confirms the LinkedIn subpost and the boost are done and the last
to-dos are checked, the task goes to **`AI Done`** with a closing comment. Ledger closed.

---

## Reference

| | |
|---|---|
| Content DB | `collection://375c70e5-c7b4-80a4-adf4-000b7ef88033` · template `375c70e5-c7b4-8006-810f-e011a60f6a65` · icon `/icons/calendar_purple.svg` |
| Tasks DB | `collection://372c70e5-c7b4-8065-bb21-000bffa5b708` · icon `/icons/grid-wide-six_orange.svg` |
| Claude's Notion identity | Main, `39cd872b-594c-817a-8412-00023f0d7dc8` |
| Wix site | `WolfStrategyLLC`, `9132186a-8059-4d87-8ae9-904358075c7d` |
| Author `memberId` | `e00ee638-af7f-4aac-aa2b-c99d795ecf78` |
| Blog URL | `https://www.wolfstrategyllc.com/post/<slug>` |
| Web Property Map | <https://app.notion.com/p/3a5c70e5c7b48156be95db3a256a8250> |

Converter tests, before merging any change to `md_to_ricos.py`:

```
python -m unittest discover blog_posts/tools
```

## Never

- Skip the ledger, or infer the phase from what Ry said instead of from the ledger.
- Push to Wix without recording the returned draft ID.
- Publish. `--publish` exists and is deliberately not the default; Ry publishes.
- Edit the copywriter's prose. Report and let a writer fix it.
- Commit anything to `planning/` that Ry would not publish — this repo is public.
- Mark the task `AI Done` while any to-do is unchecked, or drop Ry's to-dos to make it close.
- Write a Notion status change without a comment. A silent flip is an incomplete transition.
- Add a second destination to `portfolio/`, link `hire/` from anything indexed, or spend coral
  that is already rationed out.
- Edit a deployed copy in `ai-coaching-intake`. This repo is the source of truth.
