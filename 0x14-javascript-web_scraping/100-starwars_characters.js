#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const ch = JSON.parse(body).characters;
    for (let i = 0; i < ch.length; i++) {
      request(ch[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
