# Learning Objectives

- [async and await syntax](#async-and-await-syntax)
- [How to execute an async program with asyncio](#How-to-execute-an-async-program-with-asyncio)
- [How to run concurrent coroutines](#How-to-run-concurrent-coroutines)
- [How to create asyncio tasks](#How-to-creat-easyncio-tasks)
- [How to use the random module](#How-to-use-the-random-module)

## async and await syntax
```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```
"... World!" will be printed after 1 sec
 
## How to execute an async program with asyncio
```python
asyncio.run(main())
```
## How to run concurrent coroutines
you can use the asyncio.gather() function. This function allows you to execute multiple coroutines concurrently and wait for all of them to complete. 
```python
import asyncio

async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(1)
    print("Coroutine 1 completed")

async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(2)
    print("Coroutine 2 completed")

async def main():
    # Run coroutines concurrently using asyncio.gather
    await asyncio.gather(coroutine1(), coroutine2())

# Run the main function within the event loop
asyncio.run(main())

```
## How to create asyncio tasks
Asyncio tasks are a way to execute asynchronous functions concurrently within the asyncio event loop. Tasks allow you to schedule and manage the execution of coroutines asynchronously
```python
import asyncio

async def my_coroutine():
    # Your asynchronous code here
    await asyncio.sleep(1)
    print("Coroutine completed")

async def main():
    # Create tasks
    task1 = asyncio.create_task(my_coroutine())
    task2 = asyncio.create_task(my_coroutine())

    # Wait for tasks to complete
    await task1
    await task2

# Run the main function within the event loop
asyncio.run(main())

```
## How to use the random module
```python
import random

# Generate a random floating point number between 0 and 1
print("Random number:", random.random())

# Generate a random integer between 1 and 10
print("Random integer:", random.randint(1, 10))

# Select a random element from a list
my_list = [1, 2, 3, 4, 5]
print("Random choice:", random.choice(my_list))

# Shuffle a list
random.shuffle(my_list)
print("Shuffled list:", my_list)

```