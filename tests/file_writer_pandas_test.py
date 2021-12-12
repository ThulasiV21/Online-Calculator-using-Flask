"""Testing pandas file writer class"""
import pytest
from calc.utils.file_writer import FileWriter

def test_pandas_file_write_to_csv_check():
    """Testing df creation as csv file by taking user input"""
    #Arrange
    values = (1, 1, 'Addition')
    #Act
    df_csv_data = FileWriter(values).write_to_file()
    #Assert
    assert df_csv_data is not None
