#!/usr/bin/node

//a script that reads and prints the content of a file

const fs = require('fs');

const filepath = process.argv[2]

if(!filepath) {
	console.error('please provide a filepath as an arguments.');
	process.exit(1);
}

fs.readFile(filepath, 'utf8', (err, data) => {
	if (err) {
		console.log(err);
	} else {
		console.log(data);
	}

});
