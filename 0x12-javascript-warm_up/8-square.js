#!/usr/bin/node
let size = parseInt(process.argv[2]);
let side = '';

if (size || size === 0) {
  if (size >= 0) {
    for (let i = 0; i < size; i++) {
      side += 'X';
    }
    while (size--) {
      console.log(side);
    }
  }
} else {
  console.log('Missing size');
}
