"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
#from tests.calculator_result_test import clear_history_fixture_test
from calc.utils.file_reader import PandasFileReader

def test_calculator_add_static(clear_history_fixture, addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    #Arrange
    tuple_values = addition_file_fixture.value_1[5], addition_file_fixture.value_2[5]
    #Act
    Calculator.addition(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == addition_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_subtract_static(clear_history_fixture, subtraction_file_fixture):
    """Testing the subtract method of the calc"""
    #Arrange
    tuple_values = subtraction_file_fixture.value_1[5], subtraction_file_fixture.value_2[5]
    #Act
    Calculator.subtraction(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == subtraction_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_multiply_static(clear_history_fixture, multiplication_file_fixture):
    """Testing the multiplication method of the calc"""
    #Arrange
    tuple_values = multiplication_file_fixture.value_1[5], multiplication_file_fixture.value_2[5]
    #Act
    Calculator.multiplication(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == multiplication_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_divide_static(clear_history_fixture, division_file_fixture):
    """Testing the division method of the calc"""
    #Arrange
    tuple_values = division_file_fixture.value_1[5], division_file_fixture.value_2[5]
    #Act
    Calculator.division(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == division_file_fixture['result'][5].round(decimals=5) \
           and clear_history_fixture is True

def test_calculator_divide_exception_static(clear_history_fixture, division_file_fixture):
    """Testing the division method of the calc for the exception"""
    #Arrange
    tuple_values = division_file_fixture.value_1[2], division_file_fixture.value_2[0]
    #Act
    Calculator.division(tuple_values)
    #Assert
    with pytest.raises(ZeroDivisionError):
        assert Calculator.get_last_calculation_from_result() is True \
               and clear_history_fixture is True
