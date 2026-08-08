# Copywriter brief — the five-projects post

**For:** the person writing the post. **Not** the post itself, and not a draft to polish.
Everything here is raw material and constraints. Write your own sentences.

**Deliverable:** one post, target **1000 words**, at
`blog_posts/2026-08-05-five-projects/post.md`, with the front matter schema in
[`blog_posts/README.md`](../../README.md). The cover image already exists
(`cover.jpg`, beside this folder) and is described at the end of this brief.

---

## 1. Hard constraints, before anything else

Read [`docs/ryan-blog-tone.md`](../../../docs/ryan-blog-tone.md) first. It is the voice
spec and it is enforceable. Its §9 checklist runs directly against `post.md` with no
preprocessing. The four mechanical ones that fail most often:

- **Zero em dashes and en dashes.**
- **Zero exclamation points.**
- **Zero rhetorical questions.**
- **Contractions expanded.** "It is", not "it's".

Beyond the mechanics, the two rules that shape this particular piece:

- **Every strong claim is followed immediately by its limit** (§4.4). This post is about
  volume of work. It will read as bragging unless the caveats in §3 below are in the body,
  not in a footnote.
- **Every number specific and hedged, not rounded up for effect** (§5). The numbers below
  are exact. Do not round 192 to "nearly 200" and do not write "hundreds of commits".

One more, from the repo's own conventions: **a post that has a case study takes the case
study's title, verbatim.** This post has no case study, so the title is open. It is still
worth knowing, because two sibling posts in this folder follow that rule and you may be
asked to match their shape.

---

## 2. The facts, as measured

Window: **2026-07-05 to 2026-08-05**, thirty days ending the day the cover was built.

Method: `git log --all --since` across every repo, grouped where one project spans
several. File counts exclude `node_modules`, `dist`, release runtimes, lockfiles,
minified bundles, and binary assets, so they count files a person actually edited.
"Active days" is the count of distinct calendar days carrying at least one commit.

| Project | Commits | Files touched | Active days | Repos counted |
|---|---:|---:|---:|---|
| SetMaster 3 | 192 | 362 | 11 | `setmaster3` |
| GitHub + Notion SOP | 49 | 70 | 11 | `wp-github-sop`, `wp-notion-team` |
| pdpd | 82 | 709 | 12 | `pdpd-alpha`, `pdpd-shopify-app` |
| Wolfpack website | 169 | 151 | 10 | `wp-website`, `ai-coaching-intake`, `wp-rates-page` |
| AI coaching | 36 | 59 | 4 | `ai-coaching` |

**Total: 528 commits across nine repositories in thirty days.**

### 3. The caveats. These belong in the body

The tone spec requires them and they are also just true.

- **A commit is a unit of bookkeeping, not a unit of value.** SetMaster 3's 192 is partly
  a reporting artifact: its fix rounds run one issue to one branch to one pull request, so
  a round of fourteen small fixes produces at least fourteen commits by design. A project
  worked in larger chunks scores lower for the same effort. Say this plainly.
- **Line counts were deliberately left off the graphic.** Two of these projects had
  one-shot generated builds inside the window, which put insertions into six figures and
  would have made the other three invisible. The number exists and it flatters; it was not
  used. That decision is itself a small point worth one sentence.
- **Thirty days is one month, not a trend.** AI coaching's 36 commits over 4 active days
  is not a decline; it is a product whose work that month happened to be teaching rather
  than committing. Code volume measures code, and most of what that product does is not code.
- **Nine repos, five projects.** The grouping is a judgment call, not a fact. Somebody
  else could reasonably split them differently.

---

## 4. The five projects, in plain description

Use these as source, not as copy. One or two sentences each is all the post can afford.

1. **SetMaster 3** — an offline, single-user web application that replaces an Excel and
   VBA tool used professionally for years for DJ set preparation. Two jobs: a structured
   set editor, and catalog analysis across a Traktor collection and Spotify playlists.
   Currently in post-build fix rounds, tested against a real collection of several
   thousand tracks across 149 playlists. **Do not quote a track count.** The build report
   gives two different figures for the same collection (6,810 in the acceptance run,
   7,033 in its data notes), so either one would be a number you cannot defend if asked.
   The playlist count is consistent in both places.
2. **GitHub + Notion SOP** — not a product. The written operating procedure for how every
   other project is run: branching, commits, pull requests, labels, versioning, releases,
   and the mirror of that in a Notion workspace. It exists as two repos and as installed
   agent skills. It is the smallest project by volume and the one the other four depend on.
3. **pdpd** — a frontend tool for product description page catalogs at the scale of
   millions of pages: find and repair broken pages, generate and test variants, measure
   the result. Currently in research and specification, with a real test suite that stands
   up throwaway Postgres clusters rather than mocking the database.
4. **Wolfpack website** — the public pages. Landing pages, a public rates page, two résumé
   pages, two long-form case studies, a portfolio page, and now blog posts authored in
   markdown and pushed to the blog platform through its API. Static HTML with no build step.
5. **AI coaching** — the coaching product line: curriculum, session material, and the small
   tools built to run it. Mostly not code, which is exactly why its bar is short.

---

## 5. The techniques. This is the real subject of the post

The volume is the hook. The methods are the point. Pick **three or four** of these, not
all of them. Each has a concrete artifact you can point at, which matters because the tone
spec calls for proof by specificity (§4.3) rather than adjectives.

### 5.1 Specification first, and the specification is not rewritten to match the code

SetMaster 3 was built from a complete spec package written before any code: overview, data
model, UI design, and one file per feature, plus a file listing open questions that was
empty at build time. The repo's own instructions state a precedence order for conflicts and
tell the agent that the spec is input, not a mirror of the code. The build prompt says it
in one line worth quoting the sense of: the quality of the spec is the main input to the
build, so ground every feature in its spec file and do not invent product behavior.

### 5.2 A cost-tiered orchestrator, pinned so it cannot drift

The build ran with the expensive reasoning model as **orchestrator only**, and every
sub-agent on a cheaper model. This is the interesting part: a sub-agent inherits the
session model by default, which is the expensive failure mode, so the pinning was done
twice over. Once through an environment variable that sits at the top of the model
resolution order, and again by routing every agent call explicitly in the workflow script.
The prompt then instructs the orchestrator to structure an early cheap slice of work so
the pinning can be verified from per-agent token usage before the bulk of the run spawns.

The generalizable claim: **an instruction that only exists in a prompt is a hope. Pin it at
two levels and give yourself a way to check it early.**

### 5.3 Run hands-off, but log every judgment call

The same build prompt tells the agent to run to completion without checking in, with
exactly one permitted interruption: missing test data. Every decision it makes goes into a
numbered decision log instead of into a question. Build one closed with thirty-one logged
decisions. The round plans go further and separate two categories: **decisions**, which
came from a human and are settled, and **assumptions**, which the agent made and flagged
rather than asked about. Both are in the plan before the work starts.

### 5.4 One issue, one branch, one pull request, and the issue stays open

Every change gets an issue. The pull request references it plainly and is forbidden from
using closing keywords, so merging never closes anything. Instead the issue gets a
`fixed-on-develop` label the moment its pull request merges. That produces two clean
queries: open and unlabeled is the real backlog, open and labeled is the human verification
queue. The invariant is stated: every issue merged is either labeled or closed.

The point for a reader: **merging is not verifying, and the tracker should not pretend
otherwise.**

### 5.5 The gate is different per destination

Into the integration branch, self-merge with no pre-merge review, because the gate is the
full local suite green and stated in the pull request body. Into the release branch, an
external review happens before the merge. One of these projects has real continuous
integration running lint and tests on every pull request, with acceptance tests that stand
up genuine Postgres clusters in throwaway directories. Another has none at all and says so
in its instructions, which is more honest than implying a gate that does not exist.

### 5.6 Guardrails that outlive the session

This is the strongest section if you only pick one.

- **A `CLAUDE.md` in every repo** carrying its hard constraints, its precedence rules, and
  a table of which paths are writable. The reason a fresh session does not have to be
  re-briefed.
- **Skills installed as directory junctions into their source repos**, never as copies. A
  procedure that travels as a copy rots and the machines diverge. A `git pull` is the whole
  sync mechanism.
- **A fact checker rather than a wording checker.** The résumé pipeline has a script that
  asks whether anything on the page is untrue and whether two documents contradict each
  other, and one of its checks reaches into the website's HTML to confirm the project
  blurbs still match the source data. It exists because a correction once landed on the
  pages and not in the source, and nothing could see the gap.
- **Generated artifacts ship with their generator.** The two hero images in this repo,
  including this post's cover, are composed by a committed script from a committed source.
  Rebuild rather than retouch.
- **A deterministic transform instead of hand-pasting.** Blog posts are markdown in git,
  converted to the platform's content format by a tested script that never talks to the
  API. Same markdown always yields the same post, which is what makes re-pushing an edit
  safe. Posts land as unpublished drafts on purpose.

### 5.7 The work is tracked where the work is

Each task in the workspace carries its own status through the run: moved to in-progress
when the agent starts, to a distinct done state that marks it as agent-completed rather
than human-completed, with a comment on every transition. A silent status change is
treated as an incomplete one. The completion gate is objective: every checkbox in the task
body has to be checked, or the task stops short of done and names what is left.

---

## 6. Suggested outline, with word budgets

Total 1000. Adjust the split, not the total.

| § | Section | Words | Must contain |
|---|---|---:|---|
| 1 | **Open cold on the number** | 100 | 528 commits, nine repos, thirty days, five projects. No throat-clearing, no "over the past month I have been busy". Then immediately turn: the number is the least interesting thing here. This is the reversal move (§4.1). |
| 2 | **What the five are** | 150 | One or two sentences each, from §4. Resist explaining any of them fully. The reader needs enough to follow §3 onward. |
| 3 | **What the number does not mean** | 150 | The caveats from §3 above. Commit counts reward small-commit workflows. Line counts were left off on purpose and why. One month is not a trend. Put this early, not at the end, so the rest of the piece is credible. |
| 4 | **The technique that made the volume possible** | 250 | Pick one of §5.1, §5.2, or §5.3. The orchestrator pinning story (§5.2) is the most concrete and the most transferable. Include the two-layer pin and the early verification slice. |
| 5 | **The technique that made the volume safe** | 250 | Pick from §5.4, §5.5, §5.6. The `fixed-on-develop` invariant plus the fact checker is a strong pairing: one says merging is not verifying, the other says a document nobody can check will drift. |
| 6 | **Close on the smallest next step** | 100 | Per tone §7, close on the smallest thing a reader could actually do, then exactly one plainly labeled call to action. Candidate smallest step: write the constraints file for one repo you already have. Do not close on a summary of the post. |

**One reversal is required somewhere** (§4.1), and the natural one is §1 into §3: the post
looks like it is about output and is actually about the guardrails that let output be
trusted. **At most one fragment triple** in the whole piece (§4.2).

---

## 7. Traps

- **Do not let it become five mini case studies.** The projects are the setup. If §2 runs
  past 200 words the post has no room for its actual subject.
- **Do not name a client, and do not invent a testimonial.** Standing rule across every
  page in this repo.
- **Do not claim the AI wrote it all, and do not claim it wrote none of it.** The accurate
  framing is that a human wrote the specification and the rules, and agents did the
  implementation inside them. The decision logs and the human verification queue are the
  evidence that the boundary is real.
- **Do not describe the tooling by brand-name feature.** Describe what the constraint does.
  A reader on different tools should still be able to use §5.
- **Avoid the reject list in tone §6.** Check it before you file.

---

## 8. The cover image, for reference and for the alt text

`cover.jpg`, 1200 x 675. Five constellation glyphs stand in a level row, one per project,
each above a column of light whose height is that project's commit count, read against a
labelled axis that tops out at 200. The glyphs are built the same way the Wolfpack logo is,
from nodes and connecting segments with four-point stars, so the marks and the brand mark
are one family. Navy field, one coral rule at the deck baseline.

The glyphs mean specific things and you may use them in the copy: SetMaster 3 is two
program lines crossing at a transition; the SOP is a branch and a document with the bright
node on the link between them, because the procedure is the thing that was built; pdpd is a
lattice fading past the frame with one page lit; the website is three stacked plates; AI
coaching is one source radiating to a cohort chained to each other.

`cover_alt` needs writing. Describe it plainly for a screen reader, per the front matter
schema. Do not put the numbers in the alt text; put them in the body where they can be read.

---

## 9. Source files, if you want to go deeper

| Topic | File |
|---|---|
| Voice spec and pre-ship checklist | `docs/ryan-blog-tone.md` |
| Front matter schema, push procedure | `blog_posts/README.md` |
| Spec-first build, precedence rules | `setmaster3/CLAUDE.md`, `setmaster3/planning/` |
| Orchestrator pinning, hands-off policy | `setmaster3/prompts/fable-workflow-prompt.md` §0 |
| Decision log, acceptance evidence | `setmaster3/build-notes/final-report.md` |
| Decisions vs flagged assumptions | `setmaster3/build-notes/v3.0.3-round1-plan.md` |
| Branching, labels, versioning | `wp-github-sop/docs/sop/` |
| Task status lifecycle, comments | `wp-notion-team/docs/notion-sop/` |
| The fact checker | `ryan-resume-dev/resume_build/verify_facts.py` |
| The cover generator | `blog_posts/2026-08-05-five-projects/planning/build_cover.py` |
