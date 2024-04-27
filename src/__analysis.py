from __format import FormatModule
import numpy as np
import pandas as pd





class Univariate(FormatModule):
    def __init__(self) ->None:
        self.format_obj = FormatModule()
        self.format_obj.main()
        self.format_obj.merge()
        self.dataframe = self.format_obj.df
    
    def __free(self) -> None:
        self.format_obj = None
    
    
    def main(self):
        self.__free()
    
if __name__ == '__main__':
    analysis = Univariate()
    print(analysis.dataframe)
    
    


