import os
import sys
sys.path.append(os.path.abspath("."))

# ──────────────── Projecte ────────────────
project = "Repo de plantilla sphinx"
author = "Juan Bautista Talens"
language = "ca"

# ──────────────── Extensions ────────────────
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.imgconverter",
]

myst_enable_extensions = [
    "colon_fence",
    "attrs_block",
    "deflist",
]
myst_heading_anchors = 3

# ──────────────── HTML ────────────────
html_theme = "pydata_sphinx_theme"
html_title = "Repo de plantilla sphinx"
html_static_path = ["_static"]

# Logos i favicon
html_logo = "_static/assets/img/logos/logoJust.png"
html_favicon = "_static/assets/img/logos/logo50.ico"

# CSS personalitzat (ordre: general → específic)
html_css_files = [
    "assets/stylesheets/extracsspdf.css",
    "assets/stylesheets/customs.css",
    "assets/stylesheets/extra.css",
]

# Opcions del tema
html_theme_options = {
    "use_edit_page_button": True,
    "show_prev_next": True,
    "show_toc_level": 2,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/juatafe/plantilla-sphinx",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Issues",
            "url": "https://github.com/juatafe/plantilla-sphinx/issues",
            "icon": "fa-solid fa-circle-exclamation",
        },
        {
            "name": "PDF",
            "url": "https://juatafe.github.io/plantilla-sphinx/pdf/plantilla-sphinx.pdf",
            "icon": "fa-solid fa-file-pdf",
        },
    ],
}

# Context per a botó "Edita a GitHub"
html_context = {
    "github_user": "juatafe",
    "github_repo": "plantilla-sphinx",
    "github_version": "main",
    "doc_path": "docs",
}

# Llengua del buscador
html_search_language = "es"

# ──────────────── LaTeX/PDF ────────────────
latex_engine = "xelatex"

latex_elements = {
    # Fonts
    "fontpkg": r"""
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{TeX Gyre Cursor}
""",
    # Llengua i hifenació
    "preamble": r"""
\usepackage{polyglossia}
\setmainlanguage{catalan}
"""
}

# Plantilles personalitzades (si cal)
# templates_path = ["_templates"]
templates_path = ["_templates"]

html_theme_options.update({
    "content_width": "1100px",   # 1000–1200px sol quedar molt apanyat
    # afegim un slot “custom” a l'inici de la navbar
    "navbar_start": ["navbar-logo", "jb-header-logos"],  # conserva el logo del tema i el nostre bloc
})