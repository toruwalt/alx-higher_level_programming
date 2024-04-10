#!/usr/bin/node

const arg = process.argv[2];
const x = +arg;
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let i = 0; i < x; i++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
