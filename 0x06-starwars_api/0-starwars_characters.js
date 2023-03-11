#!/usr/bin/node
const process = require('process');
const request = require('request');

const urlEndpoint = 'https://swapi-api.alx-tools.com/api/films/';
const args = process.argv;
if (args.length !== 3) { process.exit(1); }
const movieId = args[2];
request.get(urlEndpoint + movieId, async function (error, response, body) {
  if (error || response.statusCode !== 200) { process.exit(1); }
  const data = JSON.parse(body);
  for (const item of data.characters) {
    await new Promise((resolve, reject) => {
      request(item, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});
