import os
import sys
import sp_lib
import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify


sys.path.insert(0, os.path.abspath(''))
release = sp_lib.__version__
project = 'amazon_sp_api: sp_lib'
copyright = '2024, Shinji Uetsuki'
author = 'Shinji Uetsuki'
release = '1.0.0'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}
source_parsers = {
    '.md': CommonMarkParser,
}
github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
