#!/usr/bin/node
const args = process.argv;
const numbers = [];
const withoutBig = [];
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
      withoutBig.push(parseInt(numbers[i]));
    }
  }
  biggest2 = Math.max(...withoutBig);
  console.log(biggest2);
}
