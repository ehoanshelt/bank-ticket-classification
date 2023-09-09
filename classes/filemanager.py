import pandas as pd

class FileManager:
    def __init__(self) -> None:
        pass

    def file_to_dataframe(filepath:str, inputtype:str) -> pd.DataFrame:
        if inputtype == "json":
            df = pd.read_json(filepath)
        
        return df