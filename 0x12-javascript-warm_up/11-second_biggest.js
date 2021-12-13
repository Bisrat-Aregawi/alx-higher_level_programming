#!/usr/bin/node
const second = process.argv.slice(2).sort(function (a, b) {
  return b - a;
})[1];
if (second) {
  console.log(second);
} else {
  console.log(0);
}
