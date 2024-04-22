#!/usr/bin/env python3
"""
This module provides wait_random function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns rundom number asynchronous
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
