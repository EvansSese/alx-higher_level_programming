#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: node write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log('File successfully written.');
  }
});
