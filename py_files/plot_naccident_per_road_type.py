def naccident_per_road_type():
    import pandas as pd
    from tqdm import tqdm

    print('reading files...')

    df = pd.read_csv('data/ukTrafficAADF.csv',
                     usecols=['AADFYear', 'LinkLength_km',
                              'PedalCycles', 'Motorcycles',
                              'CarsTaxis', 'BusesCoaches',
                              'LightGoodsVehicles', 'V2AxleRigidHGV'])

    print('computing...')

    c = {2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0,
         2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}