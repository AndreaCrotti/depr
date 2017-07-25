import pytest
try:
    from unittest import mock
except ImportError:
    import mock


from depr import deprecate


@mock.patch('warnings.warn')
def test_simple_function_deprecation(warn):
    @deprecate(reason="Should not use this anymore")
    def func():
        return 42

    assert func() == 42
    assert warn.called
    assert warn.call_args[0][0] == "Should not use this anymore"


def test_function_with_arguments():
    @deprecate(reason="Should not use this anymore")
    def func(a, b):
        return a + b

    assert func(1, 2) == 3


def test_deprecation_no_arguments():
    @deprecate
    def func():
        return 42

    @deprecate()
    def func2():
        return 42

    assert func() == 42
    assert func2() == 42


@pytest.mark.skip(reason="Not implemented yet")
def test_simple_class_deprecation():
    @deprecate(reason="deprecated")
    class A(object):
        pass

    # TODO: should it warn on every method or attribute access?
    a = A()


@mock.patch('warnings.warn')
def test_suggest_replacement(warn):
    def new_func():
        return 1

    # TODO: add if the new function is backward compatible at the arguments level or not
    @deprecate(replacement=new_func)
    def old_func():
        return 1

    assert old_func() == 1
    assert warn.called
    assert 'new_func' in warn.call_args[0][0]


class Simple:
    def __init__(self, a, b):
        self.a = a
        self.b = b


@mock.patch('warnings.warn')
def test_class_deprecation(warn):
    s = Simple(a=1, b=2)
    assert s.a == 1

    SimpleDepr = deprecate(Simple)
    s_depr = SimpleDepr(a=1, b=2)
    assert s_depr.a == 1

    assert warn.called
    assert warn.call_args[0][0] == "Simple is deprecated"


def test_object_deprecation():
    s = Simple(a=1, b=2)
    s_depr = deprecate(s)
    assert s.a == 1
    assert s_depr.a == 1
