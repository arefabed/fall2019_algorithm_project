def naccidents_vs_dates():
    import pandas as pd
    import datetime as dt

    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Date']),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=['Date']),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=['Date'])]

    c = {2005: 0, 2006: 0, 2007: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}
    for data in df:
        temp = data["Date"]
        for i in temp:
            date_time_obj = dt.datetime.strptime(i, '%d/%m/%Y')
            c[date_time_obj.year] += 1
    return c