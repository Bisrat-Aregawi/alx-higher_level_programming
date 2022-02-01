#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (err, _, bdy) => {
  if (err) return err;
  console.log(JSON.parse(bdy).title);
});
