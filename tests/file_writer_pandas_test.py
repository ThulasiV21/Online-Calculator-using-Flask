"""Testing pandas file writer class"""
import pytest
from calc.utils.file_writer import FileWriter

def test_pandas_file_write_to_csv_check():
    """Testing df creation as csv file by taking user input"""
    #Arrange
    values = (1, 1, 'Addition')
    file_name = "input_test.csv"
    #Act
    df_csv_data = FileWriter(values, file_name).write_to_file(columns=None)
    #Assert
    assert df_csv_data is not None
