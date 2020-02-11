#!/usr/bin/node
const array = require('./100-data').list;
console.log(array);
const array2 = array.map(function (x, y) { return (x * y); });
console.log(array2);
