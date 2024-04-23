#!/usr/bin/env python3
"""
This module provides measure_runtime function
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime and return it.
    """
    result = async_comprehension()
    start_time = time.time()
    await asyncio.gather(result)
    end_time = time.time()
    return end_time - start_time
