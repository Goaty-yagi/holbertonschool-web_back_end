# ES6 Basics

This repository contains examples and resources for using variable annotations in Python. Variable annotations are a feature introduced in Python 3.6 that allow you to explicitly specify the types of variables in your code, enhancing readability and enabling static type checking.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Your code will be tested using the Jest Testing Framework
- Your code will be analyzed using the linter ESLint along with specific rules that we’ll provide
- All of your functions must be exported


## Practice Exercises

### 0. Const or let?

**File:** [0-constants.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/0-constants.js)<br>
**Description:** Modify<br>

function taskFirst to instantiate variables using const<br>
function taskNext to instantiate variables using let<br>
**Requirement:** <br>
```javascript
export function taskFirst() {
  var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
```
```javascript
bob@dylan:~$ cat 0-main.js
import { taskFirst, taskNext } from './0-constants.js';

console.log(`${taskFirst()} ${taskNext()}`);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
I prefer const when I can. But sometimes let is okay
bob@dylan:~$ 
```

