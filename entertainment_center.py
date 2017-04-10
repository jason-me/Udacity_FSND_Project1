import fried_tomatoes
import media

# Defines each object/instance of .Movie below
event_horizon = media.Movie("Event Horizon",
                            "Infinite space, infinite terror",
                            "http://www.dvdsreleasedates.com/posters/800/E/Event-Horizon-movie-poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=THxBHDsgTDw",
                            "R")

donnie_darko = media.Movie("Donnie Darko",
                           "A boy has a dream about dying",
                           "http://chuckyg.com/lists/movies/posters/donnie-darko-2001.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=ZPAjREJugkw",
                           "R")

fight_club = media.Movie("Fight Club",
                         "The infamous story of Tyler Durden",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=6JnN1DmbqoU",
                         "R")

super_troopers = media.Movie("Super Troopers",
                             "A hillarious ride along with the police",
                             "http://images.moviepostershop.com/super-troopers-movie-poster-1020476783.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=dpIAI0elKpU",
                             "R")

neighbors = media.Movie("Neighbors",
                        "Welcome to the neighborhood",
                        "http://www.fatmovieguy.com/wp-content/uploads/2014/01/Neighbors-Movie-Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=suZgGFL7Olw",
                        "R")

one_flew = media.Movie("One Flew Over the Cuckoo's Nest",
                       "A criminal pleads insanity after getting into trouble",
                       "https://upload.wikimedia.org/wikipedia/en/2/26/One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=oUobWmLF9WQ",
                       "R")

# Defines an array/list of movies above
movies = [event_horizon, donnie_darko, fight_club, super_troopers, neighbors,
          one_flew]
fried_tomatoes.open_movies_page(movies)  # Calls HTML file & opens movies array
