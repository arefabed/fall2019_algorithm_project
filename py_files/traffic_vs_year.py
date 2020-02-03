def traffic_vs_year():
    import pandas as pd
    from tqdm import tqdm
    
    print('reading files...')
    
    df = pd.read_csv('data/ukTrafficAADF.csv',
                     usecols=['AADFYear', 'LinkLength_km',
                              'PedalCycles', 'Motorcycles',
                              'CarsTaxis', 'BusesCoaches',
                              'LightGoodsVehicles', 'V2AxleRigidHGV'])

    print('computing...')
    
    c = {2005: 0, 2006: 0, 2007: 0,2008:0, 2009: 0,
         2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}

    for row_ind in tqdm(df.index):
        row = df.iloc[row_ind, :]
        if row['AADFYear'] < 2005 or row['AADFYear'] > 2014:
            continue
        c[row['AADFYear']] += ((1 / 35) * row['PedalCycles'] + (2 / 35) * row['Motorcycles'] + (4 / 35) * row[
            'CarsTaxis'] + (8 / 35) * row['BusesCoaches'] + (8 / 35) * row['LightGoodsVehicles'] + (12 / 35) * row[
                                   'V2AxleRigidHGV']) / row['LinkLength_km']
    return c



