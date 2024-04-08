#!/usr/bin/node
const xxx = process.argv[2];
const numb = Number(process.argv[2]);
if (xxx && isNaN(numb)) {
  const integer = Math.floor(numb);
  console.log('My number: ', integer);
} else {
  console.log('Not a number');
}
