import functools
import warnings


# def get_version():
#     import git
#     return git.Repo('.').tags[-1].name

# __version__ = get_version()
__version__ = '0.1.7'

class Deprecator(object):
    def __init__(self, reason=None, replacement=None):
        assert not (reason and replacement), "can only pass msg or replacement, not both"
        if replacement is not None:
            assert callable(replacement), "Replacement function needs to be a callable as well"
            self.message = "Use new function {} instead".format(replacement.__name__)
        else:
            self.message = reason or "Call to deprecated function"

    def __call__(self, func):
        @functools.wraps(func)
        def _deprecate(*args, **kwargs):
            warnings.warn(self.message, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return _deprecate


def deprecate(function=None, *args, **kwargs):
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
    if callable(function):
        return Deprecator()(function)
    else:
        return Deprecator(*args, **kwargs)
