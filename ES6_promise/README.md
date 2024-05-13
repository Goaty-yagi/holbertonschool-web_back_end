# ES6 Promises

"ES6 Promises" is a repository dedicated to exploring and demonstrating the use of Promises in JavaScript, specifically focusing on the features introduced in ECMAScript 6 (ES6). 

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_promise/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Your code will be tested using Jest and the command npm run test
- Your code will be verified against lint using ESLint
- All of your functions must be exported

## Practice Exercises

### 0. Keep every promise you make and only make promises you can keep

**File:** [0-promise.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_promise/0-promise.js)<br>
**Description:** Return a Promise using this prototype function getResponseFromAPI()<br>
**Requirement:** <br>
```bash
bob@dylan:~$ cat 0-main.js
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
true
bob@dylan:~$ 
```
