---
title: "SetMaster 3 Is Live: The Traktor® Set-Prep Tool I Built for Myself"
slug: introducing-the-setmaster-application
excerpt: SetMaster 3.0.4 is live for Windows and macOS, and installation is now drag-and-drop on both platforms. A local, offline desktop application for preparing DJ sets and analyzing a Traktor® collection. Less scrolling. More mixing.
cover: cover.png
cover_alt: The SetMaster 3 Track-Playlist Matrix, showing 178 of 3,604 tracks across 5 of 83 playlists, with BPM range, key, and release year filters applied in the panel on the right.
date: 2026-08-06
tags: [DJ tools, music technology]
featured: true
---

It’s up.

SetMaster 3.0.4 is officially live for Windows and macOS, and installation is now drag-and-drop on both platforms.

No separate Python installation. No Node. No terminal commands. No setup ritual that begins with “first, open PowerShell” and ends with a musician reconsidering every decision that led them here.

Download it, open it, and start exploring your music.

SetMaster is a local, offline desktop application for preparing DJ sets and analyzing a Traktor® collection. It helps you explore, compare, filter, and organize your library without ever writing to Traktor®’s `collection.nml`.

I think of it as a set-preparation copilot:

**Less scrolling. More mixing.**

[Visit the SetMaster 3 page to see the features and download the application.](https://intake.wolfstrategyllc.com/setmaster3/)

## I Built the Tool I Actually Needed

I wanted to build an application that was not fintech, business intelligence, operations software, or another tool designed to help an executive look at a dashboard before asking why a number is red.

I wanted to learn new skills, get outside my comfort zone, and build a product I genuinely needed.

That product became SetMaster.

I have been DJing and producing music for a long time. Long enough to have developed a deep catalog, a fairly refined sense of what works in a set, and the unfortunate awareness that maintaining a serious music collection can become its own unpaid administrative position.

There is not much money in spending three hours preparing an exquisitely tuned transition between two records that twelve people may hear at 1:17 a.m.

There is, however, considerable satisfaction in it.

My collection has accumulated across years of gigs, digging, playlist building, production work, genre detours, abandoned set concepts, successful set concepts, and tracks I was absolutely certain I would remember without organizing properly.

I did not remember them.

The problem was no longer finding music. I had plenty of music.

The problem was getting from an idea in my head to the right group of tracks without repeatedly browsing the same playlists, opening the same folders, and relying on memory to reconstruct connections I had already discovered before.

That is the problem SetMaster solves.

## The Track–Playlist Matrix

The feature I use most is the **Track–Playlist Matrix**.

It puts every track against every playlist and lets me see where a selected track appears across my collection.

That sounds simple until your Traktor® library contains years of music spread across genre playlists, gig folders, set drafts, seasonal collections, reference lists, works in progress, and categories whose original logic is now known only to a younger version of yourself.

Select a track, and SetMaster instantly shows every playlist containing it.

That creates several useful paths through the library.

I can see which musical ideas I have already associated with the track. I can find overlapping set concepts. I can identify tracks that belong in several parts of my catalog. I can also spot music that exists in the collection but was never properly organized into playlists.

The matrix currently handles thousands of tracks across dozens of playlists, turning the collection into something that can be examined as data rather than browsed one folder at a time. The SetMaster landing page shows an example with 3,604 tracks across 83 playlists.

For me, this changes set preparation from filing paperwork into treasure hunting.

I select one track, find an old playlist, rediscover three records I forgot I owned, notice a possible transition, and suddenly “I’ll prepare a quick set” has become a three-hour archaeological expedition through dance music.

At least it is all in tune.

## Compound Filtering for Real Set Preparation

SetMaster also lets me filter the entire Traktor® collection using several dimensions at once.

I can combine:

- BPM ranges
- Musical keys
- Release years
- Playlist membership
- Other catalog fields

The important phrase is **at once**.

A DJ is rarely looking for “all tracks at 124 BPM” in isolation. The useful question is closer to:

> Show me tracks between 122 and 125 BPM, in compatible keys, from these playlists, within this release period.

That is how you find the record that bridges two sections of a set.

It is how you find potential mashups.

It is how you discover that a transition you have been trying to force would be much easier if you simply moved one track twenty minutes later and used something better in between.

Traktor® is excellent software for performing, organizing, and managing a collection, but SetMaster approaches the catalog from a different angle. It turns the collection into something queryable, with compound filtering across BPM, key, release year, and playlist membership.

The result is less time repeatedly rebuilding searches and more time thinking about the musical movement of the set.

## Comparing Playlists Against What I Own

Another major workflow is playlist comparison.

I use Spotify® as one part of music discovery and Traktor® as the home of the local collection I perform with. The annoying question between those two systems is:

> Of everything I have been listening to, which tracks do I already own, which ones still need organizing, and which ones do I need to buy?

Before SetMaster, that question involved more manual checking than it deserved.

SetMaster imports exported Spotify® playlist data and compares it against the local Traktor® collection. Each result can be classified as:

- **Go get**
- **Match**
- **Organize**
- **Traktor® only**

Notes persist when the comparison is run again, so the workflow does not reset every time the source data changes. The application does this through local files rather than a Spotify® API connection, which keeps the workflow offline and avoids sending collection data elsewhere.

The output is not another giant music list.

It is a shorter, actionable list of tracks that require attention.

That matters because acquiring music is the enjoyable part. Reconciling three different lists to determine whether I already bought a track is less artistically nourishing.

## One Row Is One Transition

SetMaster did not begin as a catalog-analysis application.

The original idea was a set editor built around a simple principle:

**One row is one transition.**

Most playlist interfaces display tracks vertically, one after another. That works well for showing order, but it does not fully describe what happens between two tracks.

A DJ transition has two sides:

- The track you are leaving
- The track you are entering

Between those two points are the actual performance decisions: timing, EQ movement, gain changes, hot cues, loops, tempo adjustments, and the notes you need to see while playing.

SetMaster reads that relationship from left to right.

The editor provides space for track order, hot-cue numbers, EQ and level moves, timing, formatting, and transition notes. It also includes a mix timer and exports sets to CSV, XLSX, and Markdown.

This is how the application grew from “a better set spreadsheet” into a larger system for preparing music.

The first version was a Google Sheet, then an Excel workbook. SetMaster 2 added VBA and Python, turning the Traktor® collection into structured data. SetMaster 3 rebuilt the concept as a complete local application.

The workflow has been in professional use since 2023, including in my own gigs.

I say that humbly because DJing is a strange profession in which decades of musical experience can culminate in someone asking whether you brought your own table.

Still, building and testing this against real sets matters. SetMaster did not emerge from a hypothetical product exercise about how DJs might work. It came from preparing and performing actual music, noticing repeated friction, and gradually turning those problems into software.

## The Collection Is Strictly Read-Only

One architectural decision was non-negotiable:

SetMaster does not write to Traktor®’s `collection.nml`.

It opens the collection strictly read-only. That is not a checkbox or user preference. It is an architectural constraint.

A DJ collection is too important to treat casually.

It may contain years of playlists, cue points, metadata, organization, and performance history. SetMaster is designed to analyze that collection, not modify it behind the scenes.

The application creates its own sets, notes, settings, comparisons, and derived data separately.

Your Traktor® collection remains yours.

## Local Software, Packaged Like Actual Software

One of the largest engineering challenges was not the filtering logic or the data pipeline.

It was packaging a local Python application so it behaved like a proper desktop product.

A developer can tolerate instructions involving virtual environments, package managers, environment variables, and command lines. A DJ who wants to prepare Saturday’s set should not need to become an adjunct DevOps engineer first.

SetMaster uses a local Python process with a browser-based interface running on `localhost`. There are no cloud accounts, no telemetry, and no external application calls.

Each release includes its own bundled CPython runtime, so the user does not need to install Python, Node, or any supporting development tools.

On macOS, SetMaster now ships as a proper DMG:

1. Open the disk image.
2. Drag SetMaster into Applications.
3. Launch it like another Mac application.

The application is signed with Wolfpack’s Apple Developer ID, notarized by Apple, and stapled so Gatekeeper can verify it normally. The current Mac release supports Apple silicon running macOS 14 or later.

That may sound like routine packaging if you primarily use large commercial applications.

For an independently developed local Python application, getting from “the code runs” to a signed, notarized, self-contained DMG is a substantial part of building the product.

There is a long stretch of engineering between:

> It works on my machine.

and:

> Another person can download it without installing six dependencies and believing in themselves.

## Building It With Claude and Codex

Claude and Codex were both deeply involved in the SetMaster 3 development process.

I used them throughout:

- Product specification
- Architecture
- Implementation
- Debugging
- Test design
- Refactoring
- Packaging
- Documentation
- Release preparation

That does not mean turning over engineering judgment to a chatbot and hoping the installer emerges fully notarized.

AI-assisted development works best for me when the tools are operating inside a clear architecture, explicit constraints, strong test coverage, and a carefully managed development process.

SetMaster 3 was specified before it was rebuilt. The process went through five rounds, 93 tracked issues, and a data-pipeline port verified as byte-identical to the previous version on real data.

The current application has 897 automated tests across the data pipeline, application, and interface.

Those details matter more to me than saying the application was “built with AI.”

The interesting question is not whether AI generated code.

The interesting question is whether AI helped me build a better-specified, better-tested, more complete product than I could have produced through my previous development workflow.

In this case, it did.

SetMaster gave me a reason to refine my AI architecture toolset while working in a problem space I know deeply. I could evaluate the output not only as an engineer, but as the end user who had to prepare a real set with it.

A bonus aspect of this arrangement is that hours of user testing mean hours of DJing.

This is the rare software project where saying “I need to test the product tonight” may involve a mixer, a subwoofer, and suspiciously little financial return.

## Built in the Open

SetMaster 3 is free and open source under the MIT License.

The public repository includes the source, releases, and downloadable artifacts. The application is independently developed fan software and is not affiliated with or endorsed by Native Instruments®, Spotify®, Exportify, or AlphaTheta.

There are still things to build.

Rekordbox® collection import is planned, but it does not have a release date. Perform Mode and a natural-language filtering interface have been specified and deferred rather than abandoned.

I have completed much more end-to-end testing on Windows than on macOS. The macOS package passed its clean-install acceptance test, but some of the larger golden-master and end-to-end test suites have not yet been run on a Mac.

That is part of why I am releasing the application openly.

I want DJs to use it, find the rough edges, report bugs, and suggest improvements based on how they actually prepare music.

## Download SetMaster 3

SetMaster grew out of three things I care deeply about:

- Traktor®
- Software development
- The craft of building and performing a DJ set

It is the product of a deep music catalog, years of real-world set preparation, a great deal of engineering, and possibly an unreasonable belief that every tedious personal workflow can eventually become software.

If you use Traktor® and want a faster way to explore your collection, rediscover forgotten tracks, compare playlists, and prepare more deliberate sets, visit the full SetMaster 3 page.

That page includes the complete feature overview, current platform requirements, installation instructions, GitHub repository, and download links for Windows and macOS.

## [Explore SetMaster 3 and download the application](https://intake.wolfstrategyllc.com/setmaster3/)

Happy SetMastering.

*SetMaster 3 is independent fan software and is not affiliated with, endorsed
by, or sponsored by Native Instruments®, Spotify®, or Exportify.
Traktor® is a registered trademark of Native Instruments® GmbH. Spotify® is a
registered trademark of Spotify AB.*

<!--
PUSHED TO WIX 2026-08-06 (#154). The draft post id lives in
planning/workflow.md, which is the ledger for this post. Re-pushes are a PATCH
to /blog/v3/draft-posts/{id}, never a POST. Do not push without reading it.

BODY is the copywriter draft that landed 2026-08-06 as
sm3_intro_long_format.md, now at planning/raw-blog-post.md, kept verbatim. It
replaces the 576-word short version authored under #136, which is in git
history at 46f9e26. Ry's call, this session: the long format is the post.

THE PROSE WAS NOT EDITED, per the wp-blog-writing-workflow skill. Three
mechanical changes only, none of them copy edits:
  1. the h1 was dropped, because the title lives in front matter;
  2. 15 citation spans (U+E200 cite U+E202 turn... U+E201) left by the tool
     that produced the draft were stripped, wrapper characters included. A
     first pass that matched only the visible text left 15 orphaned U+E200
     bytes behind; the span-based strip is the correct one. If a future draft
     arrives from the same tool, strip the whole U+E200..U+E201 span.
  3. trademark marks were added, below.

TRADEMARKS per sm3-specific-pages/README.md L116-121, which calls this
non-negotiable on a public page: every visible Traktor, Native Instruments,
and Spotify carries the registered mark; Exportify renders plain; the
unaffiliated line ships with the post. Rekordbox is marked too, matching the
short version. 13 Traktor, 4 Spotify, 1 Native Instruments, 1 Rekordbox in the
body, plus the title. THE TITLE MARK IS THE ONE JUDGMENT CALL: Ry chose the
draft's h1 verbatim, and "every visible" includes a title, so the two rulings
pull against each other. Marked, and flagged to him; a retitle is a two-field
patch if he wants it clean.

COVER is sm3-assets/img/a01-track-playlist-matrix.png, Ry's instruction this
session, replacing the a02 set-editor capture. Resized to 1200px wide and
palette-quantized to 256 colours, 117 KB, matching the treatment the previous
cover had. It now matches the lede: the draft opens on the Track-Playlist
Matrix as the feature Ry uses most, where the short version led on the set
editor. Checked before use: track, artist, and playlist names only, no
filesystem paths, unlike the gitignored A-08 capture that leaks a Windows user
directory. The 178 of 3,604 tracks across 5 of 83 playlists in the capture is
the same figure the body cites.

FRONT MATTER rulings from Ry, 2026-08-06: title is the draft's h1; slug is
UNCHANGED at introducing-the-setmaster-application, so the planned URL stays
put and does not follow the new headline; featured is true; tags carry over
from the short version. The excerpt is assembled from the draft's own opening
lines rather than written fresh, and the date moved to the day of the push.

ONE CTA, ONE DESTINATION still holds (Ry, 2026-08-05): the landing page at
/setmaster3/, linked at the top and again in the closing heading. No intro
call anywhere in the body. The draft adds no third destination.

TONE is not checked against anything. docs/ryan-blog-tone.md was removed
2026-08-06 (#150); the copy is the writer's and Ry's, and this post is not
auto-corrected on its way to Wix.
-->
