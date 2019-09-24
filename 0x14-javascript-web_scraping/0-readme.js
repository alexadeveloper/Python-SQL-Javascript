#!/usr/bin/node
//reads and prints the content of a file
const args = process.argv;
let fs = require('fs');
fs.readFile(args[2], 'utf8', function (err, data) {
  let mensaje = '';
  if (err) {
    mensaje = err;
  } else {
    mensaje = data;
  }
  console.log(mensaje);
});
