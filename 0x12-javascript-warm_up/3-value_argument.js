#!/usr/bin/node
// arguments input
const args = process.argv;
const value = args[2];
if (value === undefined) {
  console.log('No argument');
} else {
  console.log(value);
}
