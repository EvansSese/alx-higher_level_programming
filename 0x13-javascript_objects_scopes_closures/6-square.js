#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < size; i++) {
      console.log(c.repeat(size));
    }
    console.log(size);
  }
}

module.exports = Square;
