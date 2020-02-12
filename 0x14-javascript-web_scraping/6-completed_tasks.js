#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const r = {};
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed) {
        if (r[todos[i].userId] === undefined) {
          r[todos[i].userId] = 1;
        } else {
          r[todos[i].userId] += 1;
        }
      }
    }
    console.log(r);
  }
});
