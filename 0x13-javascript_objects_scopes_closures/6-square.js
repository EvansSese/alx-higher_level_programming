#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < 4; i++) {
      console.log(c.repeat(4));
    }
    console.log(4);
  }
}

module.exports = Square;
