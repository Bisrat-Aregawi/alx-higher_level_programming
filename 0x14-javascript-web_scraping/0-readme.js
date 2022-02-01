#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data.toString('utf8'));
});
