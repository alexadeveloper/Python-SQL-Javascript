#!/usr/bin/node
// add 2 argvs
const args = process.argv;
const size = args.length - 2;
if (size <= 1) {
  console.log('0');
} else {
  let first = parseInt(args[2], 10);
  let second = parseInt(args[3], 10);
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i], 10) > first) {
      second = first;
      first = parseInt(args[i], 10);
    }
    if (parseInt(args[i], 10) > second && parseInt(args[i], 10) < first) {
      second = parseInt(args[i], 10);
    }
  }
  console.log(second);
}
