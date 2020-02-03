def summarize():
    import pandas as pd

    cols = ['AADFYear', 'LinkLength_km', 'PedalCycles',
            'Motorcycles', 'CarsTaxis', 'BusesCoaches',
            'LightGoodsVehicles', 'V2AxleRigidHGV',
            'V3AxleRigidHGV', 'V4or5AxleRigidHGV',
            'V3or4AxleArticHGV', 'V5AxleArticHGV',
            'V6orMoreAxleArticHGV', 'AllHGVs', 'AllMotorVehicles']

    df = pd.read_csv('data/ukTrafficAADF.csv', usecols=cols)

    return df.describe()
