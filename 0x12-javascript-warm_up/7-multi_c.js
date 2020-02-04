#!/usr/bin/node
const n = parseInt(process.argv[2]);
const c = 'C is fun';
let i = 0;
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < n; i++) {
    console.log(c);
  }
}
