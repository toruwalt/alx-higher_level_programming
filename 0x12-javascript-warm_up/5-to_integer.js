#!/usr/bin/node
const xxx = process.argv[2];
const numb = Number(process.argv[2]);
if (!isNaN(numb)) {
  console.log('My number: ', xxx);
} else {
  console.log('Not a number');
}
