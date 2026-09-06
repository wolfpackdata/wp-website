"""resumekit — turns a YAML content file into an on-brand .docx résumé.

The design system it implements lives in ryan-resume-dev/resume_design/;
this package is only the Word half of it. letter.py reuses the same
stationery for cover letters.
"""

from .builder import build_resume
from .letter import build_cover_letter

__all__ = ["build_resume", "build_cover_letter"]
