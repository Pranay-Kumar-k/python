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