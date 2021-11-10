"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator

def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange
    value_a = 1
    value_b = 2
    # Act
    result = Calculator.add_number(value_a,value_b)
    # Assert
    assert result == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    # Arrange
    value_a = 1
    value_b = 2
    # Act
    result = Calculator.subtract_number(value_a, value_b)
    # Assert
    assert result == -1

def test_calculator_multiply():
    """ Testing multiplication of two numbers"""
    # Arrange
    value_a = 1
    value_b = 2
    # Act
    result = Calculator.multiply_numbers(value_a, value_b)
    # Assert
    assert result == 2

def test_calculator_division():
    """ Testing division of two numbers"""
    # Arrange
    value_a = 1
    value_b = 1
    # Act
    result = Calculator.divide_numbers(value_a, value_b)
    # Assert
    assert result == 1

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    value_a = 1
    value_b = 0
    # Act
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(value_a,value_b)
