#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'py-oauth2',
    version = '0.0.4',
    keywords = ('Python', 'OAuth', 'OAuth2', 'Douban', 'GitHub', 'Weibo'),
    description = 'A Python wrapper for the OAuth 2.0 specification.',
    long_description = open('README.rst').read(),
    license = 'MIT License',

    url = 'https://github.com/liluo/py-oauth2',
    author = 'liluo',
    author_email = 'i@liluo.org',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['httplib2'],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
