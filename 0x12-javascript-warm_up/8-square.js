#!/usr/bin/node

const args = process.argv.slice(2);
const x = Number(args[0]);

if (isNaN(x)) { console.log('Missing size') } else if (x<0) {
         } else {
		 for (let i=0; i<x; i++) {
			 console.log('X'.repeat(x));
		 }
	 }

