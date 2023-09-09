import pandas as pd
import os

class FileManager:
    def __init__(self) -> None:
        pass

    def get_file_extension(self, filename):
        fnsplit = filename.split(".")
        ext = fnsplit[len(fnsplit)-1]
        return ext

    def file_to_dataframe(self, filepath:str) -> pd.DataFrame:
        ext = self.get_file_extension(filepath)

        if ext == "json":
            df = pd.read_json(filepath)

        if ext == "csv":
            df = pd.read_csv(filepath)
        
        if ext == "xml":
            df = pd.read_xml(filepath)
        
        return df
    
    def dataframe_to_csv(self, df, dir, filename):
        if not os.path.exists(dir):
            os.mkdir(dir)

        fullname = os.path.join(dir, filename)    
        df.to_csv(fullname)
        print(f"Wrote DataFrame to {dir}/{filename}")
        return