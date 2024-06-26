# ES6_data_manipulation
ES6_data_manipulation is a comprehensive repository focused on understanding and leveraging the power of classes introduced in ECMAScript 2015 (ES6). 

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Your code will be tested using Jest and the command npm run test
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test
- All of your functions must be exported

## Practice Exercises

### 0. Basic list of objects

**File:** [0-get_list_students.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/0-get_list_students.js)<br>
**Description:** Create a function named getListStudents that returns an array of objects.<br>
**Requirement:** <br>
- Each object should have three attributes: id (Number), firstName (String), and location (String).

- The array contains the following students in order:
 -- Guillaume, id: 1, in San Francisco
 -- James, id: 2, in Columbia
 -- Serena, id: 5, in San Francisco


 ### 1. More mapping

**File:** [1-get_list_student_ids.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/1-get_list_student_ids.js)<br>
**Description:** Create a function getListStudentIds that returns an array of ids from a list of object.<br>
**Requirement:** <br>
- This function is taking one argument which is an array of objects - and this array is the same format as getListStudents from the previous task.
- 
- If the argument is not an array, the function is returning an empty array.
- 
- You must use the map function on the array.

### 2. Filter

**File:** [2-get_students_by_loc.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/2-get_students_by_loc.js)<br>
**Description:** Create a function getStudentsByLocation that returns an array of objects who are located in a specific city.<br>
**Requirement:** <br>
- It should accept a list of students (from getListStudents) and a city (string) as parameters.

- You must use the filter function on the array.

### 3. Reduce

**File:** [3-get_ids_sum.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/3-get_ids_sum.js)<br>
**Description:** Create a function getStudentIdsSum that returns the sum of all the student ids.<br>
**Requirement:** <br>
- It should accept a list of students (from getListStudents) as a parameter.

- You must use the reduce function on the array.


### 4. Combine

**File:** [4-update_grade_by_city.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/4-update_grade_by_city.js)<br>
**Description:** Create a function updateStudentGradeByCity that returns an array of students for a specific city with their new grade.<br>
**Requirement:** <br>
- It should accept a list of students (from getListStudents), a city (String), and newGrades (Array of “grade” objects) as parameters.

- newGrades is an array of objects with this format:
```javascript
{
    studentId: 31,
    grade: 78,
}
```
- If a student doesn’t have grade in newGrades, the final grade should be N/A.

- You must use filter and map combined.


### 5. Typed Arrays

**File:** [5-typed_arrays.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/5-typed_arrays.js)<br>
**Description:** Create a function named createInt8TypedArray that returns a new ArrayBuffer with an Int8 value at a specific position.<br>
**Requirement:** <br>
- It should accept three arguments: length (Number), position (Number), and value (Number).
- If adding the value is not possible the error Position outside range should be thrown.


### 6. Set data structure

**File:** [6-set.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/6-set.js)<br>
**Description:** Create a function named setFromArray that returns a Set from an array.<br>
**Requirement:** <br>
- It accepts an argument (Array, of any kind of element).


### 7. More set data structure

**File:** [7-has_array_values.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/7-has_array_values.js)<br>
**Description:** Create a function named hasValuesFromArray that returns a boolean if all the elements in the array exist within the set.<br>
**Requirement:** <br>
- It accepts two arguments: a set (Set) and an array (Array).


### 8. Clean set

**File:** [8-clean_set.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/8-clean_set.js)<br>
**Description:** Create a function named cleanSet that returns a string of all the set values that start with a specific string (startString).<br>
**Requirement:** <br>
- It accepts two arguments: a set (Set) and a startString (String).
- When a value starts with startString you only append the rest of the string. The string contains all the values of the set separated by -.


### 9. Map data structure

**File:** [9-groceries_list.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/9-groceries_list.js)<br>
**Description:** Create a function named groceriesList that returns a map of groceries with the following items (name, quantity):<br>
```bash
Apples, 10
Tomatoes, 10
Pasta, 1
Rice, 1
Banana, 5
```
**Requirement:** <br>
- Result
```bash
bob@dylan:~$ cat 9-main.js
import groceriesList from "./9-groceries_list.js";

console.log(groceriesList());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js 
Map {
  'Apples' => 10,
  'Tomatoes' => 10,
  'Pasta' => 1,
  'Rice' => 1,
  'Banana' => 5
}
bob@dylan:~$ 
```


### 10. More map data structure

**File:** [10-update_uniq_items.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/10-update_uniq_items.js)<br>
**Description:** Create a function named updateUniqueItems that returns an updated map for all items with initial quantity at 1.<br>

**Requirement:** <br>
- It should accept a map as an argument. The map it accepts for argument is similar to the map you create in the previous task.

- For each entry of the map where the quantity is 1, update the quantity to 100. If updating the quantity is not possible (argument is not a map) the error Cannot process should be thrown.