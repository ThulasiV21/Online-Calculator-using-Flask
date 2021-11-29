"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    return Calculations.clear_history()
    # You have to add the fixture function as a parameter to the test that you want to use it with

def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    #Arrange
    tuple_values = (1.0, 2.0, 3.0)
    #Act
    Calculator.__add__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == 6.0 and clear_history_fixture is True

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    #Arrange
    tuple_values = (1.0, 2.0, 3.0)
    #Act
    Calculator.__sub__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == -4.0 and clear_history_fixture is True

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication method of the calc"""
    #Arrange
    tuple_values = (1.0, 2.0, 1.5)
    #Act
    Calculator.__mul__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == 3.0 and clear_history_fixture is True

def test_calculator_divide_static(clear_history_fixture):
    """Testing the division method of the calc"""
    #Arrange
    tuple_values = (1.0, 2.0, 4.5)
    #Act
    Calculator.__truediv__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == 0.11111 \
           and clear_history_fixture is True

def test_calculator_divide_exception_static(clear_history_fixture):
    """Testing the division method of the calc"""
    #Arrange
    tuple_values = (1.0, 0.0, 4.5)
    #Act
    Calculator.__truediv__(tuple_values)
    #Assert
    with pytest.raises(ZeroDivisionError):
        assert Calculator.get_last_calculation_from_result() is True \
               and clear_history_fixture is True
