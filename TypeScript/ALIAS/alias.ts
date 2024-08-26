type Vartype = any;

let str: Vartype = "Hi my name is Misbah_Sajjad";
let bool: Vartype = true;
let num: Vartype = 18 + " year old";
let city: Vartype = "Karachi";
let arr: Vartype = ["Misbah", "Sajjad", 18 + " year old", "Karachi"];
let obj: Vartype = { name: "Misbah", age: 18 + " year old", city: "Karachi" };

console.log('String');
console.log(str);
console.warn('===============');
console.log('Boolean');
console.log(bool);
console.warn('===============');
console.log('Number');
console.log(num);
console.warn('===============');
console.log("City");
console.log(city);
console.warn('===============')
console.log('array');
console.log(arr);
console.warn('===============');
console.log('object');
console.log(obj);
console.warn('===============');
console.log('===============');

console.warn(`"name" ${str} "single" ${bool} "age" ${num} "city" ${city} "array" ${arr} "object" ${obj}`);