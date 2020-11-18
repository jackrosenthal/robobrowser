# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup

REQUIREMENTS = [
    'beautifulsoup4>=4.3.2',
    'requests>=2.6.0',
    'six>=1.9.0',
    'Werkzeug>=1.0.0',
]
TEST_REQUIREMENTS = [
    'coverage',
    'coveralls',
    'docutils',
    'mock',
    'nose',
    'sphinx',
    'tox',
]


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


setup(
    name='robobrowser-jmr',
    version=find_version('robobrowser/__init__.py'),
    description='Your friendly neighborhood web scraper',

    # Thanks to the original author (Joshua Carp, jm.carp@gmail.com)
    # for a wonderful library.  They appear to not be responding to
    # GitHub PRs, so I've made a fork.  Below is my contact info, not
    # the original author of this library.
    author='Jack Rosenthal',
    author_email='jack@rosenth.al',

    url='https://github.com/jackrosenthal/robobrowser',
    packages=['robobrowser'],
    package_dir={'robobrowser': 'robobrowser'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    python_requires='>=3.6, <4',
    license='MIT',
    zip_safe=False,
    keywords='robobrowser',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
)
