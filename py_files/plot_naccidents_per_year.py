def naccidents_per_year():
    import pandas as pd
    from tqdm import tqdm

    print('reading files...')
    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Year']),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=['Year']),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=['Year'])]
    print('computing...')
    c = {2005: 0, 2006: 0, 2007: 0, 2009: 0,
         2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}
    for data in df:
        temp = data["Year"]
        for i in tqdm(temp):
            c[i] += 1
    return c
