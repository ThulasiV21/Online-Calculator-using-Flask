""" This is the increment function"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class   Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Adding the first result to the history array"""
        return Calculator.history[0].get_result()

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adding the results to the history array"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Adding the last result to the history array"""
        # -1 gets the last item added to the list automatically
        # and you can expect it to have the get result method
        return Calculator.history[-1].get_result()

    # @staticmethod
    # def get_last_calculation_result():
    #     """Getting the latest result from history array"""
    #     # -1 index gets the last item added to history
    #     return Calculator.history[-1].get_result()

    # @staticmethod
    # def get_last_calculation_object():
    #     """Creating object for the latest
    #     result in the history array"""
    #     return Calculator.history[-1]

    @staticmethod
    def clear_history():
        """Clearing the results history array and getting the count of the history indexes"""
        Calculator.history.clear()
        return True

    @staticmethod
    def count_history():
        """Calculating the length of the history array"""
        return len(Calculator.history)

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        # create an addition object using the
        # factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        # addition = Addition(value_a,value_b)
        # <-this is not good but will work.  It will be repeated too much
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    #this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        # create an subtraction object using the
        # factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
        # addition = Addition(value_a,value_b)
        # <-this is not good but will work.  It will be repeated too much
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        #this is a shorthand way to create the
        # multiplication object and added it the history in one line
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers( value_a, value_b):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
