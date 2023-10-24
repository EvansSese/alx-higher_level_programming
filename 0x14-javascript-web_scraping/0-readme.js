#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length !== 3) {
  console.log('Usage: node read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the file asynchronously
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(`An error occurred: ${error.message}`);
  } else {
    console.log(data);
  }
});
