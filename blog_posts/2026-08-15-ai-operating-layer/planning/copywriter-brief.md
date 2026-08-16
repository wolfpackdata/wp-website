# Copywriter brief — the Wolfpack AI Command case study post

**For:** the person writing the post. **Not** the post itself, and not a draft to polish.
Everything here is raw material and constraints. Write your own sentences — with one large
exception, spelled out immediately below, that makes this brief unlike every other one in
this folder.

**Deliverable:** one post, target **1,200 words**, at
`blog_posts/2026-08-15-ai-operating-layer/post.md`, plus a LinkedIn version at
`raw-linkedin-post.md`.

> **Read this before section 1.** This brief was written in the same session as the draft
> it describes. Ry asked for the post end to end and told Claude to lift verbatim copy from
> the case study rather than reinvent it, so there was no copywriter handoff and no
> `raw-blog-post.md` — the body went straight into `post.md`. The brief is therefore a
> **record of the constraints the draft was built under and the spec for redrafting it**, not
> a handoff that was acted on. It is written in the second person anyway, because the next
> person to touch this post will be redrafting rather than reading history.

---

## 1. Hard constraints

- **The title is the case study's `h1`, verbatim:** *An AI Operating Layer for Streamlining
  Project Delivery*. Repo rule, set 2026-08-04 (#119) — one piece of work, one name. Not the
  `<title>` tag, which carries the product name and a `· Case Study` suffix meant for the tab
  and the SERP. The slug is set explicitly and does not follow the title.
- **Most of the body is lifted verbatim.** Ry's instruction: *"feel free to use verbatim copy
  from the case study for most of the blog post so you don't reinvent the wheel, same thing
  for the LinkedIn post."* The passage map lives in `source-notes.md`. Lifting is the job;
  paraphrasing a lifted paragraph into your own phrasing is the failure mode.
- **The case study's copy is Ry's own**, after his 2026-08-15 tone pass (#188/#189). The `h1`
  and standfirst are supplied copy that `case_studies/wolfpack-ai-command/planning/outline.md`
  D-019 forbids rewording without him. Treat the blunt openers and the TPS Report line the
  same way: they are his voice, not filler to smooth out.
- **The case study's evidence rules carry over in full.** No results section, no invented
  outcome, no client named, no testimonial. The system's own artifact counts are *allowed on
  the case study* because that page dates them; see the trap in section 8 about repeating one
  here.
- **No client named, and no testimonial invented.** The client in the case study is
  anonymised by shape and stays that way. Nothing in the post identifies one.
- **One destination.** The case study, then the intro call. Nothing else.

---

## 2. The facts, as measured

There is nothing to measure for this post, and that is deliberate. **It carries no numbers at
all.**

The case study carries six artifact counts — 8 skills, 54 numbered rules, 10 lettered
sections, 5 drift checks, 0 destructive tools, 1 AI identity — all counted in the system's own
repositories on **13 August 2026**, and that page states the date on the page. A count
repeated in a blog post arrives with no date attached and starts drifting the moment the
system changes. The post cites none of them and links the page that does.

The two dates the post could carry, if a redraft wants them: the practice started **November
2025**; the repositories that formalized it arrived **July 2026**. Both are on the case study.

---

## 3. The caveats, and they belong in the body

The case study's §10 ends on four "what I am explicitly not claiming" chips. **All four go in
the post body, verbatim, as their own section** — not compressed into a closing hedge, not
dropped for length. They are the most load-bearing paragraphs in the piece for the audience it
leads with, and a post that carries the argument without them reads like a pitch.

1. **Not a replacement.** Not a headcount argument. It takes the half of the role that
   consumes the hours without being the reason the role is valuable.
2. **Not an engine.** The Python layer is a teaching-grade scaffold, deliberately frozen.
3. **Not infallible.** The target is not zero errors; it is small, attributable, cross-linked
   changes that can be reversed with one instruction.
4. **Not measured.** No instrumented before-and-after study exists. The economic case is a
   mechanism, not a percentage.

---

## 4. The subject, in plain description

**Wolfpack AI Command** is a governed AI operating layer for running projects: a system of
record (Notion), a system of work (GitHub), and AI operators bound by written, versioned rules
that the AI itself is governed by. Three layers — the workspace layer, the code layer, and a
small Python agent layer where the boundaries were proven as running code before being
promoted into the written governance.

Source, not copy. The post does **not** tour the three layers — see section 5.

---

## 5. The real subject

The post is the case study's **argument**, cut to feed length. The argument is a split:

1. **The role everyone agrees on, and the job design that breaks it.** A project manager owns
   dates they cannot move, built from work they are not doing. The interruptions are the work.
2. **Two jobs in one title.** The record — status-chasing, ticket hygiene, cross-linking,
   version bookkeeping, writing down what was decided. The judgment — relationships,
   foresight, vertical communication, knowing when the plan has stopped being true. The record
   consumes most of the hours and is not why anyone hires or becomes a great PM.
3. **You cannot just stop doing it.** The record is what judgment runs on. Let it rot and you
   blind the PM rather than freeing them. This is the hinge of the whole piece.
4. **Governance before automation.** What is the AI allowed to do; who can tell what it did;
   how do we know when it went wrong and how painful is it to put back.
5. **Supervision, made concrete.** The AI's own account and name; a timestamped comment on
   every status change; no backfilling; merged is not accepted; the AI may not assign work to
   itself.

**Pick these five and stop.** The three-layer tour, the confidentiality controls, the setup
story, and the dated mistakes-to-rules table are the reason to click through to the case
study. A post that summarizes all eleven sections is a worse case study, not a better post.

If only one survives, it is **3** — it is the sentence that stops "let AI do the admin" from
sounding like a tooling suggestion.

---

## 6. Suggested outline, with word budgets

| § | Section | Words | Must contain |
|---|---|---:|---|
| 1 | Open on the person, not the problem | 230 | The three §01 paragraphs verbatim, ending on "criticism of the job design" — then, **after** them, the two framing paragraphs added in #203: this is an abbreviated summary of the case study, and the system is ready to integrate now, adding value in days not months. Do not enumerate what the case study contains; §6 already does |
| 2 | One role, two completely different jobs | 330 | Both lists verbatim; the pull quote; "Extremely boring."; the hinge; Ry's closing question |
| 3 | Not another chatbot bolted on | 300 | The ungoverned-mess paragraph; the three governance questions verbatim; the three bound systems; the version-control callout; the name's single use |
| 4 | How do you know what the AI did? | 260 | The attribution scar and **Main**; then the three rules as bullets; the self-assignment prohibition |
| 5 | What I am explicitly not claiming | 150 | All four chips, verbatim |
| 6 | The full version | 80 | Case study link, one sentence on what is in it, then the call |

Adjust the split, not the total.

---

## 7. CTAs

- **Closing CTA:** the 30-minute intro call, `https://calendar.app.google/zHNd1NA9wzb4VRLw5`,
  labelled **Work With Wolfpack** (matching the financial model post).
- **Inline links:** exactly one — *Read the case study*, pointing at
  `https://intake.wolfstrategyllc.com/wolfpack-ai-command/`.

**The case study is live.** Verified 2026-08-15 by fetching that URL: it returns the page,
h1 matching. Do not trust the repo's root `CLAUDE.md` deployment table on this point — it
does not list this case study and reads as though the page were still unshipped. It is stale;
the Notion task *5. Deploy the case study to the intake repo* is `AI Done`.

No intake-form link, no rates link, no portfolio link, no résumé download.

---

## 8. Traps

- **Never hard-wrap a list item.** The converter joins wrapped lines inside a paragraph but
  not inside a bullet (#208), and it fails silently — a two-line bullet becomes a one-item
  list plus an orphan paragraph. This post hit it and was caught at the payload stage, not by
  any check. Wrap prose freely; keep every bullet on one line.
- **Do not put a number on "days, not months".** The intro's integration claim (#203) is the
  offer's estimate, on the same footing as the case study's *"hours, not days"*. A percentage,
  a week count, or a before-and-after turns it into a measured result the work cannot support.
  It is also not an outcome claim — it says how fast the system installs, not what it produces
  once installed, which is why it coexists with the *Not measured* bullet rather than
  contradicting it.
- **Do not repeat an artifact count.** Every number on the case study is dated on that page.
  A number in a post is an undated copy that goes stale silently. This is the exact failure
  the system in the post exists to prevent, so getting it wrong here is expensive in a way it
  would not be for another post.
- **Do not restore the <50% completion figure.** Ry cut it from the case study in his
  2026-08-15 pass, and a derived post is not where it comes back.
- **Never imply the system replaces a project manager or saves headcount.** D-013 on the case
  study, and it applies to every surface that describes the system. The tedium diagnosis is
  sympathy for the role. A working PM should read this and want it.
- **The product name is rationed.** The case study spends it three times. The post spends it
  **once**, in the "the whole thing is…" paragraph. Running copy uses common nouns — the
  system, the operating layer, the command center.
- **Do not describe tooling by brand-name feature.** Notion and GitHub are named because the
  case study names them as the two kinds of system, not because the argument depends on them.
  A reader on Linear and GitLab should still be able to use every rule in the post.
- **Do not let the setup become the post.** The split is the argument. The system is the
  answer. The case study is where the answer gets its detail.
- Do not claim the AI wrote the post, and do not claim it wrote none of it.

---

## 9. The cover image

`cover.jpg`, 1200 x 675, 49 KB.

It is the case study's **hero shield**, downscaled from the deployed 2100 x 1181 original at
`case_studies/case-study-assets/img/wolfpack-ai-command-shield-hero.jpg`. A luminous shield on
a deep navy field, quartered by fine axis lines, holding the four Notion database icons — a
green triangle for products, a blue circular arrow for projects, an orange grid for tasks, a
brown meeting glyph for clients — over a faint horizon grid.

This is the same route the financial model post's cover took: its case study's hero, resized
into the post folder. The reader meets the same image on both surfaces, which is the point.

**It is generated art, so rebuild rather than retouch.** The source is built end to end by
`case_studies/wolfpack-ai-command/planning/hero/build_hero.py` from four committed Notion icon
SVGs. If it changes, regenerate the hero and redo the downscale — the exact command is in
`workflow.md`.

Considered and rejected: the finished social card
(`case-study-assets/img/og-wolfpack-ai-command.png`) has the title text baked in and would
double the headline in the feed; the tiled print variant under `planning/hero/` is texture
built for a 360 px LinkedIn tile, not a cover.

`cover_alt` is written and is in the front matter. No figures in it.

---

## 10. The LinkedIn version

**Target 350 words**, at `raw-linkedin-post.md`. It opens on the same split, keeps the hinge
("let the record rot and you blind them"), keeps the three governance questions in compressed
form, and keeps the **not measured** caveat explicitly — that one does not get dropped for
length on any surface.

It ends on a question to technical leaders and then the profile link, matching the
five-projects LinkedIn draft's convention of pointing at the profile rather than pasting a URL
in the body. No hashtags — the only other LinkedIn draft here carries none.

**It is Ry's to post**, and it is not scheduled: the case study it points at is not deployed.

---

## 11. Source files, if you want to go deeper

| Topic | File |
|---|---|
| Front matter schema, push procedure, fidelity limits | `blog_posts/README.md` |
| The post's phase, gates, and open questions | `planning/workflow.md` |
| Passage-by-passage provenance map | `planning/source-notes.md` |
| The case study itself | `case_studies/wolfpack-ai-command/index.html` |
| Its outline, decisions ledger D-001…D-021, evidence rules | `case_studies/wolfpack-ai-command/planning/outline.md` |
| Case study folder conventions and voice notes | `case_studies/README.md` |
| The hero generator | `case_studies/wolfpack-ai-command/planning/hero/build_hero.py` |
