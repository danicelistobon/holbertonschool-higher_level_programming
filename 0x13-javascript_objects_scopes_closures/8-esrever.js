#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  const r = [];
  while (l >= 0) {
    r.push(list[l]);
    l--;
  }
  return (r);
};
