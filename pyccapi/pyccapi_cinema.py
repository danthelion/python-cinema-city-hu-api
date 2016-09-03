import requests
import json
import time


import pyccapi.pyccapi_constants as pymc


class Cinema:
    """Class reperesenting one cinema and its relevant data."""

    def __init__(self, cinema_name):
        """Initialize basic data for cinema."""
        self.id = pymc.CINEMA_CODES[cinema_name]
        self.base_data = self.get_base_data(self.id)
        self.schedule_week = self.get_schedule_week(self.base_data)
        self.schedule_today = self.get_schedule_day(self.base_data)

    def get_base_data(self, c_id):
        """Get weekly movie data in JSON."""
        payload = {'subSiteId': c_id}
        r = requests.get(
            'http://www.cinemacity.hu/presentationsJSON', params=payload)
        return r.json()

    def get_schedule_week(self, base_data):
        """Get weekly movie data in JSON."""
        json_res = base_data
        weekly_schedule = {}
        for movie in json_res['sites'][0]['fe']:
            movie_title = movie['fn']
            daily_showings = {}

            showing_day_list = []
            showint_time_list = []

            for movie_data in movie['pr']:
                showing_day = movie_data['dt'].split(' ')[0]
                showing_time = movie_data['tm']

                showing_day_list.append(showing_day)
                showint_time_list.append(showing_time)

            for day, dtime in zip(showing_day_list, showint_time_list):
                daily_showings.setdefault(day, []).append(dtime)

            weekly_schedule[movie_title] = daily_showings
        return weekly_schedule

    def get_schedule_day(self, date=time.strftime('%Y/%m/%d')):
        """Get daily movie data in JSON."""
        weekly_schedule = self.base_data
        day_schedule = {}
        for ix, movie in enumerate(weekly_schedule['sites'][0]['fe']):
            movie_title = movie['fn']
            showing_times = []
            for showing in weekly_schedule['sites'][0]['fe'][ix]['pr']:
                row_date = showing['dt'].split(' ')[0]
                if row_date == date:
                    showing_times.append(showing['tm'])
            day_schedule[movie_title] = sorted(showing_times) or None
        return json.loads(json.dumps(day_schedule, ensure_ascii=False))
