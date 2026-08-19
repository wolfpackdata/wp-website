# cover_letters — application-ready letters on the résumé's stationery

Each cover letter is a small YAML file here, built into a `.docx` by
`../resume_build/cover_letter.py`. The letter matches the résumés by
construction: `resumekit/letter.py` reuses the résumé builder's own header,
footer, page geometry, and styles, so the two share one design and cannot
drift apart.

## The workflow

Ry hands a session the letter text (and the company/role). The session:

```powershell
# 1. copy the template
cp _template.yaml 2026-08-18-acme.yaml       # YYYY-MM-DD-company

# 2. fill meta + paragraphs with the supplied text, verbatim

# 3. build (from ../resume_build)
cd ..\resume_build
python cover_letter.py ..\cover_letters\2026-08-18-acme.yaml          # .docx
python cover_letter.py ..\cover_letters\2026-08-18-acme.yaml --pdf    # + PDF
```

Output lands next to the YAML as `Ryan_Hickey_Cover_Letter_<Company>.docx` —
no version in the name; letters are one-offs and the YAML is the record of
what went out. `--pdf` converts through Word (same engine as the résumé PDFs)
so the PDF paginates exactly like the DOCX.

## Conventions

- **The sign-off is always "Warmly," / Ryan.** It is the builder's default —
  letter YAMLs don't state it, and a letter text that arrives with a different
  sign-off still ships with this one unless Ry says otherwise.
- **The letter text is Ry's, verbatim.** The YAML carries it one item per
  paragraph; the builder never rewords, trims, or reflows. Editing the letter
  means editing the YAML and rebuilding — never the generated `.docx`.
- **`meta.variant` matches the résumé the letter travels with** — `eng` for
  the engineering résumé, `music` for eng-music. It picks the header role
  line, the same switch the résumé builds use.
- **`_template.yaml` is copied, never filled in place.** Its built twin,
  `Ryan_Hickey_Cover_Letter_Template.docx`, is the committed design proof —
  rebuild it (`python cover_letter.py --template`) whenever the stationery or
  letter styles change.
- **Design is code.** Wording lives in YAML; look-and-feel lives in
  `resume_build/resumekit/` (`brand.py` letter metrics, `styles.py`
  `build_letter_styles`, `letter.py`). Formatting never goes in a YAML file.
- This folder ships nothing — like the résumé folders, it exists for
  applications Ry sends directly.
