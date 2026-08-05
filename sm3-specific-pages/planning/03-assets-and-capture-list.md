# Assets and capture list

Everything the two pages need that does not exist yet, and the contract for what
ships while it doesn't.

**The headline fact, as of 2026-08-04:** Ry delivered **three** captures (A-01, A-02, A-08),
so the **case study page is now fully illustrated with zero placeholders left**. Before that
there was exactly one SetMaster 3 screenshot in existence, `app-setmaster.png` (1494×848),
which still serves A-03.

**Still true:** there is **no video of any kind**, so media remains the critical path for the
**landing page**, and it is the only part of this work Claude cannot produce.

**Two lessons from the delivered batch, worth reading before capturing more:**

1. **The planned aspect ratios were wrong.** All three landed near **2:1** (2.10, 2.11, 1.98),
   not the 16:9 and 4:3 speced below. SetMaster is a wide desktop-class UI and that is simply
   how it captures. Forcing them into the nominal frames would have cropped the sides, so the
   case study gained a `.shot--natural` class that lets a capture keep its own proportions.
   **Treat the ratios in the table below as estimates, not requirements.**
2. **The privacy rule in §1 earned its place immediately.** A-08 arrived with a Windows user
   directory and a local studio path visible, and shipped redacted. Check the frame for paths
   *before* capturing, not after.

Ry's brief: *"you'll want to have placeholders for me to put videos for me
showing the app, and different parts of the app, and placeholders for nifty
screenshots of the app in action as well."*

---

## 1. Capture conditions — read once before recording anything

These apply to every screenshot and every video. Getting them wrong means
recapturing everything.

| | Rule |
|---|---|
| **Data** | Capture against a **real, populated** collection and real sets. Empty states and `Untitled set 1` look like a demo of nothing. |
| **Window** | 1600×900 or 1920×1080, maximized. Never a windowed browser with visible chrome, bookmarks bar, or other tabs. |
| **Zoom** | Browser at 100%; app Font Size and Spacing at defaults. Screenshots taken at a custom zoom won't match each other. |
| **Theme** | Dark (the only mode). |
| **Sidebar** | Expanded, showing the RML lockup and the tree — it is a large part of what makes the app look like a real application. |
| **Privacy** | No file paths containing `C:\Users\ryanp`. Turn off the File Path column. This is the same class of leak the public-mirror scanner exists to catch. |
| **Names** | Real track and playlist names are fine and *better* — they are what makes it look used. Personal or identifying playlist names are not. |
| **Cursor** | Visible in video, hidden in stills. |
| **Format** | Stills: **PNG** from the OS capture, converted to WebP + JPEG fallback at build time. Never a phone photo of a screen, never a lossy re-crop. |

---

## 2. Screenshots

Numbered `A-nn`. The id appears in the page's placeholder, so a delivered file
has an unambiguous slot.

| id | Shows | Used on | Frame | Notes |
|---|---|---|---|---|
| **A-01** | **Track-Playlist Matrix at full scale** — many rows, many playlist columns, a filter active, the breadcrumb populated | Landing hero (fallback if no video), case study S1 | ~~16:9~~ **2.10** | ✅ **DELIVERED 2026-08-04** as `sm3-assets/img/a01-track-playlist-matrix.png` (1908×907). 178 of 3,604 tracks, 83 playlists, filter panel open on BPM range + keys + release year. Live on the case study. |
| **A-02** | **Set editor**, a real set, several transition rows, RED/YELLOW/box formatting visible, emoji in the *I like* column, STATS panel showing all four stats | Landing band 4, case study S7 | ~~16:9~~ **2.11** | ✅ **DELIVERED 2026-08-04** as `sm3-assets/img/a02-set-editor.png` (1904×904). Real set, varied formatting, emoji in *I like*, sidebar expanded with the RML lockup. **The STATS panel is closed**, so if the four stats matter, this needs a re-shoot with it open. |
| **A-03** | **Playlist Compare Tool** — a comparison page with Go get / Organize / Match flags and at least one blank-cell note filled in | Landing band 5, case study S5 | 16:9 | **Partially satisfied.** `app-setmaster.png` (1494×848) is a real Compare Tool shot and is **live on the case-study page now**. It shows the flags but **no annotated blank cell**, so this row stays open for a replacement that includes one: the note is the feature that survives re-runs, and it is the part worth picturing. |
| **A-04** | **Matrix filter drawer open** — BPM range slider, key selection, the compound filter mid-construction | Landing band 5 | 4:3 or 16:10 | Shows *how* the filtering works, which A-01 only shows the result of. |
| **A-05** | **Home / LaunchPad** with the pipeline status chip after a successful run | Landing band 7 | 16:9 | Optional. Supports the "offline, local" claims. |
| **A-06** | **Transition-row diagram** | Landing band 3, case study S3 | — | **Not a screenshot — built in HTML/CSS** (`02-…` §4.3). Listed here so it isn't mistaken for a missing capture. |
| ~~**A-07**~~ | ~~**SetMaster 2 workbook**, a real multi-tab set~~ | ~~Case study S3, landing band 6~~ | — | ❌ **RETIRED 2026-08-04**, Ry's call. Cut from the case study, not deferred. The section's prose carries the workbook era on its own and A-08 already pictures SetMaster 2. **Still open for the landing page** if band 6 wants it. |
| **A-08** | **SM2 LaunchPad tab** | Case study S4 | ~~4:3~~ **1.98** | ✅ **DELIVERED 2026-08-04** as `sm3-assets/img/a08-sm2-launchpad.png` (1434×724). ⚠️ **The delivered capture leaked two machine paths** (a Windows user directory and a local studio path) in the collection-path fields, exactly what §1 forbids. Shipped **redacted**: both values are covered and the figcaption says so. The un-redacted original is **gitignored and was never committed**, so the leak is not in history. A re-shoot with those fields cleared would let the redaction go. |
| **A-09** | **Settings → About**, showing version and the offline/read-only statement | Case study S6 | 4:3 | Optional. Good evidence for the read-only claim. |
| **A-10** | **OG share image**, 1200×630 — A-01 with a title bar composited over it | Landing `<meta>` | 1200×630 | Composed from A-01; not a separate capture. |

**Existing and reusable:** `hire/assets/img/app-setmaster.png` can stand in for
A-01 immediately, so the landing page is never *entirely* unillustrated during
the build. It is 1494×848 and will hold up at 16:9.

---

## 3. Video

The largest open question in this round and the landing page's critical path.
**Nothing here can start until Ry answers §3.3.**

### 3.1 Proposed set

| id | Video | Length | Where | Autoplay? |
|---|---|---|---|---|
| **A-V1** | **Hero loop** — silent, no narration. A tight loop of the matrix filtering live: drawer opens, BPM range drags, rows resolve. Pure motion, no story. | 8–12 s, seamless loop | Landing hero | Yes — muted, `playsinline`, reduced-motion-aware |
| **A-V2** | **Building a set** — Ry walks through adding transition rows, cues, formatting, the mix timer | 60–90 s | Landing band 4 | No — click to play |
| **A-V3** | **The Spotify®↔Traktor® loop** — Exportify CSVs in, pipeline run, comparison page, working the Go get list | 60–90 s | Landing band 5 | No |
| **A-V4** | **Digging in the matrix** — the signature workflow: one playlist, on-root ≥ 1, on-non-root = 0, curated tracks never used in a published set | 45–60 s | Landing band 5 or case study S6 | No |

**A-V1 is the one that matters most and is the cheapest to make** — it needs no
script, no voice, and no editing. If Ry only ever records one thing, this is it.

### 3.2 Technical constraints

Driven by the no-external-requests rule, which forbids a YouTube or Vimeo embed:

- **H.264 MP4**, `faststart`, plus a **WebM/VP9** source for the size win where
  it helps. `<video>` with both sources and a PNG `poster`.
- **Budget: A-V1 ≤ 2.5 MB. A-V2/3/4 ≤ 6 MB each**, `preload="none"` so they cost
  nothing until clicked. A 90-second screen capture at 1080p is ~40 MB raw —
  these need real encoding (CRF 28–32, 1280×720, 24 fps is plenty for screen
  content), not a raw export.
- **No audio track at all on A-V1.** Strip it; don't just mute it in markup.
- Narration on A-V2/3/4 is Ry's call (§3.3). If there is narration, the page needs
  **captions** — a `.vtt` track, not burned-in text.

### 3.3 Open questions for Ry

1. **How many videos**, and is A-V1 alone enough for a first ship?
2. **Narration or silent?** Silent with on-screen labels is faster to produce,
   ages better, and needs no captions. Narrated is more engaging and sounds like
   Ry, which is worth something on a page whose real audience is employers.
3. **Who edits?** Raw screen captures will not meet the size budget.
4. **Does the case study get video at all,** or does it stay a stills-and-prose
   document? Recommendation: stills only. Video on a case study is rarely watched
   and it doubles the page weight.

---

## 4. The placeholder contract

Until a slot is filled, it ships as a **designed placeholder at the exact final
aspect ratio.** Dropping the real file in must change nothing about the layout.

```
┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
│                                                 │
│                    A-V2                         │
│         SET EDITOR WALKTHROUGH · 60–90s         │
│                  1280 × 720                     │
│                                                 │
└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
```

- `--bg-row` fill, 1px **dashed** `--border-subtle`, 6px radius.
- Centred: the mono asset id, a `--type-label` caption naming the content, and the
  target dimensions.
- **Never** a grey box, a "coming soon," a spinner, or a stock image standing in.
- The page must **look deliberate with every placeholder still in it.** That is
  the acceptance test, and it is the same pattern the `hire/` pages' case-study
  frames already prove works.

Placeholders are **not** invisible to search engines on the indexed landing page —
they carry no `alt` claim about content that doesn't exist. A placeholder frame is
`aria-hidden` decorative until it holds a real asset.

---

## 5. Fonts

Both pages need self-hosted woff2 in `sm3-assets/fonts/`.

| Family | Weights | For | Source |
|---|---|---|---|
| **Inter** | 400, 500, 600, 700 | Landing page — the app's `--font-ui` | Needs downloading; not in this repo |
| **JetBrains Mono** | 400, 500 | Landing page — the app's `--font-mono` | Needs downloading; not in this repo |
| **Roboto** | 700 | Case study headings | **Already in `hire/assets/fonts/`** — copy |
| **Montserrat** | 400, 500, 600 | Case study body | **Already in `hire/assets/fonts/`** — copy |

Subset to Latin + the ® glyph, which appears constantly on both pages. Watch that
the mono face actually carries ® at the weights used; if it doesn't, ® renders in
the UI face in mono contexts by design, not by accident.

**Licensing:** Inter (OFL) and JetBrains Mono (OFL) are both fine to self-host and
redistribute. Note it in the CSS header comment.

---

## 6. Brand marks

| Asset | Where from | Rules |
|---|---|---|
| **RML mark** | `setmaster3/docs/design/brand/rml-mark.svg` | Landing page only — the nav lockup and the footer. **Never scaled up as a bitmap**; the SVG is a vector recreation and the PNGs are recovered rasters clean only at small sizes. |
| **"SetMaster 3" wordmark** | **Re-set live in Inter**, never a bitmap | The RML usage rules are explicit: the app never ships a bitmap of the wordmark, and neither does this page. |
| **Wolfpack mark** | `hire/assets/img/wolfpack-logo.png` | Case study only. |
| **Ryan portrait** | `hire/assets/img/ryan-hickey-portrait.jpg` | Case study, and landing band 10 if §11.3 says the page names him. |
| **Favicon** | The app's own — `setmaster3/frontend/public/favicon.svg` | Landing page. Makes the tab match the running app, which is a nice touch for anyone who has it open. ⚠️ **Contested.** Ry's 2026-07-31 instruction put the **Wolfpack mark** on every page in this repo, and the case study now carries it. This row is the only thing that disagrees. Open item 7 in `00-overview.md` §9. |

**Forbidden, restated because this is the asset doc and it is where someone will
look:** no Native Instruments, Traktor®, Rekordbox®, or Spotify® logo, icon, UI
screenshot, or derived graphic ships on either page. Not in a comparison, not in
an "integrates with" strip, not in a favicon, not in the OG image. The Traktor®
reference screenshots in `setmaster3/docs/design/` are internal design reference
and **must not** be confused for shippable assets.

---

## 7. Delivery checklist for Ry

In priority order — the first two unblock a buildable landing page:

- [ ] **A-V1** hero loop (8–12 s, silent) — highest value, lowest effort
- [x] **A-01** matrix at full scale — delivered 2026-08-04
- [x] **A-02** set editor with real formatting — delivered 2026-08-04 (STATS panel closed; re-shoot only if the four stats matter)
- [ ] **A-03** compare page with a note
- [ ] Answer §3.3 — video scope, narration, editing
- [ ] **A-04** filter drawer
- [ ] **A-V2**, **A-V3** walkthroughs
- [x] Confirm **A-08** is clean of machine paths — **it was not.** Two paths were leaking; shipped redacted, original gitignored. A-07 is retired, so nothing to check there. Optional: re-shoot A-08 with the collection-path fields cleared so the redaction can come off
- [ ] **A-05**, **A-09** (optional)

Everything else — fonts, marks, the A-06 diagram, the OG composite — Claude can
do without Ry.
