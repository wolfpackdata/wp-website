---
title: The Build Was Fast Because the Thinking Was Finished
slug: the-build-was-fast-because-the-thinking-was-finished
excerpt: Twenty-five days from specification to public release, with zero deviations from a written model policy. The speed is not the interesting part. The reproducibility is.
cover: cover.png
cover_alt: The SetMaster 3 Track-Playlist Matrix, showing a filtered track catalog with BPM, key, and playlist membership columns.
date: 2026-08-04
tags: [AI engineering, case study]
featured: false
---

Before any application code existed, Claude and I spent several days on planning
documents. An overview, a data model, an interface specification, ten feature
specifications, a decision log, and an open questions document closed to zero.

The instruction to the agent doing the build is one sentence.
The specification is complete and decided, and the job is to implement it, not
to re-litigate it.

Twenty-five days from specification to public release, 74 issues across four
build rounds, 867 automated tests passing.

The speed isn't the interesting part. The reproducibility is.

## Porting Logic You Cannot Afford to Change

The application is SetMaster 3, which reads a Traktor® collection strictly
read-only and cross-references it against Spotify® playlists. It's the third
version of a tool I first built as a spreadsheet in 2023.

Version two grew a Python data engine carrying years of accumulated fixes in its
matching and normalization logic. Track name cleaning, playlist name
normalization, filename normalization, key mapping. Every one was a bug I hit
and corrected while doing real work.

So the rule for the rebuild was that restructuring the stages was allowed and
changing the matching behavior was not. A rule like that is worth nothing unless
it can be checked, so the ported pipeline runs against my real collection and
its output is compared to the old engine's, byte for byte. Anything that
changes the result fails the build, including changes that look like
improvements.

The result isn't that the port is probably correct. It's that the port produces
the same bytes.

## Cost Tiering, Written Down First

The build was cost-tiered on purpose, and the policy was written down before it
started rather than justified afterward. One orchestrating agent on the frontier
model. Every sub-agent on Opus. No frontier sub-agents at all. It was enforced
two ways, by an environment variable and a per-call model pin, with zero
deviations.

Thirty-one build decisions were logged with their reasoning as they were made.
Anyone can get an application out of a model once. The harder thing is being
able to say why it came out the way it did, and this one can, 31 times over.

That's a claim about the process, not about the code being defect free. Three
hardening rounds came after build one for a reason. Windows is verified end to
end and macOS is not, because no build has ever run on a Mac, so the release
ships Windows only.

## Where to Start

If you're planning a build with AI in it, the first step isn't picking a model
or a framework. It's finishing the specification, so what you hand the builder
is a decision instead of a conversation.

The full write-up covers the transition row idea the tool is built on, the four
hardening rounds, and how a private repository holding my whole music library
gets mirrored publicly without leaking it.

[Read the case study](https://intake.wolfstrategyllc.com/setmaster3-case-study/)

SetMaster 3 does not contain any AI. It was built with it.

**[Work With Wolfpack](https://calendar.app.google/zHNd1NA9wzb4VRLw5)**

*SetMaster 3 is independent fan software and is not affiliated with, endorsed
by, or sponsored by Native Instruments®, Spotify®, or Exportify.
Traktor® is a registered trademark of Native Instruments GmbH.*

<!--
HELD FROM THE WIX PUSH. The case study this links is noindex, nofollow and is
not deployed yet (wp-website#88, #89), so the link 404s today. Push this post
only after that page is live. See wp-website#102.

Trademark discipline is inherited from the SetMaster 3 pages: every visible
Traktor / Native Instruments / Spotify carries the registered mark, Exportify
renders plain, and the unaffiliated line ships with any public page naming them.
-->
