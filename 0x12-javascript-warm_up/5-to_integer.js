#!/usr/bin/node
const myNumber = Number.isNaN(Number(process.argv[3]));
if (myNumber) {
  console.log('Not a number');
} else {
  console.log(`${process.argv[3]}`);
}
