#!/usr/bin/node
const args = process.argv;
const numbers = [];
const without_big = [];
let i;
let biggest;
let biggest2;
if (args.length < 4) {
  console.log(0);
} else {
  for (i = 2; i < args.length; i++) {
    numbers.push(parseInt(args[i]));
  }
  biggest = Math.max(...numbers);
  for (i = 0; i < numbers.length; i++) {
    if (numbers[i] !== biggest) {
      without_big.push(parseInt(numbers[i]));
    }
  }
  biggest2 = Math.max(...without_big);
  console.log(biggest2);
}
