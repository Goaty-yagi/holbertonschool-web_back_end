#!/usr/bin/env python3
"""
This module provides async_generator function
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yield random number asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
