let data: string | boolean = "sky castle";
console.log(data);

let data1: "sky castle" | true = true;
console.log(`"data " ${data1}`);
console.log('=================');

function combine(a: number | string, b: number | string, type: 678 | "present is present") {

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