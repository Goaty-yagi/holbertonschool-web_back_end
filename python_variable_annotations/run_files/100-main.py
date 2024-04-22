#!/usr/bin/env python3
import sys

sys.path.append(
    '/root/holbertonschool-web_back_end/python_variable_annotations')

safe_first_element = __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)
