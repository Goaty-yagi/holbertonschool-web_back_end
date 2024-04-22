#!/usr/bin/env python3

import sys
sys.path.append('/root/holbertonschool-web_back_end/python_async_function')
'''
Test file for printing the correct output of the wait_n coroutine
'''

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
