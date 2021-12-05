"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """Multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        for index, value  in enumerate(self.values):
            if index == 0:
                multiplication_value = value
            else:
                multiplication_value = multiplication_value * value
        return multiplication_value
