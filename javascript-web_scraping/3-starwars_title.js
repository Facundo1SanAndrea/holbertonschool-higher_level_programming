#!/usr/bin/node

const movie = process.argv[2];
const request = require('request')

const url = 'https://swapi-api.hbtn.io/api/films/' + movie;

request(movie, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.title);
    }
});