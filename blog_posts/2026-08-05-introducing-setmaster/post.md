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

FastAPI and a Python pipeline behind React 18, Vite, and TypeScript. 236 backend tests, 624 frontend, 37 end to end.

The interesting constraint was the port. Version two carried years of accumulated matching and normalization logic, every rule of it a bug hit during real work. So restructuring the stages was allowed and changing the behavior was not. The ported pipeline runs against a real 6,810 track collection and its output is compared to the old engine's byte for byte. Anything that changes the result fails the build, including changes that look like improvements.

The release bundles its own relocatable CPython. No Python install, no Node, no terminal. On Windows you double click a launcher. On macOS you open the app from Applications. Either way the UI opens in your browser on localhost.

Public repo, MIT licensed, every release and artifact listed on GitHub.

## What Is Not Ready

Windows and macOS are both available now. The Mac build arrived on 2026-08-05 as a signed, notarized app inside a disk image: drag it to Applications and open it, with no terminal and no security detour. It needs Apple silicon and macOS 14 or later, and Intel Macs are not supported. The end to end suite and the golden master pipeline tests have never been run on macOS, and the Mac artifact passed its own clean install check instead. Rekordbox® import is planned with no timeline. Perform Mode and the natural language filter bar are specified and deferred, not abandoned.

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

BOTH PRE-PUSH ITEMS ARE NOW CLEARED (2026-08-05, #144). The post is ready to
push whenever Ry wants it; it stays unpushed only because he has not asked.

1. THE CTA IS LIVE. /setmaster3/ deployed to ai-coaching-intake on 2026-08-05
   and returns 200. The gate that held this post, and held the sibling post
   before it until #108, is satisfied.
2. TEST COUNTS ARE REAL NOW. "For the Engineers" carries 236 / 624 / 37 from
   the v3.0.4 release-unblock report's final gate, run with the golden-master
   suite active, replacing the v3.0.3 figures of 206 / 624 / 37. The total is
   897, and the landing page (two places) and the case study (one) were moved
   to it in the same pass, which is what "all four move together" required.

SHA-256 CLAIM RETRACTED 2026-08-05 (Ry's ruling, #144). This paragraph used to
end "Public repo, sha256 published with the release." Checked against the live
release before deploying: v3.0.4 publishes no checksum, in its notes or as an
asset. The claim was true enough of v3.0.3, whose notes mentioned one, which is
how it survived into copy. Five other places said the same thing and all six
came out together. Do not restore it until a release actually publishes hashes.

SETTLED 2026-08-05: macOS. This note previously held item 2 open on C-03, the
hard rule against claiming macOS before a Mac artifact existed. v3.0.4 met that
condition: SetMaster 3 was built and acceptance-tested on a Mac and ships as a
signed, notarized .app inside a .dmg. "What Is Not Ready" now says both
platforms are available and carries the narrower limits that replaced the old
claim: Apple silicon, macOS 14 or later, no Intel, and suites never run on
macOS. Do not round that up to plain "macOS support" in a later edit.

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
  236 / 624 / 37 tests . build table (897 total, stated as its parts here),
    from the v3.0.4 release-unblock report's final gate. Was 206/624/37=867,
    the v3.0.3 figures, until #144.
  golden-master byte-identical port . build table
  6,810 tracks . build table (Build #1 acceptance collection)
  MIT license . build table (re-verified via the license API 2026-08-05)
  releases and artifacts public on GitHub . NOT a checksum claim, see C-11
  three years of professional use since 2023 . C-07
  Windows and macOS both available . v3.0.4 changelog and fix report, with
    C-03 narrowed rather than lifted: Apple silicon, macOS 14 or later, no
    Intel, suites never run on macOS
  signed, notarized .app inside a .dmg . v3.0.4 changelog, issue #214
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
