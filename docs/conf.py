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

# The theme to use for HTML. "alabaster" is the Sphinx default theme.
html_theme = 'alabaster'

# Theme-specific options
html_theme_options = {
    # You can add theme-specific options here
}

html_static_path = ['_static']

# -- Read the Docs configuration ---------------------------------------------
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# If you need the LaTeX output to work on Read the Docs, uncomment below:
# latex_engine = 'xelatex'

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True