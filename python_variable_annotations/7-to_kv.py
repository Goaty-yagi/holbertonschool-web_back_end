#!/usr/bin/env python3
"""
This module provides to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function receive a str and int or float and return
    tuple.
    """
    return (k, v*v)
