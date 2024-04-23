# Learning Objectives

- [How to write an asynchronous generator](#How-to-write-an-asynchronous-generator)
- [How to use async comprehensions](#How-to-use-async-comprehensions)
- [How to type-annotate generators](#How-to-type-annotate-generators)




## How to write an asynchronous generator
To write an asynchronous generator in Python, you can use the async and yield keywords together.
```python
import asyncio

async def async_generator():
    for i in range(5):
        # Simulate some asynchronous work
        await asyncio.sleep(1)
        yield i

# Example usage
async def main():
    async for item in async_generator():
        print(item)

# Run the main function within the asyncio event loop
asyncio.run(main())

```
## How to use async comprehensions
`result = [i async for i in aiter() if i % 2]`
## How to type-annotate generators
To type-annotate generators in Python, you can use the Generator type from the typing module. 
`Generator[YieldType, ArgType, ReturnType]`

- YieldType: Specifies the type of values yielded by the generator.
- ArgType: Specifies the type of the argument passed to the send() method of the generator, if any. If the generator does not use send(), this is specified as None.
- ReturnType: Specifies the type of the value returned by the generator when it terminates. If the generator does not return a value (i.e., it continues indefinitely), this is specified as None.

`AsyncGenerator[YieldType, ReturnType]`


## How to make generator functions
define a function using the def keyword as usual, but instead of using return to return a value, you use the yield keyword to yield values one at a time.