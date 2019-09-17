#!/usr/bin/node
// execute x times a function
exports.addMeMaybe = function (n, funcion) {
  funcion(n + 1);
};
