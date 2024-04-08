#!/usr/bin/node
const numb = Number(process.argv[2]);
if (!isNaN(numb)) {
  console.log('My number: ', numb);
} else {
  console.log('Not a number');
}
