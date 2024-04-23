#!/usr/bin/env python3

import asyncio
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_async_comprehension')
async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
