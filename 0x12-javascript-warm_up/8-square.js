#!/usr/bin/node
const n = parseInt(process.argv[2]);
const ch = 'X';
let i = 0;
if (process.argv.length === 2 || isNaN(n)) {
  console.log('Missing size');
} else {
  for (i = 0; i < n; i++) {
    console.log(ch.repeat(n));
  }
}
