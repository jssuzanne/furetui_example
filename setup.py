#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for furetui_exemple"""

from setuptools import setup, find_packages
import os

version = "0.1.0"
here = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(here, 'README.rst'), 'r', encoding='utf-8'
) as readme_file:
    readme = readme_file.read()

with open(
    os.path.join(here, 'CHANGELOG.rst'), 'r', encoding='utf-8'
) as changelog_file:
    changelog = changelog_file.read()

requirements = [
    'sqlalchemy',
    'anyblok',
    'psycopg2-binary',
    'anyblok_furetui',
    'anyblok_io',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='furetui_exemple',
    version=version,
    description="A short description of the Anyblok based project",
    long_description=readme + '\n\n' + changelog,
    author="Your name",
    author_email='Your address email (eq. you@example.com)',
    url='https://github.com/Your github username/furetui_exemple',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'team=furetui_exemple.team:Team'
         ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='furetui_exemple',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
