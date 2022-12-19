#!/usr/bin/node
<<<<<<< HEAD

=======
>>>>>>> 05501a4c60b20f3ce9b476a15879a1fd4fea7b53
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
<<<<<<< HEAD
});
=======
});
>>>>>>> 05501a4c60b20f3ce9b476a15879a1fd4fea7b53
