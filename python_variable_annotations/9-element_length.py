#!/usr/bin/env/ python3
"""
This module provides element_length function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a list as argument and returns
    a tuple list.
    """
    return [(i, len(i)) for i in lst]
