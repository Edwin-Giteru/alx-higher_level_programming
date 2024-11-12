#!/usr/bin/node

// a script that writes a string to a file

const fs = require('fs');

const filepath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filepath, string, 'utf-8', (err)=> {
	if (err) {
		console.log(err);
	}
});
