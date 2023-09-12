#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
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
}

module.exports = Square;
