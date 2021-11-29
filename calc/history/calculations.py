"""Calculation history Class"""
class Calculations:
    """Calculation history Class"""
    history = []

    @staticmethod
    def clear_history():
        """ clear the history list"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """ get the length of history list"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """ get the latest calculation from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result():
        """ get the last calculation from history"""
        return Calculations.get_last_calculation_object().get_result()

    @staticmethod
    def get_first_calculation():
        """ get the first calculation from history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation_from_history(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation_to_history(calculation):
        """ get a specific calculation from history"""
        Calculations.history.append(calculation)
        return Calculations.history
