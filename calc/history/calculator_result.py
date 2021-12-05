"""Calculation history Class"""
class CalculatorResult:
    """Storing the Calculation to a list named history Class"""
    history = []

    @staticmethod
    def clear_history():
        """ clear the history list"""
        CalculatorResult.history.clear()
        return True

    @staticmethod
    def count_history():
        """ get the length of history list"""
        return len(CalculatorResult.history)

    @staticmethod
    def get_last_calculation_object():
        """ get the latest calculation from history"""
        return CalculatorResult.history[-1]

    @staticmethod
    def get_last_calculation_result():
        """ get the last calculation from history"""
        return CalculatorResult.get_last_calculation_object().get_result()

    @staticmethod
    def get_first_calculation():
        """ get the first calculation from history"""
        return CalculatorResult.history[0]

    @staticmethod
    def get_calculation_from_history(num):
        """ get a specific calculation from history"""
        return CalculatorResult.history[num]

    @staticmethod
    def add_calculation_to_history(calculation):
        """ get a specific calculation from history"""
        CalculatorResult.history.append(calculation)
        return CalculatorResult.history
