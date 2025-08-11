# Duplicar la plantilla amb l'script

Aquest script crea un nou repositori Sphinx a partir d’un origen (per defecte, la plantilla), ajusta títols/URLs, fixa el nom del PDF en el workflow i activa GitHub Pages.

```{admonition} Requisits per als botons
Per als botons “Clona la plantilla a GitHub”, “Descarrega l’script” i “Descarrega el PDF” cal tindre l’extensió **sphinx_design** habilitada a `conf.py`:

```python
extensions = [
    "myst_parser",
    "sphinx_design",
]
```
```

## Ús
```bash
./scripts/nou_sphinx_repo.sh NOU_REPO "Títol nou" UsuariGitHub [ORIGEN] [NomPDF.pdf]
```

**Paràmetres**
- `NOU_REPO`: nom del repo nou que es crearà a GitHub.
- `"Títol nou"`: títol que es posarà al projecte Sphinx.
- `UsuariGitHub`: el teu usuari (o organització) de GitHub.
- `[ORIGEN]` *(opcional)*: repo origen a clonar. Si no el poses, usa la plantilla.
- `[NomPDF.pdf]` *(opcional)*: nom fix del PDF que es publicarà.

### Exemples
```bash
# Usant la plantilla per defecte
./scripts/nou_sphinx_repo.sh plantilla-sphinx "Repo de plantilla sphinx" juatafe

# Indicant un origen i un nom de PDF personalitzat
./scripts/nou_sphinx_repo.sh apunts-xarxes "Apunts de Xarxes" juatafe https://github.com/juatafe/sge.git ApuntsDeXarxes.pdf
```

## Què fa l'script
- clona l’origen,
- reescriu títols i URLs en `conf.py`,
- ajusta el workflow perquè el PDF tinga **nom fix**,
- crea el repo a GitHub i activa **Pages** damunt de `gh-pages`.

---

## 📂 Accions ràpides

```{button-link} https://github.com/juatafe/plantilla-sphinx.git
:color: primary
:shadow:
:expand:
Clona la plantilla a GitHub
```

```{button-link} https://raw.githubusercontent.com/juatafe/plantilla-sphinx/main/scripts/nou_sphinx_repo.sh
:color: success
:shadow:
:expand:
Descarrega l’script
```

```{button-link} ../pdf/plantilla-sphinx.pdf
:color: warning
:shadow:
:expand:
Descarrega el PDF generat
```

---

## Descarrega l’script dins del projecte

**Opció interna recomanada** (si el fitxer està en `docs/scripts/`):

```{download}`Descarrega l’script nou_sphinx_repo.sh <scripts/nou_sphinx_repo.sh>`
```

```{note}
El rol `{download}` només funciona si el fitxer està dins de la carpeta *source* del teu projecte Sphinx.  
Si el tens fora, usa l’enllaç “Descarrega l’script” de dalt.
```

---

## Nota sobre la “Navegació de la Secció”
Per a que aparega, esta pàgina ha d’estar **inclosa en una `toctree`** (encadenada des de l’índex) i el `:maxdepth:` ha de ser major que 0.  
Si no, la barra quedarà buida encara que el tema estiga bé configurat.