# resource - https://www.freecodecamp.org/news/learn-python-for-javascript-developers-handbook/#heading-1-brief-overview-of-javascript-and-python
print("hello world!");

for i in range(5):
    print(i)


age = 25
name = "John Doe"
print(age, name)

print(0 == "")


my_list = [1, "apple", 3.14, True]

my_tuple = (1, "banana", 2.71, False)

my_set = {1, 2, 3, 4, 5}

my_dict = {
    "name": "Alice", 
    "age": 30,
    "city": "New York"
}

if(age > 18):
    print("You are an adult.")
else:
    print("You are a minor.")

count = 0
while count < 5:
    print(count)
    count += 1
print(count)

my_list = [1, 2, 3, 4, 5]

my_list.append(6);

my_list.insert(0, 10);

my_list.remove(3);
print(my_list)

my_tuple = (1, 2, 3)
# Attempting to modify will raise an error:
# my_tuple[0] = 10  # Raises TypeError

my_set = {1, 2, 3, 4, 5, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5} - duplicates are removed

# Creating and using a set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")           # Adds "orange" to the set
fruits.add("orange")           # Adds "orange" to the set
fruits.discard("banana")       # Removes "banana" from the set
print(fruits)                  # Output: {"apple", "cherry", "orange"}


person = { name: "Alice", age: 30, "city": "New York" }
person["age"] = 31  # Update age
person["country"] = "USA"  # Add new key-value pair
print(person["age"])  
del person["city"]  # Remove key-value pair
print(person)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

import json

person_json = json.dumps(person)
print(person_json)  # Output: {"name": "Alice", "age": 31, "country": "USA"}
person_dict = json.loads(person_json)
print(person_dict)  # Output: {'name': 'Alice', 'age': 31

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

x = "global variable"
def outer_function():
    x = "outer variable"
    def inner_function():
        x = "inner variable"
        print("Inner:", x)
    inner_function()
outer_function() # output: Inner: inner variable
print("Outer:", x)

## Python lambda

square = lambda x: x ** 2
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

def greet(name="World", *args, **kwargs):
    print(f"Hello, {name}!")
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

greet("Alice", 1, 2, 3, key1="value1", key2="value2")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

generic_animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(generic_animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())  # Output: Buddy barks.

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

class Bird:
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

def get_flight_ability(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()
get_flight_ability(sparrow)    # Output: Birds can fly
get_flight_ability(penguin)    # Output: Penguins cannot fly

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.subtract(5, 3))  # Output: 2

import asyncio
import aiohttp

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/1') as response:
            data = await response.json()
            print(data)

asyncio.run(fetch_data())

import aiofiles
import asyncio

async def read_file():
    async with aiofiles.open('example.txt', mode='r') as f:
        contents = await f.read()
        print(contents)
asyncio.run(read_file())

# Concurrency: Both languages handle concurrency well, but JavaScript’s event loop and non-blocking I/O model are better suited for high-throughput, real-time applications.
# Threading: Python’s asyncio works best for I/O-bound tasks. For CPU-bound tasks, Python relies on multi-threading or multi-processing.
# Ease of Use: JavaScript’s async/await is simpler to implement for beginners, while Python requires familiarity with asyncio for similar functionality.
# JavaScript: Asynchronous programming is central to JavaScript’s design. Its event loop and Promises make it highly efficient for real-time, event-driven applications.
# Python: Asynchronous programming is a newer addition to Python, focused on handling I/O-bound tasks efficiently with asyncio.
# Syntax: Both languages use async/await, but Python requires explicit setup with asyncio, while JavaScript integrates it natively.
# To install all dependencies in requirements.txt:
# bashCopy codepip install -r requirements.txt