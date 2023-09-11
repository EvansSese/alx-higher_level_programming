#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
let result = add(parseInt(args[0]), parseInt(args[1]));
console.log(result);
