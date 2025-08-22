#!/usr/bin/env python3
"""
Setup script for Hash Verify
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="hash-verify",
    version="2.0.0",
    author="buggymaytricks",
    description="A Python script for file integrity verification using multiple hash algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/buggymaytricks/Hash-Verify",
    py_modules=["hash_verify_improved"],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Archiving",
        "Topic :: Utilities",
    ],
    keywords="hash verification integrity md5 sha1 sha256 sha512 sha3 checksum",
    entry_points={
        "console_scripts": [
            "hash-verify=hash_verify_improved:main",
        ],
    },
    install_requires=[
        # No external dependencies - uses only standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/buggymaytricks/Hash-Verify/issues",
        "Source": "https://github.com/buggymaytricks/Hash-Verify",
    },
)