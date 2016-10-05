import functools
import inspect
import warnings


class Deprecator(object):
    """
    """
    def __init__(self, msg=None, replacement=None):
        if replacement is not None:
            assert callable(replacement), "Replacement function needs to be a callable as well"
            self.msg = "Use new function {} instead".format(replacement.__name__)
        else:
            self.msg = msg or "Call to deprecated function"

    def __call__(self, func):
        @functools.wraps(func)
        def _deprecate():
            warnings.warn(self.msg, category=DeprecationWarning, stacklevel=2)
            return func()

        return _deprecate


deprecate = Deprecator
