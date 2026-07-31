"""Word paragraph styles built from the brand tokens.

Named styles rather than direct formatting, so the generated .docx stays
editable: change "WP Body" once in Word and every body paragraph follows. The
only things applied per-paragraph are the two coral rules, which live in
blocks.py where the ration is easy to audit.
"""

from __future__ import annotations

from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Inches, Pt, RGBColor

from . import brand
from .brand import METRICS as M
from .docx_helpers import RPR_SEQ, get_or_add_ordered


def _complete_font(style, font_name: str) -> None:
    """python-docx sets ascii+hAnsi only; complex-script text falls back to the
    theme font without this and the résumé ends up in two typefaces."""
    rPr = style.element.get_or_add_rPr()
    fonts = get_or_add_ordered(rPr, "w:rFonts", RPR_SEQ)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), font_name)


def _style_tracking(style, points: float) -> None:
    rPr = style.element.get_or_add_rPr()
    el = get_or_add_ordered(rPr, "w:spacing", RPR_SEQ)
    el.set(qn("w:val"), str(int(round(points * 20))))


def _style_caps(style) -> None:
    rPr = style.element.get_or_add_rPr()
    get_or_add_ordered(rPr, "w:caps", RPR_SEQ)


def _add(doc, name, *, font, size, color, bold=False, caps=False,
         tracking=0.0, space_before=0.0, space_after=0.0,
         line_spacing=None, left_indent=0.0, hanging=0.0):
    style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = doc.styles["Normal"]
    style.quick_style = True

    style.font.name = font
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = RGBColor.from_string(color)
    _complete_font(style, font)
    if caps:
        _style_caps(style)
    if tracking:
        _style_tracking(style, tracking)

    pf = style.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    if line_spacing:
        pf.line_spacing = line_spacing
        pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    if left_indent:
        pf.left_indent = Inches(left_indent)
    if hanging:
        pf.first_line_indent = Inches(-hanging)
    pf.widow_control = True
    return style


def build_styles(doc, fonts: dict) -> None:
    """fonts: one of brand.FONT_SETS values."""
    display, body, mono = fonts["display"], fonts["body"], fonts["mono"]

    # Normal is the fallback for anything unstyled; make it the body font so a
    # stray paragraph never shows up in Calibri.
    normal = doc.styles["Normal"]
    normal.font.name = body
    normal.font.size = Pt(M.body_pt)
    normal.font.color.rgb = RGBColor.from_string(brand.INK_70)
    _complete_font(normal, body)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = M.body_line_spacing
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE

    _add(doc, "WP Section", font=display, size=M.section_pt, color=brand.NAVY,
         bold=True, caps=True, tracking=M.section_tracking_pt,
         space_before=M.section_space_before_pt,
         space_after=M.section_space_after_pt)

    _add(doc, "WP Body", font=body, size=M.body_pt, color=brand.INK_70,
         space_after=M.body_space_after_pt, line_spacing=M.body_line_spacing)

    _add(doc, "WP Bullet", font=body, size=M.body_pt, color=brand.INK_70,
         space_after=M.bullet_space_after_pt, line_spacing=M.body_line_spacing,
         left_indent=M.bullet_indent_in, hanging=M.bullet_indent_in)

    _add(doc, "WP Role", font=display, size=M.role_pt, color=brand.NAVY,
         bold=True, caps=True, tracking=M.role_tracking_pt,
         space_before=M.role_space_before_pt, space_after=0.0)

    _add(doc, "WP Role Meta", font=mono, size=M.meta_pt, color=brand.INK_45,
         caps=True, tracking=M.meta_tracking_pt, space_after=2.0)

    _add(doc, "WP Project", font=display, size=M.project_pt, color=brand.NAVY,
         bold=True, space_before=M.project_space_before_pt, space_after=1.0)

    _add(doc, "WP Skill Label", font=body, size=M.skill_label_pt,
         color=brand.NAVY, bold=True, space_after=1.0)

    _add(doc, "WP Skill List", font=body, size=M.skill_list_pt,
         color=brand.INK_70, space_after=6.0, line_spacing=M.body_line_spacing)

    _add(doc, "WP Footer", font=mono, size=M.footer_pt, color=brand.INK_70,
         caps=True, tracking=M.footer_tracking_pt, space_before=0.0,
         space_after=0.0)

    # --- The header (spec §9). Plain text on every build since v2.2; the
    # `ATS` in the style names is now a description of the whole document,
    # not of one variant of it. ------------------------------------------
    _add(doc, "WP ATS Name", font=display, size=M.ats_name_pt,
         color=brand.NAVY, bold=True, caps=True,
         tracking=M.ats_name_tracking_pt, space_after=1.0)

    _add(doc, "WP ATS Role", font=body, size=M.ats_role_pt, color=brand.INK_70,
         bold=True, space_after=1.0)

    _add(doc, "WP ATS Contact", font=mono, size=M.ats_contact_pt,
         color=brand.INK_45, tracking=M.ats_contact_tracking_pt,
         space_after=M.header_space_after_pt)
