"""Testing pandas file reader class"""
import pytest
from calc.utils.file_reader import PandasFileReader

def test_pandas_read_file():
    """Testing the file type check"""

def test_pandas_file_type_csv_check():
    """Testing df creation after extracting data from csv file"""
    #Arrange
    file_name = "addition_1000values.csv"
    #Act
    df_test_csv_data = PandasFileReader(file_name, "../../tests/input_csv_files").read_file()
    #Assert
    assert df_test_csv_data is not None

def test_pandas_file_type_xlsx_check():
    """Testing df creation after extracting data from excel file"""
    #Arrange
    file_name = "addition_1000values.xlsx"
    #Act
    df_test_xlsx_data = PandasFileReader(file_name, "../../tests/input_csv_files").read_file()
    #Assert
    assert df_test_xlsx_data is not None

def test_pandas_file_type_txt_check():
    """Testing the other file type check"""
    #Arrange
    file_name = "sample_test_data.txt"
    #Act
    with pytest.raises(ValueError):
        #Assert
        assert PandasFileReader(file_name, "../../tests/input_csv_files").read_file() is True
