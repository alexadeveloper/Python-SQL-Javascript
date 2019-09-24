#!/usr/bin/node
// computes a new array
const lista = require('./100-data').list;
const newLista = [];
let ant = 0;
for (let i = 0; i < lista.length; i++) {
  newLista[i] = lista[i] * ant;
  ant = lista[i];
}
console.log(lista);
console.log(newLista);
