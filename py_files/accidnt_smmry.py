def summarize():
    import pandas as pd

    cols = ['Accident_Index', 'Police_Force',
            'Accident_Severity', 'Number_of_Vehicles',
            'Number_of_Casualties', 'Day_of_Week',
            'Speed_limit', 'Year']

    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=cols),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=cols),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=cols)]
    udf = pd.concat(df)

    return udf.describe()
