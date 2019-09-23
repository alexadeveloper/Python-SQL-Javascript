#!/usr/bin/node
// class rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        str = str + 'X';
      }
      str = str + '\n';
    }
    console.log(str.slice(0, -1));
  }

  rotate () {
    const ant = this.height;
    this.height = this.width;
    this.width = ant;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
