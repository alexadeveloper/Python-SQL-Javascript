#!/usr/bin/node
// reads and prints the content of a file

const args = process.argv;
const request = require('request');
request.get(args[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    let data = [];
    for (const i of JSON.parse(body).results) {
      data = data.concat(i.characters);
    }
    const cont = (data.filter(x => x.includes('18'))).length;
    console.log(cont);
  } else {
    console.log('Invalid');
  }
});
