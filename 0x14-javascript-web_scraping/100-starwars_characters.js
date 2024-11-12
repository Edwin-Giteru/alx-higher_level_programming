#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request({ url, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const characters = body.characters;
    for (const character in characters) {
      request({ url: characters[character], json: true }, (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          console.log(body.name);
        }
      });
    }
  }
});
