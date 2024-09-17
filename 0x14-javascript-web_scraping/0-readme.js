#!/usr/bin/node
const fs = require('fs');
const cb = (err, data) => {
  if (err) {
    console.log(err);
  }
  if (data) {
    console.log(data.toString());
  }
};
fs.readFile(process.argv[2], 'utf-8', cb);
