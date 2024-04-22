# Learning Objectives

- [Type annotations in Python 3](#Type-annotations-in-Python-3)
- [How you can use type annotations to specify function signatures and variable types](#How-you-can-use-type-annotations-to-specify-function-signatures-and-variable-types)
- [Duck typing](#Duck-typing)
- [How to validate your code with mypy](#How-to-validate-your-code-with-mypy)]
- [What is TypeVar](#What-is-TypeVar)

## Type annotations in Python 3
a way to specify the types of variables, function parameters, and return values in your code. 
EX)
## How you can use type annotations to specify function signatures and variable types
```python
name: str = "John"
age: int = 30

def greet(name: str) -> str:
    return f"Hello, {name}"

```
## Duck typing
emphasizes the behavior of objects over their specific types. The phrase "duck typing" comes from the saying, "If it looks like a duck and quacks like a duck, it must be a duck." In other words, duck typing focuses on what an object can do (its behavior or interface) rather than what it is (its specific type or class).


## How to validate your code with mypy

- Install mypy
```bash
pip3 install mypy
```

- Run the following command
```bash
mypy filename

```

## What is TypeVar
TypeVar is a generic type variable in Python's typing module that is used to declare type variables. It allows you to define a placeholder for a type that will be specified later.
It is particularly useful for creating generic functions and classes that can work with different types. It allows you to write more flexible and reusable code.
```python
from typing import TypeVar, List

# Define a type variable T
T = TypeVar('T')

# Function that returns the first element of a list
def first_element(lst: List[T]) -> T:
    return lst[0]

# Example usage
int_list = [1, 2, 3, 4, 5]
first_int = first_element(int_list)  # Inferred type: int

str_list = ['a', 'b', 'c']
first_str = first_element(str_list)  # Inferred type: str

```