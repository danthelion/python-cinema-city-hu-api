import requests
# import json


# import pyccapi.pyccapi_constants as pymc


class Movie:
    """Class representing one movie."""

    def __init__(self, movie_id):
        """Initialize basic data for movie."""
        self.base_data = self.get_base_data()
        self.id = movie_id
        self.title = self.get_movie_title(self.base_data)
        self.movie_showings = self.get_movie_showings(self.base_data)

    def get_base_data(self, c_id):
        """Get weekly movie data in JSON for every cinema."""
        r = requests.get('http://www.cinemacity.hu/presentationsJSON')
        return r.json()

    def get_movie_title(base_data):
        """Get movie title from base_data."""
        pass

    def get_movie_showings(base_data):
        """Nested dictionary {title: {venue: [time1, time2]}}."""
        pass
