import yaml
from utils.filemanager import FileManager
from utils.processing import Process_DataFrame


#Load up the raw_data as a DataFrame
fm = FileManager()
params = yaml.safe_load(open("params.yaml"))["process"]
raw_data = fm.file_to_dataframe(params["raw_file"])

#Process raw Data
pro_df = Process_DataFrame(raw_data)
pro_df.process(verbose=True)
fm.dataframe_to_csv(pro_df.data, "data/processed", "process.csv")

