### Generator

A **generator** is a special type of iterator in Python that produces values **one at a time**, on demand, instead of storing all values in memory at once.

Generators are created using the  `yield`  keyword inside a function.

### Core Characteristics

1. **Uses `yield` instead of `return`**
2. **Produces values one at a time**
3. **Maintains its state between executions**
4. **Consumes less memory**
5. **Can be iterated using a `for` loop**
6. **Implements the iterator protocol automatically**

Example:

Let's say we have a file having 10 million rows

```python
data = []

for line in file:
	data.append(line)
	
```

This will cost too much of memory as it loads everything into memory. Instead, the approach with generator is like

```python
for line in file:
	yield line
```

Let's consider another example, 

```python
def get_numbers():
	return [1, 2, 3]
	
nums = get_numbers()
print(nums) # this prints the entire numbers [1 2 3]
```

But for a generator, 

```python
def get_numbers():
	yield 1
	yield 2
	yield 3
	
nums = get_numbers()
print(nums) # returns only the generator object (lazy evaluation)
```

How `yield` works:

Normal approach:

```python
def test():
	print("A")
	return 1
	print("B")
```

returns A, and the function dies with it.

But on generator approach:

```python
def test():
	print("A")
	yield 1
	
	print("B")
	yield 2
	
	print("C")
	yield 3

gen = test()
print(next(gen))
```

It will print

```python
A
1
```

if we run it again, we get 

```python
B
2
```

The function didn't start from the beginning and resumed from where it stopped.

### Decorator

A decorator is a higher order function in Python which takes another function as input, extends or modifies its behaviour without changing its source code, and returns a new function.

### Key Characteristics

- Takes a function as an argument.
- Returns a new function.
- Modifies or extends behavior without altering the original function.
- Implemented using the `@decorator_name` syntax.
- Commonly used for logging, authentication, timing, caching, and access control.

#### Syntax:

```python
def decorator(func):
	def wrapper(*args, **kwargs):
		
		# functionality here
		return func(*args , **kwargs):
	
	return wrapper
	
@decorator
def my_function():
	pass
```

`func` here is just a variable name. it could be anything. 

Example:

```python
def logger(abc):
	
	def wrapper():
		print("Before")
		
		abc()
		
		print("After")
	
	return wrapper
```

`*args`  and  `**kwargs` are not required for functions if they are not having any parameters

Example:

```python
def logger(func):
	def wrapper(*args, **kwargs):
		print("Function started")
		
		result = func(*args, **kwargs)
		
		print("Function ended")
		
		return result
	
	return wrapper
	
@logger
def add(a, b):
	return a + b

print(add(3,4))
```

Output:

```
Function started
Function ended
7
```

### Context Managers : `with` statement

A context manager is an object that manages resources by automatically performing setup and cleanup operations before and after a block of code executes.

It is commonly used with the `with` statement

Let's say if we have a case

```python
file = open("data.txt","r")

content = file.read()

file.close()
```

if an exception occurs before `file.close()`, then the file remains open.

#### Solution with Context Managers:

```python
with open("data.txt", "r") as file:
	content = file.read()
```

when the block finishes, `file.close()` is called automatically, even if an exception occurs.

internally, it does this

```python
file = open("data.txt")

try:
	print(file.read())
finally:
	file.close()
```

#### Creating own context manager

```python
class DBConnection:
	
	def __enter__(self):
		print("Connected")
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		print("Disconnected")
		

# then can be used as 
with DBConnection():
	print("Running query")
	
```

#### Important Methods:

A context manager has two special methods
1. `__enter__()` - Runs when entering the block	
2. `__exit__()` - Runs when leaving the block. Runs even if an exception occurs.

#### Understanding the parameters of `__exit__()`

```python
class Test:
	def __enter__(self):
		print("Entering")
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		print("Exception Type:",exc_type)
		print("Exception Value:",exc_value)
		print("Traceback:",traceback)
with Test():
	1/0
```

1. `exc_type` - Contains the class of the exception
2. `exc_value` - Contains the actual exception object
3. `traceback` - Contains the information about where the error happened

### Iterators

An iterator is an object that allows traversal through a collection of data one element at a time and implements the iterator protocol using `__iter__()` and `__next__()` methods.

Example, if a normal collection (list) would be 
```python
name = [10, 20, 30]

for num in nums:
	print(num)
```

Output:

```
10
20
30
```

Internally, Python does something like:

```python

nums = [10, 20, 30]

it = iter(nums)

while True:
	try:
		num = next(it)
		print(num)
	
	except StopIteration:
		break
```

Now, using iterator explicity

```python
nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
```

#### Custom iterator class

```python
class Counter:

	def __init__(self):
		self.num = 1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.num > 5:
			raise StopIteration
			
		current = self.num
		self.num += 1
		
		return current

counter = Counter()

print(next(counter))
print(next(counter))
print(next(counter))
```

Output:

```
1
2
3
```

#### Why `__iter__()` returns `self`

The object itself is acting as an iterator.

### Async Programming

Asynchronous programming is a programming paradigm that allows a program to perform multiple tasks concurrently without blocking execution while waiting for slow operations such as network requests, database queries, or file I/O.

Also associated with: 
* Concurrency
* Non-blocking
* I/O bound tasks

Example:

```python
import time

def task1():
	print("Task 1 started")
	time.sleep()
	print("Task 1 completed")

def task2():
	print("Task 2 started")
	time.sleep()
	print("Task 2 completed")

task1()
task2()
```

Output:

```
Task 1 started
(wait 5s)
Task 1 completed

Task 2 started
(wait 5s)
Task 2 completed
```

Total time taken : `10 seconds`
This is called synchronous execution.

#### Async solution

```python
import asyncio

async def task1():
	print("Task 1 started")
	await asyncio.sleep(5)
	print("Task 1 completed")

async def task2():
	print("Task 2 started")
	await asyncio.sleep(5)
	print("Task 2 completed")
```

`async def` - this creates a coroutine function.
`await` - the keyword which lets other task run while it is waiting. 

#### Async example

```python
import asyncio

async def task1():
	print("Task 1 start")
	await asyncio.sleep(3)
	print("Task 1 End")

async def task2():
	print("Task 2 start")
	await asyncio.sleep(3)
	print("Task 2 End")

async def main():
	await task1()
	await task2()

asyncio.run(main())
```

Output

```
Task 1 start
(wait 3s)
Task 1 End

Task 2 start
(wait 3s)
Task 2 End
```

still ran sequential.

#### Running concurrently using `asyncio.gather()`

```python
import asyncio

async def task1():
	print("task 1 started")
	await asyncio.sleep(3)
	print("task 1 ended")

async def task2():
	print("task 2 started")
	await asyncio.sleep(3)
	print("task 2 ended")

async def main():
	await asyncio.gather(
		task1(),
		task2()
		)
asyncio.run(main())
```

Output would be:

```
task 1 started
task 2 started
(wait 3s)
task 1 ended
task 2 ended
```

#### Core terms to know

1. **Coroutine** - Function defined using `async def`
2. **Event Loop** - The mechanism that schedules and runs asynchronous tasks.
3. `await` - Pauses the current coroutine and allows other tasks to run.
4. `asyncio.gather()` - Runs multiple coroutines concurrently and waits for all to finish.
5. `asyncio.run()` - Starts the event loop and executes the main coroutine.


