import requests
import json
import pyccapi.pyccapi_constants as pymc


class Movie:
    """Class representing one movie."""

    def __init__(self, movie_id):
        """Initialize basic data for movie."""
        self.id = movie_id
        self.title = self.get_movie_title(self.id)
        self.show_dates = self.get_show_dates(self.id)

    def get_movie_title(movie_id):
        """Get movie title from ID."""
        pass
