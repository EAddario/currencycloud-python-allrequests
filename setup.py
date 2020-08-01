#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="currencycloud-python-allrequests",
    version="0.0.1",
    license="MIT",
    description="Executes all API calls available in the forked Currencycloud Java SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Ed Addario",
    author_email="eaddario@hotmail.com",
    url="https://github.com/EAddario/currencycloud-python-allrequests",

    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],

    python_requires='>=3.3',
    scripts=['bin/currencycloud-requests'],

    keywords=[],
    install_requires=["currencycloud-python-client", "PyYAML", "colorama"],
    tests_require=[]
)
