# Python - Async

Python - Async is a repository dedicated to asynchronous programming in Python.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_function/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- A README.md file, at the root of the folder of the project, is mandatory
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using wc
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## Practice Exercises

### 0. The basics of async

**File:** [0-basic_async_syntax.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_function/0-basic_async_syntax.py)<br>
**Description:** Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.<br>
**Requirement:** <br>
Use the random module.


### 1. Let's execute multiple coroutines at the same time with async

**File:** [1-concurrent_coroutines.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_function/1-concurrent_coroutines.py)<br>
**Description:** Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.<br>
**Requirement:** <br>
wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.


### 2. Measure the runtime

**File:** [2-measure_runtime.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_function/2-measure_runtime.py)<br>
**Description:** From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.<br>
**Requirement:** <br>
Use the time module to measure an approximate elapsed time.


### 2. Tasks

**File:** [3-tasks.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/python_async_function/3-tasks.py)<br>
**Description:** Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.<br>
**Requirement:** <br>
None
