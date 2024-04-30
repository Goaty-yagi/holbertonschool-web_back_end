# NoSQL

Python NoSQL: Explore the usage and benefits of NoSQL in Python.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/LEARNING_OBJECTIVES.md) file for details.

## Requirements
### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 - LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: // my comment
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- Your code should not be executed when imported (by using if __name__ == "__main__":)


## Practice Exercises

### 0. List all databases

**File:** [0-list_databases](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/0-list_databases)<br>
**Description:** Write a script that lists all databases in MongoDB.<br>

### 1. Create a database

**File:** [1-use_or_create_database](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/1-use_or_create_database)<br>
**Description:** Write a script that creates or uses the database my_db.<br>

### 2. Insert document

**File:** [2-insert](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/2-insert)<br>
**Description:** Write a script that inserts a document in the collection school.<br>
**Requirements**<br>
- The document must have one attribute name with value “Holberton school”
- The database name will be passed as option of mongo command


### 3. All documents

**File:** [3-all](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/3-all)<br>
**Description:** Write a script that lists all documents in the collection school.<br>
**Requirements**<br>
- The database name will be passed as option of mongo command


### 4. All matches

**File:** [4-match](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/4-match)<br>
**Description:** Write a script that lists all documents with name="Holberton school" in the collection school.<br>
**Requirements**<br>
- The database name will be passed as option of mongo command


### 5. Count

**File:** [5-count](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/5-count)<br>
**Description:** Write a script that displays the number of documents in the collection school.<br>
**Requirements**<br>
- The database name will be passed as option of mongo command

### 6. Update

**File:** [6-update](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/NoSQL/6-update)<br>
**Description:** Write a script that adds a new attribute to a document in the collection school.<br>
**Requirements**<br>
- The script should update only document with name="Holberton school" (all of them)
- The update should add the attribute address with the value “972 Mission street”
- The database name will be passed as option of mongo command
