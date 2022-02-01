#!/usr/bin/node
const request = require('request');

request(process.argv[2], (_, __, bdy) => {
  const res = JSON.parse(bdy);
  const obj = {};

  for (let i = 0; i < res.length; i++) {
    if (res[i].completed) {
      if (res[i].userId in obj) {
        obj[res[i].userId] += 1;
      } else {
        obj[res[i].userId] = 1;
      }
    }
  }

  console.log(obj);
});
