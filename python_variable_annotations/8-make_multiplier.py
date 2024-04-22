#!/usr/bin/env python3
"""
This module provides make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier.
    """
    fun: Callable[[float], float] = lambda x: x*x
    return fun
