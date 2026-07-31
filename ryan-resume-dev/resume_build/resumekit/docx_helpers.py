"""Raw-XML helpers for the handful of things python-docx doesn't expose.

Character spacing, all-caps, paragraph borders, tab stops, and PAGE/NUMPAGES
fields all have to be poked into the OOXML directly. Everything here is a thin,
single-purpose wrapper — no logic, no brand knowledge.

Unit reminders, because OOXML uses three different ones for spacing:
  · w:spacing/@w:val on rPr  → twentieths of a point   (1.2pt  → 24)
  · w:sz on a border         → eighths of a point      (2.25pt → 18)
  · w:space on a border      → whole points            (6pt    → 6)
"""

from __future__ import annotations

from docx.oxml.ns import qn
from docx.oxml import OxmlElement


# --------------------------------------------------------------------------
# Element ordering
#
# w:pPr and w:rPr are xsd:sequence, not xsd:all — their children MUST appear in
# schema order. Appending to the end produces a file Word will open but whose
# layout engine then misbehaves (in our case: ExportAsFixedFormat hung forever
# on a document that opened fine). python-docx orders the properties it sets
# itself; anything we add by hand has to be placed, not appended.
# --------------------------------------------------------------------------

PPR_SEQ = (
    "w:pStyle", "w:keepNext", "w:keepLines", "w:pageBreakBefore", "w:framePr",
    "w:widowControl", "w:numPr", "w:suppressLineNumbers", "w:pBdr", "w:shd",
    "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
    "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN",
    "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind",
    "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
    "w:textDirection", "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl",
    "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr", "w:pPrChange",
)

RPR_SEQ = (
    "w:rStyle", "w:rFonts", "w:b", "w:bCs", "w:i", "w:iCs", "w:caps",
    "w:smallCaps", "w:strike", "w:dstrike", "w:outline", "w:shadow",
    "w:emboss", "w:imprint", "w:noProof", "w:snapToGrid", "w:vanish",
    "w:webHidden", "w:color", "w:spacing", "w:w", "w:kern", "w:position",
    "w:sz", "w:szCs", "w:highlight", "w:u", "w:effect", "w:bdr", "w:shd",
    "w:fitText", "w:vertAlign", "w:rtl", "w:cs", "w:em", "w:lang",
    "w:eastAsianLayout", "w:specVanish", "w:oMath",
)


def get_or_add_ordered(parent, tag: str, seq) -> "OxmlElement":
    """Return parent's `tag` child, creating it at its schema position."""
    existing = parent.find(qn(tag))
    if existing is not None:
        return existing

    el = OxmlElement(tag)
    successors = {qn(t) for t in seq[seq.index(tag) + 1:]}
    for child in parent:
        if child.tag in successors:
            child.addprevious(el)
            return el
    parent.append(el)
    return el


# --------------------------------------------------------------------------
# Run-level
# --------------------------------------------------------------------------

def set_char_spacing(run, points: float) -> None:
    """Expand (or condense, if negative) letter spacing."""
    rPr = run._element.get_or_add_rPr()
    el = get_or_add_ordered(rPr, "w:spacing", RPR_SEQ)
    el.set(qn("w:val"), str(int(round(points * 20))))


def set_all_caps(run) -> None:
    """Display-only uppercase. The underlying text stays as typed, which is
    what keeps the résumé's live text readable to an ATS parser."""
    rPr = run._element.get_or_add_rPr()
    get_or_add_ordered(rPr, "w:caps", RPR_SEQ)


# --------------------------------------------------------------------------
# Paragraph-level
# --------------------------------------------------------------------------

def set_paragraph_border(
    paragraph,
    edge: str,
    color: str,
    size_eighths: int,
    space_points: int = 4,
    style: str = "single",
) -> None:
    """edge: 'top' | 'bottom' | 'left' | 'right'."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = get_or_add_ordered(pPr, "w:pBdr", PPR_SEQ)
    # Within pBdr the edges are themselves a sequence: top, left, bottom,
    # right, between, bar.
    edge_seq = ("w:top", "w:left", "w:bottom", "w:right", "w:between", "w:bar")
    el = get_or_add_ordered(pBdr, f"w:{edge}", edge_seq)
    el.set(qn("w:val"), style)
    el.set(qn("w:sz"), str(size_eighths))
    el.set(qn("w:space"), str(space_points))
    el.set(qn("w:color"), color)


def set_tab_stops(paragraph, stops) -> None:
    """stops: iterable of (inches, alignment) where alignment is
    'left' | 'center' | 'right'. Clears Word's default stops first."""
    pPr = paragraph._p.get_or_add_pPr()
    tabs = get_or_add_ordered(pPr, "w:tabs", PPR_SEQ)
    for child in list(tabs):
        tabs.remove(child)
    for inches, align in stops:
        tab = OxmlElement("w:tab")
        tab.set(qn("w:val"), align)
        tab.set(qn("w:pos"), str(int(round(inches * 1440))))  # twips
        tabs.append(tab)


def keep_with_next(paragraph) -> None:
    """Stop a heading or job title from being orphaned at a page break."""
    pPr = paragraph._p.get_or_add_pPr()
    get_or_add_ordered(pPr, "w:keepNext", PPR_SEQ)


def keep_lines_together(paragraph) -> None:
    pPr = paragraph._p.get_or_add_pPr()
    get_or_add_ordered(pPr, "w:keepLines", PPR_SEQ)


# --------------------------------------------------------------------------
# Fields — the reason the footer is Word text and not a pasted PNG (spec §7)
# --------------------------------------------------------------------------

def add_field(paragraph, instruction: str, placeholder: str = "1"):
    """Append a Word field, e.g. add_field(p, 'PAGE'). Returns the runs created
    so the caller can format them like any other run."""
    runs = []

    def _run(child):
        r = OxmlElement("w:r")
        r.append(child)
        paragraph._p.append(r)
        runs.append(r)
        return r

    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    _run(begin)

    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = f" {instruction} "
    _run(instr)

    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    _run(sep)

    txt = OxmlElement("w:t")
    txt.text = placeholder          # what Word shows until the field updates
    _run(txt)

    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    _run(end)

    return runs


def style_field_runs(run_elements, font_name: str, size_pt: float,
                     color: str, tracking_pt: float = 0.0,
                     caps: bool = False) -> None:
    """Apply run formatting to the raw <w:r> elements add_field() returned."""
    for r in run_elements:
        rPr = r.find(qn("w:rPr"))
        if rPr is None:
            rPr = OxmlElement("w:rPr")
            r.insert(0, rPr)                      # rPr is always first in w:r

        fonts = get_or_add_ordered(rPr, "w:rFonts", RPR_SEQ)
        for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            fonts.set(qn(attr), font_name)

        if caps:
            get_or_add_ordered(rPr, "w:caps", RPR_SEQ)

        col = get_or_add_ordered(rPr, "w:color", RPR_SEQ)
        col.set(qn("w:val"), color)

        if tracking_pt:
            sp = get_or_add_ordered(rPr, "w:spacing", RPR_SEQ)
            sp.set(qn("w:val"), str(int(round(tracking_pt * 20))))

        sz = get_or_add_ordered(rPr, "w:sz", RPR_SEQ)
        sz.set(qn("w:val"), str(int(round(size_pt * 2))))     # half-points


# --------------------------------------------------------------------------
# Tables — the core-expertise grid is a borderless layout table
# --------------------------------------------------------------------------

def strip_table_borders(table) -> None:
    tblPr = table._tbl.tblPr
    old = tblPr.find(qn("w:tblBorders"))
    if old is not None:
        tblPr.remove(old)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        el.set(qn("w:sz"), "0")
        borders.append(el)
    tblPr.append(borders)


def set_table_cell_margins(table, top=0, start=0, bottom=0, end=0) -> None:
    """Margins in inches."""
    tblPr = table._tbl.tblPr
    old = tblPr.find(qn("w:tblCellMar"))
    if old is not None:
        tblPr.remove(old)
    mar = OxmlElement("w:tblCellMar")
    for name, inches in (("top", top), ("start", start),
                         ("bottom", bottom), ("end", end)):
        el = OxmlElement(f"w:{name}")
        el.set(qn("w:w"), str(int(round(inches * 1440))))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)
