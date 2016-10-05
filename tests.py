import pytest
try:
    from unittest import mock
except ImportError:
    import mock


from depr import depr


def test_hello():
    assert 1 + 1 == 2


@mock.patch('warnings.warn')
def test_simple_function_deprecation(warn):
    @depr.deprecate(msg="Should not use this anymore")
    def func():
        return 42

    assert func() == 42
    assert warn.called
    assert warn.call_args[0][0] == "Should not use this anymore"


def test_simple_class_deprecation():
    @depr.deprecate(msg="deprecated")
    class A(object):
        pass

    # TODO: should it warn on every method or attribute access?
    a = A()


# TODO: some kind of versioning should be added too?
@mock.patch('warnings.warn')
def test_suggest_replacement(warn):
    def new_func():
        return 1

    # TODO: add if the new function is backward compatible at the arguments level or not
    @depr.deprecate(replacement=new_func)
    def old_func():
        return 1

    assert old_func() == 1
    assert warn.called
    assert 'new_func' in warn.call_args[0][0]
