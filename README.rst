***********
Flask-Konch
***********

.. |pypi-package| |build-status|

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/flask-konch.png
    :alt: Flask-Konch

An improved shell command for Flask
===================================

Flask-Konch adds an improved shell command, ``flask konch``, to the `Flask CLI <http://flask.pocoo.org/docs/0.11/cli/>`_.


Benefits of ``flask konch`` over ``flask shell``
================================================

- Uses IPython, BPython, or ptpython if available, and falls back to built-in interpreter
- Automatically imports top-level Flask functions and classes by default
- Define additional variables to include in the shell context
- Configurable banner and prompt

Flask-Konch uses `konch <https://github.com/sloria/konch>`_, a shell configuration utility, under the hood.

Get it now
----------
::

    pip install flask-konch

Usage
=====

To run the shell:

.. code-block:: bash

   export FLASK_APP=path/to/app.py
   flask konch

To add additional variables to the shell context:

.. code-block:: python

   app = Flask(__name__)
   app.config.update({
      'KONCH_CONTEXT': {
         'db': database,
         'User': User,
      }
   })


Configuration options
=====================

- ``KONCH_FLASK_IMPORTS``: Whether to automatically import top-level Flask functions and classes. Defaults to ``True``.
- ``KONCH_CONTEXT``: Dictionary of additional variables to include in the shell context.
- ``KONCH_SHELL``: May be ``'ipy'``, ``'bpy'``, ``'ptpy'``, ``'ptipy'``, ``'py'``, or ``'auto'`` (default).
- ``KONCH_BANNER``: Custom banner.
- ``KONCH_PROMPT``: Custom prompt.
- ``KONCH_CONTEXT_FORMAT``: Format to display shell context. May be ``'full'``, ``'short'``, or a function that receives the context dictionary as input and returns a string.
- ``KONCH_IPY_AUTORELOAD``: Whether to load and enable the IPython autoreload extension (must be using ``ipython`` shell).
- ``KONCH_IPY_EXTENSIONS``: List of IPython extension names to load (must be using ``ipython`` shell).
- ``KONCH_PTPY_VI_MODE``: Enable vi mode (must be using ``ptpython`` shell).



Project Links
=============

- PyPI: https://pypi.python.org/pypi/flask-konch
- Issues: https://github.com/sloria/flask-konch/issues

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/flask-konch/blob/master/LICENSE>`_ file for more details.


.. |pypi-package| image:: https://badge.fury.io/py/flask-konch.svg
    :target: http://badge.fury.io/py/flask-konch
    :alt: Latest version
.. .. |build-status| image:: https://travis-ci.org/sloria/flask-konch.svg?branch=pypi
..     :target: https://travis-ci.org/sloria/flask-konch
..     :alt: Travis-CI
