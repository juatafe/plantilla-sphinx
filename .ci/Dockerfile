FROM python:3.11-slim
ENV DEBIAN_FRONTEND=noninteractive

# Sistemes per a PDF/SVG/imatge
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-xetex texlive-latex-recommended texlive-latex-extra \
    texlive-fonts-recommended texlive-lang-european latexmk lmodern \
    inkscape imagemagick poppler-utils ghostscript \
    ca-certificates git curl \
 && rm -rf /var/lib/apt/lists/*

# Actualitza pip/setuptools i instal·la només el que gastes
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir \
      sphinx \
      pydata-sphinx-theme \
      myst-parser \
      sphinx-copybutton
# (NO instal·lem sphinxcontrib-imgconverter perquè tu uses sphinx.ext.imgconverter)

WORKDIR /work
