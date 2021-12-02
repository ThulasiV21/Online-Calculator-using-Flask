"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """returns the addition result"""
        return sum(self.values)
    