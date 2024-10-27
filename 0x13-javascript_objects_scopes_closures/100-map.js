#!/usr/bin/node

const list = require('./100-data').list;

const newlist = list.map((value, index) => value * index);
console.log(list);
console.log(newlist);
