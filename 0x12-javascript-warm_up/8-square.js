#!/usr/bin/node

const args = process.argv.slice(2);
let i, j;

if (args.length > 0) {
  const size = parseInt(args[0]);
  if (!isNaN(size)) {
    for (i = 0; i < size; i++) {
      let row = '';
      for (j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
