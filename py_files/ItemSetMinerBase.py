from tqdm import tqdm
import pandas as pd
import numpy as np


class ItemSetMinerBase:

    def __init__(self):

        self.data = None
        self.enumeration_dic = {}
        self.itemset_dic = {}

    def read_data(self, fields) -> None:
        print('reading files...')

        df = [pd.read_csv('data/accidents_2005_to_2007.csv',
                          usecols=fields, nrows=30000)]  # ,
        #   pd.read_csv('data/accidents_2009_to_2011.csv',
        #               usecols=fields),
        #   pd.read_csv('data/accidents_2012_to_2014.csv',
        #               usecols=fields)]

        self.data = pd.concat(df)

    def generate_enumeration_dic(self):
        print('generating transaction dictionary...')

        uniques = 0
        for i in tqdm(self.data.index):
            if self.data.iloc[i, 1] not in self.enumeration_dic:
                self.enumeration_dic[self.data.iloc[i, 1]] = uniques
                self.data.iloc[i, 1] = uniques
                uniques += 1
            else:
                self.data.iloc[i,
                               1] = self.enumeration_dic[self.data.iloc[i, 1]]
            if self.data.iloc[i, 0] not in self.itemset_dic:
                self.itemset_dic[self.data.iloc[i, 0]] = {}
                self.itemset_dic[self.data.iloc[i, 0]
                                 ][self.data.iloc[i, 1]] = 1
            elif self.data.iloc[i, 1] not in self.itemset_dic[self.data.iloc[i, 0]]:
                self.itemset_dic[self.data.iloc[i, 0]
                                 ][self.data.iloc[i, 1]] = 1
            self.itemset_dic[self.data.iloc[i, 0]][self.data.iloc[i, 1]] += 1

    def threshold(self, theta):
        self.itemset_dic = {ukey: {key: value for key, value in uvalue.items() if value >= theta}
                            for ukey, uvalue in self.itemset_dic.items()}

    def binarize(self):
        self.itemset_dic = {ukey: [key for key in uvalue.keys()]
                            for ukey, uvalue in self.itemset_dic.items()}

    def summarize(self):
        temp = np.concatenate([list(val for val in uvalue.values())
                               for uvalue in self.itemset_dic.values()])
        q0 = np.min(temp)
        print('Q0: ', q0)
        q1 = np.quantile(temp, .25)
        print('Q1: ', q1)
        q2 = np.median(temp)
        print('Q2: ', q2)
        q3 = np.quantile(temp, .75)
        print('Q3: ', q3)
        q4 = np.max(temp)
        print('Q4: ', q4)
        mean = np.mean(temp)
        print('mean: ', mean)
        return q0, q1, q2, q3, q4, mean

# Data Mining and Analysis:Fundamental Concepts and Algorithms Mohammed J. Zaki Wagner Meira Jr.

    def _dEclat(self, p: (int, list, int), minsup: int, f: list):
        self.declat_depth += 1
        if(self.declat_depth > 1000):
            raise BufferError("too many layers")
        for i, di, si in p:
            self.frequent_itemsets.append((set(i), si))
            p0 = []
            for j, dj, sj in p:
                if(j <= i):
                    continue
                ij = i+j
                dij = [item for item in dj if item not in di]
                sij = si - len(dij)
                if(sij > minsup):
                    p0.append((ij, dij, sij))
            if p0:
                self._dEclat(p0, minsup, self.frequent_itemsets)

    def dEclat(self, minsup):
        self.declat_depth = 0
        self.frequent_itemsets = []
        uniques = list(range(len(self.enumeration_dic.keys())))
        p = [([key], [item for item in uniques if item not in value], len(value))
             for key, value in self.itemset_dic.items() if len(value) > minsup]
        self._dEclat(p, minsup, self.frequent_itemsets)
        del self.declat_depth
        print(self.frequent_itemsets)

    def association_rules():
        pass
