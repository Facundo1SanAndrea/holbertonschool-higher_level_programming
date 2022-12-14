#!/usr/bin/node
// Writes and prints the content of a file

const path = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

request.appendFile(path, str, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
});