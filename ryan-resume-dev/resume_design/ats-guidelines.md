# ATS compatibility — design guidelines

**A résumé is read by a parser before it is read by a person.** If the parser
files it badly, the design never gets an audience. So on this package ATS
compatibility is a **critical constraint on the design**, ranked with legibility
and brand — not a compliance checkbox applied afterwards.

That ordering is not theoretical here. It was learned the expensive way; §2 is
the receipt.

Scope: this document covers the whole `.docx`. The header specifically is
`header-footer-spec.md` §9.

---

## 1. The rule

> Every fact a human needs in order to act on this résumé — who it is, how to
> reach them, where they worked, when — must survive being reduced to plain
> text with all formatting discarded.

Anything that fails that test is a defect, however good it looks. Anything that
passes is fair game, including tables, colour, and unusual type.

The corollary matters as much: **this is not a licence to design badly.** ATS
folklore ("no tables ever", "no colour", "one column or nothing") mostly
predates the parsers in use now, and most of it is unverified. Test the claim
against the actual file — §5 — and design freely inside what survives.

## 2. What went wrong, and how it was found

Through v2.1 the header was a 7.5in PNG. Extracting the text from
`Ryan_Hickey_Resume_eng-only_v2.1.docx` — every `<w:t>` in
`word/document.xml`, roughly what a parser sees — produced this as the **first
string in the document**:

```
Professional Summary
```

The name, email, LinkedIn, GitHub, and location appeared **nowhere** in the text
stream. All of them were pixels. A parser reading that file built a candidate
record with no name and no way to make contact. The only live contact text in
the whole document was the email in the Word footer — which is in
`word/footer1.xml`, a part a good number of parsers skip.

That shipped in v1.0, v2.0, and v2.1. Nothing in the build or the fact-checker
noticed, because every check ran against the YAML, and in the YAML everything
looked present and correct. **The failure was invisible at the layer we were
checking.** That is the general lesson: ATS defects live in the artifact, not in
the source, so they have to be checked in the artifact.

v2.2 removed the image header. `verify_facts.py` **check 5** now reads the built
`.docx` and fails unless the name and every contact detail extract as text and
the document opens with the name.

## 3. What this document is, structurally

Verified against the v2.2 build, not assumed:

| Feature | Count | Verdict |
|---|---|---|
| Images (`w:drawing`) | **0** | Nothing whatsoever is carried by a picture |
| Tables (`w:tbl`) | 1 | Core Expertise. Fine — see below |
| Text boxes (`w:txbxContent`) | 0 | Never use one; parsers routinely drop them |
| Section columns | 1 | Single-column document flow |
| Real list numbering (`w:numPr`) | 0 | Bullets are literal glyphs — see §6 |
| Field codes in the body | 0 | `PAGE`/`NUMPAGES` live in the footer only |
| Styles applying `w:caps` | 5 | Display-only uppercase — see below |

**The table is not a problem, and it was worth checking rather than assuming.**
An outside review claimed the two-column Core Expertise section "extracts in a
scrambled reading order." It doesn't. `blocks.render_grid` fills the table
row-major, so document order *is* reading order, and each label is immediately
followed by its own skill list:

```
AI Engineering & Agent Development
Prompt Engineering · Claude Code · Claude Skills & Subagents · …
Software Engineering & Architecture
Python · SQL · VBA & Advanced Excel · …
```

A minority of legacy parsers dislike tables categorically, and that is a real
if small cost. It is paid knowingly for a layout that puts six skill groups in
the space of three. Keep it to **one** table, keep it **borderless and
row-major**, and never nest one.

**Uppercase is display-only.** Section headings and role titles are *stored*
mixed-case and rendered uppercase by `w:caps` in the style. The parser reads
`Professional Experience`, the reader sees `PROFESSIONAL EXPERIENCE`. Never type
caps into the YAML — you would lose that for nothing.

**The Word footer carries nothing exclusively.** Name, email, and org appear
there for the human, and every one of them also appears in the body header. A
parser that skips `footer1.xml` entirely loses no fact.

## 4. Rules for anything added later

1. **No fact may exist only as an image.** There are currently zero images. If
   one is ever added — the wolf mark beside the name is the sanctioned case,
   `header-footer-spec.md` §9 — it must be decoration sitting next to real text
   that already says the same thing.
2. **Nothing load-bearing in the Word header or footer parts.** Body text only.
3. **No text boxes, no floating shapes, no multi-column section breaks.**
   In-line content in a single flow.
4. **Contact details go in the body, at the top, as the first thing.** Not
   merely present — *first*. Parsers weight document position when guessing
   which string is the candidate's name.
5. **Store text in its natural case**; do case transforms in the style.
6. **Dates stay in a form a parser can read as a range** — `2015–2025` on its
   own line under the role. Don't fold them into prose.
7. **Ship `.docx`, not PDF**, when a portal accepts either. Word documents parse
   more reliably and more consistently than PDFs, which have to be reconstructed
   from positioned glyphs.
8. **Fonts don't affect extraction.** Roboto/Montserrat missing is a visual
   problem (`--fonts safe`), never a parsing one. Don't trade type quality for
   imagined ATS safety.
9. **Re-run check 5 after any change to `builder.py` or the styles.** It is
   cheap and it is the only thing standing between this and a repeat of §2.

## 5. How to check a claim instead of believing it

Most ATS advice is folklore. The file is right here — read it:

```powershell
cd ..\resume_build ; python build.py ; python verify_facts.py
```

For an ad-hoc look at exactly what a parser sees:

```python
from verify_facts import docx_text
print(docx_text("../eng_only/Ryan_Hickey_Resume_eng-only_v2.2.docx")[:400])
```

`docx_text` deliberately ignores images and the header/footer parts, because a
good number of parsers do too. If a fact isn't in that string, it isn't in the
résumé as far as an ATS is concerned.

## 6. Known compromise

**Bullets are a literal `▸` character plus a tab, not a Word list.** Every
bullet extracts as `▸\tBuilt the company's first quantitative insights…`. Most
parsers strip leading punctuation; `▸` (U+25B8) is uncommon enough that some
won't. The cost is a stray glyph at the head of a bullet, not a lost fact, so it
has not been changed — but a real `w:numPr` list, or a plain `•`, would remove it
if a parser is ever seen mangling it.

## 7. What is deliberately not done

- **No keyword stuffing, and no white-on-white text.** Both are detectable, both
  are read as dishonest by any human who finds them, and the résumé's actual
  problem was never keyword density.
- **The table stays.** See §3 — the reading order was tested, not assumed.
- **Colour and the coral ration stay.** Neither affects text extraction at all.
- **The page count is not being cut for ATS reasons.** Length is a human-reader
  question; parsers do not care.
