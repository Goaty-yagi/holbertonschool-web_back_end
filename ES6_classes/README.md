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

### 3. Methods, static methods, computed methods names..... MONEY

**File:** [3-currency.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/3-currency.js)<br>
**Description:** Implement a class named Currency:<br>
**Requirement:** <br>
- Constructor attributes:
 -- code (String)
 -- name (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter and setter for each attribute.
- Implement a method named displayFullCurrency that will return the attributes in the following format name (code).


### 4. Pricing

**File:** [4-pricing.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/4-pricing.js)<br>
**Description:** Import the class Currency from 3-currency.js<br>
Implement a class named Pricing:<br>
**Requirement:** <br>
- Constructor attributes:
 -- amount (Number)
 -- currency (Currency)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter and setter for each attribute.
- Implement a method named displayFullPrice that returns the attributes in the following format amount currency_name (currency_code).
- Implement a static method named convertPrice. It should accept two arguments: amount (Number), conversionRate (Number). The function should return the amount multiplied by the conversion rate.


### 5. A Building

**File:** [5-building.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/5-building.js)<br>
**Description:** Implement a class named Building:<br>
**Requirement:** <br>
- Constructor attributes:
 -- sqft (Number)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter for each attribute.
- Consider this class as an abstract class. And make sure that any class that extends from it should implement a method named evacuationWarningMessage.
 -- If a class that extends from it does not have a evacuationWarningMessage method, throw an error with the message Class extending Building must override evacuationWarningMessage


 ### 6. Inheritance

**File:** [6-sky_high.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/6-sky_high.js)<br>
**Description:** Implement a class named SkyHighBuilding that extends from Building:<br>
**Requirement:** <br>
- Constructor attributes:
 -- sqft (Number) (must be assigned to the parent class Building)
floors (Number)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter for each attribute.
- Override the method named evacuationWarningMessage and return the following string Evacuate slowly the NUMBER_OF_FLOORS floors.


### 7. Airport

**File:** [7-airport.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/7-airport.js)<br>
**Description:** Implement a class named Airport:<br>
**Requirement:** <br>
- Constructor attributes:
 -- name (String)
 -- code (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- The default string description of the class should return the airport code (example below).


### 8. Primitive - Holberton Class

**File:** [8-hbtn_class.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/8-hbtn_class.js)<br>
**Description:** Implement a class named HolbertonClass:<br>
**Requirement:** <br>
- Constructor attributes:
 -- size (Number)
 -- location (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- When the class is cast into a Number, it should return the size.
- When the class is cast into a String, it should return the location.



### 9. Hoisting

**File:** [9-hoisting.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/9-hoisting.js)<br>
**Description:** Fix this code and make it work.<br>
**Requirement:** <br>
```javascript
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
  }
}


export const listOfStudents = [student1, student2, student3, student4, student5];
```

Result
```javascript
bob@dylan:~$ cat 9-main.js
import listOfStudents from "./9-hoisting.js";

console.log(listOfStudents);

const listPrinted = listOfStudents.map(
    student => student.fullStudentDescription
);

console.log(listPrinted)

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js
[
  StudentHolberton {
    _firstName: 'Guillaume',
    _lastName: 'Salva',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'John',
    _lastName: 'Doe',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Albert',
    _lastName: 'Clinton',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Donald',
    _lastName: 'Bush',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Jason',
    _lastName: 'Sandler',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  }
]
[
  'Guillaume Salva - 2020 - San Francisco',
  'John Doe - 2020 - San Francisco',
  'Albert Clinton - 2019 - San Francisco',
  'Donald Bush - 2019 - San Francisco',
  'Jason Sandler - 2019 - San Francisco'
]
bob@dylan:~$ 
```

### 10. Vroom

**File:** [10-car.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_classes/10-car.js)<br>
**Description:** Implement a class named Car:<br>
**Requirement:** <br>
- Constructor attributes:
 -- brand (String)
 -- motor (String)
 -- color (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Add a method named cloneCar. This method should return a new object of the class.