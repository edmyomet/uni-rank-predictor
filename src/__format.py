import numpy as np
import pandas as pd

def get_dataset(filepath:str) -> pd.core.frame.DataFrame:
    return pd.read_csv(filepath)

def add_column(dataset:pd.core.frame.DataFrame, values:list,type:str='Year') -> pd.core.frame.DataFrame:
    if type == 'Year':
        dataset['Year'] = values
        return dataset

class FormatModule:
    def __init__(self) -> None:
        self.year_list: list[int] = [2016,2017,2018,2019,2020,2021]     
        self.rank_list = [] * 6
        self.df = None
           
    def __init_rank_list(self) -> None:
        for year in self.year_list:
            self.rank_list.append(get_dataset(filepath=rf'datasets\EngineeringRanking_{year}.csv'))
    
    def __add_year_details(self) -> None:
        for index in range(6):
            df = self.rank_list[index]
            year = self.year_list[index]
            
            df = add_column(df, [year]*df.shape[0])
    
    def __merge_save(self) -> pd.core.frame.DataFrame:
        self.df = pd.concat(self.rank_list, ignore_index=True)
        #self.df.to_csv(r'datasets\merged.csv')
        return self.df
        
    def merge(self):
        self.df = self.__merge_save()
    def main(self):
        self.__init_rank_list()
        self.__add_year_details()
        #self.__merge_save()
        

if __name__ == '__main__':
    fm = FormatModule()
    fm.main()
    fm.df = fm.merge()