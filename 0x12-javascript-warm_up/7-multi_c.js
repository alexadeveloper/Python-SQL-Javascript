#!/usr/bin/node
// loop to languages
const args = process.argv;
const large = parseInt(args[2]);
const frase = 'C is fun';
if (isNaN(large)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < large; i++) {
    console.log(frase);
  }
}
