#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node get_request.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error(error.message);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
