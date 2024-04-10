#!/usr/bin/node

const argA = process.argv[2];
const a = +argA;
const argB = process.argv[3];
const b = +argB;

function add (a, b) {
  if ((isNaN(a) || a === undefined) || ((isNaN(b) || b === undefined))) {
    console.log('NaN');
  } else {
    const d = a + b;
    console.log(d);
  }
}

add(a, b);
