# Python_variable_annotations

This repository contains examples and resources for using variable annotations in Python. Variable annotations are a feature introduced in Python 3.6 that allow you to explicitly specify the types of variables in your code, enhancing readability and enabling static type checking.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/LEARNING_OBJECTIVES.md) file for details.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your classes should have a documentation (python3 -c 'print(**import**("my_module").MyClass.**doc**)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)' and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Practice Exercises

### 0. Integers addition

**File:** [0-add.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/0-add.py)<br>
**Description:** Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.<br>
**Requirement:** <br>
None

### 1. Basic annotations - concat

**File:** [1-concat.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/1-concat.py)<br>
**Description:** Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.<br>
**Requirement:** <br>
None

### 2. Basic annotations - floor

**File:** [2-floor.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/2-floor.py)<br>
**Description:** Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.<br>
**Requirement:** <br>
None

### 3. Basic annotations - to string

**File:** [3-to_str.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/3-to_str.py)<br>
**Description:** Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.<br>
**Requirement:** <br>
None

### 4. Define variables

**File:** [4-define_variables.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/4-define_variables.py)<br>
**Description:** Define and annotate the following variables with the specified values.<br>
**Requirement:** <br>

- a, an integer with a value of 1
- pi, a float with a value of 3.14
- i_understand_annotations, a boolean with a value of True
- school, a string with a value of “Holberton”

### 5. Complex types - list of floats

**File:** [5-sum_list.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/5-sum_list.py)<br>
**Description:** Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.<br>
**Requirement:** <br>
None

### 6. Complex types - mixed list

**File:** [6-sum_mixed_list.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/6-sum_mixed_list.py)<br>
**Description:** Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.<br>
**Requirement:** <br>
None

### 7. Complex types - string and int/float to tuple

**File:** [7-to_kv.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/7-to_kv.py)<br>
**Description:** Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.<br>
**Requirement:** <br>
None

### 8. Complex types - functions

**File:** [8-make_multiplier.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/8-make_multiplier.py)<br>
**Description:** Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.<br>
**Requirement:** <br>
None

### 9. Let's duck type an iterable object

**File:** [9-element_length.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/9-element_length.py)<br>
**Description:** Annotate the below function’s parameters and return values with the appropriate types.<br>
**Requirement:** <br>
None

### 10. Duck typing - first element of a sequence

**File:** [100-safe_first_element.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/100-safe_first_element.py)<br>
**Description:** Augment the following code with the correct duck-typed annotations.<br>
**Requirement:** <br>

```python
# The types of the elements of the input are not known
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```

```python
bob@dylan:~$ cat 100-main.py
#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)

bob@dylan:~$ ./100-main.py
{'lst': typing.Sequence[typing.Any], 'return': typing.Optional[typing.Any]}
```

### 11. More involved type annotations

**File:** [101-safely_get_value.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/101-safely_get_value.py)<br>
**Description:** Given the parameters and the return values, add type annotations to the function.<br>
**Requirement:** <br>

```python
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
```

### 12. Type Checking

**File:** [102-type_checking.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_variable_annotations/102-type_checking.py)<br>
**Description:** Use mypy to validate the following piece of code and apply any necessary changes.<br>
**Requirement:** <br>

```python
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
```
