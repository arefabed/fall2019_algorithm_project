import pandas as pd
from tqdm import tqdm

print('reading files...')

df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Police_Force', 'Day_of_Week']),
      pd.read_csv('data/accidents_2009_to_2011.csv',
                  usecols=['Police_Force', 'Day_of_Week']),
      pd.read_csv('data/accidents_2012_to_2014.csv',
                  usecols=['Police_Force', 'Day_of_Week'])]

df = fd[0]

for row_index in df.index:
    row = df.iloc[row_index,:]
    print(row)
    break