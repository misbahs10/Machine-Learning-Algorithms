var data = "sky castle";
console.log(data);
var data1 = true;
console.log("\"data \" ".concat(data1));
console.log('=================');
function combine(a, b, type) {
    if (type === 678) {
        return (+a) + (+b);
    }
    else if (typeof a === "string" && typeof b === "string") {
        return a + b;
    }
    else {
        return a.toString() + b.toString();
    }
}
console.log(combine(456, 899, 678));
console.log("=================");
console.log(combine("(Goblin)", " (No_Handsome_Guy)", "present is present"));
