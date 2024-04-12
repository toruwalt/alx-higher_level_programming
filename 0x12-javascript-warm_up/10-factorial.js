#!/usr/bin/node

const argA = process.argv[2];
const a = +argA;

function factorial (a) {
  if (isNaN(a) || a === undefined) {
    return 1;
  } else {
    if (a === 1 || a === 0) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
}

console.log(factorial(a));
