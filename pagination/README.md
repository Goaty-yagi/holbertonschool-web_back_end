# NoSQL

Python NoSQL: Explore the usage and benefits of NoSQL in Python.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/pagination/LEARNING_OBJECTIVES.md) file for details.

## Requirements


- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.


## Practice Exercises

### 0. Simple helper function

**File:** [0-simple_helper_function.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/pagination/0-simple_helper_function.py)<br>
**Description:** Write a function named index_range that takes two integer arguments page and page_size.<br>
**Requirement:** <br>
- The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

- Page numbers are 1-indexed, i.e. the first page is page 1.


### 1. Simple pagination

**File:** [1-simple_pagination.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/pagination/1-simple_pagination.py)<br>
**Description:** Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.<br>
**Requirement:** <br>
- You have to use this CSV file (same as the one presented at the top of the project)
- Use assert to verify that both arguments are integers greater than 0.
- Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
- If the input arguments are out of range for the dataset, an empty list should be returned.


### 2. Hypermedia pagination

**File:** [2-hypermedia_pagination.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/pagination/2-hypermedia_pagination.py)<br>
**Description:** Replicate code from the previous task.<br>
Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:<br>
**Requirement:** <br>
- page_size: the length of the returned dataset page
- page: the current page number
- data: the dataset page (equivalent to return from previous task)
- next_page: number of the next page, None if no next page
- prev_page: number of the previous page, None if no previous page
- total_pages: the total number of pages in the dataset as an integer

- Make sure to reuse get_page in your implementation.
- You can use the math module if necessary.

### 3. Deletion-resilient hypermedia pagination

**File:** [3-hypermedia_del_pagination.py](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/pagination/3-hypermedia_del_pagination.py)<br>
**Description:** The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.<br>

Start 3-hypermedia_del_pagination.py with this code:<br>
Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.<br>
**Requirement:** <br>
- The method should return a dictionary with the following key-value pairs:
 -- index: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
 -- next_index: the next index to query with. That should be the index of the first item after the last item on the current page.
 -- page_size: the current page size
 -- data: the actual page of the dataset

- Use assert to verify that index is in a valid range.
- If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.


- Make sure to reuse get_page in your implementation.
- You can use the math module if necessary.


