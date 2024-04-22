#!/usr/bin/env python3

import sys
import asyncio
sys.path.append('/root/holbertonschool-web_back_end/python_async_function')
'''
Test file for printing the correct output of the wait_n coroutine
'''

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
