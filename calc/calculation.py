"""This is going to be the Calculation object"""

class Calculation:
    """Initializing objects"""
    def __init__(self, value_a, value_b):
        self._value_a = value_a
        self._value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """Using class method to create objects of all individual operations"""
        return cls(value_a,value_b)

    @property
    def value_a(self):
        """Getter For Value A"""
        return self._value_a

    @property
    def value_b(self):
        """Getter For Value B"""
        return self._value_b
