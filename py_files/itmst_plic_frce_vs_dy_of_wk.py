from py_files.itmst_miner_base import ItemSetMinerBase

class NPoliceVsDayOfWeek(ItemSetMinerBase):
    def __init__(self):
        super().__init__()

        self.fields = ['Police_Force', 'Day_of_Week']

        super().read_data(self.fields)
        super().generate_enumeration_dic()
        
    
