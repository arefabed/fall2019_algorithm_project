import pandas as pd

df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Year']),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=['Year']),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=['Year'])]
udf = pd.concat(df)
c = {2005: 0, 2006: 0, 2007: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}