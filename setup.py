#!/usr/bin/python3
from setuptools import setup, find_packages

readme = open("README.rst").read()

setup(
	name = "consolemsg",
	version = "0.2",
	description = "Simple semantic functions for colorfull console messages",
	author = "David Garcia Garzon",
	author_email = "voki@canvoki.net",
	url = 'https://github.com/GuifiBaix/python-consolemsg',
	long_description = readme,
	license = 'GNU General Public License v3 or later (GPLv3+)',
	py_modules = [ 'consolemsg' ],
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Multimedia',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: OS Independent',
	],
)

