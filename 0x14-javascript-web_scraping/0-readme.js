#!/usr/bin/node
const fs = require('fs');
const cb = (err, data) => {
 console.log(err || data);
};
fs.readFile(process.argv[2], 'utf-8', cb);
