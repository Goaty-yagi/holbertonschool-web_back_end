#!/usr/bin/env python3

import asyncio
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_async_function')
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
