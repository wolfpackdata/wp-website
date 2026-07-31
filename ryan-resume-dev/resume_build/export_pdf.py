#!/usr/bin/env python
"""Export both résumés to PDF and stage all four downloads for the hire pages.

    python build.py ; python verify_facts.py ; python export_pdf.py

Reads the version from ./VERSION, finds the .docx each variant's build wrote,
converts it to PDF through Word, and copies the .docx/.pdf pair into
../../hire/assets/dl/ under the names the public pages link.

Why Word and not LibreOffice: the .docx was laid out by Word, so converting with
the same engine is the only way to guarantee the PDF paginates identically. A
résumé that reflows in conversion is a different document.

Why the rename is scripted: the build artifacts carry a version
(`Ryan_Hickey_Resume_eng-only_v2.2.docx`) so a later round can tell which wording
an application went out with — but a hiring manager should never see a version
string in their downloads folder. Doing the rename here, rather than by hand,
is what stops a rebuilt résumé from leaving a stale file on the pages.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERSION_FILE = HERE / "VERSION"
DOWNLOAD_DIR = HERE.parent.parent / "hire" / "assets" / "dl"

# Word's ExportAsFixedFormat enumerations. Hard-coded rather than pulled from
# the type library so the script runs without a generated COM cache.
WD_EXPORT_FORMAT_PDF = 17
WD_EXPORT_OPTIMIZE_FOR_PRINT = 0
WD_EXPORT_ALL_DOCUMENT = 0
WD_EXPORT_DOCUMENT_WITH_MARKUP = 7
WD_DO_NOT_SAVE_CHANGES = 0

# variant slug -> (build output dir, public download stem)
VARIANTS = {
    "eng-only": (HERE.parent / "eng_only", "Ryan-Hickey-Resume"),
    "eng-music": (HERE.parent / "eng_music_combo", "Ryan-Hickey-Resume-Music"),
}


def read_version() -> str:
    v = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not v:
        raise ValueError(f"{VERSION_FILE} is empty")
    return v


def source_docx(out_dir: Path, slug: str, version: str) -> Path:
    """The .docx build.py just wrote, versioned or --release."""
    versioned = out_dir / f"Ryan_Hickey_Resume_{slug}_v{version}.docx"
    if versioned.exists():
        return versioned
    release = out_dir / "Ryan_Hickey_Resume.docx"
    if release.exists():
        return release
    raise FileNotFoundError(
        f"No built resume in {out_dir} for v{version}. Run `python build.py` first."
    )


def export(pairs: list[tuple[Path, Path]]) -> None:
    """Convert each (docx, pdf) pair through one Word instance."""
    try:
        import win32com.client
    except ImportError:
        sys.exit(
            "pywin32 is required for PDF export:  pip install pywin32\n"
            "(The .docx builds fine without it - only this step needs Word.)"
        )

    word = None
    try:
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = False

        for src, pdf in pairs:
            doc = word.Documents.Open(str(src), ReadOnly=True, Visible=False)
            try:
                doc.ExportAsFixedFormat(
                    OutputFileName=str(pdf),
                    ExportFormat=WD_EXPORT_FORMAT_PDF,
                    OpenAfterExport=False,
                    OptimizeFor=WD_EXPORT_OPTIMIZE_FOR_PRINT,
                    Range=WD_EXPORT_ALL_DOCUMENT,
                    Item=WD_EXPORT_DOCUMENT_WITH_MARKUP,
                    IncludeDocProps=True,
                    KeepIRM=True,
                    CreateBookmarks=1,        # wdExportCreateHeadingBookmarks
                    DocStructureTags=True,    # tagged PDF — the parseability property
                    BitmapMissingFonts=True,
                    UseISO19005_1=False,
                )
            finally:
                doc.Close(WD_DO_NOT_SAVE_CHANGES)
            print(f"  PDF   {pdf.name}")
    finally:
        # Always quit: a stranded headless WINWORD keeps a file handle open and
        # the next run fails with a lock nobody can see in Task Manager.
        if word is not None:
            word.Quit()


def main() -> int:
    version = read_version()
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Staging resume downloads (v{version}) -> {DOWNLOAD_DIR}")

    pairs = []
    for slug, (out_dir, stem) in VARIANTS.items():
        src = source_docx(out_dir, slug, version)
        docx_dest = DOWNLOAD_DIR / f"{stem}.docx"
        shutil.copy2(src, docx_dest)
        print(f"  DOCX  {docx_dest.name}   <- {src.name}")
        pairs.append((src, DOWNLOAD_DIR / f"{stem}.pdf"))

    export(pairs)

    print("\nDone. Four artifacts staged:")
    for f in sorted(DOWNLOAD_DIR.iterdir()):
        print(f"  {f.name}  ({f.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
