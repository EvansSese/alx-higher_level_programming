#!/usr/bin/node

const fs = require('fs');
const path = require('path');

if (process.argv.length !== 5) {
  console.error('Usage: node concat-files.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const concatenateFiles = (file1, file2, destination) => {
  try {
    const data1 = fs.readFileSync(file1, 'utf8');
    const data2 = fs.readFileSync(file2, 'utf8');

    fs.writeFileSync(destination, data1 + data2);

    console.log('Files concatenated successfully!');
  } catch (err) {
    console.error('An error occurred:', err.message);
  }
};

concatenateFiles(sourceFile1, sourceFile2, destinationFile);
