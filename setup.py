# Author: Jason Dsouza
# Github: http://www.github.com/jasmcaus

from setuptools import setup, find_packages

VERSION = '0.1.7'

DESCRIPTION = """A Python library including support for Deep Learning models built using the Keras framework."""

LONG_DESCRIPTION = DESCRIPTION + """ This repository is actively being maintained. If there are any issues, kindly open a thread in the 'Issues' pane on the official Github repository. """

AUTHOR = 'Jason Dsouza: http://www.github.com/jasmcaus'

VERSION_PY_TEXT = """
# This file is automatically generated during the generation of setup.py
# Copyright 2020, Kangeras

author = '%(author)s'
version = '%(version)s'
full_version = '%(full_version)s'
release = %(isrelease)s
if not release:
    version = full_version
"""

# Repository on PyPi.org = https://pypi.org/project/caer/


def write_version_py(filename='kangeras/version.py'):
    print('[INFO] Writing version.py')
    TEXT = VERSION_PY_TEXT
    FULL_VERSION = VERSION
    ISRELEASED = True

    a = open(filename, 'w')
    try:
        a.write(TEXT % {'author': AUTHOR,
                        'version': VERSION,
                       'full_version': FULL_VERSION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()


def setup_package():
    # Rewrite the version file everytime
    write_version_py()

    setup(
        name="kangeras",
        version=VERSION,
        author="Jason Dsouza",
        author_email="jasmcaus@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        url="https://github.com/jasmcaus/kangeras",
        download_url = "https://pypi.org/project/kangeras/",
        project_urls={
            "Bug Tracker": "https://github.com/jasmcaus/kangeras/issues",
            "Source Code": "https://github.com/jasmcaus/kangeras",
        },
        packages=find_packages(),
        install_requires=['tensorflow'],
        keywords=['computer vision', 'deep learning', 'tensorflow', 'keras', 'convolutional neural networks', 'opencv', 'matplotlib'],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Operating System :: MacOS",
            "Operating System :: Microsoft :: Windows",
            "License :: OSI Approved :: MIT License",
        ],
    )


if __name__ == '__main__':
    setup_package()