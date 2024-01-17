import re
from setuptools import setup, find_packages


INSTALL_REQUIRES = ["flask>=2.2.5", "konch>=4"]
EXTRAS_REQUIRE = {
    "tests": ["pytest"],
    "lint": [
        "flake8==7.0.0",
        "flake8-bugbear==24.1.16",
        "pre-commit~=3.6",
    ],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]
PYTHON_REQUIRES = ">=3.8"


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname) as fp:
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
    python_requires=PYTHON_REQUIRES,
    license="MIT",
    zip_safe=False,
    keywords="flask-konch",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Shells",
    ],
    test_suite="tests",
    entry_points={"flask.commands": ["konch=flask_konch.cli:cli"]},
)
