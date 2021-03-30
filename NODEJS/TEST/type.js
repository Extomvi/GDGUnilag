const age = 21;

const addMyAge = age + 30;

// console.log(addMyAge);
// console.log("Are you working?");

const firstName = "Tomiwa";
const lastName = "Adedokun";

// const fullName = `${firstName} ${lastName}`;
// console.log(fullName);

const isTrue = 1 > 2;
// console.log(Boolean());

const Interns = ["Bori", "osi", "Chioma"];
Interns.push("Oma"); //adds to the last element
// console.log(Interns);
Interns.shift(); // removes from the first element
// console.log(Interns); 
Interns.pop(); // removes from the last element
// console.log(Interns); 
Interns.unshift("Kilanko"); // adds to the front of the array
Interns.push("Amaka");
Interns.push("Shonibare");
Interns.shift();
Interns.unshift("Ekene");
Interns.pop();
// console.log(Interns);

const fullName = "Tomiwa Adedokun";
// console.log(fullName.includes(lastName));
// console.log(firstName.slice(0, 6)); // slicing(index starts from 1 in js unlike 0 in python)

const jsFunc = {
    ninj1: "ome",
    ninj2: "Jane",
    ninj3: "Bammy"
}

// console.log(Object.values(jsFunc));  // gives every entry value
// console.log(Object.entries(jsFunc)); // gives the key and the values

const topSpenders = [
    "wizkid",
    "burnaboy",
    "davido",
    "bella"
]

// console.log(topSpenders.includes("wizkid")); // checks through the array to find elements in them
//iteration operation
const updatedTopSpenders = topSpenders.filter(item => {
    return !item.startsWith("w")
});
// console.log(updatedTopSpenders);

// include, filter & map
const updatedSpenders = topSpenders.map((item, index, mainArray) => {
    return `celeb_${item}`
});
// console.log(updatedSpenders);

//function

var number = 5;

function doIt(){
    const number = 15;
    return number;
}
console.log(doIt())



