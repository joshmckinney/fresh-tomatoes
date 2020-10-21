import webbrowser


class Video():
    # Define parent class with shared instance variables
    def __init__(self, title, poster, plot):
        self.title = title
        self.poster = poster
        self.plot = plot

    def play_trailer(self):
        webbrowser.open(self.trailer)


class Movie(Video):
    # Define child class for movies
    def __init__(self, title, poster, plot,
                 movie_year, movie_trailer):
        Video.__init__(self, title, poster, plot)
        self.year = movie_year
        self.trailer = movie_trailer


class TVshow(Video):
    # Define child class for tv shows
    def __init__(self, title, poster, plot,
                 pilot_trailer, total_seasons, is_live):
        Video.__init__(self, title, poster, plot)
        self.trailer = pilot_trailer
        self.seasons = total_seasons
        self.live = is_live
