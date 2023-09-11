#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
let result = add(args[0], args[1]);
console.log(result);
