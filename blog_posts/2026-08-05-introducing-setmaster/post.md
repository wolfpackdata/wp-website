---
title: Introducing the SetMaster Application
slug: introducing-the-setmaster-application
excerpt: An offline set preparation and catalog analysis app for Traktor. One row is one transition, read left to right. It runs on your machine, reads your collection strictly read-only, and never phones home.
cover: cover.png
cover_alt: The SetMaster 3 set editor, showing a magenta OUT TRACK column group beside a cyan IN TRACK group, with BPM, key, level, and mix notes across each transition row.
date: 2026-08-05
tags: [DJ tools, music technology]
featured: false
---

Every DJ tool I have used lists tracks top to bottom, one track per row. That is a library view. A library view is not a plan.

SetMaster 3 reads left to right. Out track on the left, in track on the right, and everything you decided about the move between them in the columns after it. Where you leave, where you land, what you do in the middle.

It shipped publicly on 2026-07-31, it is free, it is MIT licensed, and it runs entirely on your own machine.

## One Row Is One Transition

That is the whole idea, and the rest of the app falls out of it.

A row carries the BPM and key on both sides, your cue numbers, whether the lows get cut or left open, the level you are launching into, and your own notes for the move. Format cells RED, YELLOW, or boxed by hand. Mark tracks with an emoji palette you define yourself. A mix timer tells you how long each section runs and how long the whole set does.

Export the finished set to CSV, XLSX, or Markdown when you want it somewhere else.

None of that requires a collection. Set preparation stands alone, and Traktor® is never a prerequisite.

## Your Catalog, Queryable

The optional half loads your Traktor® collection and cross-references it against Exportify CSVs of your Spotify® playlists. Compound filter and sort across everything at once, past what Traktor® itself will do, which is the part that turns forty minutes of digging into one pass.

The comparison is the useful direction: what you have been listening to, held against what you do not own yet. Notes you write in the blank cells survive every re-run, because a snapshot merge puts them back.

No Spotify® API, no accounts, no cloud, no telemetry, no external calls of any kind. Your `collection.nml` is opened strictly read-only and never written.

## For the Engineers

FastAPI and a Python pipeline behind React 18, Vite, and TypeScript. 206 backend tests, 624 frontend, 37 end to end.

The interesting constraint was the port. Version two carried years of accumulated matching and normalization logic, every rule of it a bug hit during real work. So restructuring the stages was allowed and changing the behavior was not. The ported pipeline runs against a real 6,810 track collection and its output is compared to the old engine's byte for byte. Anything that changes the result fails the build, including changes that look like improvements.

The release bundles its own relocatable CPython. No Python install, no Node, no terminal. Double click a launcher and the UI opens in your browser on localhost.

Public repo, sha256 published with the release.

## What Is Not Ready

Windows is available now. The Mac build is written and structurally fixed, and it is waiting on a Mac to build and verify it. Rekordbox® import is planned with no timeline. Perform Mode and the natural language filter bar are specified and deferred, not abandoned.

SetMaster 3 contains no AI. It was built with it, which is a different claim.

Three years of professional use since 2023, three rebuilds, and it is still the thing I open before a gig.

**[Get SetMaster 3](https://intake.wolfstrategyllc.com/setmaster3/)**

*SetMaster 3 is independent fan software and is not affiliated with, endorsed
by, or sponsored by Native Instruments®, Spotify®, or Exportify.
Traktor® is a registered trademark of Native Instruments GmbH. Spotify® is a
registered trademark of Spotify AB.*

<!--
NOT PUSHED TO WIX. Authored only, per Ry (2026-08-05). No draft post id exists
yet, so the first push is a POST to /blog/v3/draft-posts, not a PATCH.

TWO THINGS TO SETTLE BEFORE PUSHING:

1. The CTA is dead today. https://intake.wolfstrategyllc.com/setmaster3/ is
   unbuilt and 404s (#85, #86; sm3-specific-pages/README.md). The sibling post
   was held from the push for exactly this reason once already, when its case
   study was still undeployed, and went up only after #108 made the page return
   200. Same gate applies here.
2. Ry's brief says the landing page will carry downloads and install
   instructions for BOTH platforms. Claims ledger C-03 is a hard rule against
   claiming macOS until a Mac artifact exists, so this post says "Windows is
   available now" and describes the Mac build as waiting. When the Mac artifact
   ships, that paragraph is the line to update.

TITLE is Ry's, given verbatim in the brief. The README's rule that a post
carries its case study's title does not bind here: this is a product
introduction pointing at the landing page, not the case-study post. That post
already exists as 2026-08-04-build-fast-thinking-finished and carries the case
study's h1. Two posts, two jobs, deliberately different titles.

ONE CTA, ONE DESTINATION, and no intro call anywhere in the body (Ry,
2026-08-05). This deliberately breaks with the sibling post, whose CTA is the
calendar. The case study is not linked either, so the landing page is the only
way out of this post; its origin band carries the case-study link.

EVERY FACTUAL CLAIM traces to sm3-specific-pages/planning/04-claims-ledger.md
section 1. Nothing new is asserted here. Specifically:
  read-only collection.nml, offline, no telemetry . product table
  set prep stands alone, Traktor never a prerequisite . product table, binding rule
  RED / YELLOW / box, emoji palette, mix timer, CSV/XLSX/Markdown . product table
  compound filter and sort beyond Traktor, notes survive re-run . product table
  file-based Spotify via Exportify, no Spotify API . product table
  bundled CPython, no Python/Node/terminal, double-click launchers . product table
  206 / 624 / 37 tests . build table (867 total, stated as its parts here)
  golden-master byte-identical port . build table
  6,810 tracks . build table (Build #1 acceptance collection)
  first public release 2026-07-31, MIT, sha256 . build table
  three years of professional use since 2023 . C-07
  Windows now / Mac waiting . C-03, phrased in its approved form
  Rekordbox planned, Perform Mode deferred . history table
  "contains no AI, built with it" . prohibitions table, the easiest mistake to make

TRADEMARKS per sm3-specific-pages/README.md: every visible Traktor, Native
Instruments, and Spotify carries the registered mark, Exportify renders plain,
and the unaffiliated line ships with any public page naming them.

COVER is sm3-assets/img/a02-set-editor.png resized to 1200px wide and
palette-quantized to 256 colors, 145 KB. Deliberately a different capture from
the sibling post's Track-Playlist Matrix, since the two posts run days apart.
Checked before use: the capture shows track and set names only, no filesystem
paths, unlike the A-08 original that is gitignored for leaking a Windows user
directory.

TONE follows docs/ryan-blog-tone.md. Section 9 checked and clean: 0 em dashes,
0 en dashes, 0 exclamation points, 0 question marks, 576 words. The one
apostrophe in the body is the possessive "the old engine's", not a contraction,
so the post is stricter on that rule than the sibling SetMaster post, which
shipped with several. The section 4.1 reversal opens the post, in the form the
landing page spec already approved for its transition-row band.
-->
