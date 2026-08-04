# SetMaster 3: From a Spreadsheet on a Plane to a Shipped Application

> **Copy deck, draft 1** (2026-07-31). Written to
> [`01-case-study-outline.md`](01-case-study-outline.md) in the house voice defined by
> [`docs/ryan-blog-tone.md`](../../docs/ryan-blog-tone.md). Every fact traces to
> [`04-claims-ledger.md`](04-claims-ledger.md). This is the text the page gets built
> from; it is not the page. Tone-compliance notes and open items are at the end.

---

**Kicker:** CASE STUDY · 2026

I am a professional DJ. I built my own set preparation tool three times in three
years. The third one is a specified, tested, offline web application that anyone
can download and run on their own machine.

| | |
|---|---|
| 25 days | specification to public release |
| 74 issues | across four build rounds |
| 867 tests | automated, passing |
| Byte-identical | pipeline port, verified on real data |

*[Hero image: A-01, the Track-Playlist Matrix at full scale]*

---

## The Tedious Part

I keep about 7,000 tracks in Traktor®, drawn from a personal music library many
times that size. I also perform with DJ partners, so some of their catalog sits on
my machine as well.

Preparing a set inside Traktor® or Rekordbox® alone was slow. The slow part was
never the mixing. It was the searching, the filtering, the sorting, and the
cross-checking against sets I had already played, so that I did not put the same
track in front of the same listeners too often. Staying fresh is part of the job.

There was a second version of the same problem. I maintain Spotify® playlists on
the go, and those playlists are a record of what I have actually been listening to
and want to play. Reconciling them against what I own in Traktor® was manual work
every time.

Streaming was supposed to make this easier. It made it larger. When access
replaces ownership the library grows, and organizing a larger library is more
work, not less.

The problem was not that I had too little music. The problem was that I could not
get from an idea in my head to the tracks that fit it fast enough.

I am a data engineer. I kept seeing the automation.

---

## One Row Is One Transition

The first version was a Google Sheet, built in 2023. I chose Google Sheets for one
reason, which was cross-device backup without any work on my part. It moved to
Excel later.

I used it in professional settings immediately. It was never a side project that
became serious. It went straight into paid work, which is why the logic inside it
survived two rewrites without changing.

The idea that everything else grew from is small. Traktor® and Rekordbox® present a
set the way a playlist reads, top to bottom, one track per row. Notes attached to a
track in that layout are hard to read and take up room that the track list needs.

So I gave a row a different job. One row is one transition. The track I am coming
from on the left, the track I am going into on the right, and everything about the
move between them in the columns in the middle.

That is the part of a set that actually requires preparation. The track order is a
list, and a list is easy. The transition is where the cue points, the level moves,
the tempo changes, and the notes to myself live, and reading one left to right is
how I think about it when I am standing behind the equipment.

A spreadsheet was the right container for the rest of it. Tracks move earlier and
later while a set develops, you replace things, you add things, and you need
somewhere to write down what you liked, what you did not, and where you left off.
Copy, paste, drag, and white space between sections did all of that without my
having to build any of it.

It grew. It became a multi-tab workbook that I added to on planes between gigs,
and it grew a second view for performing: zoomed in, more room, color coded, so
that a glance during a long set was enough to bring a rehearsed transition back.

*[Sidebar: The Transition Row. Diagram A-06]*

*[Image: A-07, a real SetMaster 2 set tab]*

---

## The Catalog Becomes Data

The next version added a VBA and Python backend behind the workbook. That is
SetMaster 2, and it is the point where the tool stopped being a spreadsheet.

It read my Traktor® collection into the workbook so that the catalog could be
filtered like data instead of browsed like a folder. Compound filters against key
and BPM, fast switching between them, artist search. I used it during set
preparation and never during a performance, which kept the two activities separate
and kept the tool honest about what it was for.

It took minutes off the tedious part, every session, for years.

One thing about SetMaster 2 is worth stating plainly, because it is still true of
the current version. The catalog half and the set preparation half were never
dependent on each other. The transition editor works with nothing loaded at all.

*[Image: A-08, the SetMaster 2 LaunchPad tab]*

---

## The Comparison That Changed the Tool

Then I built a one-off flow that took the Python output from SetMaster 2, imported
CSV exports of my Spotify® playlists from exportify.net, and compared the two.

That is when the tool became something other than a faster spreadsheet. The
comparison answers a question I had been answering by hand for years: of everything
I have been listening to and actually want to play, which of it do I not own yet.
The answer is a short list. I buy from the short list, and the tracks are in the
next set.

It saved hours every month. That number is mine and it is not instrumented, so
treat it as an estimate from the person who was doing the work before and after.

Lexicon deserves a mention here. Lexicon has a comparison tool and it is a strong
one. It did not do the bulk list filtering I wanted, which is why I kept building,
but this was never meant to compete with it. It is a different application of the
same underlying idea, which is that a music catalog is metadata and metadata can be
queried.

*[Image: A-03, the Playlist Compare Tool]*

---

## The Rebuild

I became a cloud architect in early 2025, and the job changed how I looked at the
workbook. I did not get time to act on it until this year, and the web application
version started in early July 2026.

There was also a defect that no amount of additions to the workbook was going to
fix. The prototype's connection to Traktor® was Windows only. That was the single
largest reason to rebuild rather than continue.

### The Specification Came First

I gave Claude the prototype and all of the VBA, and we spent several days on
planning documents before any application code existed. What came out of that is a
complete specification package: an overview, a data model, a user interface
specification, ten feature specifications, a decision log, and an open questions
document closed to zero.

The instruction in the repository to the agent doing the build is one sentence.
The specification is complete and decided, and the job is to implement it, not to
re-litigate it.

That is the artifact I would point at first. The build was fast because the
thinking was finished.

### The Pipeline Was Ported, Not Rewritten

SetMaster 2's data engine carried years of accumulated fixes in its matching and
normalization logic: track name cleaning, playlist name normalization, filename
normalization, key mapping. Those fixes exist because real music metadata is
inconsistent, and every one of them was a bug I hit and corrected while working.

The rule for the rebuild was that restructuring the stages was allowed and changing
the matching behavior was not.

A rule like that is worth nothing unless it can be checked. So the ported pipeline
is covered by golden-master tests that compare its output to the original engine's
output on my real collection, byte for byte. Pandas is pinned and the CSV round
trips between stages were kept specifically to preserve those bytes.

The result is not that the port is probably correct. The result is that the port
produces the same bytes, and a change to the matching behavior fails the build.

*[Sidebar: Golden-Master Testing]*

### The Constraints Were Decided Before the Code

Three constraints were fixed at specification time and are still fixed.

`collection.nml` is opened strictly read-only. SetMaster never writes to it or to
any other Native Instruments® file. That is stated in the specification, restated
in the interface, and checked with SHA-256 snapshots of the file.

The application is fully offline. A local backend process and a browser interface
on localhost, with no cloud, no accounts, no telemetry, and no external API calls.
Your library never leaves your machine because there is nowhere for it to go.

It is single user. There is no authentication and no multi-tenancy, and it was not
architected for either.

### Four Rounds, Seventy-Four Issues

Build one finished on 2026-07-07 and was tagged. After it came three hardening
rounds against a real backlog: 26 issues, then 12, then 36. One issue, one branch,
one pull request each.

Merging a fix does not close its issue in this repository. The issue stays open
until I have verified it against my own data. The person who has to live with the
tool is the one who decides whether it works, and that is a workflow rule, not a
preference.

I was also out playing during those rounds, so the application was being used in
live situations while it was being fixed.

The acceptance criteria were demonstrated against my real files rather than
fixtures. The real collection loads at 6,810 tracks across 149 playlists. The
digging workflow I use most, which finds curated tracks I have never put in a
published set, returns 111 rows in a single pass. A note typed into a blank
comparison cell survives a re-import and a full re-run of the pipeline, which is
the behavior that makes the comparison worth annotating at all.

### Packaging for People Without a Terminal

Before this existed the launchers assumed a developer checkout, which meant the
first public release could not have started on a clean machine.

Each release is now a self-contained payload per operating system. Unpack it and
double-click a launcher. No Python, no Node, no terminal.

The detail I would call out is small and it is the kind of thing that decides
whether a release works. A virtual environment is not a portable runtime, because
its configuration points at an absolute path to a base Python that will not exist
on someone else's machine. So the payload ships a relocatable CPython with the
locked dependencies installed into it, and the artifact smoke check fails the build
if a developer virtual environment ever appears inside it.

### Publishing a Private Repository Safely

The private repository contains my entire real Traktor® library as test data,
tracked since the first commit. The public repository had to contain none of it.

Rewriting the history to remove it was considered and rejected. A history rewrite
is one mistake away from a permanent leak, and a tree with no history has no leak
surface at all. So the public repository is a generated mirror, rebuilt from
scratch at each release, carrying no history and accepting no code back.

It has two defenses that do not share any logic. The first is an allowlist that
decides what ships, because a denylist fails open and a file nobody thought about
would go out. The second is a scanner that runs against the generated tree rather
than the source, on the reasoning that the allowlist is the component most likely
to have a bug, so the thing that catches a bad allowlist must not be built on it.
It checks file sizes, forbidden paths, content patterns, and SHA-256 hashes against
the known collection file.

Any finding aborts the build and deletes the output. There is no warn and continue
mode. This is not theoretical. The first real run caught a machine path string
inside an interface placeholder, which is exactly the class of thing that survives
code review.

### What Is Not Finished

Windows is verified end to end. macOS is not.

The macOS launchers and the macOS build script are written and structurally
correct, and no build of SetMaster 3 has ever been run on a Mac, because no Mac was
available. So the release ships as Windows only and the changelog says so in three
places a reader would actually look. There is a written checklist that would earn
the macOS claim, and it is tracked as an open issue.

Perform Mode is deferred, and so is the natural-language filter bar. Rekordbox®
collection import is planned with no date on it.

I would rather publish that list than have someone find it.

---

## What It Does Now

SetMaster 3 does two jobs.

The first is set preparation: a structured editor for writing out a set as
transition rows, with track order, hot cue numbers, EQ and level moves, timing, and
mix notes.

The second is catalog analysis: it reads a Traktor® collection strictly read-only,
cross-references it against Spotify® playlists exported through Exportify, and
finds the two gaps that matter, which are tracks I own but have not organized and
tracks on my playlists that I do not own. It also runs compound filters and sorts
across the whole collection that Traktor® itself does not offer.

The first job does not depend on the second. SetMaster 3 is fully usable with no
collection ever loaded, and Traktor® is not a prerequisite for it. Set rows are
typed by hand, and the only thing a loaded collection adds to the editor is
name suggestions while typing.

Inside the editor the useful parts are the ones that came from using it: cell
formatting I control, an emoji palette I can edit, validation lists I can rename,
export to CSV, XLSX, and Markdown, and a mix timer that tells me how long each
section runs and how long the whole mix is.

The framing that matters most is that it becomes the source of truth. I am not
fighting Traktor® or Rekordbox® filtering to make a set. I am working in the place
the set lives.

*[Images: A-02 set editor, A-04 filter drawer]*

---

## The Flight to Los Angeles

I was on a plane to Los Angeles to play that night, with Traktor® open and
SetMaster next to it, digging through the catalog. The set was already prepared.

I found transitions I liked well enough to consider putting into a finished set on
the day of the gig, which is not a small thing to do. SetMaster let me lock them
in: the cue points, the moves, the notes about what to do and when. By the time we
landed I was confident enough to play them.

That night, during the set, I switched over to SetMaster and read the notes I had
written that afternoon on the plane.

That was SetMaster 2, and it is the moment I stopped thinking of it as a
spreadsheet with color coding. Preparation and performance were the same document,
six hours apart, and the notes were the thing that carried across.

> **Connect the idea in your head with the tracks that fit it, faster.**

The current version does not have the dedicated performance view that the workbook
grew. The set editor is there to switch to, and it works, and a proper Perform Mode
is specified and waiting rather than built. That flight is the reason it is on the
list instead of off it.

In my own words at the time, this is beyond a fancy spreadsheet with color coding.
It actually improves the craft.

---

## Teaching, and What Is Next

A set page is a legible artifact, and that has always suggested a second use to me.
Not for beginners, but for intermediate DJs who already understand transitions and
song composition, a written-out transition is a good way to learn how to cue a
track and how to line up key, BPM, and cue points. A student can study one complex
transition, or a group of them, at their own pace.

Rekordbox® collection import is planned. I do not have a date for it, and it is
currently listed out of scope rather than in progress, which is what planned with
no date honestly looks like.

SetMaster 3 was built as a portfolio piece for AI engineering work, and it is
actively developed. It is also the tool I use to do my job.

---

## Where to Find It

SetMaster 3 is free, MIT licensed, and available now for Windows. The source is
public and every release publishes a SHA-256 hash alongside the artifact.

The smallest next step is to look at it. Read the code, or download it and open it
against your own collection, which it will not modify.

If you are hiring for AI engineering, data platform, or technical operations work,
the fastest way to talk about any of this is a call.

**[ Contact Ryan ]** · [Download SetMaster 3](https://intake.wolfstrategyllc.com/setmaster3/) · [Source on GitHub](https://github.com/wolfpackdata/setmaster)

*SetMaster 3 is independent fan software and is not affiliated with, endorsed by,
or sponsored by Native Instruments®, Spotify®, or Exportify. Traktor® is a
registered trademark of Native Instruments GmbH. Spotify® is a registered trademark
of Spotify AB.*

---
---

# Sidebars

Each runs alongside the section named, not in the main column.

## The Transition Row
*Runs alongside One Row Is One Transition*

A playlist reads down. A transition reads across.

The left group is the track you are leaving, the right group is the track you are
landing on, and the columns between them hold the cue numbers, the level and EQ
moves, and the note you wrote to yourself the last time you rehearsed it.

Magenta is out. Cyan is in. That has been the color language since the workbook and
it did not change in the rebuild, because it was already learned.

## Golden-Master Testing
*Runs alongside The Pipeline Was Ported, Not Rewritten*

A rewrite that is "basically the same" is a rewrite that will surprise you later.

Golden-master testing sets a harder bar. The old engine and the new engine both run
against real data, and the outputs are compared byte for byte. Anything that
changes the result fails, including changes that look like improvements.

That bar is only reachable because the data is real. Synthetic fixtures would have
passed while the messy cases that produced the original fixes went untested.

## How the Build Was Run
*Runs alongside The Specification Came First*

| 1 day | 31 decisions | 0 deviations |
|---|---|---|

The build was cost-tiered on purpose, and the policy was written down before it
started rather than justified after. One orchestrating agent ran on the frontier
model. Every sub-agent ran on Opus. No frontier sub-agents were spawned at all.

The policy was enforced two ways, by an environment variable and by a per-call
model pin, and there were zero deviations across the entire build.

What came out of it, in about a day, was an application that passed all four
acceptance criteria end to end against real data. Verification ran through a
Playwright suite driving the real built application, re-run independently rather
than taken on the builder's word, and 31 build decisions were logged with their
reasoning as they were made.

The speed is not the interesting part. The reproducibility is. Anyone can get an
application out of a model once. The question is whether you can say why it came
out the way it did, and this one can, 31 times over.

SetMaster 3 does not contain any AI. It was built with it.

## Stack
*Runs alongside The Rebuild*

FastAPI and a ported Python pipeline. React 18, Vite, and TypeScript. SQLite.
pytest, vitest, and Playwright. A bundled CPython in every release payload.

---
---

# Notes on this draft

## Length

**2,692 words** in the main column, plus **372** across the four sidebars
(counted, not estimated). That is 42 words over the outline's 2,650 budget, which
is close enough to call on target, and well outside `ryan-blog-tone.md` §7's
stated 350 to 1,200 words.

That length rule is scoped to blog posts, and this is a different artifact with a
different job. Flagging it rather than silently exceeding it. If Ry wants it
inside 1,200, the cut is *The Rebuild*, which is 40 percent of the piece, and I
would argue against making it.

## Tone compliance

Checked against §9 of the tone guide.

| Rule | Status |
|---|---|
| Zero em dashes and en dashes | Pass |
| Zero exclamation points | Pass |
| Zero rhetorical questions | Pass. The two sentences that could have been questions are written as statements: *"The question is whether you can say why it came out the way it did"* |
| Contractions expanded | Pass |
| Quotation marks only at arm's length | Pass. The only quoted phrase is *"basically the same"* in the golden-master sidebar, which is the idea being rejected |
| At least one reversal (§4.1) | Four. *"The problem was not that I had too little music. The problem was that I could not get to the tracks fast enough"* · *"The result is not that the port is probably correct. The result is that the port produces the same bytes"* · *"The speed is not the interesting part. The reproducibility is"* · *"It was never a side project that became serious"* |
| At most one fragment triple (§4.2) | One, in Packaging: *"No Python, no Node, no terminal"* |
| Concrete run-on lists (§4.3) | Three, all concrete nouns: the specification package contents, the matching-logic fixes, the stack sidebar |
| Numbers specific and hedged | Pass. *"about 7,000"*, *"in about a day"*, and the hours-per-month claim is explicitly marked as an uninstrumented estimate |
| Every strong claim followed by its limit | Pass, and *What Is Not Finished* is an entire section of it |
| No client named, no testimonial invented | Pass. Lexicon is named as a peer product, not a client |
| No word from the reject list | Pass |
| Opens cold on something concrete | Pass. First sentence is a track count |
| Closes on the smallest next step, one plain CTA | Pass. *"The smallest next step is to look at it"*, then **Contact Ryan** |
| Paragraphs 1 to 4 sentences | Pass |
| Subheads are Title Case statements | Pass, none are questions |

**One deliberate deviation.** §7 asks for exactly one CTA. The closing carries one
CTA and two plain links, because a case study that does not link the thing it
describes is broken. **Contact Ryan** is the only button; the other two are text.

**Point of view.** First person throughout, which §2 assigns to Ry narrating what
he did. The reader stays in the third person until the final section, where the
piece turns toward the ask and *"you"* appears for the first time.

## What changed from the outline

**The anecdote is SetMaster 2** (Ry, 2026-07-31), which settled the open question
in S8 and improved the section. It now argues **for** Perform Mode rather than
around it: the flight is the reason a performance view is specified and waiting,
which turns a deferred feature into a considered one with a story behind it. The
S8 caveat is now the tone guide's §4.4 immediate-caveat pattern, and the ledger
row and outline note both need updating to match.

**S3 absorbed the performance-view beat** rather than leaving it as a standalone
aside, so that the flight in S8 pays it off directly.

**The thesis pull quote lost its quotation marks.** It reads as the piece's own
conclusion rather than as something being quoted, which is what §3.6 asks for.

## Open items

1. **Title.** Option 1 is used here. §10 of the outline holds the other three.
2. **The hours-per-month figure.** Currently hedged as an uninstrumented estimate.
   That is the honest framing, and Ry may prefer to drop the number entirely.
3. ~~"Rekordbox" carries no ®~~ — **CLOSED (Ry, 2026-07-31).** It now carries one,
   here and across the whole planning set. This extends the repo's enumerated
   trademark rule, which listed only Traktor, Native Instruments, and Spotify.
4. **The SetMaster 2 year** is not stated in the prose, only "the next version".
   That sidesteps the soft ~2024 date. If Ry confirms it, one sentence gains a year.
5. **The 6,810 figure** appears in the main column. The ledger notes the build
   report cites both 6,810 and 7,033. 6,810 is the acceptance-run number and is the
   one used.
