#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (...args) {
    if (args[0] === 'C') {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          const x = 'C';
          process.stdout.write(x);
        }
        process.stdout.write('\n');
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
