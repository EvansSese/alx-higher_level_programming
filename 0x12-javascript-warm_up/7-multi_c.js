#!/usr/bin/node

const args = process.argv.slice(2);
let i = 0;

if (args[0] !== undefined && !isNaN(args[0])) {
  while (i < args[0]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurences');
}
