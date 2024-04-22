#!/usr/bin/env python3
import sys
sys.path.append('/root/holbertonschool-web_back_end/python_variable_annotations')
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)