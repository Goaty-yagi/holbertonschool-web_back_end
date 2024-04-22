#!/usr/bin/env python3
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_variable_annotations')
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)