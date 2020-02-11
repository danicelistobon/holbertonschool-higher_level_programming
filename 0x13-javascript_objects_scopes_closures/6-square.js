#!/usr/bin/node
const Square = require('./5-square');
let ch = 'X';
module.exports = class Square2 extends Square {
  charPrint (c) {
    if (c) {
      ch = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
};
