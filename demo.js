// resource - https://www.freecodecamp.org/news/learn-python-for-javascript-developers-handbook/#heading-1-brief-overview-of-javascript-and-python
console.log("hello world!");

for (let i = 0; i < 5; i++) {
    console.log(i);
}

let age = 25;
const name = "John Doe";
console.log(age, name);

console.log(0 == "");
console.log(0 === "");

let myArray = [1, "apple", true, null];

const myArray2 = [1, "apple", true, null];

let mySet = new Set([1, 2, 3, 4, 5]);

let myObject = {
    name: "John Doe",
    age: 30,
    city: "New York"
};

if(age > 18) {
    console.log("You are an adult.");
}
else {
    console.log("You are a minor.");
}

count = 0;
while(count < 5) {
    console.log(count);
    count++;
}
console.log("Count is now: " + count);

let myArr = [1, 2, 3, 4, 5];
myArr.push(6);
myArr.unshift(0);
myArr.splice(1, 0, 10);
myArr.splice(2, 1);
myArr.splice(myArr.indexOf(2), 1); // Removes the first occurrence of 2
console.log(myArr);

// Creating and using a set
let fruits = new Set(["apple", "banana", "cherry"]);
fruits.add("orange");           // Adds "orange" to the set
fruits.delete("banana");        // Removes "banana" from the set
console.log(fruits);            // Output: Set { "apple", "cherry", "orange" }

let person = { name: "Alice", age: 30, city: "New York" };
person.age = 31;
console.log(person.age);  // Output: 31
person.country = "USA";
delete person.city;
console.log(person);  // Output: { name: "Alice", age: 31, city: "New York", country: "USA" }

let personJson = JSON.stringify(person);
console.log(personJson);  // Output: '{"name":"Alice","age":31,"country":"USA"}'
let personObj = JSON.parse(personJson);
console.log(personObj);  // Output: { name: "Alice", age: 31, country: "USA" }

function greet(name) {
    return `Hello, ${name}!`;
}
console.log(greet("Alice"));  // Output: Hello, Alice!

function outerFunction() {
    let x = "enclosing";

    function innerFunction() {
        let x = "local";
        console.log(x);
    }

    innerFunction();
}

outerFunction(); // Output: local

const square = (x) => x * x;
console.log(square(5)); // Output: 25

const numbers = [1, 2, 3, 4, 5];
const squaredNumbers = numbers.map(num => num * num);
console.log(squaredNumbers); // Output: [1, 4, 9, 16, 25]

function greet(name = "World", ...args) {
    console.log(`Hello, ${name}!`);
    console.log("Arguments:", args);
}

greet("Alice", 1, 2, { color: "blue", age: 30 });

class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}

const genericAnimal = new Animal("Generic Animal");
const dog = new Dog("Rex");

genericAnimal.speak(); // Output: Generic Animal makes a sound.
dog.speak();           // Output: Rex barks.

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

const person1 = new Person("Alice", 30);
person1.greet(); // Output: Hello, my name is Alice and I am 30 years old.

class Bird {
    fly() {
        return "Birds can fly.";
    }
}

class Penguin extends Bird {
    fly() {
        return "Penguins cannot fly.";
    }   
}

function getFlightAbility(bird) {
    return bird.fly();
}

const sparrow = new Bird();
const penguin = new Penguin();

console.log(getFlightAbility(sparrow)); // Output: Birds can fly.
console.log(getFlightAbility(penguin)); // Output: Penguins cannot fly.

// javascript prototype


function Calculator() {}

Calculator.prototype.add = function(a, b) {
    return a + b;
}

Calculator.prototype.subtract = function(a, b) {
    return a - b;
}

const calc = new Calculator();
console.log(calc.add(5, 3)); // Output: 8
console.log(calc.subtract(5, 3)); // Output: 2

// same implementation using class
class CalculatorClass {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }
}

const calcClass = new CalculatorClass();
console.log(calcClass.add(5, 3)); // Output: 8
console.log(calcClass.subtract(5, 3)); // Output: 2

fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });

async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

fetchData();

const socket = new WebSocket('ws://example.com/socket');
socket.onmessage = function(event) {
    console.log('Message from server:', event.data);
}

// Concurrency: Both languages handle concurrency well, but JavaScript’s event loop and non-blocking I/O model are better suited for high-throughput, real-time applications.
// Threading: Python’s asyncio works best for I/O-bound tasks. For CPU-bound tasks, Python relies on multi-threading or multi-processing.
// Ease of Use: JavaScript’s async/await is simpler to implement for beginners, while Python requires familiarity with asyncio for similar functionality.
// JavaScript: Asynchronous programming is central to JavaScript’s design. Its event loop and Promises make it highly efficient for real-time, event-driven applications.
// Python: Asynchronous programming is a newer addition to Python, focused on handling I/O-bound tasks efficiently with asyncio.
// Syntax: Both languages use async/await, but Python requires explicit setup with asyncio, while JavaScript integrates it natively.

try {
    const result = 10 / 0;
    if (!isFinite(result)) {
        throw new Error("Cannot divide by zero.");
    }
}
catch (error) {
    console.error("Error:", error.message);
}
finally {
    console.log("Execution completed.");
}