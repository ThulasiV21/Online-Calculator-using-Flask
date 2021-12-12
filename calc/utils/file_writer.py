"""Writes input from user to a csv file"""

import os
import pandas as pd

class FileWriter:
    """File writer to csv class"""
    def __init__(self, user_input, file_name):
        self._user_input = user_input
        self._file_name = file_name


    @property
    def user_input(self):
        return self._user_input

    @property
    def file_name(self):
        return self._file_name

    def write_to_file(self, columns):
        """Method to write users input data to csv file"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../../calc/utils", self.file_name)
        df_data = pd.DataFrame([self.user_input], columns=columns)
        df_data.to_csv(file_path, index=False, sep=',', mode='a', header=False)
        return file_path
