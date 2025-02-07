#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, { json: true }, (err, res, body) => {
        if (err || res.statusCode !== 200) {
            console.error("Error: Unable to fetch data. Check the Movie ID.");
            return;
        }
        
        const characters = body.characters;
        characters.forEach(characterUrl => {
            request(characterUrl, { json: true }, (charErr, charRes, charBody) => {
                if (!charErr && charRes.statusCode === 200) {
                    console.log(charBody.name);
                }
            });
        });
    });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <Movie ID>");
} else {
    getMovieCharacters(process.argv[2]);
}

