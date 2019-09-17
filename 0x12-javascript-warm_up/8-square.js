#!/usr/bin/node
// loop to languages
const args = process.argv;
const size = parseInt(args[2]);
const value = 'X';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(value.repeat(size));
  }
}
