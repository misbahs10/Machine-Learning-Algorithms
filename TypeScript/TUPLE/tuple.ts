//            TUPLE TYPE IN TYPESCRIPT
// 1. Tuple is a fixed size array with a fixed type

let tuple: [string, string, number, number, boolean] = ['Queen Of Tear', 'Vincenzo', 67, 87, false]
tuple.push('All of us are Death');
tuple[3] = 78;
console.log(tuple);
console.log('------------------');

console.log(tuple[0]); // Queen of Tear
console.log(tuple[1]); // Vincenzo
console.log(tuple[2]); // 67
console.log(tuple[3]); // 87
console.log(tuple[4]); // false