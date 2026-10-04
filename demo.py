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


