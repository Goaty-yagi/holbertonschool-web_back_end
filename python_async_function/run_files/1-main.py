#!/usr/bin/env python3

import asyncio
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_async_function')
'''
Test file for printing the correct output of the wait_n coroutine
'''

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
