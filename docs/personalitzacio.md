# Personalització

## Tema i opcions
El tema està en `conf.py`:
```python
html_theme = "pydata_sphinx_theme"
html_theme_options = { "show_prev_next": True, ... }
```

## Logos i favicon
- `html_logo = "_static/assets/img/logos/logoJust.png"`
- `html_favicon = "_static/assets/img/logos/logo50.ico"`

## CSS propi
Afig els teus CSS a `_static/assets/stylesheets/` i declara’ls en `html_css_files` (ordre de més general a més específic).
