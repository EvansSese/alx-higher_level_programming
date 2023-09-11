#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  let secondLargest = sortedArgs[1];

  for (let i = 2; i < sortedArgs.length; i++) {
    if (sortedArgs[i] !== sortedArgs[0]) {
      secondLargest = sortedArgs[i];
      break;
    }
  }
  console.log(secondLargest);
}
