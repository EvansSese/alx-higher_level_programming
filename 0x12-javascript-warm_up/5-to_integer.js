#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length > 0) {
  const firstArg = parseInt(args[0]);
  
  if (!isNaN(firstArg)) {
    console.log('My number: ' + firstArg);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
