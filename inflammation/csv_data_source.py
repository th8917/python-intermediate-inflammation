import models
import os 
import glob

class CSVDataSource:
    """
    Loads all the inflammation csvs within a specified folder 
    """
    def __init__(self,data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {self.data_dir}")
        data = map(models.load_csv, data_file_paths)
        return list(data)