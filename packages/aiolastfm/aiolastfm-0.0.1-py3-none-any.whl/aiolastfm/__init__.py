# Future
from __future__ import annotations

# Standard Library
import logging
from typing import Final, Literal, NamedTuple

# My stuff


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: Final[VersionInfo] = VersionInfo(major=0, minor=0, micro=1, releaselevel="final", serial=0)

__title__: Final[str] = "aiolastfm"
__author__: Final[str] = "Axelancerr"
__copyright__: Final[str] = "Copyright 2022-present Axelancerr"
__license__: Final[str] = "MIT"
__version__: Final[str] = "0.0.1"
__maintainer__: Final[str] = "Aaron Hennessey"
__source__: Final[str] = "https://github.com/Axelware/aiolastfm"

logging.getLogger("aiolastfm")
