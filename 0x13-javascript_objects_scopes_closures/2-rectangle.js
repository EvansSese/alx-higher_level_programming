#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0) {
      return;
    }
    if (h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
