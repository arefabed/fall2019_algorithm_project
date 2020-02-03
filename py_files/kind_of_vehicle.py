def kind_of_vehicle():
    import pandas as pd
    from tqdm import tqdm
    
    print('reading files...')
    
    df = pd.read_csv('data/ukTrafficAADF.csv',
                     usecols=['AADFYear',
                              'PedalCycles', 'Motorcycles',
                              'CarsTaxis', 'BusesCoaches',
                              'LightGoodsVehicles', 'V2AxleRigidHGV'])
    
    print('computing...')
    c = {2000: 0, 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0,
         2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0}
    vehicle = {'PedalCycles': 0, 'Motorcycles': 0,
                'CarsTaxis': 0, 'BusesCoaches': 0,
                'LightGoodsVehicles': 0, 'V2AxleRigidHGV': 0}
    
    for row_ind in tqdm(df.index):
        row = df.iloc[row_ind, :]
        c[row['AADFYear']] = vehicle
        keys = row.to_dict()
        del keys['AADFYear']
        for item in keys:
            c[row['AADFYear']][item] += row[item]
    return c
