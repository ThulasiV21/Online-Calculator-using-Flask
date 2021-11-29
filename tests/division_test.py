"""Testing Division"""
import pytest
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    mynumbers = (1.0,2.0,4.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.125

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    mynumbers = (1.0, 0.0, 1.0)
    division = Division(mynumbers)
    # Act
    # Assert
    with pytest.raises(ZeroDivisionError):
        #import pdb;pdb.set_trace()
        result = division.get_result()
        assert result is True
