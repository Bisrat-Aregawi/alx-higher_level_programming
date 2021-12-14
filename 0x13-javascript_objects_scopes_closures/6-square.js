#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    let width = '';

    for (let i = 0; i < this.height; i++) width += C || 'X';
    for (let i = 0; i < this.height; i++) console.log(width);
  }
}

module.exports = Square;
