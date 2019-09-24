#!/usr/bin/node
// reads and prints the content of a file

const args = process.argv;
const request = require('request');
request.get('http://swapi.co/api/films/' + args[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
