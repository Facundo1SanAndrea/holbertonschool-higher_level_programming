#!/usr/bin/node
<<<<<<< HEAD

=======
>>>>>>> 05501a4c60b20f3ce9b476a15879a1fd4fea7b53
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const mydata = JSON.parse(body);
    let c = 0;
    for (const i of mydata.results) {
      for (const j of i.characters) {
        if (j.endsWith('/18/')) {
          c += 1;
        }
      }
    }
    console.log(c);
  }
<<<<<<< HEAD
});
=======
});
>>>>>>> 05501a4c60b20f3ce9b476a15879a1fd4fea7b53
