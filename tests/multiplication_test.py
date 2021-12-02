"""Testing Multiplication"""
import logging
from calc.calculations.multiplication import Multiplication

logger = logging.getLogger(__name__)

def test_calculation_multiplication(multiplication_file_fixture):
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    for index, row in multiplication_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        multiplication = Multiplication.create(tuple_values)
    #Assert
        result = multiplication.get_result()
        logger.info("%s  - %s * %s = %s", index, row.value_1, row.value_2, result)
        assert result == multiplication_file_fixture['result'][index]
