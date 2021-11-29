""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.history.calculations import Calculations
from calc.calculations.division import Division

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_calculation_from_result():
        """ Last value from calculation"""
        return Calculations.get_last_calculation_result()
    @staticmethod
    def add_numbers( values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation(Addition(values))
        return True
    @staticmethod
    def subtract_numbers( values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_calculation(Subtraction(values))
        return True
    @staticmethod
    def multiply_numbers( values: tuple):
        """ multiplication number from result"""
        Calculations.add_calculation(Multiplication(values))
        return True
    @staticmethod
    def divide_numbers( values: tuple):
        """ Division number from result"""
        Calculations.add_calculation(Division(values))
        return True
