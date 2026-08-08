---
title: The Engineering System Behind AI Assisted Development
slug: engineering-system-behind-ai-assisted-development
excerpt: Five projects across nine repositories took 528 commits between July 5 and August 5, 2026. The number is the least interesting part of the story, and the engineering system that made that output reviewable is the useful subject.
cover: cover.jpg
cover_alt: Five constellation glyphs stand in a level row on a dark navy field, one for each project, each above a vertical column of light whose height shows that project's commit count against a labelled scale.
date: 2026-08-05
tags: [AI engineering, engineering leadership]
featured: false
---
528 commits. Nine repositories. Thirty days. Five projects.

That is the headline number from the work I completed between July 5 and August 5, 2026.

It is also the least interesting part of the story.

The useful subject is the engineering system that made that level of AI assisted output understandable, reviewable, and safe enough to trust.

I built these projects personally, using Claude and OpenAI agents as implementation partners. I wrote the specifications, defined the operating constraints, made the architecture decisions, and reviewed the results. The agents increased my execution capacity, but they did not replace engineering judgment.

## Five Projects, Not Five Case Studies

SetMaster 3 is an offline, single user web application that replaces an Excel and VBA system I used professionally for DJ set preparation. It combines a structured set editor with catalog analysis across a Traktor collection and 149 Spotify playlists.

The GitHub and Notion SOP is the operating procedure behind the other projects. It defines branching, pull requests, labels, versioning, releases, task states, and the relationship between code work and its operational record.

pdpd is a product description page system designed for catalogs that may contain millions of pages. Its test suite uses temporary Postgres clusters rather than pretending the database boundary does not matter.

The Wolfpack website includes landing pages, public rates, resumes, case studies, portfolio material, and a markdown based blog publishing system. The site remains deliberately simple, with static HTML and no build step.

AI coaching contains curriculum, session material, and the small tools that support delivery. Much of its real work happens in teaching rather than in code.

> **SetMaster 3 in depth:** read the [case study](https://intake.wolfstrategyllc.com/setmaster3-case-study/), or download the application from its [public repository](https://github.com/wolfpackdata/setmaster).

## What 528 Commits Does Not Mean

A commit is a unit of bookkeeping, not a unit of value.

SetMaster 3 produced 192 commits partly because its repair workflow uses one issue, one branch, and one pull request for each fix. Fourteen small fixes therefore create at least fourteen commits by design. Another project may carry the same effort in larger batches and report a much smaller number.

I also left line counts out of the comparison. Two projects included generated builds that pushed insertions into six figures. The number was real, but it would have flattered those projects while making the others nearly invisible.

Thirty days is one month, not a trend. AI coaching recorded 36 commits across four active days because the work that month was mostly live teaching. Code volume measures code, not the full value of a product whose primary output is human capability.

Even the grouping requires judgment. Nine repositories became five projects because several repositories serve one operating system. Somebody else could reasonably divide them another way.

The number is useful only after its limits are stated.

## The Technique That Made the Volume Possible

The most transferable technique was a cost tiered orchestration model with explicit controls against model drift.

The expensive reasoning model acted as the orchestrator. It interpreted the specification, divided the work, ordered dependencies, and evaluated results. Subagents handled narrower implementation tasks on a less expensive model.

A hidden failure mode sits inside that structure. A subagent may inherit the parent session model by default. Without a hard control, the workflow can quietly run every task on the expensive model and erase the economics that made the architecture worthwhile.

I pinned the subagent model at two levels.

First, an environment variable sat at the top of the model resolution order. Second, every agent call in the workflow routed explicitly to the intended model. The instruction therefore existed both outside the prompt and inside the execution path.

The workflow also began with a small, inexpensive slice of work. I inspected per-agent token usage before allowing the bulk of the run to spawn. That early check converted an assumption into evidence while the cost of being wrong was still low.

An instruction that only exists in a prompt is a hope. The limit is that duplicated controls still need observation. A durable workflow puts the constraint in more than one layer and creates an early way to prove that it is holding.

## The Techniques That Made the Volume Safe

Speed became useful only after the verification system caught up with it.

Every change begins as an issue. Each issue receives its own branch and pull request. The pull request references the issue, but it does not close it when merged.

Instead, a merged change receives a `fixed-on-develop` label. Open and unlabeled issues are the development backlog. Open and labeled issues are waiting for human verification.

Merging is not verifying. The limit is that this workflow creates more bookkeeping than a lightweight project may need. For these projects, the separation is worth it because a passing test suite cannot prove that the product feels correct in real use.

The same principle appears in a fact checker I built for resume and website content. It does not review style. It asks whether statements are true and whether related documents contradict each other. One check reaches into the website HTML and compares project descriptions with their source data.

That tool exists because a correction once landed on the published pages but not in the source. The pages looked right, but the system had begun to drift.

A document that no process can verify will eventually become unreliable. Automated checks only catch the contradictions they were designed to inspect. Human review still owns meaning, context, and judgment.

Each repository also carries a constraints file that defines precedence rules, writable paths, and hard boundaries. A new agent session can enter the project without depending on my memory of the last session. The file does not eliminate mistakes, but it makes the operating assumptions visible and testable.

## Start With One Constraints File

The smallest useful version of this system is not a multi-agent build.

It is one constraints file in one repository you already use.

Write down what the project is, which source wins when instructions conflict, which paths may be changed, how tests are run, what counts as complete, and which decisions require human verification.

That file will not create 528 commits. It will make the next commit easier to trust.

For CTOs and engineering leaders, that is the opportunity in AI assisted development. The goal is not to remove engineers from the loop. The goal is to move engineering judgment into specifications, controls, tests, and verification systems that allow more implementation work without losing accountability.

[Contact Wolfpack](https://www.wolfstrategyllc.com/contact-3)
<!--
Wix draft post id: a40dfc18-fd60-4353-9a4d-c7a043dc77b7
Pushed 2026-08-05 as an unpublished draft. To update rather than duplicate,
PATCH /blog/v3/draft-posts/a40dfc18-fd60-4353-9a4d-c7a043dc77b7.

Tag ids used for this post:
  AI engineering          1e614466-776a-4b7e-9fa8-5da9e3eee0f3  (already existed)
  engineering leadership  cc7c1304-6a3f-4aa3-b6f6-4518ee1ef4ed  (created for this post)

Cover media id: e00ee6_b8ba03000f854c46b39428b97b29f908~mv2.jpg
Uploaded via generate-upload-url + PUT; returned hash matched the local
cover.jpg md5 (6df37b7c83d6d30c41b79659c1a4d760), 1200x675, 83,739 bytes.
-->
