# Deprecate decorator

[![Build Status](https://travis-ci.org/AndreaCrotti/depr.png)](https://travis-ci.org/AndreaCrotti/depr)

[![Coverage Status](https://coveralls.io/repos/github/AndreaCrotti/depr/badge.svg?branch=master)](https://coveralls.io/github/AndreaCrotti/depr?branch=master)

Simple decorator to deprecate functions in your codebase.


Can be used passing a reason for deprecation:

    @deprecate(reason="Changed to a better way")
    def function():
        pass

A callable with the new function to use:

    @deprecate(replacement=other_callable)
    def function():
         pass


Or just no options, and it will still raise a DeprecatationWarning using the deprecated function name:
or just:


    @deprecate
    def function():
        pass
