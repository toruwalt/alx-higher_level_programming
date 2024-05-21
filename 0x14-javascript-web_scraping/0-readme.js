#!/usr/bin/node

const fs = require('fs');
const a = process.argv[2];

// Read the file asynchronously
fs.readFile(a, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
