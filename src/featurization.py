import yaml
from utils.filemanager_util import FileManager
from utils.featurization_util import Featurization_Util


#Load up the raw_data as a DataFrame
fm = FileManager()
params = yaml.safe_load(open("params.yaml"))["featurization"]
processed_data = fm.file_to_dataframe(params["processed_file"])

f_util = Featurization_Util(processed_data)
f_util.check_nlp_library()
f_util.featurize_data()

fm.dataframe_to_csv(f_util.data, "data/featured", "featurized_data.csv")


