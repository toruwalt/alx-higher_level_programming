#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

// Read the file asynchronously
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
