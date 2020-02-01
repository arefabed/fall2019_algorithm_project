def traffic_vs_year():
    import pandas as pd
    df = pd.read_cvs('../data/ukTrafficAADF.csv',
                     usecols=['AADFYear', 'LinkLength_km',
                              'PedalCycles', 'Motorcycles',
                              'CarsTaxis', 'BusesCoaches',
                              'LightGoodsVehicles', 'V2AxleRigidHGV'])

    c = {2005: 0, 2006: 0, 2007: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}
    # for data in df:
    #     temp = data["Date"]
    #     for i in temp:
    #         date_time_obj = dt.datetime.strptime(i, '%d/%m/%Y')
    #         c[date_time_obj.year] += 1

    for traff in df:
        # vehicule = traff ['AADFYear','LinkLength_km',
        #                        'PedalCycles', 'Motorcycles',
        #                        'CarsTaxis', 'BusesCoaches',
        #                        'LightGoodsVehicles','V2AxleRigidHGV']
        # for i in vehicule:
        #     number_of_vehicle =
        print(traff)
    return c
