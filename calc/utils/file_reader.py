"""read file type of external file"""
import os
import pandas as pd

class PandasFileReader:
    """File reader class"""
    def __init__(self, file_name, file_path=""):
        self._file_name = file_name
        self._file_path = file_path

    @property
    def file_name(self):
        return self._file_name

    def read_file(self):
        """Method to read the file type"""
        function_handler = None
        if ".csv" in self.file_name:
            function_handler = self._process_csv_file
        elif ".xlsx" in self.file_name:
            function_handler = self._process_xlsx_file
        else:
            raise ValueError("Unknown File Type")
        return function_handler()

    def _process_xlsx_file(self):
        """Method to process data from excel file to df"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../../tests/input_excel_files", self.file_name)
        df_data = pd.read_excel(io=file_path, index_col=None, names=["value_1", "value_2", "result"], dtype='float')
        return df_data

    def _process_csv_file(self, header=None):
        """Method to process data from csv file to df"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, self._file_path, self.file_name)
        df_data = pd.read_csv(file_path , header=header, names=["value_1", "value_2", "result"])
        return df_data
