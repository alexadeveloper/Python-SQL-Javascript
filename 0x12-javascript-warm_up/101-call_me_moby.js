#!/usr/bin/node
// execute x times a function
exports.callMeMoby = function (n, funcion) {
  for (let i = 1; i <= n; i++) {
    funcion();
  }
};
