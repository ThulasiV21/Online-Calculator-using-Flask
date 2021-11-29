""" This is the increment function"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class   Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adding the results to the history array"""
        Calculator.history.append(calculation)

    @staticmethod
    def get_last_calculation_result():
        """Getting the latest result from history array"""
        # -1 index gets the last item added to history
        return Calculator.history[-1].get_result()

    @staticmethod
    def get_last_calculation_object():
        """Creating object for the latest result in the history array"""
        return Calculator.history[-1]

    @staticmethod
    def clear_history():
        """Clearing the results history array and getting the count of the history indexes"""
        Calculator.history.clear()
        return Calculator.count_history()

    @staticmethod
    def count_history():
        """Calculating the length of the history array"""
        return len(Calculator.history)

    @staticmethod
    def add_number(value_a, value_b):
        """ Instantiating  Addition object and passing value a and value b to the constructor"""
        #This is using a factory create method to return an instance of the class
        Calculator.add_calculation_to_history(Addition.create(value_a,value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        Calculator.add_calculation_to_history(Subtraction.create(value_a,value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def multiply_numbers( value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def divide_numbers( value_a, value_b):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_last_calculation_result()
