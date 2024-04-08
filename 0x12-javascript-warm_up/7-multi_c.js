#!/usr/bin/node
const message = 'C is fun';
const numOfRepeats = process.argv[2];
let i = 0;
if (Number.isNaN(Number(numOfRepeats))) {
  console.log('Missing number of occurences');
}
while (i < numOfRepeats) {
  console.log(message);
  i += 1;
}
