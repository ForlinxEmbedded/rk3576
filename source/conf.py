# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

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
latex_documents = [
('hardware',
'abc.tex',
'FET3576-C Hardware Manual',
'Forlinx Embedded Technology Co., Ltd',
'manual',
False)
]

latex_elements = {
    'preamble': r'''
    \usepackage{fontspec}
    \usepackage{xeCJK}
    \setCJKmainfont{Noto Serif CJK SC}  % 设置中文字体为宋体（可以替换为你喜欢的中文字体）
    \setcounter{secnumdepth}{0} % 禁用章节自动编号
	
   
    \setmainfont{Times New Roman}  % 设置英文字体为 Times New Roman（可以根据需求调整）
    '''
}
# Enable numbered headings
numfig = False

latex_show_urls = 'footnote'
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_copy_source = False

