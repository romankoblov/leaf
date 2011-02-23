#!/usr/bin/env python
# encoding: utf-8

setup(name='Leaft',
    version='0.4',
    description='Simple Python library for HTML parsing',
    author='Roman Koblov',
    author_email='pingu.g@gmail.com',
    url='https://github.com/penpen/Leaf',
    license='MIT',
    keywords=['html', 'parsing', 'web scrapping'],
    packages=['leaf'],
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Topic :: Scientific/Engineering :: Information Analysis'],
    install_requires = ['lxml'],
    long_description=open('README.rst')
)