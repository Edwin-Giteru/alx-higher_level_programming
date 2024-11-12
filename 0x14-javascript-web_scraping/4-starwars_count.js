#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request({url, json: true}, (error, response, body) => {
	if (error) {
		console.log(error);
	} else if (response.statusCode === 200) {
		const films = response.results;
		let count = 0;
		for (const index in films) {
			const characters =films[index].characters;
			for (const character in characters) {
				if (characters[character].includes('18')) {
					count++;
				}
			}
		}
		console.log(count);
	}
});
