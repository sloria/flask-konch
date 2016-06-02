# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages


REQUIRES = [
    'Flask>=0.11',
    'konch>=2.0.0',
]

def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version('flask_konch/__init__.py')


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='flask-konch',
    version=__version__,
    description='An improved shell command for the Flask CLI',
    long_description=read('README.rst'),
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/flask-konch',
    packages=find_packages(exclude=("test*", )),
    package_dir={'flask-konch': 'flask-konch'},
    include_package_data=True,
    install_requires=REQUIRES,
    license=read("LICENSE"),
    zip_safe=False,
    keywords='flask-konch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='tests',
    entry_points={
        'flask.commands': [
            'konch=flask_konch.cli:cli'
        ]
    },
)
