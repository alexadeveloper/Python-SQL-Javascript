#!/usr/bin/node
// class square
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str = '';
    let rep = c;
    if (c == null) {
      rep = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        str = str + rep;
      }
      str = str + '\n';
    }
    console.log(str.slice(0, -1));
  }
};
