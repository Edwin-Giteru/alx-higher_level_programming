#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filePath = process.argv[3];

request ({url:URL, json: false}, (error, response, body) => {
	if (error) {
		console.log(error);
	} else if (response.statusCode === 200); {
		fs.writeFile(filePath, body, 'utf-8', (error) => {
			if (error) {
				console.log(error);
			}
		});
	}
});
