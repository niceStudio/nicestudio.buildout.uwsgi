# -*- coding: utf-8 -*-
# Copyright (c) 2024  niceStudio, Inc. All rights reserved.
# See also LICENSE.txt
import os
import sys

source_dirname = 'src'

project_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(project_dir, source_dirname))

import nicestudio.buildout.uwsgi

kwargs = {
    'name': 'nicestudio.buildout.uwsgi',
    # 'version': '1.0.dev3',
    'version': getattr(nicestudio.buildout.uwsgi, '__version__'),
    'description': 'Buildout recipe downloading, compiling and configuring uWSGI.',
    'long_description': open('README.md').read(),
    'author': 'niceStudio, Inc',
    'author_email': 'service@niceStudio.com.tw',
    'license': 'BSD',
    'url': 'https://github.com/niceStudio/nicestudio.buildout.uwsgi',
    'package_dir': {'': 'src'},
    # 'packages': find_namespace_packages('src'),
    # namespace_packages=['nicestudio', ],
    'include_package_data': True,
    'zip_safe': False,
    'classifiers': [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    'install_requires': [
        'zc.recipe.egg',
    ],
    'entry_points': {'zc.buildout': ['default = nicestudio.buildout.uwsgi:UWSGI']},
}

try:
    from setuptools import find_namespace_packages

    kwargs['packages'] = find_namespace_packages(where='src')
except ImportError:
    from setuptools import find_packages

    kwargs['packages'] = find_packages(where='src')
    kwargs['namespace_packages'] = ['nicestudio', ]

from setuptools import setup

setup(**kwargs)
