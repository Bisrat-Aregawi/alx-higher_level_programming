#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, _, bdy) => {
  if (err) return err;
  const result = JSON.parse(bdy).results;
  let count = 0;
  const character = 'https://swapi-api.hbtn.io/api/people/18/';
  for (let i = 0; i < result.length; i++) {
    for (let j = 0; j < result[i].characters.length; j++) {
      if (result[i].characters[j] === character) {
        count += 1;
      }
    }
  }
  console.log(count);
});
