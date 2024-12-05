# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))  # or the path to your package

# -- Project information -----------------------------------------------------
project = 'OntoWeaver'
author = 'Johann Dreo, Marko Baric, Claire Laudy, Matthieu Najm, Benno Schwikowski'
release = '0.1'
version = '0.1.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'  # Read the Docs requires this to be explicitly set

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for internationalization ----------------------------------------
language = None

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # or any other theme you want
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

# -- Setup for Read the Docs (RTD) ------------------------------------------
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS') == 'True'

if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'sphinx_rtd_theme'

# This is to make sure that Read the Docs builds PDFs using your LaTeX settings
latex_engine = 'xelatex'  # or 'pdflatex', 'lualatex', etc

# -- Options for intersphinx -------------------------------------------------
# This configures intersphinx, which links to other projects' documentation
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}

# -- Options for todo extension ----------------------------------------------
# If you have any :todo:`some task` in your documentation, they can be shown
# if you set this
todo_include_todos = True