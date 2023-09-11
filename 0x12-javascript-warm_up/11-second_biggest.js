#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  let secondLargest = sortedArgs[1];

  for (let i = 1; i < sortedArgs.length; i++) {
    if (sortedArgs[i] !== sortedArgs[0]) {
      secondLargest = sortedArgs[i];
      break;
    }
  }
  console.log(secondLargest);
}
