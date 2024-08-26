//             UNION TYPE IN TYPESCRIPT
// 1. Union type describes a value that can be one of several types
// 2. Union type is written with the pipe symbol ( | ) between each type
function combine(a, b) {
    if (typeof a === "number" && typeof b === "number") {
        return a + b;
    }
    else if (typeof a === "string" && typeof b === "string") {
        return a + b;
    }
    else {
        return a.toString() + b.toString();
    }
}
console.log(combine(456, 899));
console.log("=================");
console.log(combine("(Goblin)", " (No_Handsome_Guy)"));
