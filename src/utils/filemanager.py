import pandas as pd
import os

class FileManager:
    def __init__(self) -> None:
        pass

    def file_to_dataframe(self, filepath:str, inputtype:str = "json") -> pd.DataFrame:
        if inputtype == "json":
            df = pd.read_json(filepath)
        
        return df
    
    def dataframe_to_csv(self, df, dir, filename):
        if not os.path.exists(dir):
            os.mkdir(dir)

        fullname = os.path.join(dir, filename)    
        df.to_csv(fullname)
        print(f"Wrote DataFrame to {dir}/{filename}")
        return