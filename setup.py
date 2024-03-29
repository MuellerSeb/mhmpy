# -*- coding: utf-8 -*-
"""mhmpy: a python API for the mesoscale Hydrological Model."""

import os
import codecs
import re

from setuptools import setup, find_packages


# find __version__ ############################################################


def read(*parts):
    """Read file data."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    """Find version without importing module."""
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


###############################################################################


DOCLINES = __doc__.split("\n")
README = open("README.md").read()
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development",
    "Topic :: Utilities",
]

VERSION = find_version("mhmpy", "_version.py")

setup(
    name="mhmpy",
    version=VERSION,
    maintainer="Sebastian Mueller",
    maintainer_email="sebastian.mueller@ufz.de",
    description=DOCLINES[0],
    long_description=README,
    long_description_content_type="text/markdown",
    author="Sebastian Mueller",
    author_email="info@geostat-framework.org",
    url="https://github.com/MuellerSeb/mhmpy",
    license="MIT",
    classifiers=CLASSIFIERS,
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    include_package_data=True,
    install_requires=[
        # "numpy>=1.13.0",
    ],
    extras_require={},
    packages=find_packages(exclude=["tests*", "docs*"]),
)
