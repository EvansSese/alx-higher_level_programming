#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <=0 || (Math.sign(parseInt(w))) === -1 || (Math.sign(parseInt(h))) === -1) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
