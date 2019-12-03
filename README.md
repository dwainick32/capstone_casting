This project is the final project for the Udacity Full Stack Developer Nano Degree 

The project is to simulate a casting agency. This includes having actors and movies and assigning actors to movies. 

This project has two models/tables: A movie table that holds all the movies and an actors table that holds all the actors. For each movie, there are many actors so there is a one to many relationship there. 

To login or set up an account, go to the following url: 

https://casting-capstone.auth0.com/authorize?audience=cast&response_type=token&client_id=UdxgyT6RC2frwGoZ7lJEO3FDCRRoDZq0&redirect_uri=https://capstone-casting.herokuapp.com/login-results

There are three roles within the API. Casting Assistant, Casting Director and Executive Producer. The logins for the three roles has been provided in the separate notes 

The url for the API:
https://capstone-casting.herokuapp.com/

The endpoints are as follows: 

GET '/movies'
    This endpoint fetches all the movies in the database and displays them as json 

GET '/actors'
    This endpoint fetches all the actors in the databse and displays them as json 

POST '/movies/create'
    This endpoint will create a new movie in the database based on the json that is in the body of the request 

POST '/actors/create'
    This endpoint will create a new actor in the database based on the json that is in the body of the request 

DELETE '/movies/delete/int:movie_id'
    This endpoint will delete the movie that corresponds to the movie ID that is passed into the url 

DELETE '/actors/delete/int:actor_id'
    This endpoint will delete the actor that corresponds to the actor ID that is passed into the url 

PATCH '/actors/patch/int:actor_id' 
    This endpoint will modify the actor that corresponds to the actor ID that is passed into the url based on the json that is passed into the body of the request 

PATCH '/movies/patch/int:movie_id'
    This endpoint will modify the movie that corresponds to the movie ID that is passed into the url based on the json that is passed into the body of the request