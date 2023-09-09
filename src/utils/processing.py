import sys
import numpy as np
import pandas as pd

class Process_DataFrame:
    def __init__(self, df: pd.DataFrame, expected_column:str = "_source") -> None:
        if expected_column in df:
            self.data = df
        else:
            print(f"DataFrame needs to include the {expected_column} column. No column found")
            sys.exit()

    # We're expecting all the data we need to be in a _source column in the dataset.
    # We don't need any of the other data
    def strip_source(self, column:str = "_source", expected_column:str = "complaint_what_happened") -> bool:
        
        print("Striping source data in progress")
        list = self.data.unstack()
        self.data = pd.DataFrame(list[column].values.tolist())
        print("Striping source data completed")

        if expected_column in self.data:
            return True
        else:
            print("We're expecting {expected_column} to be present in the {column}. {expected_column} is not found")
            sys.exit() 
    
    def remove_nulls(self, verbose:bool = True) -> bool:
        if verbose:
            print(f"Shape of Dataframe before nulls removed is {self.data.shape}")
        
        self.data["complaint_what_happened"] = self.data["complaint_what_happened"].replace('', np.nan, regex = True)

        print("Removed blanks successfully!")
        
        self.data = self.data[~self.data["complaint_what_happened"].isnull()]

        if verbose:
            print(f"Shape of Dataframe after nulls removed is {self.data.shape}")

        return True
    
    def process(self, verbose:bool = False):
        self.strip_source()
        self.remove_nulls(verbose=verbose)
