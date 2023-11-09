#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      const characterPromises = characters.map((characterUrl) => {
        return new Promise((resolve) => {
          request.get(characterUrl, (error, response, body) => {
            if (error) {
              console.log(error);
              resolve(null);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then((characterNames) => {
          characterNames.forEach((name) => {
            console.log(name);
          });
        })
        .catch((error) => {
          console.log(error);
        });
    }
  });
}

getMovieCharacters(movieId);
