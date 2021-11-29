"""Testing the calculation class"""

from calc.calculations.calculation import Calculation

def test_convert_args_to_list_float():
    """Testing the overridden method of super class"""
    #Arrange
    values = 1,2,3,4
    #Act
    numbers_tuple = Calculation.convert_args_to_list_float(values)
    #Assert
    assert numbers_tuple == [1.0,2.0,3.0,4.0]

def test_get_result():
    """Testing the overridden method of super class + abstract class and method"""
    assert Calculation.get_result(self=None) is True
