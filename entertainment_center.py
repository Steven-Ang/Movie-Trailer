# -*- coding: utf-8 -*-
import media
import fresh_tomatoes


# Synopsis
goodfellas_synopsis = "The story of Henry Hill and his life through the teen years into the years of mafia, covering his relationship with wife Karen Hill and his Mob partners Jimmy Conway and Tommy DeVitto in the Italian-American crime syndicate."  # NOQA

godfather_synopsis = "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."  # NOQA

silence_of_the_lambs_synopsis = "A young F.B.I. cadet must confide in an incarcerated and manipulative killer to receive his help on catching another serial killer who skins his victims."  # NOQA

halloween_synopsis = "Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield to kill again."  # NOQA

the_shining_synopsis = "Jack Torrance accepts a caretaker job at the Overlook Hotel, where he, along with his wife Wendy and their son Danny, must live isolated from the rest of the world for the winter. But they aren't prepared for the madness that lurks within."  # NOQA

evangelion_synopsis = "Concurrent theatrical ending of the TV series Shin Seiki Evangelion (1995)."  # NOQA

# Create multiple movie instances
goodfellas = media.Movie(
    "Goodfellas",
    goodfellas_synopsis,
    "https://images-na.ssl-images-amazon.com/images/I/51rOnIjLqzL.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qo5jJpHtI1Y"
)

godfather = media.Movie(
    "The Godfather",
    godfather_synopsis,
    "https://movietalkexpress.files.wordpress.com/2015/12/the-godfather.jpeg",  # NOQA
    "https://www.youtube.com/watch?v=sY1S34973zA"
)

silence_of_the_lambs = media.Movie(
    "The Silence of The Lambs",
    silence_of_the_lambs_synopsis,
    "https://images-na.ssl-images-amazon.com/images/I/410VHPrwUPL._SY450_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=RuX2MQeb8UM"  # NOQA
    )

halloween = media.Movie(
    "Halloween",
    halloween_synopsis,
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzk1OGU2NmMtNTdhZC00NjdlLWE5YTMtZTQ0MGExZTQzOGQyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xHuOtLTQ_1I"
    )

the_shining = media.Movie(
    "The Shining",
    the_shining_synopsis,
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5Cb3ik6zP2I"
    )

evangelion = media.Movie(
    "The End of Evangelion",
    evangelion_synopsis,
    "https://images-na.ssl-images-amazon.com/images/I/51XFaesw92L.jpg",  # NOQA
    "https://www.youtube.com/watch?v=IQrXRBh94IA"  # NOQA
    )

# Store all of the movie in an array named "movies"
movies = [
    goodfellas, godfather, silence_of_the_lambs,
    halloween, the_shining, evangelion
]

# Open a static web page and display all the movies
fresh_tomatoes.open_movies_page(movies)
