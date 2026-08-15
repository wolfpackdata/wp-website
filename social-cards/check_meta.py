#!/usr/bin/env python
"""Check every deploying page's <head> for a complete, self-consistent social card.

WHY THIS EXISTS
---------------
A link preview is assembled from four things that live in four different places:
the page's `<link rel="canonical">`, its `og:` block, its `twitter:card`, and an
image file sitting in some other folder that only reaches the public through a
manual copy into `wolfpackdata/ai-coaching-intake`. Nothing in this repo made
those four agree, so a correction could land in one of them and not the others
and nothing could see the gap — the identical failure mode
`ryan-resume-dev/resume_build/verify_facts.py` exists for, where a fact was
fixed on a page and not in the YAML it was copied from.

The gap is not hypothetical here either. Two public, indexed, client-facing case
studies shipped with zero `og:` tags each; `roi-calculator/` shipped with no
canonical at all; `ai-coaching/` shipped a text-only card because it had a title
and a description but no image. All four were found by a manual sweep in August
2026, which is exactly the kind of sweep a script should be doing.

The subtlety this script is really guarding is the deploy mapping. `og:image`
must be an absolute `https://intake.wolfstrategyllc.com/...` URL, and the folder
it names is frequently NOT the folder the file lives in here:

    intake /sm3-assets/...              ->  sm3-specific-pages/sm3-assets/...
    intake /case-study-assets/...       ->  case_studies/case-study-assets/...
    intake /ops-fin-model-case-study/   ->  case_studies/ops_fin_model_support/
    intake /rates_public/               ->  rates/

A relative-path habit, or a path written from the repo layout rather than the
deployed one, produces a URL that 404s only after the copy is made and only for
the scraper — never in a local browser. LinkedIn caches a preview for roughly a
week, so a card that scrapes wrong stays wrong past the moment it mattered.

WHEN TO RUN IT
--------------
    python social-cards/check_meta.py     # from the repo root
    # exit 0 = clean, 1 = drift, and it says which page and which check

Run it before any PR that touches a page `<head>`, before generating or
replacing a card image, and again before a deploy copy into the intake repo —
it is verification step 5 of the social-cards plan
(`docs/social-cards-and-linkedin-readiness-plan.md` §9). It is stdlib only, so
it needs no environment: no Pillow, no pip install, no network. It reads the
image dimensions itself, straight out of the PNG IHDR chunk and the JPEG SOF
marker, so a declared `og:image:width` that no longer matches the file is caught
rather than trusted.

What it deliberately does NOT check: `og:site_name`. `hire/` and `github/` omit
it on purpose (plan D-013 declined the retro-add), so requiring it would make
this script fail on pages that are correct.
"""

from __future__ import annotations

import html
import struct
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent

HOST = "https://intake.wolfstrategyllc.com"

# --------------------------------------------------------------------------
# The page table. Every index.html in this repo that reaches the public, and
# the URL path it reaches it at. Folder name is NOT the URL path for four of
# them — that mismatch is half of what this script is for.
#
# Add a row here when a new page folder ships. A page missing from this table
# is a page nothing is guarding.
# --------------------------------------------------------------------------
PAGES = [
    ("roi-calculator/index.html", "/roi-calculator/"),
    ("rates/index.html", "/rates_public/"),
    ("ai-coaching/index.html", "/ai-coaching/"),
    ("hire/ryan-hickey/index.html", "/hire/ryan-hickey/"),
    ("hire/ryan-hickey-music/index.html", "/hire/ryan-hickey-music/"),
    ("portfolio/index.html", "/portfolio/"),
    ("github/index.html", "/github/"),
    ("case_studies/ops_fin_model_support/index.html", "/ops-fin-model-case-study/"),
    # The music-gear M&A case study. Its folder also ships transaction-map.html,
    # which is deliberately NOT a row here: it is `noindex`, it is reached only
    # from the report's "Open full width" affordance, and it carries no og: block
    # to guard. Nothing is being missed — a card exists so a page survives being
    # pasted somewhere, and that page is the report.
    ("case_studies/consolidation_under_pressure/index.html", "/consolidation-under-pressure/"),
    ("case_studies/wolfpack-ai-command/index.html", "/wolfpack-ai-command/"),
    ("sm3-specific-pages/setmaster3/index.html", "/setmaster3/"),
    ("sm3-specific-pages/setmaster3-case-study/index.html", "/setmaster3-case-study/"),
]

# Shared asset folders that deploy to the intake root beside the page folders.
# The page folders themselves are derived from PAGES below, so they are never
# stated twice and can never disagree with the page table.
SHARED_ASSET_MAP = {
    "/sm3-assets/": "sm3-specific-pages/sm3-assets/",
    "/case-study-assets/": "case_studies/case-study-assets/",
}

# The meta set every page must carry, and the attribute each one is keyed by.
# og:* are `property=`, twitter:* are `name=` — but this script accepts either
# spelling, because a card renders the same and the distinction is not the
# defect worth failing a build over.
REQUIRED = (
    "og:type",
    "og:title",
    "og:description",
    "og:url",
    "og:image",
    "twitter:card",
)

# Required in addition when the card is a large-image card: a scraper that gets
# no dimensions may skip the crop it would otherwise do, and alt text is the
# only thing a screen reader gets from a card that is otherwise pure image.
LARGE_CARD_EXTRAS = ("og:image:width", "og:image:height", "og:image:alt")

LARGE_CARD = "summary_large_image"


# --------------------------------------------------------------------------
# Head parsing
# --------------------------------------------------------------------------


class HeadMeta(HTMLParser):
    """Collect <link rel=...> and <meta> from a document's <head>.

    Stops at </head> so a `<meta>` inside the body (or inside a JSON-LD block
    that got mangled) cannot be mistaken for a card tag.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.done = False
        # key -> list of content strings, in document order. A list rather than
        # a scalar so duplicates are visible instead of last-one-wins.
        self.meta: dict[str, list[str]] = {}
        self.links: dict[str, list[str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.done:
            return
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta":
            key = a.get("property") or a.get("name")
            if key:
                self.meta.setdefault(key.strip().lower(), []).append(
                    html.unescape(a.get("content", "")).strip()
                )
        elif tag == "link":
            rel = a.get("rel", "").strip().lower()
            if rel:
                self.links.setdefault(rel, []).append(
                    html.unescape(a.get("href", "")).strip()
                )

    def handle_endtag(self, tag: str) -> None:
        if tag == "head":
            self.done = True


def read_head(path: Path) -> HeadMeta:
    parser = HeadMeta()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


# --------------------------------------------------------------------------
# Deploy mapping — intake URL path -> repo path
# --------------------------------------------------------------------------


def deploy_map() -> dict[str, str]:
    """intake-path prefix -> repo-path prefix, longest match wins.

    Page folders come from PAGES so the two can never drift; shared asset
    folders are the only hand-written rows. Anything unmatched maps 1:1.
    """
    mapping = dict(SHARED_ASSET_MAP)
    for repo_path, url_path in PAGES:
        repo_dir = str(Path(repo_path).parent).replace("\\", "/") + "/"
        mapping[url_path] = repo_dir
    return mapping


def url_to_repo_path(url: str) -> str | None:
    """Map an absolute intake URL to the repo path the file lives at.

    Returns None if the URL is not on the intake host at all — check 4 reports
    that separately, since it is a different mistake from a wrong folder.
    """
    if not url.startswith(HOST + "/"):
        return None
    path = url[len(HOST):]
    path = path.split("?", 1)[0].split("#", 1)[0]

    mapping = deploy_map()
    for prefix in sorted(mapping, key=len, reverse=True):
        if path.startswith(prefix):
            return mapping[prefix] + path[len(prefix):]
    return path.lstrip("/")


# --------------------------------------------------------------------------
# Tracked-file index
# --------------------------------------------------------------------------


def tracked_files() -> tuple[set[str] | None, str | None]:
    """The `git ls-files` set, or (None, warning) if git is unavailable.

    Tracked-ness — not mere existence — is the right test: the deploy copies
    the git-tracked file list, not the folder (`sm3-assets/` holds a gitignored
    capture that leaks a Windows user directory), so an untracked image is one
    that will simply not be there after the copy.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "ls-files"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        return None, f"git unavailable ({exc.__class__.__name__}) — falling back to os.path.exists; an UNTRACKED image will pass this run and vanish on deploy"
    return {line.strip() for line in out.stdout.splitlines() if line.strip()}, None


# --------------------------------------------------------------------------
# Image dimensions, stdlib only (no Pillow — this script must run bare)
# --------------------------------------------------------------------------

PNG_SIG = b"\x89PNG\r\n\x1a\n"
# SOF markers that carry a frame header. 0xC4 (DHT), 0xC8 (JPG), 0xCC (DAC)
# share the range and are not frame headers.
JPEG_SOF = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


def png_size(data: bytes) -> tuple[int, int] | None:
    if not data.startswith(PNG_SIG) or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def jpeg_size(data: bytes) -> tuple[int, int] | None:
    if not data.startswith(b"\xff\xd8"):
        return None
    i = 2
    end = len(data)
    while i + 3 < end:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        if marker == 0xFF:          # fill byte
            i += 1
            continue
        if i + 4 > end:
            return None
        seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker in JPEG_SOF:
            if i + 9 > end:
                return None
            height, width = struct.unpack(">HH", data[i + 5:i + 9])
            return width, height
        i += 2 + seg_len
    return None


def image_size(path: Path) -> tuple[int, int] | None:
    """(width, height), or None if the format is not one we can read."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    return png_size(data) or jpeg_size(data)


# --------------------------------------------------------------------------
# The checks
# --------------------------------------------------------------------------


def one(values: list[str]) -> str:
    return values[0] if values else ""


def check_page(
    repo_path: str,
    url_path: str,
    tracked: set[str] | None,
    errors: list[str],
) -> None:
    """Run checks 1-5 against one page, appending a line per failure.

    Every failure line names the page, the check number, what was found, and
    what to do about it — a bare "missing tag" on a ten-page sweep costs more
    time to act on than it saves to emit.
    """
    label = repo_path
    path = REPO_ROOT / repo_path
    if not path.is_file():
        errors.append(
            f"{label}: PAGES names a page that does not exist — {path}\n"
            f"    if the page was removed or moved, remove or update its row"
        )
        return

    head = read_head(path)
    expected_canonical = HOST + url_path

    # -- check 1: canonical present and correct ----------------------------
    canonicals = head.links.get("canonical", [])
    if not canonicals:
        errors.append(
            f"{label}: 1. no <link rel=\"canonical\"> in <head>\n"
            f"    add: <link rel=\"canonical\" href=\"{expected_canonical}\">"
        )
    elif len(canonicals) > 1:
        errors.append(
            f"{label}: 1. {len(canonicals)} <link rel=\"canonical\"> tags — exactly one is allowed\n"
            + "".join(f"    found: {c!r}\n" for c in canonicals).rstrip()
        )
    elif canonicals[0] != expected_canonical:
        errors.append(
            f"{label}: 1. canonical does not match this page's deployed URL\n"
            f"    found:    {canonicals[0]!r}\n"
            f"    expected: {expected_canonical!r}\n"
            f"    fix the tag, or fix this page's row in PAGES if the URL moved"
        )
    canonical = one(canonicals)

    # -- check 2: the required meta set, non-empty, no duplicates ----------
    for key in REQUIRED:
        values = head.meta.get(key, [])
        if not values:
            errors.append(
                f"{label}: 2. missing <meta> {key}\n"
                f"    the card renders without it, wrongly — see plan §5 for the block to add"
            )
        elif len(values) > 1:
            errors.append(
                f"{label}: 2. duplicate <meta> {key} — {len(values)} copies, scrapers disagree on which wins\n"
                + "".join(f"    found: {v!r}\n" for v in values).rstrip()
            )
        elif not values[0]:
            errors.append(
                f"{label}: 2. <meta> {key} is present but empty\n"
                f"    an empty content= is worse than a missing tag: it looks intentional"
            )

    og_url = one(head.meta.get("og:url", []))
    og_image = one(head.meta.get("og:image", []))
    twitter_card = one(head.meta.get("twitter:card", []))

    # -- check 3: og:url == canonical, exactly -----------------------------
    if og_url and canonical and og_url != canonical:
        at = next(
            (i for i, (a, b) in enumerate(zip(og_url, canonical)) if a != b),
            min(len(og_url), len(canonical)),
        )
        errors.append(
            f"{label}: 3. og:url does not equal the canonical href\n"
            f"    diverges at character {at}\n"
            f"    og:url:    {og_url!r}\n"
            f"    canonical: {canonical!r}\n"
            f"    they must be byte-identical — a trailing slash counts"
        )

    # -- check 4: og:image absolute, on the intake host, and tracked -------
    image_repo_path: str | None = None
    if og_image:
        if not og_image.startswith("https://"):
            errors.append(
                f"{label}: 4. og:image is not an absolute https URL — {og_image!r}\n"
                f"    a relative og:image resolves against the scraper, not the page; "
                f"it must start with {HOST}/"
            )
        elif not og_image.startswith(HOST + "/"):
            errors.append(
                f"{label}: 4. og:image is not on the deploy host — {og_image!r}\n"
                f"    expected a URL under {HOST}/ ; this repo serves nothing itself"
            )
        else:
            image_repo_path = url_to_repo_path(og_image)
            full = REPO_ROOT / image_repo_path
            if tracked is None:
                if not full.is_file():
                    errors.append(
                        f"{label}: 4. og:image names a file that is not in this repo\n"
                        f"    url:  {og_image}\n"
                        f"    maps to: {image_repo_path}\n"
                        f"    (git was unavailable; existence checked, tracked-ness not)"
                    )
            elif image_repo_path not in tracked:
                where = "exists on disk but is UNTRACKED" if full.is_file() else "does not exist"
                errors.append(
                    f"{label}: 4. og:image {where} after the deploy mapping\n"
                    f"    url:     {og_image}\n"
                    f"    maps to: {image_repo_path}\n"
                    f"    the deploy copies the git-tracked file list, not the folder — "
                    f"an untracked image will 404 on the live card"
                )

    # -- check 5: large-image cards need dimensions and alt, and the -------
    #             declared dimensions must match the actual file
    if twitter_card == LARGE_CARD:
        for key in LARGE_CARD_EXTRAS:
            values = head.meta.get(key, [])
            if not values or not values[0]:
                errors.append(
                    f"{label}: 5. twitter:card is {LARGE_CARD} but {key} is missing or empty\n"
                    f"    a large card without dimensions can be cropped wrong, and "
                    f"without alt it is unreadable to a screen reader"
                )
            elif len(values) > 1:
                errors.append(
                    f"{label}: 5. duplicate <meta> {key} — {len(values)} copies\n"
                    + "".join(f"    found: {v!r}\n" for v in values).rstrip()
                )

        declared_w = one(head.meta.get("og:image:width", []))
        declared_h = one(head.meta.get("og:image:height", []))
        if image_repo_path and declared_w and declared_h:
            full = REPO_ROOT / image_repo_path
            if full.is_file():
                actual = image_size(full)
                if actual is None:
                    errors.append(
                        f"{label}: 5. cannot read the dimensions of {image_repo_path}\n"
                        f"    only PNG and JPEG are readable here; declared "
                        f"{declared_w}x{declared_h} is unverified"
                    )
                else:
                    try:
                        want = (int(declared_w), int(declared_h))
                    except ValueError:
                        errors.append(
                            f"{label}: 5. og:image:width/height are not integers — "
                            f"{declared_w!r} x {declared_h!r}"
                        )
                    else:
                        if want != actual:
                            errors.append(
                                f"{label}: 5. declared og:image dimensions do not match the file\n"
                                f"    declared: {want[0]}x{want[1]}\n"
                                f"    actual:   {actual[0]}x{actual[1]}  ({image_repo_path})\n"
                                f"    fix the tags, or rebuild the card at the declared size"
                            )


# --------------------------------------------------------------------------


def main() -> int:
    # Windows consoles default to cp1252, which mangles the em dashes this
    # script's own messages use. Failure output that is itself hard to read is
    # a bad guard, so ask for UTF-8 where the runtime supports it.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
        except (AttributeError, OSError, ValueError):
            pass

    errors: list[str] = []
    tracked, warning = tracked_files()
    if warning:
        print(f"warning: {warning}\n", file=sys.stderr)

    per_page: list[tuple[str, int]] = []
    for repo_path, url_path in PAGES:
        before = len(errors)
        check_page(repo_path, url_path, tracked, errors)
        per_page.append((repo_path, len(errors) - before))

    width = max(len(p) for p, _ in per_page)
    for repo_path, count in per_page:
        status = "PASS" if count == 0 else f"FAIL ({count})"
        print(f"  {repo_path.ljust(width)}  {status}")
    print()
    sys.stdout.flush()  # so the table lands above the stderr detail, not after it

    if errors:
        failing = sum(1 for _, c in per_page if c)
        print(
            f"FAIL — {len(errors)} problem(s) across {failing} of {len(PAGES)} page(s)\n",
            file=sys.stderr,
        )
        for e in errors:
            print(f"  x {e}", file=sys.stderr)
        return 1

    print(
        f"OK — {len(PAGES)} pages: canonical matches the deployed URL, "
        f"{len(REQUIRED)} required tags present and unique, og:url == canonical, "
        f"every og:image absolute, tracked, and correctly sized."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
