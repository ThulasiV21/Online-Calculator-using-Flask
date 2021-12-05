""" This is the calculator class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.history.calculator_result import CalculatorResult
from calc.calculations.division import Division

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_calculation_from_result():
        """ Last value from calculation"""
        return CalculatorResult.get_last_calculation_result()

    @staticmethod
    def addition(values: tuple):
        """ adds list of numbers"""
        CalculatorResult.add_calculation_to_history(Addition.create(values))
        return True

    @staticmethod
    def subtraction(values: tuple):
        """ subtract a list of numbers from result"""
        CalculatorResult.add_calculation_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def multiplication(values: tuple):
        """ multiply list of numbers from result"""
        CalculatorResult.add_calculation_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def division(values: tuple):
        """ Divide list of numbers from result"""
        CalculatorResult.add_calculation_to_history(Division.create(values))
        return True
