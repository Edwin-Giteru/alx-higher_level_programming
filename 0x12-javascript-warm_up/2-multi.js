#!/usr/bin/node

const args = process.argv.slice(2);
let x = parseInt(args[0]);

if (isNaN(x)) { console.log('Missing number of occurrences'); } else if (x < 0) { // if x is negative
} else {
  while (x !== 0) {
    console.log('C is fun');
    x--;
  }
}
