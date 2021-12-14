#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) return err;
  let text = data.toString();
  fs.readFile(process.argv[3], (err, data) => {
    if (err) return err;
    text += data.toString();
    fs.writeFile(process.argv[4], text, (err) => {
      if (err) return err;
    });
  });
});
