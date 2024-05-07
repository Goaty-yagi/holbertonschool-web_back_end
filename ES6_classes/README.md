# ES6 classes
ES6 Classes" is a comprehensive repository focused on understanding and leveraging the power of classes introduced in ECMAScript 2015 (ES6). 

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Your code will be tested using Jest and the command npm run test
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test

## Practice Exercises

### 0. You used to attend a place like this at some point

**File:** [0-classroom.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/0-classroom.js)<br>
**Description:** Implement a class named ClassRoom:<br>
**Requirement:** <br>
- Prototype: export default class ClassRoom
- It should accept one attribute named maxStudentsSize (Number) and assigned to _maxStudentsSize

### 1. Let's make some classrooms

**File:** [1-make_classrooms.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/1-make_classrooms.js)<br>
**Description:** Import the ClassRoom class from 0-classroom.js.<br>
**Requirement:** <br>
- Implement a function named initializeRooms. It should return an array of 3 ClassRoom objects with the sizes 19, 20, and 34 (in this order).


### 2. A Course, Getters, and Setters

**File:** [2-hbtn_course.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/2-hbtn_course.js)<br>
**Description:** Implement a class named HolbertonCourse:<br>
**Requirement:** <br>
- Constructor attributes:
 -- name (String)
 -- length (Number)
 -- students (array of Strings)
- Make sure to verify the type of attributes during object creation
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter and setter for each attribute.