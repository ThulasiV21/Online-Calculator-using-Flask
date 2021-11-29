"""Testing the Calculator"""
import pprint
import pytest
from calculator.calculator import Calculator


#clear_history_test = None

# This is how you define a function that will run
# each time you pass it to a test, it is called a fixture
@pytest.fixture(name="clear_history_test")
def fixtures_clear_history_test():
    """Clearing the history array"""
    return Calculator.clear_history()

def test_calculator_add(clear_history_test):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.count_history() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    assert clear_history_test is True
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history_test):
    """Testing the clear function of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.count_history() == 4
    assert Calculator.clear_history() is True
    assert Calculator.count_history() == 0
    assert clear_history_test is True

def test_count_history(clear_history_test):
    """Testing the count function of the calculator"""
    assert Calculator.count_history() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.count_history() == 2
    assert clear_history_test is True

def test_get_last_calculation_result(clear_history_test):
    """Testing the get last result function of the calculator"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5
    assert clear_history_test is True

def test_get_first_calculation_result(clear_history_test):
    """Testing the get first claculation function of the calculator"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4
    assert clear_history_test is True

def test_calculator_subtract(clear_history_test):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1
    assert clear_history_test is True

def test_calculator_multiply(clear_history_test):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2
    assert clear_history_test is True

def test_calculator_division(clear_history_test):
    """ Testing division of two numbers"""
    assert Calculator.divide_numbers(1,1) == 1
    assert Calculator.divide_numbers(2,1) == 2
    assert Calculator.divide_numbers(3,1) == 3
    assert clear_history_test is True

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(1,0)
