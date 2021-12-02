"""Testing Division"""
import logging
import pytest
from calc.calculations.division import Division

logger = logging.getLogger(__name__)

def test_calculation_division(division_file_fixture, file_name=None):
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    for index, row in division_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        division = Division.create(tuple_values)
        try:
    #Assert
            result = division.get_result()
            logger.info("%s  - %s / %s = %s", index, row.value_1, row.value_2, result)
            assert division.get_result() == division_file_fixture['result'][index].round(decimals=5)
        except ZeroDivisionError:
            logger.error("%s %s Divide by zero error" ,index, file_name )
            with pytest.raises(ZeroDivisionError):
                assert division.get_result() is True
