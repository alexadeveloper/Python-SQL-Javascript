#!/usr/bin/node
// reads and prints the content of a file

const args = process.argv;
const fs = require('fs');
fs.writeFile(args[2], args[3], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
