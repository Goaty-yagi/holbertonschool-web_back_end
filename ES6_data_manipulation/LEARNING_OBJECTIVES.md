# Learning Objectives

- [How to use map, filter and reduce on arrays](#How-to-use-map,-filter-and-reduce-on-arrays)
- [Typed arrays](#Typedarrays)
- [The Set, Map, and Weak link data structures](#The-Set,-Map,-and-Weak-link-data-structures)

## How to use map, filter and reduce on arrays
### map
```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
// doubled: [2, 4, 6, 8, 10]

```
### filter
```javascript
const numbers = [1, 2, 3, 4, 5];
const evens = numbers.filter(num => num % 2 === 0);
// evens: [2, 4]

```
### reduce
```javascript
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
// sum: 15

```
## Typed arrays
Typed arrays are a special type of array-like object provided by JavaScript to handle binary data in a more efficient manner. Unlike regular arrays, which can hold various types of data, typed arrays are designed to hold a single data type and are optimized for performance.

### ArrayBuffer
It is a buffer to store binary data which is read only.
```javascript
// Create a new ArrayBuffer with a byte length of 8
const buffer = new ArrayBuffer(8);
```

### typed array views
 provide a structured way to access and manipulate binary data stored in an ArrayBuffer. These views allow you to interpret the raw binary data in the ArrayBuffer as arrays of specific data types, such as integers or floating-point numbers.
```javascript
// Create a new ArrayBuffer with a byte length of 4
const buffer = new ArrayBuffer(4);

// Create a Uint8Array view into the buffer
const uint8Array = new Uint8Array(buffer);

// Set values in the Uint8Array
uint8Array[0] = 10;
uint8Array[1] = 20;
uint8Array[2] = 30;
uint8Array[3] = 40;

// Access values in the Uint8Array
console.log(uint8Array); // Uint8Array [ 10, 20, 30, 40 ]

// Another way with DataView
const view = new DataView(buffer);
  view.setInt8(position, value);
```
## The Set, Map, and Weak link data structures
The Set, Map, and WeakMap are data structures introduced in ES6 (ECMAScript 2015) to efficiently manage collections of unique values or key-value pairs

### Set
- A Set is a collection of unique values where each value may occur only once.
- It can store any type of value, including primitives or object references.
- Values in a Set are stored in insertion order, and duplicates are automatically eliminated.
- Useful for scenarios where you need to store a collection of unique items or quickly check for existence of an item.

```javascript
const mySet = new Set();
mySet.add(1);
mySet.add(2);
mySet.add(3);
mySet.add(1); // Duplicates are automatically eliminated
console.log(mySet); // Set { 1, 2, 3 }

```

### Map

- A Map is a collection of key-value pairs where each key may occur only once.
- It allows you to associate values with keys and efficiently retrieve them later.
- Both keys and values can be of any type, including objects.
- Unlike objects, keys in a Map can be any value, including objects, functions, and primitive values.

```javascript
const myMap = new Map();
myMap.set('name', 'John');
myMap.set('age', 30);
console.log(myMap.get('name')); // John
console.log(myMap.get('age')); // 30
```

### WeakMap

- A WeakMap is similar to a Map, but with some key differences:
- Keys must be objects (primitive values are not allowed).
- Values are weakly referenced, meaning they do not prevent garbage collection of the object they reference.
- Useful for scenarios where you need to associate additional data with objects without preventing them from being garbage collected.
```javascript
const weakMap = new WeakMap();
const obj = {};
weakMap.set(obj, 'value');
console.log(weakMap.get(obj)); // value

```


## Primitive values
Primitive values in JavaScript are data types that are immutable (cannot be changed) and are not objects. In JavaScript, there are six primitive data types:

- String: Represents textual data, enclosed within single ('') or double ("") quotes.
Example: "Hello, world"

- Number: Represents numeric data, including integers, floating-point numbers, and special numeric values such as NaN (Not a Number) and Infinity.
Example: 42, 3.14

- Boolean: Represents a logical value of either true or false.
Example: true, false

- Undefined: Represents an uninitialized or undefined value.
Example: undefined

- Null: Represents the absence of any value or a null reference.
Example: null

- Symbol: Represents a unique and immutable value that may be used as the key of an Object property.
Example: Symbol("description")

