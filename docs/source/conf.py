# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Add the katana directory so imports work without installing katana w/ pip
sys.path.insert(0, os.path.abspath("../../"))


# -- Project information -----------------------------------------------------

project = "Katana"
copyright = "2019, Caleb Stewart, John Hammond"
author = "Caleb Stewart, John Hammond"

# The full version, including alpha/beta/rc tags
release = "1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "canonical_url": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

autodoc_mock_imports = [
    "requests",
    "argparse",
    "magic",
    "pyzbar",
    "PIL",
    "clipboard",
    "jinja2",
    "enchant",
    "Crypto",
    "pytesseract",
    "dulwich",
    "bs4",
    "base58",
    "socks",
    "scipy",
    "pydub",
    "matplotlib",
    "pdftotext",
    "PyPDF2",
    "OpenSSL",
    "primefac",
    "cmd2",
    "watchdog",
    "dbus",
    "notify2",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Master document
master_doc = "index"
