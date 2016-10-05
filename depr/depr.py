import functools
import inspect
import warnings


class Deprecator(object):
    """
    """
    def __init__(self, reason=None, replacement=None):
        assert not (reason and replacement), "can only pass msg or replacement, not both"
        if replacement is not None:
            assert callable(replacement), "Replacement function needs to be a callable as well"
            self.reason = "Use new function {} instead".format(replacement.__name__)
        else:
            self.reason = reason or "Call to deprecated function"

    def __call__(self, func):
        @functools.wraps(func)
        def _deprecate():
            warnings.warn(self.reason, category=DeprecationWarning, stacklevel=2)
            return func()

        return _deprecate


def deprecate(func_or_reason=None, *args, **kwargs):
    if callable(func_or_reason):
        return Deprecator()(func_or_reason)
    else:
        return Deprecator(*args, **kwargs)
