#!/usr/bin/node
// class logMe
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
