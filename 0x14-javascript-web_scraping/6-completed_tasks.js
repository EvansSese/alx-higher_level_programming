#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log(`Usage: node ${process.argv[0]} <API_URL>`);
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    try {
      const todos = JSON.parse(body);
      const completedTasks = {};

      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });

      for (const userId in completedTasks) {
        console.log(`${userId}: ${completedTasks[userId]}`);
      }
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
