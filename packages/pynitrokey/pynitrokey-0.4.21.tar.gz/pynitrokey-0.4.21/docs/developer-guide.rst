pynitrokey Developer Guide
==========================

Linters
-------

We use `flake8`_ for style checks, `black`_ for code formatting, `isort`_ for import sorting and `mypy`_ for static type analysis.  To run all checks, execute ``make check``.  (Before using it for the first time, you have to call ``make init`` to setup a virtual environment and install the required dependencies.)

.. _flake8: https://flake8.pycqa.org/en/latest/
.. _black: https://github.com/psf/black
.. _isort: https://github.com/PyCQA/isort
.. _mypy: https://github.com/python/mypy

mypy is configured to only check annotated code.  If you add new code, please consider adding type annotations and enabling strict checks for your modules in ``mypy.ini``.

Please make sure that all checks pass for your code before opening a PR.

Signed Commits
--------------

If you have an OpenPGP key, please sign all your commits with it.  We require all commits on the master branch to be signed.  If you don’t have an OpenPGP key, a developer that reviewed your commits will sign them for you.

Design Patterns
---------------

Output and Error Handling
~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``pynitrokey.helpers.local_print`` for printing messages to the user.  This helper method also adds the output to the log file.

To report an error, use ``pynitrokey.helpers.local_critical`` or raise a ``pynitrokey.cli.exceptions.CliException`` (that uses ``local_critical`` internally).  Per default, this adds a support hint to the output that points the user to the log file.

Password Input
~~~~~~~~~~~~~~

Commands that require a password should first try to read the password from an environment variable.  If the environment variable is not set, they should prompt the user to enter the password.  Passwords must not be passed as a command-line argument.
