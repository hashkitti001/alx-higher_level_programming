#!/usr/bin/node
const argOne = Number(process.argv[2]);
const argTwo = Number(process.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(argOne, argTwo));
