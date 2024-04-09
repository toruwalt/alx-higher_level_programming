#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (((Number.isInteger(w)) && w > 0) && ((Number.isInteger(h)) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
	let x = "X"
        process.stdout.write(x);
      }
      process.stdout.write("\n");
    }
  }
}

module.exports = Rectangle;
