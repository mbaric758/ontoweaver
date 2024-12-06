# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'OntoWeaver'
author = 'Johann Dreo, Marko Baric, Claire Laudy, Matthieu Najm, Benno Schwikowski'
release = '0.1'
version = '0.1.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Include documentation from docstrings
    'sphinx.ext.napoleon',  # Support for Google-style docstrings
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.todo',      # Support for todo items
]

templates_path = ['_templates']
source_suffix = '.rst'  # Only use RestructuredText
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Use the Read the Docs theme
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp'
}

# -- Read the Docs configuration ---------------------------------------------
on_rtd = os.environ.get('READTHEDOCS') == 'True'