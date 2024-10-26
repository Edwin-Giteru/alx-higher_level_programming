#!/usr/bin/node
/* a script that prints the first argument passed to it */

const args = process.argv.slice(2);
if (args[2] === undefined) { console.log('No Argument'); } else { console.log(args[2]); }
