#!/usr/bin/node

const movie = procces.argv[2];
const request = require('request');

request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const data = JSON.parse(body);
    let counter = 0;
    data.results.forEach(film => {
      film.characters.forEach(pj => {
        if (pj.endsWith('/18/')) {
          counter++;
        }
      });
    });
    console.log(counter);
});