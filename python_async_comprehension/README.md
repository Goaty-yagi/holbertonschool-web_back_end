# Python async comprehension

Python Async Comprehension: Explore the usage and benefits of asynchronous comprehensions in Python.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_comprehension/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.x)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.


## Practice Exercises

### 0. Async Generator

**File:** [0-basic_async_syntax.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_comprehension/0-basic_async_syntax.py)<br>
**Description:** Write a coroutine called async_generator that takes no arguments.<br>
**Requirement:** <br>
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.


### 1. Async Comprehensions

**File:** [1-async_comprehension.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_comprehension/1-async_comprehension.py)<br>
**Description:** Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.<br>
**Requirement:** <br>
The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.


### 2. Run time for four parallel comprehensions

**File:** [2-measure_runtime.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_comprehension/2-measure_runtime.py)<br>
**Description:** Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.<br>
**Requirement:** <br>
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
