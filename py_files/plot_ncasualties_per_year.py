def ncasualties_per_year():
    import pandas as pd
    from tqdm import tqdm

    print('reading files...')

    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Year', 'Number_of_Casualties']),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=['Year', 'Number_of_Casualties']),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=['Year', 'Number_of_Casualties'])]

    print('computing...')

    c = {2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0,
         2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}
    for item in df:
        for row_ind in tqdm(item.index):
           row = item.iloc[row_ind, :]
           c[row['Year']] += row['Number_of_Casualties']
    return c
