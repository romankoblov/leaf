#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages
import os.path


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='leaf',
    version='1.0.3',
    description='Simple Python library for HTML parsing',
    author='Roman Koblov',
    author_email='pingu.g@gmail.com',
    url='https://github.com/penpen/leaf',
    license='MIT',
    keywords=['html', 'parsing', 'web scrapping'],
    packages=['leaf'],
    data_files=[
            ('', ['LICENSE.txt', 'README.rst', 'AUTHORS.rst'])
    ],
    package_data={
        '': ['*.txt', '*.rst', '*.md']
    },
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Topic :: Scientific/Engineering :: Information Analysis'],
    install_requires=['setuptools', 'lxml', 'cssselect', 'six'],
    long_description=read('README.rst') + read('CHANGES.rst'),
)
