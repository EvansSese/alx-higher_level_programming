#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log(`Usage: node ${process.argv[0]} <Movie_ID>`);
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    try {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      const fetchCharacter = (url) => {
        request(url, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(characterError);
          } else if (characterResponse.statusCode !== 200) {
            console.error(characterResponse.statusCode);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
            if (characterUrls.length > 0) {
              fetchCharacter(characterUrls.shift());
            }
          }
        });
      };

      if (characterUrls.length > 0) {
        fetchCharacter(characterUrls.shift());
      }
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
