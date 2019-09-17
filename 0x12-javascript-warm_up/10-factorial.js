#!/usr/bin/node
// add 2 argvs
const args = process.argv;
const conv = parseInt(args[2], 10);
if (isNaN(conv)) {
  console.log('1');
} else {
  const num = factorial(conv);
  console.log(num);
}
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
