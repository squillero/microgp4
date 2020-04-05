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
import time

sys.path.insert(0, os.path.abspath('../../src'))

import microgp

# -- Project information -----------------------------------------------------

project = microgp.__name__
release = microgp.__version__
author = microgp.__author__
copyright = f"2020 Giovanni Squillero & Alberto Tonda"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['m2r',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx_rtd_theme',
              'sphinx.ext.napoleon']

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = list()

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = f"{microgp.name} {microgp.version}"
html_short_title = f"microgp{microgp.__version__}"
html_show_copyright = False
html_show_sphinx = True
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
html_logo = '../images/logo/150x150.png'
html_favicon = '../images/icons/24x24.ico'
html_show_sourcelink = False

html_theme_options = {
    'canonical_url': 'https://microgp4.readthedocs.io/',
    'analytics_id': 'UA-28094298-6',  # Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = list()

master_doc = 'index'

rst_prolog = f"""
.. |ugp_name| replace:: {microgp.name}
.. |ugp_version| replace:: {microgp.version}
.. |now| replace:: {time.ctime()}
"""