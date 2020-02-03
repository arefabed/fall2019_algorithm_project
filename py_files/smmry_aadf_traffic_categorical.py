def summarize():
    import pandas as pd

    cols = ['Estimation_method', 'Estimation_method_detailed']

    df = pd.read_csv('data/ukTrafficAADF.csv',usecols=cols)
    descriptor = {}
    for name in cols:
        descriptor[name] = {}
        for item in df[name]:
            if(item in descriptor[name]):
                descriptor[name][item] += 1
            else:
                descriptor[name][item] = 0

    return descriptor
