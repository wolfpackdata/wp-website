# `blog_posts/` — blog content, authored here, pushed to Wix

The blog runs on **Wix** and stays there. This folder does not host or serve
anything; it moves *authoring* into the repo so posts are written in markdown,
reviewed in git, and pushed to Wix through the API instead of pasted by hand.

Same policy as every other folder in this repo: **this repo is the source of
truth.** Never edit a published post in the Wix dashboard and expect it to
survive — change `post.md` and re-push.

## One folder per post

```
blog_posts/
  2026-08-04-the-model-is-your-beacon/
    post.md          # front matter + markdown body
    cover.jpg        # hero image — .png or .jpg, whichever suits the art
    diagram.png      # optional, post-specific assets
```

The cover's **extension is not fixed**; the `cover` front matter key names the file, and the
converter reads it from there. `_template/` ships a `.png` placeholder, but a photographic or
composed cover belongs in JPEG — the financial model post's cover is a 1200px JPEG at 165 KB
where the same image as PNG would be roughly eight times that.

Folder name is `YYYY-MM-DD-slug`, dated by intended publish date. The folder
name is **not** the URL — the URL comes from the `slug` front matter key (or is
derived from the title when `slug` is omitted).

Start from [`_template/post.md`](_template/post.md).

## Front matter

| Key | Required | What it does |
|---|---|---|
| `title` | **yes** | Post title. Also the fallback for `slug` and cover alt text. **Quote it if it contains a colon.** |
| `slug` | no | URL path — `wolfstrategyllc.com/post/<slug>`. Derived from the title if omitted. |
| `excerpt` | no | Feed and social preview text. Wix autogenerates one if omitted. |
| `cover` | no | Filename of the hero image, in this folder. |
| `cover_alt` | no | Alt text for the cover. Falls back to `title`. |
| `date` | no | Intended publish date. Recorded for the author; Wix stamps its own on publish. |
| `tags` | no | Wix blog tags, resolved to tag IDs at push time. Inline `[a, b]` or a block list. |
| `featured` | no | `true` marks the post featured on the blog. |

**A post that has a case study carries the case study's title, verbatim.** Ry's rule, set
2026-08-04 (#119): the same piece of work should not be called two different things in two
places. Take the case study's `h1`, not its `<title>` tag — the tag carries a subtitle and a
`· Case Study` suffix that exist for the browser tab and the search result, not as the name of
the work. **Retitling does not touch the slug**, which is set explicitly so the URL stays put;
and a title with a colon in it, which this pairing tends to produce, must be quoted.

Unknown keys are a hard error rather than a silent no-op, so a typo surfaces
before the push instead of after it.

## Markdown support

The converter covers what prose posts need:

| Markdown | Ricos |
|---|---|
| `#` … `######` | `HEADING` levels 1-6 |
| paragraphs (wrapped lines join) | `PARAGRAPH` |
| `**bold**`, `*italic*`, `~~strike~~` | `BOLD`, `ITALIC`, `STRIKETHROUGH` decorations |
| `` `inline code` `` | plain text, contents verbatim — see the fidelity limits below |
| `[text](url)` | `LINK` decoration, opens in a new tab |
| `- item` / `1. item` | `BULLETED_LIST` / `ORDERED_LIST` |
| `> quote` | `BLOCKQUOTE` |
| ```` ```lang ```` fences | `CODE_BLOCK`, contents verbatim |
| `---` | `DIVIDER` |
| `![alt](file.png)` | `IMAGE`, resolved to a Wix media ID |
| `<!-- comment -->` | stripped |

Not supported, by choice: tables, footnotes, nested lists, raw HTML. If a post
needs one, add it to the converter rather than hand-editing in Wix — the point
of the pipeline is that `post.md` fully determines the post.

Decorations nest (`**bold *both* bold**`), inline code is literal inside, and
`snake_case` underscores do not open emphasis.

## Paragraph spacing

**Every block gets a blank line after it, inserted automatically.** Markdown
separates paragraphs with a blank line, but Ricos does not carry that blank line
as anything, so consecutive `PARAGRAPH` nodes arrive butted together and Wix
renders them as one dense slab with no gap between them. `space_blocks()`
inserts an empty `PARAGRAPH` between every pair of adjacent block nodes to
restore it.

An empty paragraph, and not a margin or a line height, because Wix strips
styling it does not recognize when it saves a draft (the same behavior that
costs inline code its `FONT_FAMILY`, below) and an empty paragraph is exactly
what the Wix editor writes when an author presses Enter twice. It is the one
spacing device known to survive the round trip.

**Do not hand-author blank paragraphs in `post.md` to force spacing.** They are
added at payload assembly, so a manual one arrives doubled. Write normal
markdown and let the converter space it.

## Known fidelity limits

Verified against the live Wix API by pushing a draft and reading it back. These
are Wix behaviors, not converter bugs, and the converter does not pretend
otherwise:

- **Inline code has no visual styling.** Ricos has no inline-code decoration,
  and Wix silently strips `FONT_FAMILY` on save — tested with both `monospace`
  and `Courier New`. Backticked text arrives verbatim but looks like body copy.
  For anything where the monospace matters, use a fenced code block, which
  survives intact.
- **`hashtags` is not settable.** Submitted values come back empty. Tags are
  separate Wix entities addressed by ID, which is why the push step creates
  them through the Tags API and sets `tagIds`.
- **A draft's `url` preview is derived from the title, not `seoSlug`.**
  `seoSlug` is stored correctly; the preview path just does not reflect it
  before publish. Confirm the final URL in the Wix dashboard when the slug
  matters.

## Pushing a post

The converter never talks to Wix. It reads files and writes JSON; the push is a
separate step Claude runs through the Wix connector, which is already
authenticated — **no API key is stored in this repo.**

Ask Claude to "push `blog_posts/<folder>` to Wix as a draft". It runs:

1. **List what needs resolving.**
   ```
   python blog_posts/tools/md_to_ricos.py blog_posts/<folder> --list-images
   python blog_posts/tools/md_to_ricos.py blog_posts/<folder> --list-tags
   ```
2. **Upload each image to the Wix Media Manager**, collecting the returned
   media IDs into a `media.json` of `{"cover.png": "<media id>", …}`.
3. **Create each tag** via `POST /blog/v3/tags` with `{"label": …,
   "language": "en"}`, collecting the IDs into a `tags.json` of
   `{"ai": "<tag id>", …}`. Creating a tag that already exists returns the
   existing one, so this is safe to repeat.
4. **Build the payload.**
   ```
   python blog_posts/tools/md_to_ricos.py blog_posts/<folder> \
       --media-map media.json --tag-map tags.json --out payload.json
   ```
5. **POST it** to `https://www.wixapis.com/blog/v3/draft-posts`.

Missing maps degrade loudly, not silently: an unresolved image is a hard error,
and declared-but-unmapped tags print a warning that the post will publish
untagged.

The post lands as an **unpublished draft** in the Wix dashboard. Review it
there and hit publish yourself — nothing reaches the public without that click.
`--publish` exists but is deliberately not the default.

`media.json`, `tags.json`, and `payload.json` are build artifacts. Keep them out
of git.

### Re-pushing an edited post

A draft post has an ID. To update rather than duplicate, `PATCH
/blog/v3/draft-posts/{id}` with the rebuilt payload. Record the returned ID when
a post is first pushed — without it the next push creates a second post.

## Site facts

| | |
|---|---|
| Site | `WolfStrategyLLC` (`9132186a-8059-4d87-8ae9-904358075c7d`) |
| Blog URL | `https://www.wolfstrategyllc.com/post/<slug>` |
| Author `memberId` | `e00ee638-af7f-4aac-aa2b-c99d795ecf78` |
| Categories | none defined — posts are organized by tags |
| Size limit | 400KB per post, enforced by the converter |

The author `memberId` is the default in the converter and matches the existing
published posts. A post pushed under a different member shows a different byline.

## Tests

```
python -m unittest discover blog_posts/tools
```

Stdlib only, no dependencies, consistent with this repo's no-build-step
convention. Run them before merging a converter change.

## Tone

Post copy follows [`docs/ryan-blog-tone.md`](../docs/ryan-blog-tone.md). Its §9
checklist is runnable against `post.md` directly, since the markdown has no head
or scripts to strip: em dashes, exclamation points, question marks, and
contractions should all come back zero.

Two things to strip before counting, or the numbers lie: the front matter block,
and HTML comments. One known false positive survives anyway — image syntax
`![alt](file.png)` registers as an exclamation point. Count images and subtract,
rather than rewording prose that was already fine.
