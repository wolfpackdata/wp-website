# Copywriter brief template

Fill this in at `blog_posts/<folder>/planning/copywriter-brief.md`. The worked example is
`blog_posts/2026-08-05-five-projects/planning/copywriter-brief.md`, which produced a shipped
post from this exact shape.

**Guidance lines are in blockquotes and get deleted.** Everything else is the brief.

> **Voice is not your subject.** The repo's tone guide was removed 2026-08-06 (#150) because
> the copywriting agent already writes in Ry's voice. This brief carries facts, structure,
> constraints, and traps. It never tells the writer how to build a sentence, never supplies
> draft prose, and never lists banned punctuation.
>
> **The writer cannot see the session that produced this.** Every fact it needs is in here.
> The source-file table at the end is for going deeper, not for filling gaps you left.
>
> **This repo is public.** Nothing goes in here that Ry would not publish.

---

# Copywriter brief — <post subject>

**For:** the person writing the post. **Not** the post itself, and not a draft to polish.
Everything here is raw material and constraints. Write your own sentences.

**Deliverable:** one post, target **<N> words**, at `blog_posts/<folder>/raw-blog-post.md`,
plus a LinkedIn version at `raw-linkedin-post.md`. Front matter is added separately, so
neither file needs it.

> Set the word target from the piece. The posts here run 350 to 1,200 words. Say the number;
> "medium length" produces 2,000 words.

---

## 1. Hard constraints

> The things that make the post wrong if broken, in order of how easily they are broken.
> Standing ones across every post here:

- **No client named, and no testimonial invented.** Anonymize by shape.
- **Numbers are exact.** <List the figures and their source. Say explicitly which must not be
  rounded, and name any figure that has two conflicting sources so the writer avoids it
  entirely rather than picking one.>
- **A post that has a case study carries the case study's title, verbatim** — its `h1`, not
  its `<title>` tag. <Name the case study and its `h1`, or say the title is open.>
- <Post-specific constraints.>

---

## 2. The facts, as measured

> Everything checkable, with its method. A table where the facts are comparable. State the
> measurement window and what was excluded, so the writer can describe the method if the post
> needs it.

---

## 3. The caveats, and they belong in the body

> What the facts do not mean. Not a footnote and not a closing hedge: name where they go.
> A post that makes a strong claim and buries its limits reads as a brag.

---

## 4. The subject, in plain description

> One or two sentences per thing. Mark this as source, not copy. If the post covers several
> items, say how much room the whole section gets, because this is the section that overruns
> and starves the actual argument.

---

## 5. The real subject

> The hook is rarely the point. Lay out the material the post is actually about, in numbered
> subsections, each with a concrete artifact behind it. Tell the writer to pick three or four
> rather than covering all of them, and say which is strongest if only one survives.

---

## 6. Suggested outline, with word budgets

> The section that does the most work. Adjust the split, not the total.

| § | Section | Words | Must contain |
|---|---|---:|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## 7. CTAs

> Where the post asks for something, and exactly what it points at. Get this from the Notion
> task or from Ry; do not invent a destination.

- **Closing CTA:** <destination and label>
- **Inline links:** <any in-body links, and where they go>

> The current intro-call calendar is `https://calendar.app.google/zHNd1NA9wzb4VRLw5`. The
> `…/13EANJ63HKqMc76z6` link is the 45-minute tutoring calendar and is never the funnel CTA.

---

## 8. Traps

> The specific ways this post goes wrong. Standing ones:

- Do not let the setup become the post.
- Do not claim the AI wrote it all, and do not claim it wrote none of it.
- Do not describe tooling by brand-name feature. Describe what the constraint does, so a
  reader on different tools can still use it.
- <Post-specific traps.>

---

## 9. The cover image

> The file, its dimensions, and a plain description of what is in it. If the cover does not
> exist yet, say so and describe what it will be.

`cover.<ext>`, <W> x <H>. <Description.>

`cover_alt` needs writing — describe it plainly for a screen reader. Do not put figures in the
alt text; they belong in the body where they can be read in context.

---

## 10. The LinkedIn version

> What changes. Shorter, opens on the same hook, carries the caveats in compressed form, and
> ends on the post link rather than the calendar. Say the target length.

---

## 11. Source files, if you want to go deeper

| Topic | File |
|---|---|
| Front matter schema, push procedure | `blog_posts/README.md` |
| | |
