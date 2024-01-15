from importlib.metadata import PackageNotFoundError, version
from typing import Optional

__version__ : Optional[str]
try:
    __version__ = version(__package__)
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = None
