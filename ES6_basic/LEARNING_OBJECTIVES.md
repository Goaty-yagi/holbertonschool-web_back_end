# Learning Objectives

- [What ES6 is](#What-ES6-is)
- [New features introduced in ES6](#New-features-introduced-in-ES6)
- [The difference between a constant and a variable](#The-difference-between-a-constant-and-a-variable)
- [Block-scoped variables](#Block-scoped-variables)
- [Arrow functions and function parameters default to them](#Arrow-functions-and-function-parameters-default-to-them)
- [Rest and spread function parameters](#Rest-and-spread-function-parameters)
- [String templating in ES6](#String-templating-in-ES6)
- [Object creation and their properties in ES6](#Object-creation-and-their-properties-in-ES6)
- [Iterators and for-of loops](#Iterators-and-for-of-loops)

## Advanced
- [What is NodeJS](#What-is-NodeJS)
- [What is ESLint](#What-is-ESLint)
- [What is Babel](#What-is-Babel)

## What ES6 is
ES6 is ECMA Script 2015 is known as ES6
## New features introduced in ES6
### 1, Arrow Functions:
```javascript
// ES5
var double = function(x) {
    return x * 2;
};

// ES6
const double = x => x * 2;

```
### 2, Block-Scoped Variables:
```javascript
// ES5
var x = 10;
if (true) {
    var x = 20;
}
console.log(x); // 20

// ES6
let y = 10;
if (true) {
    let y = 20;
}
console.log(y); // 10

```
### 3, Template Literals
```javascript
// ES6
const name = 'John';
const greeting = `Hello, ${name}!`;
const multiline = `This is a
multiline string`;
```

### 4, Destructuring Assignment
```javascript
// ES6
const person = { name: 'John', age: 30 };
const { name, age } = person;

```
### 5, Default Parameters
```javascript
// ES6
function greet(name = 'World') {
    console.log(`Hello, ${name}!`);
}

```

### 6, Rest Parameters and Spread Syntax
```javascript
// ES6
function sum(...numbers) {
    return numbers.reduce((acc, val) => acc + val, 0);
}

const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6


```
### 7, Classes
```javascript
// ES6
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    area() {
        return this.width * this.height;
    }
}
const rect1 = new Rectangle(5, 10);
console.log(rect1.area()); // Output: 50

// without new, this in the class refer to global scope
const rect2 = Rectangle(5, 10);
console.log(rect2); // Output: undefined

```
### Modules
```javascript
// ES6 (module.js)
export function square(x) {
    return x * x;
}

// ES6 (main.js)
import { square } from './module';


```

## The difference between a constant and a variable
Constant is immutable variable, a variable is a variable
## Block-scoped variables
Block-scoped variables are variables that are scoped to the nearest enclosing block. In JavaScript, let and const declarations introduce block-scoped variables. This means that variables declared with let or const are only accessible within the block (curly braces {}) where they are defined, including nested blocks.
```javascript
function example() {
  if (true) {
    let x = 10; // block-scoped variable
    console.log(x); // 10
  }
  console.log(x); // ReferenceError: x is not defined
}

```
## Arrow functions and function parameters default to them
See above example
## Rest and spread function parameters
See above example
## String templating in ES6
See above example
## Object creation and their properties in ES6
See above example of class
## Iterators and for-of loops
Iterators and the for...of loop are features introduced in ES6 (ECMAScript 2015) to work with iterables in JavaScript.

### Iterators:
An iterator is an object that provides a sequence of values, typically used within a loop. It has a next() method that returns an object with two properties: value, which is the next value in the sequence, and done, which is a boolean indicating whether the iterator is finished.
```javascript
const iterable = [1, 2, 3];
const iterator = iterable[Symbol.iterator]();
console.log(iterator.next()); // Output: { value: 1, done: false }
console.log(iterator.next()); // Output: { value: 2, done: false }
console.log(iterator.next()); // Output: { value: 3, done: false }
console.log(iterator.next()); // Output: { value: undefined, done: true }

```

### for...of loop:
The for...of loop is used to iterate over iterable objects (arrays, strings, maps, sets, etc.) It simplifies the process of iterating over values compared to traditional for or forEach loops.
```javascript
const iterable = [1, 2, 3];
for (const value of iterable) {
  console.log(value);
}
// Output:
// 1
// 2
// 3

```

## What is NodeJS
Node.js is a runtime environment that allows you to run JavaScript code on the server side. It is built on the V8 JavaScript engine, which is the same engine that powers the Google Chrome browser. Node.js enables developers to write server-side code using JavaScript, which was traditionally used only for client-side scripting in web browsers.

1, Asynchronous and event-driven: Node.js uses non-blocking, asynchronous I/O operations, which makes it efficient and suitable for handling a large number of concurrent connections.

2, Single-threaded, non-blocking architecture: Node.js employs an event loop mechanism that allows it to handle multiple requests concurrently without creating additional threads for each request. This makes Node.js lightweight and scalable.

3, Package ecosystem: Node.js has a rich ecosystem of third-party packages available through npm (Node Package Manager), which allows developers to easily install and use libraries, frameworks, and tools for building web applications.

4, Cross-platform: Node.js is cross-platform and runs on various operating systems, including Windows, macOS, and Linux.

5, JavaScript everywhere: With Node.js, developers can use JavaScript for both server-side and client-side development, enabling full-stack JavaScript development.


## What is ESLint
ESLint is a static code analysis tool for identifying problematic patterns found in JavaScript code. It analyzes your code to detect errors, enforce coding standards, and ensure consistency across your codebase. ESLint can catch syntax errors, detect potential bugs, enforce code style guidelines, and provide suggestions for improvement.

You can configure ESLint to customize the rules it applies to your code, including which rules to enable, disable, or override. ESLint also supports plugins and custom rules, allowing you to extend its functionality to suit your specific needs.

By integrating ESLint into your development workflow, you can maintain code quality, improve readability, and reduce the likelihood of introducing bugs or issues as your project grows.

## What is Babel
Babel is a popular JavaScript compiler that allows developers to write code using the latest ECMAScript (JavaScript) syntax, even if it's not yet supported by all browsers. It transforms (or transpiles) modern JavaScript code into a backward-compatible version that can be run in older browsers or environments that do not support the latest features.

1, Support for Latest JavaScript Features: Babel enables developers to use the newest JavaScript syntax, including features from ES6 (ECMAScript 2015) and beyond, such as arrow functions, template literals, destructuring, async/await, and more.

2, Plugin Architecture: Babel's modular plugin system allows developers to customize the compilation process and add support for specific features or transformations. There are plugins available for various use cases, such as syntax transformations, polyfills, and optimizations.

3, Presets: Babel presets are pre-configured sets of plugins that target specific environments or use cases. For example, the @babel/preset-env preset automatically determines the transformations needed based on the specified target environments, allowing developers to write code without worrying about browser compatibility.

4, Integration with Build Tools: Babel integrates seamlessly with build tools like webpack, Rollup, and npm scripts, allowing developers to incorporate it into their development workflow. It can be used to compile JavaScript files during the build process, enabling the use of modern syntax while ensuring compatibility with target environments.

5, Support for JSX: Babel also supports JSX, a syntax extension used primarily with React for writing HTML-like code within JavaScript files. It can transpile JSX syntax into regular JavaScript function calls, making it compatible with browsers.