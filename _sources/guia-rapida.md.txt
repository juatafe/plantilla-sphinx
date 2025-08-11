# Guia ràpida

## 1) Desenvolupament en local
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # opcional si uses el contenidor del workflow
sphinx-build -b html docs docs/_build/html
python -m http.server -d docs/_build/html 8000
```

## 2) Estructura
```
docs/
  ├─ index.md
  ├─ guia-rapida.md
  ├─ personalitzacio.md
  ├─ duplicar-plantilla.md
  ├─ _static/
  ├─ _templates/
  └─ conf.py
```

## 3) Publicació
Només cal fer *push* a `main`. El workflow compila **HTML** i **PDF** i els puja a `gh-pages`.
