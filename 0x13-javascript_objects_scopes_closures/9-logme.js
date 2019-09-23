#!/usr/bin/node
// class logMe
let cont = 0;
exports.logMe = function (item) {
  console.log(cont + ': ' + item);
  cont = cont + 1;
};
