//use const where variable values do not change
var a = 5;
var b = 33;
var c = "best";
//I suggest use let instead of var everywhere, 
//because let has blocked scope
if (true) {
    var z = 4;
    //use z
}
else {
    var z = "string";
    //use z
}
console.log("let: " + z); // Error: z is not defined in this scope
