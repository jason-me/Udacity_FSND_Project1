import webbrowser
# Invokes the module webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

# Defines a class variable as an example
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# Defines the instance variables present in each instance of the class.Movie
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating  # additional variable for rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)  # opens url in web browser
