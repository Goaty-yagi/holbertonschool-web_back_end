# Learning Objectives

- [How to define a Class](#How-to-define-a-Class)
- [How to add methods to a class](#How-to-add-methods-to-a-class)
- [Why and how to add a static method to a class](#Why-and-how-to-add-a-static-method-to-a-class)
- [How to extend a class from another](#How-to-extend-a-class-from-another)
- [Metaprogramming and symbols](#Metaprogramming-and-symbols)

## How to define a Class
1, Decrire class with a class declaration.
2, Set constructor method to initialize an object.
```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
  }
}

// Creating an instance of the class
const person1 = new Person('Alice', 30);

// Calling a method on the instance
person1.greet(); // Output: Hello, my name is Alice and I'm 30 years old.

```
## How to add methods to a class
See above example
## Why and how to add a static method to a class
### Why Add a Static Method:

- Utility Functions: Static methods are often used for utility functions that are related to the class but don't operate on individual instances.

- Class-Level Operations: Sometimes, you may need to perform operations at the class level, such as creating new instances based on certain criteria or performing calculations using class properties.

```javascript
class MyClass {
  constructor(value) {
    this.value = value;
  }
  
  // Instance method
  getValue() {
    return this.value;
  }
  
  // Static method
  static double(value) {
    return value * 2;
  }
}

// Usage
const instance = new MyClass(5);

console.log(instance.getValue()); // Outputs: 5

// Calling the static method directly on the class
console.log(MyClass.double(3)); // Outputs: 6

```
## How to extend a class from another
```javascript
// Define a superclass
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound`);
  }
}

// Define a subclass that extends the superclass
class Dog extends Animal {
  constructor(name, breed) {
    // Call the superclass constructor using super()
    super(name);
    this.breed = breed;
  }

  // Add a method specific to the Dog subclass
  bark() {
    console.log(`${this.name} barks`);
  }
}

// Create an instance of the subclass
const dog = new Dog('Buddy', 'Golden Retriever');

// Call methods from both the superclass and the subclass
dog.speak(); // Outputs: Buddy makes a sound
dog.bark();  // Outputs: Buddy barks

```
## Metaprogramming and symbols

### Metaprogramming
Metaprogramming is a programming technique where a program can modify or generate its own code during runtime. It allows developers to write code that can inspect, analyze, and manipulate other parts of the program or even itself.

- 1, Code Generation: Programs can generate code dynamically based on certain conditions or input. This can be useful for generating repetitive code patterns or for customizing behavior based on runtime data.

- 2, Reflection: Reflection allows a program to inspect and manipulate its own structure at runtime. In languages like JavaScript and Python, reflection allows you to inspect object properties, methods, and metadata, and even modify them dynamically.
- 3, Dynamic Code Execution: Metaprogramming enables programs to execute code dynamically, such as evaluating expressions, invoking functions, or instantiating objects based on runtime conditions.
- 4, Macro Systems: Some programming languages provide macro systems that allow developers to define custom compile-time transformations or code generation rules. Macros are often used to extend the language syntax or automate repetitive tasks.
- 5, Template Metaprogramming: In languages like C++ and D, template metaprogramming allows developers to perform computations at compile-time using template parameters and type deduction. This technique is commonly used for optimizing code or implementing complex data structures.
- 6, Aspect-Oriented Programming (AOP): AOP is a programming paradigm that separates cross-cutting concerns, such as logging, authentication, and error handling, from the main application logic. Metaprogramming techniques are often used to weave these aspects into the codebase dynamically.

### Symbols
Symbols are a primitive data type introduced in ES6 (ECMAScript 2015). They are unique and immutable values that can be used as property keys in objects. Unlike strings, symbols are guaranteed to be unique, even if they have the same description.

- 1, Uniqueness: Each symbol value returned by Symbol() or Symbol.for() is unique. Even if you create two symbols with the same description, they are not equal. 
```javascript
const symbol1 = Symbol("foo");
const symbol2 = Symbol("foo");

console.log(symbol1 === symbol2); // false

```

- 2, Description: Symbols can have an optional description, which is useful for debugging but does not affect their uniqueness.

```javascript
const symbol = Symbol("foo");
console.log(symbol.description); // "foo"

```

- 3, Object Property Keys: Symbols can be used as unique property keys in objects. They are ideal for defining non-enumerable properties that should not be accessed accidentally.
```javascript
const obj = {};
const mySymbol = Symbol("mySymbol");

obj[mySymbol] = "Hello";
console.log(obj[mySymbol]); // "Hello"

```

- 4, Well-known Symbols: JavaScript provides several built-in symbols that represent common behaviors or language features. For example, Symbol.iterator is used to define an iterator for custom objects, enabling them to be iterated using for...of loops.
```javascript
const myIterable = {
    [Symbol.iterator]: function* () {
        yield 1;
        yield 2;
        yield 3;
    }
};

for (const value of myIterable) {
    console.log(value); // 1, 2, 3
}
```

5, Global Symbol Registry: Symbols created with Symbol.for() are stored in a global symbol registry, allowing them to be shared across different parts of an application.

```javascript
const symbol1 = Symbol.for("foo");
const symbol2 = Symbol.for("foo");

console.log(symbol1 === symbol2); // true

```

Symbols are often used to define unique keys for object properties, especially in cases where you want to avoid naming collisions with other properties or libraries. They provide a way to create private or internal properties that cannot be accessed or modified unintentionally.