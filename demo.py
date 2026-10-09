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

#  Python Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
else:
    print("Division successful:", result)
finally:
    print("Execution completed.")

# Debugging in Python:
import logging

logging.basicConfig(level=logging.ERROR)
logging.error("An error occurred.")

import pdb; pdb.set_trace()

import pytest

def add(a,b):
    return a+b

def test_add_positive_numbers():
    assert add(2,3) == 5

def test_add_negative_numbers():
    assert(-2,-3) == -5

# In Python, coverage.py is the standard tool for measuring test coverage.

# Example: Generating Coverage Reports with Pytest and Coverage.py

# pip install pytest coverage
# coverage run -m pytest
# coverage report

# name: Python CI

# on: [push]

# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#     - uses: actions/checkout@v2
#     - uses: actions/setup-python@v2
#       with:
#         python-version: '3.9'
#     - run: pip install -r requirements.txt
#     - run: pytest --cov=.

# Example: Selenium Test

from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://example.com/login")
    driver.find_element_by_id("username").send_keys("user")
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_css_selector("button[type='submit']").click()
    assert "dashboard" in driver.current_url
    driver.quit()

# Web Scraper in Python
# Python’s libraries, such as BeautifulSoup and Requests, make web scraping straightforward and efficient.

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response =requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract specific data
titles = soup.find_all("h2")
for title in titles:
    print(title.text)

# Creating a REST API
# Python: Flask
# Python’s Flask framework is lightweight and ideal for quickly building APIs.

# Example: REST API in Python

from Flask import Flask, jsonify

app = Flask(__name__)
@app.route('api/data', methods=["GET"])
def get_data():
    return jsonify({"message": "hello world"})
if __name__ == '__main__':
    app.run(debug=True)

# Automation Scripts: File Handling, Network Requests, and Scripting
# Python: Automation with os and shutil
# Python excels at automation tasks, making file and system operations straightforward.

# Example: File Automation in Python

import os
import shutil

# Create a directory
os.makedirs("example_dir", exist_ok=True)

# Move a file
shutil.move("source.txt", "example_dir/destination.txt")

# List files in a directory
for file in os.listdir("example_dir"):
    print(file)

# Data Processing and Visualization
# Python: Data Science with Pandas and Matplotlib
# Python dominates data processing and visualization with libraries like Pandas and Matplotlib.

# Example: Data Analysis in Python

import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 18]}
df = pd.DataFrame(data)

# Plot the data
df.plot(x='Name', y='Age', kind='bar')
plt.show()

# Machine Learning and AI
# Python: TensorFlow
# Python’s TensorFlow library simplifies building machine learning models.

# Example: Machine Learning in Python

import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(optimizer='sgd', loss='mean_squared_error')
# Train the model
xs = [1, 2, 3, 4]
ys = [2, 4, 6, 8]
model.fit(xs, ys, epochs=500, verbose=0)

# Predict
print(model.predict([5]))  # Output: [[10]]

# Open Source Libraries: NPM vs. PyPI
# Both Python and JavaScript have centralized repositories for distributing and installing open-source libraries: PyPI (Python Package Index) for Python and NPM (Node Package Manager) for JavaScript.

# Python: PyPI

# PyPI hosts over 400,000 packages, supporting fields like data science, web development, machine learning, and automation.

# Popular libraries include:

# Pandas for data manipulation.

# NumPy for numerical computing.

# Django and Flask for web development.

# BeautifulSoup and Scrapy for web scraping.

# Example: Installing and Using a PyPI Library

# pip install requests
import requests

response = requests.get("https://api.example.com/data")
print(response.json())

# Popular Python Libraries for Data Science:

# Pandas: Data manipulation and analysis.

# NumPy: Numerical computing and arrays.

# Matplotlib/Seaborn: Data visualization.

# Scikit-learn: Machine learning algorithms.

# TensorFlow/Keras: Deep learning frameworks.