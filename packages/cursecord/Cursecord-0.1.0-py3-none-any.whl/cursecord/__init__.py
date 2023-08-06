#!/usr/bin/env python3

__author__ = "Andy"
__license__ = "MIT"
__version__ = "0.1.0-alpha"

from typing import Literal, NamedTuple


class Version(NamedTuple):
    major: int
    minor: int
    patch: int

    id: Literal["alpha", "beta", "final"]


version = Version(0, 1, 0, "alpha")
