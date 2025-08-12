# Plantilla Sphinx (HTML + PDF)

Benvinguda! Esta és la portada de la plantilla. Baix tens una vista ràpida i enllaços útils.

{grid} 1 1 2 2
:gutter: 2

:::grid-item
:::card{Guia ràpida}
:link: guia-rapida
**Comandes** i flux bàsic per a treballar en local i publicar.
:::
:::

:::grid-item
:::card{Personalització}
:link: personalitzacio
Canvia tema, logo, CSS i opcions del `conf.py`.
:::
:::

:::grid-item
:::card{Duplicar amb un script}
:link: duplicar-plantilla
Com usar `scripts/nou_sphinx_repo.sh` per a clonar i personalitzar.
:::
:::

{/grid}


```{toctree}
:hidden:
:maxdepth: 0

guia-rapida
personalitzacio
duplicar-plantilla
```

## Estat del projecte
- Tema: **pydata-sphinx-theme**
- PDF: es publica en `pdf/<slug>.pdf` i apareix com a icona a la barra superior.
- Build & Deploy: automàtic via **GitHub Actions** → `gh-pages`.