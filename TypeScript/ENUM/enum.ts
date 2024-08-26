//        ENUM TYPE IN TYPESCRIPT
enum index {
    boys_over_flowers,
    its_okey_but_not_be_okey,
    true_beauty
}
console.log(index);
console.log('---------------');

console.log(index.boys_over_flowers);
console.log(index.its_okey_but_not_be_okey);
console.log(index.true_beauty);
console.log('---------------');

console.log(index[0]);
console.log(index[1]);
console.log(index[2]);
console.log('---------------');

console.log(index['boys_over_flowers']);
console.log(index['its_okey_but_not_be_okey']);
console.log(index['true_beauty']);
console.log('---------------');

console.log(index['0']);
console.log(index['1']);
console.log(index['2']);
console.log('---------------');

console.log(index['boys_over_flowers'] === 0);
console.log(index['its_okey_but_not_be_okey'] === 1);
console.log(index['true_beauty'] === 2);