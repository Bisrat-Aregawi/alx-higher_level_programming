#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const elem in dict) {
  if (!newDict[dict[elem]]) {
    newDict[dict[elem]] = [elem];
  } else {
    newDict[dict[elem]].push(elem);
  }
}
console.log(newDict);
