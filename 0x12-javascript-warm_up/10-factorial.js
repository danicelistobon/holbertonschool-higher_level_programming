#!/usr/bin/node
const n = parseInt(process.argv[2]);
function fact (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
console.log(fact(n));
