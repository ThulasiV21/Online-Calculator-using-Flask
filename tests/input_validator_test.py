"""Testing input validator class"""
import pytest
from calc.utils.input_validator import InputValidator

def test_input_validation_with_numbers():
    """Testing input validation for input as numbers"""
    #Arrange
    value1 = '1'
    value2 = '2'
    #Act
    user_input_check1 = InputValidator(value1, value2).validate()
    #Assert
    assert user_input_check1 == ('1','2')

def test_input_validation_with_alphanumeric():
    """Testing input validation for input as alphanumeric"""
    #Arrange
    value1 = '1'
    value2 = 'a'
    #Act
    user_input_check2 = InputValidator(value1, value2).validate()
    #Assert
    assert user_input_check2 is False
