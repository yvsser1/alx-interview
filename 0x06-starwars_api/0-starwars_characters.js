#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

// Get the movie data first
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to get character name from URL
  const getCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        if (response.statusCode !== 200) {
          reject(new Error(`Invalid status code: ${response.statusCode}`));
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  // Process characters in sequence to maintain order
  const printCharactersInOrder = async () => {
    try {
      for (const characterUrl of characters) {
        const name = await getCharacterName(characterUrl);
        console.log(name);
      }
    } catch (error) {
      console.error('Error getting character:', error);
    }
  };

  printCharactersInOrder();
});
