# Learning Objectives

- [Type annotations in Python 3](#Type-annotations-in-Python-3)
- [How you can use type annotations to specify function signatures and variable types](#How-you-can-use-type-annotations-to-specify-function-signatures-and-variable-types)
- [Duck typing](#Duck-typing)
- [How to validate your code with mypy](#How-to-validate-your-code-with-mypy)

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
pip install mypy
```