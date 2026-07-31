# resume_build — internal résumé generator

Turns a YAML content file into an on-brand `.docx`. Implements the Word half of
`../resume_design/`; that folder stays the design source of truth.

```powershell
cd ryan-resume-dev\resume_build
pip install -r requirements.txt
python build.py
```

Writes both résumés next to the folder each belongs to:

| Target | Content | Output |
|---|---|---|
| `eng-music` | `content/eng_music.yaml` | `../eng_music_combo/Ryan_Hickey_Resume_eng-music_v2.4.docx` |
| `eng-only` | `content/eng_only.yaml` | `../eng_only/Ryan_Hickey_Resume_eng-only_v2.4.docx` |

Useful flags — `--only eng-only`, `--release`, `--density tight`, `--fonts safe`,
`--suffix`. `--help` for the rest.

Each output folder holds **only the current build**; superseded ones move to its
`archived/` subfolder (which also holds the human-edited v0 the round started
from). The build never writes there — move by hand when a version is retired.

There is **one build**. Through v2.1 there were effectively two — a picture
banner for humans and an ATS-safe text header behind `--header text` — and the
image one was the default. See "The header is text" below for why that is gone.

## Versioning

**One version per round, both résumés**, held in `VERSION` as a single line.
`v2.0` is a round's first build; every iteration inside the round bumps the minor
(`v2.1`, `v2.2`, …). The next content round starts at `v3.0`. Every iteration
appends to [`CHANGELOG.md`](CHANGELOG.md), and each round's plan lands in
[`docs/`](docs/).

Build artifacts carry the version so a later round can tell which wording an
application actually went out with. The copy Ry *sends* should not:

```powershell
python build.py --release     # Ryan_Hickey_Resume.docx, no version in the name
```

The version still lands in the docx properties on a release build, so a clean
filename is not a lost audit trail.

### Page count

The design system's spacing comes from the page proofs, which were laid out for
readability rather than to a page budget. Measured in Word — "ink" is where the
content actually stops, which matters more than the page count:

| Build | eng-music | eng-only |
|---|---|---|
| v0 (published) | 2 pages | — |
| v1 `--density default` | 3 | 3 |
| v1 `--density tight` | 3 | 2 |
| v2.0 `--density default` | 3 pages / ~2.7 of ink | 3 pages / ~2.6 of ink |
| v2.1 `--density default` | 3 pages / ~2.7 of ink | 3 pages / ~2.7 of ink |
| **v2.2 `--density default`** | **3 pages / ~2.64 of ink** | **3 pages / ~2.65 of ink** |

v2.2 bought back a little room — the text header is shorter than the 1.333in
banner it replaced — and dropped the file from ~130KB to ~41KB, since the PNG
was most of it.

v2.3 and v2.4 are content-only and were not re-measured in Word — v2.3 added
about fifteen words to the command-center entry, v2.4 about a paragraph to each
Education section.

The v2 round ships at default density: Ry set the tolerance at 2.5 pages and both
land just past it, so buying a page back is not worth the compression.

If it ever does matter, `tight` pulls type and leading back without changing the
hierarchy or the coral ration (`brand.DENSITIES`). The lever after that: v0 set
each role as one line (`TITLE — Company | 2023–2026`), where this system gives
the dates their own mono line — about six lines across the document. That is a
small change to `blocks.render_experience`, deliberately not wired up, because it
departs from the design proof.

## Checking the résumés

```powershell
python build.py ; python verify_facts.py   # exit 0 = clean, 1 = drift, says where
```

Five checks against one declared fact table at the top of the script:

1. every role's `(title, org, dates)` appears in `EMPLOYERS`
2. every figure on either page — money, durations, years, headcount — appears in
   `FIGURES` with a note saying what it is
3. every fact in `SHARED` that appears on one résumé appears on both
4. the banner artboards, `brand.CONTACT`, and each `meta.subject` agree
5. the built `.docx` yields the name and every contact detail as extractable
   text, and opens with the name

Check 3 is the one that earns its keep day to day: the two résumés state the
same facts in deliberately different words, so nothing but this stops them
drifting apart. Its reach stops at this folder, though — v2.4 exists because the
`hire/` landing pages carried corrected music facts for two rounds while these
YAMLs carried the wrong ones, and no check here can see that. When a fact lives
in both places, fixing one is half the job. Check 4 keeps the design record and the shipped strings in
agreement — they live in different folders and nothing else couples them.

Check 5 is the odd one out: it reads the built `.docx`, not the YAML, so run
`build.py` first. It exists because the failure it guards was invisible to every
other check and shipped for three versions — see below.

**The fact table is the source of truth.** When a check fails, fix the résumé, or
change the table first and then the résumé — never quietly widen the table to
make a red build green.

*(`verify_verbatim.py` was retired at v2.0. Its contract — "eng-music says
exactly what v0 said" — was a valid question exactly once, for a round that was a
restyling and nothing else.)*

## Layout

```
resume_build/
├── VERSION                  the round version, one line
├── CHANGELOG.md             what changed in each version, newest first
├── build.py                 CLI: parse args, load YAML, call the builder
├── verify_facts.py          the fact table and the four checks
├── docs/
│   └── v2-plan.md           the round plan the current content was built from
├── content/
│   ├── eng_music.yaml       engineering + music, for music-adjacent companies
│   └── eng_only.yaml        engineering, music reduced to subtle depth
└── resumekit/
    ├── brand.py             tokens mirrored from resume_design (colours, sizes, paths)
    ├── styles.py            builds the named Word styles from those tokens
    ├── blocks.py            one renderer per section type
    ├── docx_helpers.py      raw-XML bits python-docx doesn't expose
    └── builder.py           page setup, header, sections, footer, save
```

**Content is data, design is code.** Editing wording means editing YAML and
nothing else. Editing the look means `brand.py` (a value) or `styles.py` (how a
style is composed). If you find yourself putting formatting into a YAML file,
the section type is missing a feature — add it to `blocks.py` instead.

## Content schema

```yaml
meta:
  slug: eng-only              # goes in the build filename
  output_dir: ../eng_only     # relative to resume_build/
  variant: music | eng        # picks the role line
  footer_org: Wolfpack Data & Strategy
sections:
  - type: prose        # title + paragraphs[]
  - type: grid         # title + columns + items[]{label, skills[]}
  - type: experience   # title + roles[]{title, org?, dates?, bullets[]} + closing?
  - type: bullets      # title + bullets[]
  - type: lines        # title + lines[]
  - type: projects     # title + items[]{name, body}
```

Every section also takes an optional `note:` — a small grey parenthetical set
beside the heading. `experience` also takes `closing:`, one body paragraph after
the last role.

## Things that will bite you

**The header must stay text.** The name, role line, and contact line are the
first three paragraphs of the document body. That is not a style preference —
it is the difference between an ATS filing this résumé under Ryan's name and
filing it under no name at all. Check 5 enforces it. The document-wide rules
this belongs to are `../resume_design/ats-guidelines.md`; read them before
adding any image, text box, column, or second table.

**The banner artboards still exist, and still have to agree.**
`resume_design/preview/header-*.png` and the HTML in
`resume_design/templates/export/` are no longer embedded in anything, but they
remain the design record of the header and `brand.ROLE_LINES` / `brand.CONTACT`
are mirrored from them. Change a header string and you change it in both places,
then re-run `resume_design/templates/export-png.ps1`. Check 4 exists because it
is easy to do one and forget the other.

**Page margins are load-bearing.** The design is drawn on a 7.5in text column —
the core-expertise table width and the footer's right tab stop are both measured
off it, so it needs 0.5in side margins on Letter. `builder._setup_page` asserts
it.

**Coral is rationed to three uses** (`brand.CORAL_RATION`): the rule under the
header contact line, the footer hairline, the section-heading underline. All
three are now `set_paragraph_border(..., CORAL, ...)` calls in this codebase —
before v2.2 slot 1 was baked into the banner PNG. Adding a fourth means one of
them has to give it up.

**The footer is Word text, not an image**, so `PAGE`/`NUMPAGES` stay live fields.
Word shows a placeholder `1` until the fields update — that happens on open,
print, or PDF export. Don't "fix" it in the generated file; regenerate.

**Section headings and role titles are stored mixed-case** and displayed
uppercase via `w:caps`. That keeps the underlying text readable to an ATS parser
while looking like the design. Don't type them in caps in the YAML.

**`w:pPr` and `w:rPr` children are an ordered sequence, not a set.** Appending an
element rather than placing it at its schema position produces a file Word opens
but whose layout engine then misbehaves. Use `docx_helpers.get_or_add_ordered()`;
the tag sequences and the story behind them are in that file.

**Roboto and Montserrat** are the brand fonts and are not bundled with Windows.
`build.py` warns on every run if either is missing; `--fonts safe` substitutes
Arial and Corbel. Both were installed on Ry's machine as of v2.0. Since v2.2 the
name is text rather than a PNG, so a missing Roboto now reaches the masthead.

## The header is text

Every build carries a plain-text header — name, role line, contact line, coral
rule — and there is no way to build any other kind.

Through v2.1 the default was a 7.5in picture banner, with the text header
available behind `--header text` for online applications. Extracting the text
from the v2.1 build showed what that actually shipped: the first parseable
string in the document was `Professional Summary`. The name, email, LinkedIn,
GitHub, and location were pixels and nothing else. A parser reading it built a
candidate record with no name and no way to make contact.

The old arrangement was right about the risk and wrong about the remedy: it
depended on choosing the correct export every time, and the cost of choosing
wrong was total. One header, always parseable, removes the choice.

What was given up: the navy banner, the wolf mark, and the RML mark no longer
appear on the résumé. The artboards keep them (`../resume_design/preview/`), and
`header-footer-spec.md` §9 records the one way to put a mark back without
reopening any of this — the wolf at 0.55in, in line with text, beside a name
that is still real text.

Full rationale: `../resume_design/header-footer-spec.md` §9.
