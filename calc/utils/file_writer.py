"""Writes input from user to a csv file"""

import os
import pandas as pd

class FileWriter:
    """File writer to csv class"""
    def __init__(self, user_input):
        self._user_input = user_input

    @property
    def input_value1(self):
        return self._user_input

    def write_to_file(self):
        """Method to write users input data to csv file"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../../calc/utils", "input.csv")
        print(file_path)
        df_data = pd.DataFrame([self._user_input], columns=['value1', 'value2', 'operation'])
        df_csv_data = df_data.to_csv(file_path, index=False, sep=',')
        return df_csv_data
