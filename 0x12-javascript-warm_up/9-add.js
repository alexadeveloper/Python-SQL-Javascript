#!/usr/bin/node
// add 2 argvs
const args = process.argv;
const num = parseInt(args[2], 10);
const num2 = parseInt(args[3], 10);
function add (a, b) {
  console.log(a + b);
}
add(num, num2);
