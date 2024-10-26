#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) { console.log(0); } else {
  const intArgs = args.sort((a, b) => a - b);
  console.log(intArgs[intArgs.length - 2]);
}
