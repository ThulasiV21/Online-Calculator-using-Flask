"""Testing Division"""
import pytest
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    numbers = (1.0,2.0,4.0)
    # Act
    division = Division.create(numbers)
    #Assert
    assert division.get_result() == 0.125

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    numbers = (1.0, 0.0, 1.0)
    # Act
    division = Division.create(numbers)
    # Assert
    with pytest.raises(ZeroDivisionError):
        assert division.get_result() is True
