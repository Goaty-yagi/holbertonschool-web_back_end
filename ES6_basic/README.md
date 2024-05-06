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

### 1. Block Scope

**File:** [1-block-scoped.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/1-block-scoped.js)<br>
**Description:** Given what you’ve read about var and hoisting, modify the variables inside the function taskBlock so that the variables aren’t overwritten inside the conditional block.<br>
**Requirement:** <br>

```javascript
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task, task2];
}
```

```bash
bob@dylan:~$ cat 1-main.js
import taskBlock from './1-block-scoped.js';

console.log(taskBlock(true));
console.log(taskBlock(false));
bob@dylan:~$
bob@dylan:~$ npm run dev 1-main.js
[ false, true ]
[ false, true ]
bob@dylan:~$
```

### 2. Arrow functions

**File:** [2-arrow.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/2-arrow.js)<br>
**Description:** Rewrite the following standard function to use ES6’s arrow syntax of the function add (it will be an anonymous function after)<br>
**Requirement:** <br>

```javascript
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = function add(newNeighborhood) {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
```

```bash
bob@dylan:~$ cat 2-main.js
import getNeighborhoodsList from './2-arrow.js';

const neighborhoodsList = new getNeighborhoodsList();
const res = neighborhoodsList.addNeighborhood('Noe Valley');
console.log(res);
bob@dylan:~$
bob@dylan:~$ npm run dev 2-main.js
[ 'SOMA', 'Union Square', 'Noe Valley' ]
bob@dylan:~$
```

### 3. Parameter defaults

**File:** [3-default-parameter.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/3-default-parameter.js)<br>
**Description:** Condense the internals of the following function to 1 line - without changing the name of each function/variable.

Hint: The key here to define default parameter values for the function parameters.<br>
**Requirement:** <br>

```javascript
export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
  if (expansion1989 === undefined) {
    expansion1989 = 89;
  }

  if (expansion2019 === undefined) {
    expansion2019 = 19;
  }
  return initialNumber + expansion1989 + expansion2019;
}
```

```bash
bob@dylan:~$ cat 3-main.js
import getSumOfHoods from './3-default-parameter.js';

console.log(getSumOfHoods(34));
console.log(getSumOfHoods(34, 3));
console.log(getSumOfHoods(34, 3, 4));
bob@dylan:~$
bob@dylan:~$ npm run dev 3-main.js
142
56
41
bob@dylan:~$
```

### 4. Rest parameter syntax for functions

**File:** [4-rest-parameter.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/4-rest-parameter.js)<br>
**Description:** Modify the following function to return the number of arguments passed to it using the rest parameter syntax<br>
**Requirement:** <br>

```javascript
export default function returnHowManyArguments() {}
```

```javascript
> returnHowManyArguments("Hello", "Holberton", 2020);
3
>
```

```bash
bob@dylan:~$ cat 4-main.js
import returnHowManyArguments from './4-rest-parameter.js';

console.log(returnHowManyArguments("one"));
console.log(returnHowManyArguments("one", "two", 3, "4th"));
bob@dylan:~$
bob@dylan:~$ npm run dev 4-main.js
1
4
bob@dylan:~$
```

### 5. The wonders of spread syntax

**File:** [5-spread-operator.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/5-spread-operator.js)<br>
**Description:** Rewrite the return statement to use a template literal so you can the substitute the variables you’ve defined.<br>
**Requirement:** <br>

```javascript
export default function concatArrays(array1, array2, string) {}
```

```bash
bob@dylan:~$ cat 5-main.js
import concatArrays from './5-spread-operator.js';

console.log(concatArrays(['a', 'b'], ['c', 'd'], 'Hello'));

bob@dylan:~$
bob@dylan:~$ npm run dev 5-main.js
[
  'a', 'b', 'c',
  'd', 'H', 'e',
  'l', 'l', 'o'
]
bob@dylan:~$
```

### 6. Take advantage of template literals

**File:** [6-string-interpolation.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/6-string-interpolation.js)<br
**Description:** Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. Your function body should be one line long.<br>
**Requirement:** <br>

```javascript
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return 'As of ' + year + ', it was the seventh-highest income county in the United States'
        / ', with a per capita personal income of ' + budget.income + '. As of 2015, San Francisco'
        / ' proper had a GDP of ' + budget.gdp + ', and a GDP per capita of ' + budget.capita + '.';
}
```

```bash
bob@dylan:~$ cat 6-main.js
import getSanFranciscoDescription from './6-string-interpolation.js';

console.log(getSanFranciscoDescription());

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js 
As of 2017, it was the seventh-highest income county in the United States, with a per capita personal income of $119,868. As of 2015, San Francisco proper had a GDP of $154.2 billion, and a GDP per capita of $178,479.
bob@dylan:~$
```


### 7. Object property value shorthand syntax

**File:** [7-getBudgetObject.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/7-getBudgetObject.js)<br
**Description:** Notice how the keys and the variable names are the same?
Modify the following function’s budget object to simply use the object property value shorthand syntax instead.<br>
**Requirement:** <br>

```javascript
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return 'As of ' + year + ', it was the seventh-highest income county in the United States'
        / ', with a per capita personal income of ' + budget.income + '. As of 2015, San Francisco'
        / ' proper had a GDP of ' + budget.gdp + ', and a GDP per capita of ' + budget.capita + '.';
}
```

```bash
bob@dylan:~$ cat 6-main.js
import getSanFranciscoDescription from './6-string-interpolation.js';

console.log(getSanFranciscoDescription());

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js 
As of 2017, it was the seventh-highest income county in the United States, with a per capita personal income of $119,868. As of 2015, San Francisco proper had a GDP of $154.2 billion, and a GDP per capita of $178,479.
bob@dylan:~$
```

### 8. No need to create empty objects before adding in properties

**File:** [8-getBudgetCurrentYear.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/8-getBudgetCurrentYear.js)<br
**Description:** Rewrite the getBudgetForCurrentYear function to use ES6 computed property names on the budget object.<br>
**Requirement:** <br>

```javascript
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  budget[`income-${getCurrentYear()}`] = income;
  budget[`gdp-${getCurrentYear()}`] = gdp;
  budget[`capita-${getCurrentYear()}`] = capita;

  return budget;
}
```

```bash
bob@dylan:~$ cat 8-main.js
import getBudgetForCurrentYear from './8-getBudgetCurrentYear.js';

console.log(getBudgetForCurrentYear(2100, 5200, 1090));

bob@dylan:~$
bob@dylan:~$ npm run dev 8-main.js 
{ 'income-2021': 2100, 'gdp-2021': 5200, 'capita-2021': 1090 }
bob@dylan:~$
```


### 9. ES6 method properties

**File:** [9-getFullBudget.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/9-getFullBudget.js)<br
**Description:** Rewrite getFullBudgetObject to use ES6 method properties in the fullBudget object.<br>
**Requirement:** <br>

```javascript
import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars: function (income) {
      return `$${income}`;
    },
    getIncomeInEuros: function (income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
```

```bash
bob@dylan:~$ cat 9-main.js
import getFullBudgetObject from './9-getFullBudget.js';

const fullBudget = getFullBudgetObject(20, 50, 10);

console.log(fullBudget.getIncomeInDollars(fullBudget.income));
console.log(fullBudget.getIncomeInEuros(fullBudget.income));

bob@dylan:~$
bob@dylan:~$ npm run dev 9-main.js 
$20
20 euros
bob@dylan:~$
```


### 10. For...of Loops

**File:** [10-loops.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/10-loops.js)<br
**Description:** Rewrite the function appendToEachArrayValue to use ES6’s for...of operator. And don’t forget that var is not ES6-friendly.<br>
**Requirement:** <br>

```javascript
export default function appendToEachArrayValue(array, appendString) {
  for (var idx in array) {
    var value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
```

```bash
bob@dylan:~$ cat 10-main.js
import appendToEachArrayValue from './10-loops.js';

console.log(appendToEachArrayValue(['appended', 'fixed', 'displayed'], 'correctly-'));

bob@dylan:~$
bob@dylan:~$ npm run dev 10-main.js 
[ 'correctly-appended', 'correctly-fixed', 'correctly-displayed' ]
bob@dylan:~$
```

### 11. Iterator

**File:** [11-createEmployeesObject.js](https://github.com/Goaty-yagi/holbertonschool-web_back_end/blob/main/ES6_basic/11-createEmployeesObject.js)<br
**Description:** Write a function named createEmployeesObject that will receive two arguments:
- departmentName (String)
- employees (Array of Strings)<br>
```javascript
export default function createEmployeesObject(departmentName, employees) {

}
```
**Requirement:** <br>

```javascript
{
     $departmentName: [
          $employees,
     ],
}
```

```bash
bob@dylan:~$ cat 11-main.js
import createEmployeesObject from './11-createEmployeesObject.js';

console.log(createEmployeesObject("Software", [ "Bob", "Sylvie" ]));

bob@dylan:~$
bob@dylan:~$ npm run dev 11-main.js 
{ Software: [ 'Bob', 'Sylvie' ] }
bob@dylan:~$
```
