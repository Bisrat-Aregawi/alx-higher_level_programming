#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (_, __, bdy) => {
  const result = JSON.parse(bdy);

  for (let i = 0; i < result.characters.length; i++) {
    request(result.characters[i], (_, __, bdy2) => {
      console.log(JSON.parse(bdy2).name);
    });
  }
});
