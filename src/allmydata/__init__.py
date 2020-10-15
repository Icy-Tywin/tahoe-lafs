"""
Decentralized storage grid.

community web site: U{https://tahoe-lafs.org/}

This file has been ported to Python 3.
"""

from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from future.utils import PY2
if PY2:
    from future.builtins import filter, map, zip, ascii, chr, hex, input, next, oct, open, pow, round, super, bytes, dict, list, object, range, str, max, min  # noqa: F401

__all__ = [
    "__version__",
    "full_version",
    "branch",
    "__appname__",
    "__full_version__",
]

__version__ = "unknown"
try:
    from allmydata._version import __version__
except ImportError:
    # We're running in a tree that hasn't run update_version, and didn't
    # come with a _version.py, so we don't know what our version is.
    # This should not happen very often.
    pass

full_version = "unknown"
branch = "unknown"
try:
    from allmydata._version import full_version, branch
except ImportError:
    # We're running in a tree that hasn't run update_version, and didn't
    # come with a _version.py, so we don't know what our full version or
    # branch is. This should not happen very often.
    pass

__appname__ = "tahoe-lafs"

# __full_version__ is the one that you ought to use when identifying yourself
# in the "application" part of the Tahoe versioning scheme:
# https://tahoe-lafs.org/trac/tahoe-lafs/wiki/Versioning
__full_version__ = __appname__ + '/' + str(__version__)


# Install Python 3 module locations in Python 2:
from future import standard_library
standard_library.install_aliases()


# Monkey-patch 3rd party libraries:
from ._monkeypatch import patch
patch()
del patch
