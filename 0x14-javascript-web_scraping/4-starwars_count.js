#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const r = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < r.length; i++) {
      const ch = r[i].characters;
      for (let j = 0; j < ch.length; j++) {
        if (ch[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
