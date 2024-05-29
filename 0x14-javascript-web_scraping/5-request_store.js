#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const file = process.argv[3];
const url = process.argv[2];

// Write from API to the file asynchronously
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log(`status_error: ${response.statusCode}`);
  }
});
