# Plantilla Sphinx + GitHub Pages (HTML + PDF)

Aquesta plantilla està pensada perquè el teu **repo** siga alhora *plantilla + tutorial*.
Inclou:
- Portada `docs/index.md` amb targetes i guia d'ús.
- Pàgines `docs/guia-rapida.md`, `docs/personalitzacio.md` i `docs/duplicar-plantilla.md`.
- Workflow per a **Build & Deploy** d'HTML i PDF a **GitHub Pages** (usant un contenidor).
- `scripts/nou_sphinx_repo.sh` per a crear un nou repo a partir d'este.
- `conf.py` adaptat a **pydata-sphinx-theme** i a **PDF** amb `xelatex`.

## Ús ràpid
1) Desenvolupament en local:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # opcional si no uses el contenidor
   sphinx-build -b html docs docs/_build/html
   ```

2) Publicació automàtica: fes *push* a `main` i el workflow publicarà a `gh-pages`.
