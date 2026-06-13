# Object-Oriented Programming (OOP) in Python

## Why OOP?

OOP helps organize code by combining data and behavior into objects.

### Benefits

- Reusability
- Maintainability
- Scalability
- Modularity

---

## Everything in Python is an Object

```python
def sum(x, y):
    return x + y

print(type(sum))
```

Functions are objects in Python.

---

## Class and Object

A **class** is a blueprint.

An **object** is an instance of a class.

```python
class Sample:

    # Constructor executes when an object is created
    def __init__(self, name):
        self.name = name

    # Method
    def fun1(self):
        print("Hello")

    def fun_add(self, x):
        return x + 1


# Object creation
s = Sample("Vicks")

print(s.name)

s.fun1()

print(type(s))
```

---

## self Keyword

- `self` refers to the current object instance.
- It allows an object to access its own attributes and methods.
- Python automatically passes `self` when instance methods are called.

Example:

```python
class Person:

    def __init__(self, name):
        self.name = name


p1 = Person("Vignesh")
p2 = Person("Rahul")
```

For `p1`, `self` refers to `p1`.

For `p2`, `self` refers to `p2`.

---

# Class Variables vs Instance Variables

```python
class Student:

    school = "ABC School"  # Class Variable

    def __init__(self, name):
        self.name = name    # Instance Variable


s1 = Student("Tim")
s2 = Student("Bill")
```

### Class Variable

```python
Student.school
```

Shared across all objects.

### Instance Variable

```python
self.name
```

Unique for every object.

---

# Types of Methods

## Instance Method

Uses object state.

```python
class Student:

    def show(self):
        print(self.name)
```

---

## Class Method

Uses class state.

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

Usage:

```python
Student.show_school()
```

---

## Static Method

Independent utility function.

```python
class MathUtils:

    @staticmethod
    def add(x, y):
        return x + y
```

Usage:

```python
MathUtils.add(5, 3)
```

### Quick Summary

```text
Instance Method -> uses self
Class Method    -> uses cls
Static Method   -> uses neither
```

---

# Encapsulation

Encapsulation is controlling access to an object's internal state.

The object controls how its data is accessed and modified.

Instead of allowing outside code to directly modify data, methods provide controlled access.

---

## Without Encapsulation

```python
class BankAccount:

    def __init__(self):
        self.balance = 1000


acc = BankAccount()

acc.balance = -99

print(acc.balance)
```

Output:

```text
-99
```

Anyone can modify the data.

---

## With Encapsulation

```python
class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount()

acc.deposit(500)

print(acc.get_balance())
```

Output:

```text
1500
```

---

## Name Mangling

```python
self.__balance
```

Python internally converts it to:

```python
_BankAccount__balance
```

So this fails:

```python
acc.__balance
```

But this works:

```python
acc._BankAccount__balance
```

---

## Python Does Not Have True Private Variables

Unlike Java or C++, Python uses:

- Naming conventions
- Name mangling

Privacy is based on developer discipline.

Think:

```text
Please don't touch this.
```

instead of

```text
You cannot touch this.
```

---

## Encapsulation != Data Hiding

Encapsulation means:

> Bundling data and methods together and controlling access to an object's internal state.

---

# Abstraction

Abstraction means:

> Showing only the essential features and hiding implementation details.

---

## ABC (Abstract Base Class)

Python provides abstraction through the `abc` module.

```python
from abc import ABC, abstractmethod
```

- `ABC` = Abstract Base Class
- Built-in class from Python's standard library
- Enables abstraction
- Enforces contracts for child classes

---

## Example

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")
```

### What Happens Here?

Vehicle says:

```text
Any class that claims to be a Vehicle
must implement start().
```

Car fulfills that contract.

---

# Using Multiple Classes

```python
class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):

        if len(self.students) < self.max_students:
            self.students.append(student)
            return True

        return False

    def get_average_grade(self):

        value = 0

        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 20, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)

course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())
```

---

# Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

---

## Example

```python
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):

    def speak(self):
        print("Meow")


class Dog(Pet):

    def speak(self):
        print("Bark")


p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34)
c.show()
```

---

# super()

Used to access methods and constructors from the parent class.

---

## Without super()

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

---

## With super()

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

## Calling Parent Methods

```python
class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    def speak(self):
        super().speak()
        print("Bark")
```

Output:

```text
Animal Sound
Bark
```

---

# Overriding

Python supports method overriding.

A child class provides its own implementation of a parent method.

---

## Method Overriding

```python
class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    def speak(self):
        print("Bark")


dog = Dog()

dog.speak()
```

Output:

```text
Bark
```

---

## Constructor Overriding

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

Better version:

```python
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

## Complete Overriding

Child completely replaces parent behavior.

```python
class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    def speak(self):
        print("Bark")
```

---

## Partial Overriding

Child extends parent behavior.

```python
class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    def speak(self):
        super().speak()
        print("Bark")
```

Output:

```text
Animal Sound
Bark
```

---

# Overriding vs Overloading

## Overriding

Parent method is replaced.

```python
class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        pass
```

---

## Overloading

Same method name with different parameters.

Java Example:

```java
add(int a, int b)
add(int a, int b, int c)
```

Python does not support traditional method overloading.

```python
class Test:

    def add(self, x):
        pass

    def add(self, x, y):
        pass
```

The second method replaces the first.

---

# Polymorphism

Polymorphism means:

> Same interface, different behavior.

Different objects respond differently to the same method call.

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

```text
Bark
Meow
```

Same method name.

Different behavior.

---

# Composition

Composition means:

> A class contains objects of another class.

Also known as a:

```text
HAS-A relationship
```

---

## Example 1

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()


car = Car()

car.engine.start()
```

Relationship:

```text
Car HAS-A Engine
```

---

## Example 2

```python
class Book:

    def __init__(self, name):
        self.name = name


class Library:

    def __init__(self):
        self.books = []


library = Library()

library.books.append(Book("Harry Potter"))
library.books.append(Book("LOTR"))
```

Relationship:

```text
Library HAS-A Books
```

---

# Inheritance vs Composition

## Inheritance

```text
IS-A Relationship
```

Examples:

```text
Dog IS-A Animal

Car IS-A Vehicle
```

---

## Composition

```text
HAS-A Relationship
```

Examples:

```text
Car HAS-A Engine

Library HAS-A Books
```

---

# OOP Quick Revision Sheet

```text
Class = Blueprint

Object = Instance of a class

self = Current object

Class Variable = Shared across all objects

Instance Variable = Unique for each object

Instance Method = Uses self

Class Method = Uses cls

Static Method = Uses neither

Inheritance = IS-A relationship

Composition = HAS-A relationship

Encapsulation = Hide/protect data

Abstraction = Hide complexity

Polymorphism = Same interface, different behavior

Overriding = Child replaces parent implementation

super() = Access parent implementation
```