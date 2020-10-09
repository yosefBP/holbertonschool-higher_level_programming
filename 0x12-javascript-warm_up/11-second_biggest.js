#!/usr/bin/node
const array = process.argv;
const numArray = [];

if (array.length <= 3) {
  console.log(0);
} else {
  const numbers = array.slice(2, array.leng);
  for (const num1 of numbers) {
    numArray.push(parseInt(num1));
  }
  const firstMax = Math.max(...numArray);
  const numArray2 = numArray.filter(secondMax => secondMax < firstMax);
  console.log(Math.max(...numArray2));
}
