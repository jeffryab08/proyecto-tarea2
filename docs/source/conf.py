# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Habilitar la ruta raíz para que Sphinx localice main.py y processor.py
sys.path.insert(0, os.path.abspath("../../"))

# Añadir extensiones integradas esenciales para extraer docstrings
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Soporte para Google-style docstrings
    "sphinx.ext.viewcode",  # Agrega enlaces directos al código fuente
]

# Modificar el tema si lo deseas (opcional, ej. 'sphinx_rtd_theme')
html_theme = "alabaster"


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Procesador de Imagenes - Tarea 2'
copyright = '2026, Jeffry Araya'
author = 'Jeffry Araya'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
