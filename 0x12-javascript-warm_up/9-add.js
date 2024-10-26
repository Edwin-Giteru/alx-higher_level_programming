#!/usr/bin/node

const args = process.argv.slice(2);
const one = parseInt(args[0]);
const two = parseInt(args[1]);
function add(a, b) {
	return a + b;
}
console.log(add(one, two));
