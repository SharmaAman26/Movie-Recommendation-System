# Movie-Recommendation-System
This project goes through the process of mashing up data from two different APIs to make movie recommendations. 
The TasteDive API lets us provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. 
The OMDB API lets us provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

This project will put those two together and use TasteDive to get related movies for a whole list of titles. 
It’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which it get through making API calls to the OMDB API.)

