#!/usr/bin/env python3
import sys

sys.path.append(
    '/root/holbertonschool-web_back_end/python_variable_annotations')
make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
