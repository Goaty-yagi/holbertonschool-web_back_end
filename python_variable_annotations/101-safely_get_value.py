#!/usr/bin/env python3
"""
This module provides safe_first_element function
"""
from typing import TypeVar, Mapping, Any, Union, Optional

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[T] = None
) -> Union[Any, T]:
    """
    Retrives value form the dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
