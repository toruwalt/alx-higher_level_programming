#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

// Read the file asynchronously
fs.writeFile(file, text, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
