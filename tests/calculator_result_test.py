"""Testing the Calculator"""

from calc.history.calculator_result import CalculatorResult

def test_add_calculation_to_history(clear_history_fixture, setup_history_test_fixture):
    """Testing clear history returns true for success after adding the calculation to the list"""
    #Assert
    #import pdb;pdb.set_trace()
    assert CalculatorResult.count_history() == 4
    # assert clear_history_fixture is True
    # assert setup_addition_calculation_fixture is True

def test_clear_calculation_history(clear_history_fixture, setup_history_test_fixture):
    """Testing clear history returns true for success after clearing the history list"""
    #Assert
    assert CalculatorResult.count_history() == 4
    CalculatorResult.clear_history()
    assert CalculatorResult.count_history() == 0
    assert CalculatorResult.clear_history() is True
    # assert clear_history_fixture is True
    # assert setup_addition_calculation_fixture is True

def test_get_calculation(clear_history_fixture, setup_history_test_fixture):
    """Testing getting a specific calculation out of the history"""
    #Assert
    assert CalculatorResult.get_calculation_from_history(0).get_result() == 3.0
    assert CalculatorResult.get_calculation_from_history(1).get_result() == -2.0
    assert CalculatorResult.get_calculation_from_history(2).get_result() == 12.0
    assert CalculatorResult.get_calculation_from_history(3).get_result() == 0.8
    # assert clear_history_fixture is True
    # assert setup_addition_calculation_fixture is True

def test_get_last_calculation_result(clear_history_fixture, setup_history_test_fixture):
    """Testing getting the last calculation from the history"""
    #Assert
    assert CalculatorResult.get_last_calculation_result() == 0.8
    # assert clear_history_fixture is True
    # assert setup_addition_calculation_fixture is True

def test_get_first_calculation_result(clear_history_fixture, setup_history_test_fixture):
    """Testing getting the first calculation from the history"""
    #Assert
    assert CalculatorResult.get_first_calculation().get_result() == 3.0
    # assert clear_history_fixture is True
    # assert setup_addition_calculation_fixture is True

def test_count_of_history(clear_history_fixture, setup_history_test_fixture):
    """Testing getting the count of calculation from the history"""
    #Assert
    assert CalculatorResult.count_history() == 4
    # assert clear_history_fixture is True
    # assert setup_addition_calculation_fixture is True
