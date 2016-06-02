***********
Flask-Konch
***********

|pypi-package| |build-status| |docs|

An improved shell command for Flask
===================================

Flask-Konch adds an improved shell command, ``flask konch``, to the `Flask CLI <http://flask.pocoo.org/docs/0.11/cli/>`_


Benefits of ``flask konch`` over ``flask shell``
================================================

- Uses IPython, BPython, or ptpython if available, and falls back to built-in interpreter
- Automatically imports top-level Flask functions and classes by default
- Define additional variables to include in the shell context
- Configurable banner and prompt

Get it now
----------
::

    pip install flask-konch


http://flask-konch.readthedocs.io/
========================================

Project Links
=============

- Docs: http://flask-konch.rtfd.org/
- Changelog: http://flask-konch.readthedocs.io/en/latest/changelog.html
- PyPI: https://pypi.python.org/pypi/flask-konch
- Issues: https://github.com/sloria/flask-konch/issues

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/flask-konch/blob/master/LICENSE>`_ file for more details.


.. |pypi-package| image:: https://badge.fury.io/py/flask-konch.svg
    :target: http://badge.fury.io/py/flask-konch
    :alt: Latest version
.. |build-status| image:: https://travis-ci.org/sloria/flask-konch.svg?branch=pypi
    :target: https://travis-ci.org/marshmallow-code/flask-konch
    :alt: Travis-CI
.. |docs| image:: https://readthedocs.org/projects/flask-konch/badge/
   :target: http://flask-konch.readthedocs.io/
   :alt: Documentation

