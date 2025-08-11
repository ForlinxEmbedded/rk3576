# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os 

project = 'FET3506-C/OK3506-C'
copyright = '2025, Forlinx Embedded Technology Co., Ltd'
author = 'Forlinx Embedded Technology Co., Ltd'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',    
    '.md': 'markdown',
}
latex_engine = 'xelatex'

latex_elements = {
    'fontpkg':
    '\\usepackage{lmodern}',
    'preamble': r'''
      \usepackage{fontspec}
      \setmonofont{DejaVu Sans Mono}[Scale=0.8]
      \setcounter{secnumdepth}{0}
      \setcounter{tocdepth}{1}  % Adjust the depth of the ToC if needed
      
    ''',
}

latex_documents = [


('hardware',
'abc.tex',
'FET3576-C Hardware Manual',
'Forlinx Embedded Technology Co., Ltd',
'manual',
False)
]


# Enable numbered headings
numfig = False

latex_show_urls = 'footnote'
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_copy_source = False

html_context = {
    "pdf_base_url": "_static/pdf",
}

