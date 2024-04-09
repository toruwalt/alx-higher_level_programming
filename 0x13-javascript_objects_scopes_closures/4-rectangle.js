#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (((Number.isInteger(w)) && w > 0) && ((Number.isInteger(h)) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        const x = 'X';
        process.stdout.write(x);
      }
      process.stdout.write('\n');
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const swap = this.height;
    this.height = this.width;
    this.width = swap;
  }
}

module.exports = Rectangle;
