#!/usr/bin/node

const request = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
const url = link + id;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const prop = JSON.parse(body);
    console.log(prop.title);
  } else {
    console.log(`status_error: ${response.statusCode}`);
  }
});
