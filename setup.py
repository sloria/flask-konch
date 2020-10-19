# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages


INSTALL_REQUIRES = ["Flask>=0.11", "konch>=2.0.0"]
EXTRAS_REQUIRE = {
    "tests": ["pytest"],
    "lint": [
        "flake8==3.8.4",
        "flake8-bugbear==20.1.4",
        "pre-commit~=2.7",
    ],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="flask-konch",
    version=find_version("flask_konch/__init__.py"),
    description="An improved shell command for the Flask CLI",
    long_description=read("README.rst"),
    author="Steven Loria",
    author_email="sloria1@gmail.com",
    url="https://github.com/sloria/flask-konch",
    packages=find_packages(exclude=("test*",)),
    package_dir={"flask-konch": "flask-konch"},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    zip_safe=False,
    keywords="flask-konch",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Shells",
    ],
    test_suite="tests",
    entry_points={"flask.commands": ["konch=flask_konch.cli:cli"]},
)
