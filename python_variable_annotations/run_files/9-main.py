#!/usr/bin/env python3
import sys

sys.path.append(
    '/root/holbertonschool-web_back_end/python_variable_annotations')
element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
