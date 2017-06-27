import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    The constructor takes four arguments:

    * movie_title: name of the movie
    * movie_storyline: the synopsis of the movie
    * poster_image: poster of the movie
    * trailer_youtube: youtube trailer of the movie
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Initialise all of the instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Opens the trailer in the web browser
        webbrowser.open(self.trailer_youtube_url)
