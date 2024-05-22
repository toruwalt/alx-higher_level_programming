#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const prop = JSON.parse(body);
    const props = prop["results"];
    const propss = props["characters"];
    for (const y in props) {
      for (z in y.characters) {
        console.log("z");
      }
    }
    let m = 0;
    for (const x in prop["results"]) {
//      for (const y in x["characters"]) {
        m += 1;
//      }
    }
    console.log(m);
/*    let m = 0;
    for (let i = 0; i<prop.films.length; i++)
	  {m += 1}
    console.log(m)*/
  } else {
    console.log(`status_error: ${response.statusCode}`);
  }
});
