#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmid}`;

request({url, json: true}, (error, response, body) => {
	if (error) { console.log(error);
	} else if (response.statusCode === 200)  {
		console.log(body.title);
	}
});
