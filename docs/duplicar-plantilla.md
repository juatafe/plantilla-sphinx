# Duplicar la plantilla amb l'script

## Ús
```bash
./scripts/nou_sphinx_repo.sh NOU_REPO "Títol nou" UsuariGitHub [ORIGEN] [NomPDF.pdf]
```

### Exemples
```bash
./scripts/nou_sphinx_repo.sh plantilla-sphinx "Repo de plantilla sphinx" juatafe
./scripts/nou_sphinx_repo.sh apunts-xarxes "Apunts de Xarxes" juatafe https://github.com/juatafe/sge.git ApuntsDeXarxes.pdf
```

L'script:
- clona l'origen,
- reescriu títols i URLs en `conf.py`,
- ajusta el workflow per a deixar el PDF amb **nom fix**,
- crea el repo a GitHub i activa **Pages** sobre `gh-pages`.


[COPIA-PEGA]
{button-link} https://github.com/juatafe/plantilla-sphinx.git
:color: primary
:shadow:
:expand:

Clona la plantilla a GitHub
[/COPIA-PEGA]