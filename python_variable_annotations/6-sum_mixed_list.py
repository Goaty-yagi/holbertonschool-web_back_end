#!/usr/bin/env python3
"""
This module provides sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function receive a union list and return
    sum of them.
    """
    return sum(mxd_lst)
