def kind_of_vehicle_per_year():
    import pandas as pd
    from tqdm import tqdm

    print('reading files...')

    df = pd.read_csv('data/ukTrafficAADF.csv',
                        usecols=['AADFYear',
                                'PedalCycles', 'Motorcycles',
                                'CarsTaxis', 'BusesCoaches',
                                'LightGoodsVehicles', 'V2AxleRigidHGV'])

    print('computing...')
    c = {}
    vehicle = {'PedalCycles': 0, 'Motorcycles': 0,
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
