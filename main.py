import media
import fresh_tomatoes

# Movie info
# Instance variable reference
# -- (self, title, poster, plot, imdb, movie_year, movie_trailer)
spaceballs = media.Movie(
    "Space Balls",
    """
    https://images-na.ssl-images-amazon.com/images/M/MV5BMjVjOGQ0OTctNDhkZC00ZGNiLWI2ZGEtYjZlMWZjOTlkNDlhXkEyXkFqcGdeQXVyNjg1MjEwOTM@._V1_UX182_CR0,0,182,268_AL_.jpg
    """,
    """
    Planet Spaceballs' President Skroob sends Lord Dark Helmet
     to steal planet Druidia's abundant supply of air to replenish their own,
      and only Lone Starr can stop them.
    """,
    "1987",
    "https://www.youtube.com/watch?v=RUnhzwnn_Q0")

supertroopers = media.Movie(
    "Super Troopers",
    """
    https://images-na.ssl-images-amazon.com/images/M/MV5BYzAyOTZjZDItZjNiYy00YTA3LWEyYWMtZTA0NmUzYjZhNjg0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg
    """,
    """
    Five Vermont state troopers, avid pranksters with a knack for screwing up,
     try to save their jobs and out-do the local police department by solving
      a crime.
    """,
    "2001",
    "https://www.youtube.com/watch?v=MPhWl_S8ies")

wargames = media.Movie(
    "Wargames",
    """
    https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyMTE3OTk3NF5BMl5BanBnXkFtZTcwOTkwNDc3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg
    """,
    """
    A young man finds a back door into a military central computer in
     which reality is confused with game-playing,
      possibly starting World War III.
    """,
    "1983",
    "https://www.youtube.com/watch?v=hbqMuvnx5MU")

# TV show info
# Instance variable reference
# -- (self, title, poster, plot, imdb, pilot_trailer, total_seasons, is_live)
futurama = media.TVshow(
    "Futurama",
    """
    https://images-na.ssl-images-amazon.com/images/M/MV5BNzA2ZDk2ZTUtMWU2Yi00NDVmLTk1ODEtMmFmMjQyNWYzODI0XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg
    """,
    """
    Fry, a pizza guy, is accidentally frozen
     in 1999 and thawed out New Year's Eve 2999.
    """,
    "https://www.youtube.com/watch?v=0rY0HJT_CvM",
    "7",
    "Not in production.")

silicon_valley = media.TVshow(
    "Silcon Valley",
    """
    https://images-na.ssl-images-amazon.com/images/M/MV5BOTA4MTE3MTQwMF5BMl5BanBnXkFtZTgwNzk4MTg4MTI@._V1_UX182_CR0,0,182,268_AL_.jpg
    """,
    """
    Follows the struggle of Richard Hendricks,
     a silicon valley engineer trying to build
      his own company called Pied Piper.
    """,
    "https://www.youtube.com/watch?v=69V__a49xtw",
    "4",
    "In Production")

doctor_who = media.TVshow(
    "Doctor Who",
    """
    https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0OTc0YzMtMTdjNS00MGU3LThlZWItYmU4MjliZmQ0OTkzXkEyXkFqcGdeQXVyMjc5OTMxMzQ@._V1_UY268_CR10,0,182,268_AL_.jpg
    """,
    """
    The further adventures of the time-traveling
     alien adventurer and his companions.
    """,
    "https://www.youtube.com/watch?v=Gdi50ZJnE9Y",
    "10",
    "In Production")

movies = [spaceballs, supertroopers, wargames]
tvshows = [futurama, silicon_valley, doctor_who]
fresh_tomatoes.open_page(movies, tvshows)
