#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
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

  charPrint (c) {
    if (this.size > 0) {
      let char = 'C'
      if (c === undefined) {
        char = 'X'
      }
      for (let i = 0; i < this.size; i++) {
        console.log(char.repeat(this.size));
      }
    }
  }
}

module.exports = Square;