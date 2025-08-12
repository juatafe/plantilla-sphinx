import os
import sys
import re
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
    "sphinx_design", 
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

def slugify(s: str) -> str:
    return re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()

# Si el repo és "usuari/repo", agarrem "repo"; si no hi ha env (build local), fem servir el títol del projecte
_repo = os.environ.get("GITHUB_REPOSITORY", "")
_repo_name = _repo.split("/")[-1] if _repo else ""
site_slug = _repo_name or slugify(project)

# Enllaç relatiu al PDF dins del site (p. ex. pdf/plantilla-sphinx.pdf)
pdf_url = f"pdf/{site_slug}.pdf"

# Opcions del tema
html_theme_options = {
    "show_nav_level": 1, # quant nivell d’arbre es desplega d’entrada
    "navigation_depth": 2, # profunditat del TOC
    "collapse_navigation": False,
    "secondary_sidebar_items": ["page-toc", "sourcelink", "edit-this-page"],
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
            "url": pdf_url,
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
html_search_language = "ca"

# ──────────────── LaTeX/PDF ────────────────
latex_engine = "xelatex"

latex_elements = {
    "fontpkg": r"""
\usepackage{fontspec}
\IfFontExistsTF{TeX Gyre Pagella}{
  \setmainfont{TeX Gyre Pagella}
}{
  \setmainfont{Latin Modern Roman}
}
\IfFontExistsTF{TeX Gyre Heros}{
  \setsansfont{TeX Gyre Heros}
}{
  \setsansfont{Latin Modern Sans}
}
\setmonofont{Latin Modern Mono}
""",
    "preamble": r"""
\usepackage{polyglossia}
\setmainlanguage{catalan}
"""
}
latex_documents = [
    ("index", f"{site_slug}.tex", project, author, "manual"),
]

# Opcions de LaTeX


# Plantilles personalitzades (si cal)
# templates_path = ["_templates"]
templates_path = ["_templates"]

html_theme_options.update({
    
    # afegim un slot “custom” a l'inici de la navbar
    "navbar_start": ["navbar-logo", "jb-header-logos"],  # conserva el logo del tema i el nostre bloc
})