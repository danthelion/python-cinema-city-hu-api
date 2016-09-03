import os
import pyccapi.pyccapi_cinema as pyccc
# import pyccapi.pyccapi_movie as pyccm

# import pandas as pd
import pprint as pp


def main():
    """Main business logic."""
    # os.system('chcp 65001') # Change console character encoding
    cinema = pyccc.Cinema('WestEnd')

    weekly_schedule = cinema.schedule_week
    today_schedule = cinema.schedule_today

    # pp.pprint(today_schedule)
    # pp.pprint(weekly_schedule)
    # pp.pprint(cinema.get_schedule_day('2016/09/07'))
    pp.pprint(cinema.get_schedule_day())
    # pp.pprint(today_schedule['Szemfényvesztők 2 (12)'])
    # print(cinema.get_schedule_day('2016/09/01')['Szemfényvesztők 2 (12)'])

    # df = pd.DataFrame.from_dict(weekly_schedule, orient='index')
    # df.to_excel('a.xlsx')
    # print(df)

if __name__ == '__main__':
    main()
