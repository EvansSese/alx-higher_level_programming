#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log(`Usage: node ${process.argv[0]} <URL> <output_file_path>`);
  process.exit(1);
}

const url = process.argv[2];
const outputPath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    fs.writeFile(outputPath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
