"""Subtraction Class"""

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        # for i in range(len(self.values)):
        #     result = self.values[i] - self.values[i+1]
        # return result

        #difference_of_values = 0.0
        for index, value  in enumerate(self.values):
            if index == 0:
                difference_of_values = value
            else:
                difference_of_values = difference_of_values - value
        return difference_of_values
