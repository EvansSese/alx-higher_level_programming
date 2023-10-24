#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
