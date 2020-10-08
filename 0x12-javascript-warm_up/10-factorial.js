#!/usr/bin/node
const num = parseInt(process.argv[2]);
let result = 1;

function factorial (num) {
  if (num > 0) {
    for (let i = num; i > 0; i--) {
      result *= i;
    }
    return console.log(result);
  }
}
if (!num) console.log(1);
else factorial(num);
