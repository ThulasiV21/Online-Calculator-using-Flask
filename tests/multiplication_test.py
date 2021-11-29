"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    numbers = (1.0,2.0,3.0)
    # Act
    multiplication = Multiplication.create(numbers)
    #Assert
    assert multiplication.get_result() == 6.0
