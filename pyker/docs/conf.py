import os
import sys
from typing import List

# make pyker modules importable
sys.path.insert(0, os.path.abspath(".."))

extensions: List[str] = [
    "sphinx.ext.autodoc",  # pull in docstrings
    "sphinx.ext.napoleon",  # Google / NumPy style docstrings
    "sphinxcontrib.mermaid",  # support Mermaid diagrams
]

# Optional settings
html_theme = "sphinx_rtd_theme"
autodoc_typehints = "description"
