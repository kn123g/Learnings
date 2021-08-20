let arr = [1,2];
let a = arr;
let b = [1,4];
a = b;
console.log(arr, a , b) 
// a=[1,3]
a.push(5);
console.log(arr, a, b)