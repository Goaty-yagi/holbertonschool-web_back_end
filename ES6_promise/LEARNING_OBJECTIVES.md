# Learning Objectives

- [Promises (how, why, and what)](#Promises-(how, why, and what))
- [How to use the then, resolve, catch methods](#How-to-use-the-then,-resolve,-catch-methods)
- [How to use every method of the Promise object](#How-to-use-every-method-of-the-Promise-object)
- [Throw / Try](#Throw-/-Try)
- [The await operator](#The-await-operator)
- [How to use an async function](#How-to-use-an-async-function)


## Promises (how, why, and what)
### 1, Creating a Promise
```javascript
const myPromise = new Promise((resolve, reject) => {
  // Perform asynchronous operation
  if (/* error condition */) {
    reject(new Error('Promise rejected error'));
  } else {
    resolve('Promise resolved data');
  }
});

// Consuming the Promise
myPromise
  .then((data) => {
    console.log('Promise resolved:', data);
  })
  .catch((error) => {
    console.error('Promise rejected:', error);
  });
```

### 2, Consuming a Promise
```javascript
myPromise.then((data) => {
  console.log('Promise resolved:', data);
}).catch((error) => {
  console.error('Promise rejected:', error);
});
```

### 3, Chaining Promises
```javascript
myPromise
  .then((data) => {
    console.log('Step 1:', data);
    return 'Step 2 data';
  })
  .then((data) => {
    console.log('Step 2:', data);
    return new Promise((resolve) => {
      setTimeout(() => resolve('Step 3 data'), 1000);
    });
  })
  .then((data) => {
    console.log('Step 3:', data);
  })
  .catch((error) => {
    console.error('Promise chain error:', error);
  });

```
### 4, Handling Errors
```javascript
myPromise.catch((error) => {
  console.error('Promise rejected:', error);
});

```

### 5, Promise.all() and Promise.race(): The Promise.all()
```javascript
const promises = [promise1, promise2, promise3];
Promise.all(promises)
  .then((results) => {
    console.log('All promises resolved:', results);
  })
  .catch((error) => {
    console.error('One or more promises rejected:', error);
  });

```

## How to use the then, resolve, catch methods
See above
## How to use every method of the Promise object
Seems every method doesn't exist in promise obj.
## Throw / Try
```javascript
function divide(x, y) {
  if (y === 0) {
    throw 'Division by zero error'; // Throwing a string
  }
  return x / y;
}

try {
  console.log(divide(10, 0));
} catch (error) {
  console.error('Error:', error); // Handling the thrown error
}
```
## The await operator
```javascript
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function asyncFunction() {
  console.log('Start');
  
  // Pause execution until the Promise returned by delay() is resolved
  await delay(2000);

  console.log('After 2 seconds');
}

asyncFunction();

```
## How to use an async function

### 1, Defining an async function:
```javascript
async function fetchData() {
  // Asynchronous operations here
  return 'Data fetched';
}
```

### 2, Calling the async function:
```javascript
fetchData()
  .then(data => {
    console.log(data); // Output: Data fetched
  })
  .catch(error => {
    console.error(error);
  });
```

Alternatively, you can also use the await keyword inside another async function to call the async function synchronously:

```javascript
async function getData() {
  try {
    const data = await fetchData();
    console.log(data); // Output: Data fetched
  } catch (error) {
    console.error(error);
  }
}

getData();

```