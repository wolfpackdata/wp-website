---
title: Nobody Reads the Sign
slug: nobody-reads-the-sign
excerpt: "There is a speed limit sign on my street. There is also a speed bump. Only one of them has ever changed how anybody drives. I spent two weeks turning our GitHub process from the first thing into the second, because most of the commits in my repositories are now written by AI agents, and an agent can merge a pull request faster than I can read the diff."
cover: cover.jpg
cover_alt: PLACEHOLDER — replace when the hero lands.
date: 2026-09-05
tags: [AI engineering, engineering leadership, governance, process]
featured: false
---

There is a speed limit sign on my street.

There is also a speed bump.

Only one of them has ever changed how anybody drives.

I have been thinking about that distinction for two weeks, because most of the commits in my repositories are now written by AI agents, and I had a process document that was very much a sign.

## The thing about a document is that it is a suggestion

An AI agent can open, implement, review, and merge a pull request in the time it takes a person to read the diff.

That is genuinely useful. It is also the whole problem.

Speed is only worth having if three things stay true: work is **attributable** to a named actor, changes are **reversible**, and the rules an agent follows are the same rules on every machine and in every session.

An ordinary process document fails all three the moment the agent is faster than the person reading it. Because a document nobody re-reads is a suggestion.

I had written a good one. Ten rules, clear headings, examples. It was correct. It was also, functionally, a laminated sign on a wall that agents drove past at speed.

## So I built the speed bumps

The standard operating procedure that governs my 36 repositories is still written down. That part did not change.

What changed is that it is now **loaded into the agent, guarded in the session, checked on the forge, and enforced by branch rulesets.** Four layers, each catching what the one before it cannot.

**Loaded into the agent.** The rules are packaged as skills that load automatically when a session touches the relevant work, so nobody has to paste the SOP into a prompt and hope. They are linked into each machine rather than copied, because a copy rots and a link stays in lockstep through `git pull`.

**Guarded in the session.** Hooks refuse the call. Try to commit to `main` and it does not go through. Try to write to Notion before the session has proved which account it is acting as and it does not go through. These are forcing functions, not security boundaries, and the honest claim is small: they turn "remember to check" into "the call does not complete until you have."

**Checked on the forge.** Every issue carries acceptance criteria and a verification plan, so "done" is testable by someone other than the author. Workflows label the issues a merge references, so the verification queue is maintained by a machine instead of by an agent remembering.

**Enforced by branch rulesets.** Organization-level rules requiring pull requests, one Code Owner approval into `main`, squash-only into `develop`, no force-push. This is the actual speed bump. Not memory, not etiquette — the forge simply declines.

## The rule I would keep if I could only keep one

The reviewer and the implementer are different accounts, on different models, in different repositories.

Claude Code implements, under my own GitHub identity, and never merges to `main`, never closes an issue, never confirms its own version bump.

Codex reviews, under its own GitHub account, with its own permissions, submitting an actual verdict.

The same session can never both write the code and sign it off.

That is the property that makes an AI-reviewed merge mean anything at all. Everything else in the SOP is plumbing around it. Two accounts, or the review is a model reading its own work and telling you it looks great.

No agent graded its own homework at any point in the two weeks.

## The numbers, since you will ask

Between August 22 and September 5: 82 pull requests merged, 55 issues closed, 10 open and triaged, four releases, and 36 repositories brought to one baseline.

One number I like more than any of those: the automation now lives in **one** copy of each workflow, reached by 32 repositories through an eleven-line stub pinned to a tag. Changing the fleet is one edit and a tag move.

It used to be a 32-repository sweep with 32 reviews. That is the kind of arithmetic that quietly decides whether you ever improve anything.

And one I like even more: the weekly fleet audit says **nothing** when the fleet is clean.

A weekly all-clear email is right 51 weeks a year, which trains its reader to close the 52nd one unread. Silence when healthy is not a missing feature. It is the feature.

## Now the part where I tell you what broke

A process write-up that records only successes is a brochure.

Three things went wrong, and all three are filed as issues with a decision attached, because that is supposed to be the normal operation of the system rather than an embarrassing exception to it.

**The merge gate had not been enforcing.** Mid-round it turned out the required check could be satisfied in a way that let merges through. Seven merges record a bypass. The fix landed inside the same round, and every merge after it records a clean pass. The round report leads with this rather than with a feature list, which felt bad to write and was obviously correct.

**A release merged to `main` before its mandatory review existed.** Raised as an issue, ruled on, recorded. Not quietly corrected at two in the morning.

**A labeling workflow marked an issue fixed that had only been referenced.** The convention gap is filed and open rather than patched invisibly.

I am not listing these because confession is fashionable. I am listing them because "we built a governance system" is an unfalsifiable claim, and "here are the three times it failed and what we did" is not.

## What this is actually for

If you are evaluating anyone's AI-assisted delivery — mine included — the useful questions are not about model choice.

They are: *can you tell who did what, can you undo it, and does the process hold when nobody is watching?*

Which model wrote the function is close to irrelevant. Whether there is an attributable actor on every change, a reversible path for every merge, and a reviewer who is structurally incapable of being the author is the entire question.

The sign on my street still says 25.

The speed bump is the reason anybody drives 25.

<!--
Draft 2 — the five-minute read, for Ry's comparison against draft 1 (post.md).

  - Target was 1,000-1,300 words. Written to the tone of
    blog_posts/2026-08-26-applied-ai-engineer/post.md: first person, short
    paragraphs, a running physical analogy, dry rather than jokey, headings that
    are sentences, and the argument carried by structure instead of by a summary.
  - EVERY fact traces to planning/source-report.md. The speed limit / speed bump
    frame, the laminated sign, and the brochure line are the only additions, and
    all three are figures of speech rather than claims. No figure was changed and
    no outcome was invented.
  - Cut from draft 1, deliberately, to make the length: the ten rules as a list,
    the role table, the six risk tiers, the skill and hook inventories, the nine
    scripts, the per-release history, and the v1.5.0 plan. What survives is the
    argument — sign versus speed bump, two accounts, the numbers, the failures.
  - Same Wix constraints as draft 1: no tables, no nested lists, every list item
    on one line, and backticked names render as plain text.
  - Title, slug, excerpt and tags are PROVISIONAL. This draft's title and slug
    differ from draft 1's on purpose — pick one draft, and its front matter
    travels with it.

To promote this draft: replace post.md with this file's contents. Nothing else
in the folder or the ledger assumes which one wins.
-->
