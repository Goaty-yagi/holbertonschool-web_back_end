#!/usr/bin/env python3

import asyncio
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_async_comprehension')
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
