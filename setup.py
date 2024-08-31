# -*- coding: utf-8 -*-
# Copyright (c) 2024  niceStudio, Inc. All rights reserved.
# See also LICENSE.txt
from setuptools import setup, find_packages

setup(
    name='nicestudio.buildout.uwsgi',
    version='1.0dev0',
    description='Buildout recipe downloading, compiling and configuring uWSGI.',
    long_description=open('README.txt', 'r').read(),
    author='niceStudio, Inc',
    author_email='service@niceStudio.com.tw',
    license='BSD',
    url='https://github.com/niceStudio',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['nicestudio', 'buildout'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        'zc.recipe.egg',
    ],
    entry_points={'zc.buildout': ['default = nicestudio.buildout.uwsgi:UWSGI']},
)
