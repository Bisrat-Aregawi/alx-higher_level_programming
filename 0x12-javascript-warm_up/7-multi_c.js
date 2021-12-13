#!/usr/bin/node
let i = parseInt(process.argv[2]);

if (i || i === 0) {
  if (i >= 0) {
    while (i--) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
