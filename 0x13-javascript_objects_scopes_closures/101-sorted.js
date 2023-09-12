#!/usr/bin/node

const { dict } = require('./101-data');

const userOccurrences = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (userOccurrences[occurrence] === undefined) {
    userOccurrences[occurrence] = [userId];
  } else {
    userOccurrences[occurrence].push(userId);
  }
}

console.log(userOccurrences);
