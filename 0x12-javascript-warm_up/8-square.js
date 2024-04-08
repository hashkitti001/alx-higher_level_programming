#!/usr/bin/node
const size = process.argv[2];
if (Number.isNaN(Number(size))) {
  console.log('Missing size');
}
for (let rows = 0; rows < size; rows++) {
  console.log('#'.repeat(size));
}
