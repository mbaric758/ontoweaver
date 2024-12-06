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
    'myst_parser',  # For markdown support with Sphinx 3.0+
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
source_suffix = ['.rst', '.md']  # Include Markdown files
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Use Read the Docs theme
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# If you have your own conf.py tweaks, they can go here

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp'
}

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True

# -- Options for Read the Docs PDF generation --------------------------------
latex_engine = 'xelatex'  # Use XeLaTeX for better Unicode support

# -- Read the Docs configuration ---------------------------------------------
on_rtd = os.environ.get('READTHEDOCS') == 'True'