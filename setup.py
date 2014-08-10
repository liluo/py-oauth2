#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='py-oauth2',
    version='0.0.10',
    keywords=('Python', 'pyoauth2', 'OAuth2', 'Douban', 'GitHub', 'Weibo'),
    description='A Python wrapper for the OAuth 2.0 specification.',
    long_description=open('README.rst').read(),
    license='MIT License',

    url='https://github.com/liluo/py-oauth2',
    author='liluo',
    author_email='i@liluo.org',

    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
