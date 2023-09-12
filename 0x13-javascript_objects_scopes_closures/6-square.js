#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor(size) {
    super(size);
  }

  print () {
    super.print();
  }

  rotate () {
    super.rotate();
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    if (this.size > 0) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}

module.exports = Square;