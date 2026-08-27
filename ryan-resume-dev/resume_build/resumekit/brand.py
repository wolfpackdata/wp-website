"""Brand tokens, mirrored from ../../resume_design/.

Single source of truth for the DOCX side of the design system. Every value here
has a counterpart in resume_design/templates/css/resume-brand.css or a rule in
resume_design/header-footer-spec.md; the comment on each says which.

Change a value here and the spec is now wrong. Update both.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# Palette — spec §4. Hex without '#', which is what RGBColor.from_string wants.
# --------------------------------------------------------------------------
NAVY = "000B29"      # the name, section headings, role titles
CORAL = "F95954"     # RATIONED — see CORAL_RATION below
INK_70 = "4A5068"    # body copy, footer text          7.9:1 on white
INK_45 = "6B7186"    # dates, separators, page number  4.8:1 on white (AA floor)
INK_SEP = "9AA0B0"   # decorative separators only      below AA — never words
RULE = "D8DBE4"      # hairlines on white

# Coral appears in exactly three places across the whole résumé (spec §4).
# All three are Word paragraph borders since v2.2 — before that slot 1 was
# baked into the banner PNG and this module owned only 2 and 3.
CORAL_RATION = (
    "1. header contact-line bottom rule",
    "2. footer top hairline",
    "3. section-heading underline",
)

# --------------------------------------------------------------------------
# Fonts — brand-reference.md §4.
#
# Word has no font stacks, so the CSS monospace stack collapses to Consolas:
# it is in the site's stack and ships with Windows. Roboto and Montserrat do
# NOT ship with Windows — build.py warns when they are missing and --fonts safe
# swaps in substitutes that are actually installed.
# --------------------------------------------------------------------------
FONT_SETS = {
    "brand": {"display": "Roboto", "body": "Montserrat", "mono": "Consolas"},
    "safe": {"display": "Arial", "body": "Corbel", "mono": "Consolas"},
}


@dataclass
class Metrics:
    """Type and spacing, in points and inches. Spec §3 and the page proofs.

    Deliberately NOT frozen: apply_density() mutates the single shared instance
    in place, because styles.py and blocks.py bind `METRICS` at import time and
    rebinding the module attribute would not reach them.
    """

    # Page — spec §8 step 1. The 7.5in text column depends on 0.5in margins.
    margin_in: float = 0.5
    footer_distance_in: float = 0.42          # spec §7 step 1

    # Gap between the header block and the first section — spec §8 step 2.
    # Named banner_space_after_pt through v2.1, when the header was a PNG.
    header_space_after_pt: float = 6.0

    # Section heading — proof `.proof__h`
    section_pt: float = 9.5
    section_tracking_pt: float = 1.2          # ≈ 0.13em at 9.5pt
    section_space_before_pt: float = 10.0
    section_space_after_pt: float = 3.0
    section_rule_eighths: int = 18            # 2.25pt — coral slot 3
    section_rule_gap_pt: int = 3

    # Role title + date line — proof `.proof__jt` / `.proof__jm`
    role_pt: float = 9.0
    role_tracking_pt: float = 0.2
    role_space_before_pt: float = 7.0
    meta_pt: float = 7.0
    meta_tracking_pt: float = 0.35

    # Body copy and bullets — proof `.proof__p` / `.proof__ul`
    body_pt: float = 8.5
    body_line_spacing: float = 1.20           # ≈ CSS line-height 1.45
    body_space_after_pt: float = 4.0
    bullet_indent_in: float = 0.16
    bullet_space_after_pt: float = 2.0
    bullet_glyph: str = "▸"              # ▸ — the site's list bullet

    # Core-expertise grid
    skill_label_pt: float = 8.5
    skill_list_pt: float = 8.0
    skill_sep: str = " · "               # · — the site's run-in separator

    # Selected projects
    project_pt: float = 9.0
    project_space_before_pt: float = 6.0

    # Footer — spec §7
    footer_pt: float = 6.5
    footer_tracking_pt: float = 0.4
    footer_rule_eighths: int = 6              # 0.75pt — coral slot 2
    footer_rule_gap_pt: int = 6
    footer_tab_in: float = 7.5

    # ATS plain-text header — spec §9
    ats_name_pt: float = 26.0
    ats_name_tracking_pt: float = 0.3
    ats_role_pt: float = 9.0
    ats_contact_pt: float = 7.5
    ats_contact_tracking_pt: float = 0.2
    ats_rule_eighths: int = 18                # 2.25pt

    # Cover letter (resumekit/letter.py). Same fonts, palette, header and
    # footer as the résumés; only the body scale differs. A résumé is dense by
    # design — 8.5pt body earns its keep across three packed pages — but a
    # one-page letter at that size reads as small type floating in white space,
    # so the letter body sits at conventional correspondence scale. These are
    # not density levers; apply_density() never touches them.
    letter_body_pt: float = 10.0
    letter_body_line_spacing: float = 1.35
    letter_body_space_after_pt: float = 10.0
    letter_date_space_before_pt: float = 22.0  # air between header rule and date
    letter_block_space_before_pt: float = 14.0 # recipient block / salutation / closing
    letter_signature_pt: float = 10.5


METRICS = Metrics()

# --------------------------------------------------------------------------
# Density
#
# The design system's spacing is drawn from the page proofs, which were laid
# out for readability rather than for a page budget. On the full eng-music
# content that lands at 3 pages, where the published v0 was 2. "tight" pulls
# type and leading back toward v0's density without touching the design's
# proportions — same hierarchy, same ration, less air.
#
# The header block's own type is not a density lever; it is the one thing on the
# page a parser has to read, so it stays at full size.
# --------------------------------------------------------------------------
DENSITIES = {
    "default": {},
    "tight": {
        "body_pt": 8.0,
        "body_line_spacing": 1.10,
        "body_space_after_pt": 2.5,
        "bullet_space_after_pt": 1.0,
        "section_pt": 9.0,
        "section_space_before_pt": 7.0,
        "section_space_after_pt": 2.0,
        "section_rule_gap_pt": 2,
        "role_pt": 8.5,
        "role_space_before_pt": 4.5,
        "meta_pt": 6.5,
        "skill_label_pt": 8.0,
        "skill_list_pt": 7.5,
        "project_pt": 8.5,
        "project_space_before_pt": 4.0,
        "header_space_after_pt": 4.0,
    },
}


def apply_density(name: str) -> None:
    """Mutate the shared METRICS in place. Call before building any styles."""
    if name not in DENSITIES:
        raise ValueError(f"density must be one of {sorted(DENSITIES)}, got {name!r}")
    for field_name, value in DENSITIES[name].items():
        if not hasattr(METRICS, field_name):
            raise AttributeError(f"DENSITIES['{name}'] sets unknown metric {field_name!r}")
        setattr(METRICS, field_name, value)

# The contact facts, verified in brand-reference.md §7. The header renders these
# as text, so they are the only copy on the page — and they must still match the
# strings in the resume_design banner artboards, which remain the design record
# of the header even though nothing embeds them any more. Spec §6;
# verify_facts.py check 4 enforces it.
CONTACT = {
    "name": "Ryan Hickey",
    "email": "ryan@wolfstrategyllc.com",
    "linkedin": "linkedin.com/in/workwithryan",
    "github": "github.com/wolfpackdata",       # added v2.0
    "location": "San Francisco Bay Area",
    "org": "Wolfpack Data & Strategy",
}

# `COO` added v2.0. Four titles fit because COO is short; a fifth would not.
ROLE_LINES = {
    "music": "Applied AI Engineer · Data & AI Systems Architect · COO · Professional Musician",
    "eng": "Applied AI Engineer · Data & AI Systems Architect · COO · Technical Operator",
}
