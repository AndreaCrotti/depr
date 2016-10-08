===================
Deprecate decorator
===================

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |requires| |coveralls|
        | |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |travis| image:: https://travis-ci.org/ionelmc/pytest-benchmark.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/pytest-benchmark

.. |requires| image:: https://requires.io/github/AndreaCrotti/depr/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/AndreaCrotti/depr/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/AndreaCrotti/depr/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/AndreaCrotti/depr

.. |codecov| image:: https://codecov.io/github/ionelmc/pytest-benchmark/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/pytest-benchmark

.. |landscape| image:: https://landscape.io/github/ionelmc/pytest-benchmark/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/pytest-benchmark/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/80e2960677c24d5083a802dd57df17dc.svg?style=flat
    :target: https://www.codacy.com/app/ionelmc/pytest-benchmark
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/pytest-benchmark/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/pytest-benchmark
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/depr.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/depr

.. |downloads| image:: https://img.shields.io/pypi/dm/depr.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/depr

.. |wheel| image:: https://img.shields.io/pypi/wheel/depr.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/depr

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/depr.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/depr

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/depr.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/depr


Installation
============

::

   pip install depr



Documentation
=============


Simple decorator to deprecate functions in your codebase.


Can be used passing a reason for deprecation:

::

    @deprecate(reason="Changed to a better way")
    def function():
        pass

A callable with the new function to use:

::

    @deprecate(replacement=other_callable)
    def function():
         pass


Or just no options, and it will still raise a DeprecatationWarning using the deprecated function name:

::

    @deprecate
    def function():
        pass
   
