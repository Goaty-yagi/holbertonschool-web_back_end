#!/usr/bin/env python3

import asyncio
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_async_comprehension')
measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

