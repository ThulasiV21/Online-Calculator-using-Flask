"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    numbers = (10.0,5.0,2.5)
    # Act
    subtraction = Subtraction.create(numbers)
    #Assert
    assert subtraction.get_result() == 2.5
