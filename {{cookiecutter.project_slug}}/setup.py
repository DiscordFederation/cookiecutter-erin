#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file for {{cookiecutter.project_name}}.
"""

import codecs
import os
import re
import sys

from setuptools import setup, find_packages

# Add your requirements here according to pep-0508
INSTALL_REQUIRES = [
    "glia @ git+https://github.com/DiscordFederation/Glia.git@rewrite#egg=glia[voice]"
]

EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov',
        'pytest-runner',
    ],
    'docs': [
        'Sphinx',
        'sphinx_rtd_theme'
    ]
}

# Variables
path_here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    # https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(path_here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []

setup(
        version=find_version('{{cookiecutter.project_slug}}', '__init__.py'),
        packages=find_packages(exclude=['docs', 'tests']),
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        setup_requires=[] + sphinx,
        extras_require=EXTRAS_REQUIRE
)

if __name__ == "__main__":
    pass
