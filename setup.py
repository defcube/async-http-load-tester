#!/usr/bin/env python
from distutils.core import setup

readme = open('README.rst').read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='async-http-load-tester',
    version='0.0.1',
    author_email='gattster@gmail.com',
    author='Philip Gatt',
    description="A tool to measure concurrent serving capacity",
    long_description=readme,
    # url='http://github.com/defcube/django-logging-command/',
    py_modules=["django_logging_command"],
    data_files=[('', ['README.rst'])],
    install_requires=required
    )