#!/usr/bin/node
// arguments input
const args = process.argv;
const large = args.length - 2;
if (large === 0) {
  console.log('No argument');
} else if (large === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
