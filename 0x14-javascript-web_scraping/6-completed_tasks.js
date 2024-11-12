#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request({ url, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    for (const instance in body) {
      if (body[instance].completed && completed[body[instance].userId] === undefined) {
        completed[body[instance].userId] = 1;
      } else if (body[instance].completed) {
        completed[body[instance].userId] += 1;
      }
    }
    console.log(completed);
  }
});
