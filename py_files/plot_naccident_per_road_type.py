def naccident_per_road_type():
    import pandas as pd
    from tqdm import tqdm

    print('reading files...')

    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Year', 'Road_Type']),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=['Year', 'Road_Type']),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=['Year', 'Road_Type'])]

    print('computing...')



    c = {}
    road_type = {'Single carriageway': 0, 'Motorcycles': 0,
               'CarsTaxis': 0, 'BusesCoaches': 0,
               'LightGoodsVehicles': 0, 'V2AxleRigidHGV': 0}

    for row_ind in tqdm(df.index):
        row = df.iloc[row_ind, :]
        keys = row.to_dict()
        if row['AADFYear'] not in c:
            c[row['AADFYear']] = dict(vehicle)
        del keys['AADFYear']
        for item in keys:
            c[row['AADFYear']][item] += row[item]

    return c