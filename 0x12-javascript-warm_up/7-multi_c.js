#!/usr/bin/node
const msm = 'C is fun';
const arg = process.argv;
const valArg = parseInt(arg[2], 10);

if (isNaN(valArg)) console.log('Missing number of occurrences');
for (let i = 0; i < valArg; i++) {
  console.log(msm);
}
