#!/usr/bin/node
// reads and prints the content of a file

const args = process.argv;
const request = require('request');
const fs = require('fs');

request.get(args[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(args[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
