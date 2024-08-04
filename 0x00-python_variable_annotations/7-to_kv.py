#!/usr/bin/env python3

"""Contains the to_kv Module"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """takes two args and return a tuple of the rsult"""
    return (k, v*v)
