"""Testing Division"""
import pytest
from calc.calculations.division import Division
from calc.utils.file_reader import PandasFileReader

def test_calculation_division(division_file_fixture):
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    for index, row in division_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        division = Division.create(tuple_values)
        try:
    #Assert
            assert division.get_result() == division_file_fixture['result'][index].round(decimals=5)
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert division.get_result() is True
