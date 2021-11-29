"""Testing Addition"""
import pandas as pd
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    numbers = (1.0,2.0,3.0,4.0)
    #Act
    addition = Addition.create(numbers)
    #Assert
    assert addition.get_result() == 10.0
