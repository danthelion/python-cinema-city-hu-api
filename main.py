import os
import pyccapi.pyccapi_cinema as pyccc
# import pyccapi.pyccapi_movie as pyccm

# import pandas as pd
import pprint as pp


def main():
    """Main business logic."""
    # os.system('chcp 65001') # Change console character encoding
    cinema = pyccc.Cinema('Duna Plaza')

    # CINEMA SHOWCASE BLOCK

    # Weekly schedule of cinema - every movie
    # weekly_schedule = cinema.schedule_week

    # Today schedule of cinema - every movie
    # today_schedule = cinema.schedule_today

    # Print todays schedule
    # pp.pprint(today_schedule)

    # Print weekly schedule
    # pp.pprint(weekly_schedule)

    # Print daily schedule for any date (from today to one week from today interval, default: today)
    # pp.pprint(cinema.get_schedule_day('2016/09/07'))
    # pp.pprint(cinema.get_schedule_day())

    # Get movie showtimes from weekly schedule
    # pp.pprint(weekly_schedule['Szemfényvesztők 2 (12)'])

    # Get movie showtimes from daily schedule
    # print(cinema.get_schedule_day('2016/09/01')['Szemfényvesztők 2 (12)'])

    # Pandas DataFrame input style and xlsx export test.
    # df = pd.DataFrame.from_dict(weekly_schedule, orient='index')
    # df.to_excel('a.xlsx')
    # print(df)

    # Movies avaliable this week
    movies_week = cinema.all_movies_week
    print(movies_week)

    # Movies avaliable today
    # movies_today = cinema.all_movies_today
    # print(movies_today)

    # Movies avaliable at set date
    # movies_day = cinema.get_all_movies_day('2016/09/05')
    # print(movies_day)

    # MOVIE SHOWCASE BLOCK


if __name__ == '__main__':
    main()
