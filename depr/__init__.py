import functools
import warnings
import inspect


class Deprecator(object):
    def __init__(self, reason=None, replacement=None):
        assert not (reason and replacement), "can only pass msg or replacement, not both"
        self.replacement = replacement
        self.reason = reason

    def __call__(self, to_deprecate):
        @functools.wraps(to_deprecate)
        def _deprecate(*args, **kwargs):
            if self.replacement is not None:
                assert callable(self.replacement), "Replacement function needs to be a callable as well"
                message = "Use new function {} instead".format(self.replacement.__name__)
            else:
                message = self.reason or "{} is deprecated".format(to_deprecate.__name__)

            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            return to_deprecate(*args, **kwargs)

        return _deprecate


def deprecate(to_deprecate=None, *args, **kwargs):
    """Mark a function as deprecated, can be used in these ways

    @deprecate(reason="Changed to a better way")
    def function():
        pass

    @deprecate(replacement=other_callable)
    def function():
         pass

    or just:
    @deprecate
    def function():
        pass

    """
    if callable(to_deprecate):
        return Deprecator()(to_deprecate)
    elif to_deprecate is None or inspect.isclass(to_deprecate):
        return Deprecator(*args, **kwargs)
    else:
        # should add some way to warn whenever the object
        # itself is accessed (possibly using getters/setters?)
        return to_deprecate
