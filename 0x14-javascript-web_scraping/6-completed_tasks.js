#!/usr/bin/node
// reads and prints the content of a file

const args = process.argv;
const request = require('request');

request.get(args[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const task = JSON.parse(body);
  const data = {};
  for (const i of task) {
    if (i.completed === true) {
      if (data[i.userId] === undefined) {
        data[i.userId] = 1;
      } else {
        data[i.userId]++;
      }
    }
  }
  console.log(data);
});
