def naccident_per_road_type():
    import pandas as pd
    from tqdm import tqdm

    print('reading files...')

    df = [pd.read_csv('data/accidents_2005_to_2007.csv', usecols=['Year', 'Road_Type']),
          pd.read_csv('data/accidents_2009_to_2011.csv', usecols=['Year', 'Road_Type']),
          pd.read_csv('data/accidents_2012_to_2014.csv', usecols=['Year', 'Road_Type'])]

    print('computing...')

    c = {}
    road_type = {'Single carriageway': 0, 'Dual carriageway': 0,
                 'One way street': 0, 'Roundabout': 0,
                 'Slip road': 0, 'Unknown': 0}
    for item in df:
        for row_ind in tqdm(item.index):
            row = item.iloc[row_ind, :]
            keys = row.to_dict()
            if row['Year'] not in c:
                c[row['Year']] = dict(road_type)
            c[row['Year']][row['Road_Type']] += 1

    return c


if __name__ == '__main__':
    naccident_per_road_type()
