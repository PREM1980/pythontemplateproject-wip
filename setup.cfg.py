[metadata]
name = pythontemplateproject
summary = Add a short description here!
author = Prem
author-email = prem1pre@gmail.com
license = LICENSE
home-page = https://github.com/PREM1980/pythontemplateproject
description-file = README.rst
# Add here all kinds of additional classifiers as defined under
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifier =
    Development Status :: 4 - Beta
    Programming Language :: Python

[entry_points]
# Add here console scripts like:
# console_scripts =
#     script_name = scaffold_test.module:function
# For example:
# console_scripts =
#     fibonacci = scaffold_test.skeleton:run
# as well as other entry_points.


[files]
# Add here 'data_files', 'packages' or 'namespace_packages'.
# Additional data files are defined as key value pairs of target directory
# and source location from the root of the repository:
packages =
    scaffold_test
# data_files =
#    share/scaffold_test_docs = docs/*

[extras]
# Add here additional requirements for extra features, like:
# PDF =
#    ReportLab>=1.2
#    RXP

[test]
# py.test options when running `python setup.py test`
addopts = tests

[tool:pytest]
# Options for py.test:
# Specify command line options as you would do when invoking py.test directly.
# e.g. --cov-report html (or xml) for html/xml output or --junitxml junit.xml
# in order to write a coverage file that can be read by Jenkins.
addopts =
    --cov scaffold_test --cov-report term-missing
    --junitxml report/junit.xml
    --verbose

[aliases]
docs = build_sphinx

[bdist_wheel]
# Use this option if your package is pure-python
universal = 1

[build_sphinx]
source_dir = docs
build_dir = docs/_build

[pbr]
# Let pbr run sphinx-apidoc
autodoc_tree_index_modules = True
# autodoc_tree_excludes = ...
# Let pbr itself generate the apidoc
# autodoc_index_modules = True
# autodoc_exclude_modules = ...
# Convert warnings to errors
# warnerrors = True

[devpi:upload]
# Options for the devpi: PyPI server and packaging tool
# VCS export must be deactivated since we are using setuptools-scm
no-vcs = 1
formats = bdist_wheel