Changelog
=========

2.0.0 (2019-01-13)
******************

Features:

* Add ``KONCH_IPY_COLORS`` and ``KONCH_IPY_HIGHLIGHTING_STYLE`` options.


Bug fixes:

* Respect ``KONCH_IPY_EXTENSIONS`` option.

Other changes:

* Drop support for Python 3.4. Python 2.7 and >=3.5 are supported.

1.2.0 (2017-10-26)
******************

* Add Flask shell context (added with
  ``app.shell_context_processor()``) to the konch context (`#1 <https://github.com/sloria/flask-konch/pull/1>`_)
  Thanks `@sbhtw  <https://github.com/sbhtw>`_.


1.1.0 (2016-06-12)
******************

* Add ``KONCH_OUTPUT`` config option.

1.0.0 (2016-06-01)
******************

* First PyPI release.
