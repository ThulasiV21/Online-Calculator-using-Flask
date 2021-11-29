"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication
from calc.utils.file_reader import PandasFileReader

def test_calculation_multiplication(multiplication_file_fixture):
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    for index, row in multiplication_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        multiplication = Multiplication.create(tuple_values)
    #Assert
        assert multiplication.get_result() == multiplication_file_fixture['result'][index]
