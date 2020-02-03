def summarize():
    import pandas as pd

    cols = ['Road_Type']

    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=cols),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=cols),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=cols)]
    udf = pd.concat(df)['Road_Type']

    descriptor = {}
    for item in udf:
        if(item in descriptor):
            descriptor[item] += 1
        else:
            descriptor[item] = 0

    return descriptor
  