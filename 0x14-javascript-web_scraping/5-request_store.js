#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], (_, __, bdy) => {
  fs.writeFile(process.argv[3], bdy, (err) => {
    if (err) return err;
  });
});
