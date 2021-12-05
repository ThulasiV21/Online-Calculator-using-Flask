"""Calculation Class"""
from abc import ABC, abstractmethod

class Calculation(ABC):
    """ calculation abstract base class"""
    def __init__(self,values: tuple):
        """ constructor method"""
        self._values = Calculation.convert_args_to_list_float(values)

    @property
    def values(self):
        """Getter method for values"""
        return self._values

    @staticmethod
    def convert_args_to_list_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float

    @classmethod
    def create(cls, values: tuple):
        """Using class method to create objects of all individual operations"""
        return cls(values)

    @abstractmethod
    def get_result(self):
        """creating this class to show abstraction"""
        return True
    