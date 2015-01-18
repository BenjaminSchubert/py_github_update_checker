#!/usr/bin/python3
# -*- Coding : UTF-8 -*-


from os import path
import github_update_checker
from setuptools import setup, find_packages

file_path = path.abspath(path.dirname(__file__))
with open(path.join(file_path, "README.md"), encoding="UTF-8") as f:
    long_description = f.read()


setup(
    name="github_update_checker",
    version=github_update_checker.__version__,
    description="A simple update checker for github in python",
    long_description=long_description,
    url="https://github.com/Tellendil/py_github_update_checker",
    author="Benjamin Schubert",
    author_email="ben.c.schubert@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    keywords="update",
    packages=find_packages()
)
