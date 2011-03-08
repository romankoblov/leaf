#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages
import os.path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='leaf',
    version='0.4',
    description='Simple Python library for HTML parsing',
    author='Roman Koblov',
    author_email='pingu.g@gmail.com',
    url='https://github.com/penpen/Leaf',
    license='MIT',
    keywords=['html', 'parsing', 'web scrapping'],
    packages=['leaf'],
    data_files=[
            ('', ['LICENSE', 'README.rst'])
    ],
    package_data={
        '': ['*.txt', '*.rst', '*.md']
    },
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Topic :: Scientific/Engineering :: Information Analysis'],
    install_requires = ['setuptools', 'lxml'],
    long_description=read('README.rst'),
)