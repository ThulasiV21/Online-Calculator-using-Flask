"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division calculation object"""
    def get_result(self):
        """get the division results"""
        #initial_value = 1.0
        for index, value in enumerate(self.values):
            if index == 0:
                division_value = value
            else:
                division_value = division_value / value
        return round(division_value, 5)

            # pprint.pprint(value)
        # return difference_of_values
        # for value in self.values:
        #     result = result / value
        # return result
