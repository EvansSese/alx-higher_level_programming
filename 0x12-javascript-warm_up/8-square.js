#!/usr/bin/node

const args = process.argv.slice(2);
let i, j;

if (args.length > 0) {
  const size = parseInt(args[0]);
  if (!isNaN(size)) {
    for (i = 0; i <= size; i++) {
      for (j = 0; j <= size; j++) {
        console.log('X');
      }
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
