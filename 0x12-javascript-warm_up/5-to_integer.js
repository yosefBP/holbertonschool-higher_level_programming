#!/usr/bin/node
const arg = process.argv;
const valArg = parseInt(arg[2], 10);

if (!arg[2]) {
  console.log('Not a number');
} else if (isNaN(valArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${valArg}`);
}
