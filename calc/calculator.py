""" This is the increment function"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtract number from result"""
        return Subtraction.subtract(value_a,value_b)