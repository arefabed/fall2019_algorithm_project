from tqdm import tqdm
import pandas as pd
import numpy as np

class ItemSetMinerBase:

    def __init__(self):

        self.data = None
        self.fields = None
        self.enumeration_dic = {}
        self.itemset_dic = {}

    def read_data(self, fields) -> None:
        print('reading files...')

        df = [pd.read_csv('data/accidents_2005_to_2007.csv',
                          usecols=fields)]#,
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
                self.data.iloc[i, 1] = self.enumeration_dic[self.data.iloc[i, 1]]
            if self.data.iloc[i, 0] not in self.itemset_dic:
                self.itemset_dic[self.data.iloc[i, 0]] = {}
                self.itemset_dic[self.data.iloc[i, 0]][self.data.iloc[i, 1]] = 1
            elif self.data.iloc[i, 1] not in self.itemset_dic[self.data.iloc[i, 0]]:
                self.itemset_dic[self.data.iloc[i, 0]][self.data.iloc[i, 1]] = 1
            self.itemset_dic[self.data.iloc[i, 0]][self.data.iloc[i, 1]] += 1

    def threshold(self,theta):
        raise NotImplementedError

    def summarize_enumeration():
        raise NotImplementedError