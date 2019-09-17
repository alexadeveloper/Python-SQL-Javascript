#!/usr/bin/node
// arguments input
const args = process.argv;
const value1 = parseInt(args[2], 10);
if (isNaN(value1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + value1);
}
