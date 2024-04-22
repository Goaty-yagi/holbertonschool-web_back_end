#!/usr/bin/env python3
"""
This module provides safe_first_element function
"""
from typing import Optional, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Retrieve the first element of the list
    """
    if lst:
        return lst[0]
    else:
        return None
