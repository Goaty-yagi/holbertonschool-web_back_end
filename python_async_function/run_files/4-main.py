#!/usr/bin/env python3

import sys
import asyncio
sys.path.append('/root/holbertonschool-web_back_end/python_async_function')
task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
