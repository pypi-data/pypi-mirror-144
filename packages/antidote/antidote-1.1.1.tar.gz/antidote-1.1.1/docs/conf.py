#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Antidote documentation build configuration file, created by
# sphinx-quickstart on Sat Oct 14 22:07:20 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# sys.path.insert(0, os.path.abspath('..'))
# sys.path.insert(0, os.path.abspath('_themes'))

import antidote

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    # 'sphinx_autodoc_typehints',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx'
]

# Python code that is treated like it were put in a testcleanup directive for
# every file that is tested, and for every group.
doctest_global_setup = """
from antidote._internal import state
state.init()
"""
doctest_global_cleanup = """
from antidote._internal import state
state.reset()
"""

autodoc_member_order = 'bysource'
autoclass_content = "both"

# This config value contains the locations and names of other projects
# that should be linked to in this documentation.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}

# Prefix each section label with the name of the document it is in.
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Antidote'
copyright = '2017, Benjamin Rabier'
author = 'Benjamin Rabier'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tag.
release = antidote.__version__
# The short X.Y version.
version = release.rsplit(".", 1)[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'flask_theme_support.FlaskyStyle'

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
add_module_names = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "sphinx_rtd_theme"

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {
#     'show_powered_by': False,
#     'github_user': 'Finistere',
#     'github_repo': 'antidote',
#     'github_banner': True,
#     'show_related': False,
#     'note_bg': '#FFF59C'
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Antidotedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Antidote.tex', 'Antidote Documentation',
     'Benjamin Rabier', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dependency manager', 'Antidote Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Antidote', 'Antidote Documentation',
     author, 'Antidote', 'One line description of project.',
     'Miscellaneous'),
]


# def do_not_skip_antidote(app, what, name, obj, skip, options):
#     return (name != "__antidote__") and skip


def setup(app):
    # Fix image path
    with open('../README.rst', 'r') as readme, \
            open('_build/README.rst', 'w') as build_readme:
        build_readme.write(readme.read()
                           .replace('docs/_static/img', '_static/img')
                           .replace('.. code-block:: python',
                                    '.. testcode:: readme'))

    app.add_css_file('css/style.css')  # may also be an URL
