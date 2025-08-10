import os, sys
sys.path.append(os.path.abspath("."))

project = "Repo de plantilla sphinx"
author = "Juan Bautista Talens"
language = "ca"

extensions = ["myst_parser", "sphinx_copybutton", "sphinx.ext.imgconverter"]

myst_enable_extensions = ["colon_fence", "attrs_block", "deflist"]
myst_heading_anchors = 3

html_theme = "pydata_sphinx_theme"
html_title = "Repo de plantilla sphinx"
html_static_path = ["_static"]
html_logo = "_static/assets/img/logos/logoJust.png"          # el teu logo gran
html_favicon = "_static/assets/img/logos/logo50.ico"

# Carrega els teus CSS (ordre importa: de general -> específic)
html_css_files = [
    "assets/stylesheets/customs.css",
    "assets/stylesheets/extra.css",
]

html_theme_options = {
    "use_edit_page_button": True,
    "show_prev_next": True,
    "show_toc_level": 2,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {"name": "GitHub", "url": "https://github.com/juatafe/plantilla-sphinx", "icon": "fa-brands fa-github"},
        {"name": "Issues", "url": "https://github.com/juatafe/plantilla-sphinx", "icon": "fa-solid fa-circle-exclamation"},
        {"name": "PDF", "url": "https://juatafe.github.io/plantilla-sphinx/pdf/plantilla-sphinx.pdf", "icon": "fa-solid fa-file-pdf"},
    ],
}

html_context = {
    "github_user": "juatafe",
    "github_repo": "sge",
    "github_version": "main",
    "doc_path": "docs",
}

html_search_language = "es"

latex_engine = "xelatex"

latex_elements = {
    # IMPORTANT: sobreescriu l’elecció de fonts que fa Sphinx (evita FreeSerif)
    "fontpkg": r"""
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{TeX Gyre Cursor}
""",
    # Llengua i hifenació (polyglossia)
    "preamble": r"""
\usepackage{polyglossia}
\setmainlanguage{catalan}
"""
}

# templates_path = ["_templates"]  # Sphinx ja ho té per defecte
