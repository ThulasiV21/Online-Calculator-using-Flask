"""Testing the calculation class"""

from calc.calculations.calculation import Calculation
from calc.utils.file_reader import PandasFileReader

def test_convert_args_to_list_float(subtraction_test_file_fixture):
    """Testing the method of super class"""
    #Arrange
    numbers_tuple = subtraction_test_file_fixture.value_1[0], \
                    subtraction_test_file_fixture.value_2[0], \
                    subtraction_test_file_fixture.value_1[1], \
                    subtraction_test_file_fixture.value_2[1]
    #Act
    numbers_tuple_list = Calculation.convert_args_to_list_float(numbers_tuple)
    #Assert
    assert numbers_tuple_list == [2.0,1.0,4.0,2.0]

def test_get_result():
    """Testing the overridden method of super class + abstract class and method"""
    assert Calculation.get_result(self=None) is True
