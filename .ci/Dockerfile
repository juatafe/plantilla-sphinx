FROM python:3.11-slim
ENV DEBIAN_FRONTEND=noninteractive

# Eines de LaTeX + SVG/imatge necessàries per a latexpdf
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-xetex texlive-latex-recommended texlive-latex-extra \
    texlive-fonts-recommended texlive-lang-european latexmk lmodern \
    inkscape imagemagick poppler-utils ghostscript \
    ca-certificates git curl \
 && rm -rf /var/lib/apt/lists/*

# Paquets Python base del teu projecte
RUN pip install --no-cache-dir \
    sphinx \
    pydata-sphinx-theme \
    myst-parser \
    sphinx-copybutton \
    sphinxcontrib-imgconverter

WORKDIR /work
