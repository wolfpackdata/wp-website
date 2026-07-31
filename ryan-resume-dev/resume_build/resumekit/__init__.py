"""resumekit — turns a YAML content file into an on-brand .docx résumé.

The design system it implements lives in ryan-resume-dev/resume_design/;
this package is only the Word half of it.
"""

from .builder import build_resume

__all__ = ["build_resume"]
