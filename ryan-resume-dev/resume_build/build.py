#!/usr/bin/env python
"""Build Ryan Hickey's résumés from the YAML content files.

    python build.py                      # both, at the version in ./VERSION
    python build.py --only eng-only
    python build.py --release            # drop the version from the filename
    python build.py --density tight      # pull spacing back toward v0
    python build.py --fonts safe         # substitute installed fonts

Outputs land next to the résumé they belong to (eng_music_combo/, eng_only/).

The header is plain text — name, role line, contact line — on every build. The
image banner was removed at v2.2; see resumekit/builder.py for why.

Versioning: one version per round, both résumés, held in ./VERSION as a single
line (`2.0`). Build artifacts carry it — `Ryan_Hickey_Resume_eng-music_v2.0.docx`
— so a later round can tell which wording an application actually went out with.
`--release` writes `Ryan_Hickey_Resume.docx` instead: a recruiter should never
see a version string in the filename. Every iteration appends to CHANGELOG.md.
"""

from __future__ import annotations

import argparse
import sys
import winreg
from pathlib import Path

import yaml

from resumekit import brand, build_resume

HERE = Path(__file__).resolve().parent
CONTENT_DIR = HERE / "content"
VERSION_FILE = HERE / "VERSION"

TARGETS = {
    "eng-music": CONTENT_DIR / "eng_music.yaml",
    "eng-only": CONTENT_DIR / "eng_only.yaml",
}


def read_version() -> str:
    """The round version, e.g. '2.0'. One value for both résumés."""
    v = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not v:
        raise ValueError(f"{VERSION_FILE} is empty")
    return v


def output_path(meta: dict, version: str, release: bool, suffix: str) -> Path:
    """<output_dir>/Ryan_Hickey_Resume[_<slug>_v<version>][<suffix>].docx"""
    out_dir = (HERE / meta["output_dir"]).resolve()
    stem = "Ryan_Hickey_Resume"
    if not release:
        stem += f"_{meta['slug']}_v{version}"
    return out_dir / f"{stem}{suffix}.docx"


def installed_font_families() -> set[str]:
    """Registered font names, so we can warn before Word silently substitutes."""
    names: set[str] = set()
    for hive, key in (
        (winreg.HKEY_LOCAL_MACHINE,
         r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"),
        (winreg.HKEY_CURRENT_USER,
         r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"),
    ):
        try:
            with winreg.OpenKey(hive, key) as k:
                for i in range(winreg.QueryInfoKey(k)[1]):
                    names.add(winreg.EnumValue(k, i)[0])
        except OSError:
            continue
    return names


def warn_missing_fonts(fonts: dict) -> None:
    try:
        installed = installed_font_families()
    except Exception:          # non-Windows, or a locked registry — not fatal
        return
    missing = [
        f for f in {fonts["display"], fonts["body"], fonts["mono"]}
        if not any(name.startswith(f) for name in installed)
    ]
    if not missing:
        return
    print(
        f"  ! {', '.join(sorted(missing))} not installed — Word will substitute.\n"
        f"    Install from fonts.google.com, or rebuild with --fonts safe.\n"
        f"    (Since v2.2 the header is text too, so this reaches the name.)",
        file=sys.stderr,
    )


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        content = yaml.safe_load(f)
    for key in ("meta", "sections"):
        if key not in content:
            raise ValueError(f"{path.name} is missing top-level '{key}'")
    return content


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", choices=sorted(TARGETS),
                    help="build one résumé instead of both")
    ap.add_argument("--density", choices=sorted(brand.DENSITIES),
                    help="body spacing; 'tight' pulls back toward v0's page count")
    ap.add_argument("--fonts", choices=sorted(brand.FONT_SETS), default="brand",
                    help="brand = Roboto/Montserrat; safe = installed substitutes")
    ap.add_argument("--suffix", default="",
                    help="appended to the output filename stem")
    ap.add_argument("--release", action="store_true",
                    help="write Ryan_Hickey_Resume.docx — no version in the name")
    args = ap.parse_args(argv)

    version = read_version()
    fonts = brand.FONT_SETS[args.fonts]
    warn_missing_fonts(fonts)

    targets = {args.only: TARGETS[args.only]} if args.only else TARGETS
    failures = 0

    for name, yaml_path in targets.items():
        if not yaml_path.exists():
            print(f"  x {name}: {yaml_path} not found", file=sys.stderr)
            failures += 1
            continue

        content = load(yaml_path)
        out = output_path(content["meta"], version, args.release, args.suffix)

        try:
            written = build_resume(
                content, out,
                fonts=fonts, density=args.density, version=version,
            )
        except Exception as exc:
            print(f"  x {name}: {type(exc).__name__}: {exc}", file=sys.stderr)
            failures += 1
            continue

        size_kb = written.stat().st_size / 1024
        rel = written.resolve().relative_to(HERE.parent)
        print(f"  + {name:10s} -> {rel}  ({size_kb:,.0f} KB)")

    print(f"    version {version}" + ("  (release build)" if args.release else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
