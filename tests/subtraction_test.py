"""Testing Subtraction"""
import logging
from calc.calculations.subtraction import Subtraction

logger = logging.getLogger(__name__)


def test_static_calculation_subtraction(subtraction_file_fixture):
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    for index, row in subtraction_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
    #Act
        subtraction = Subtraction.create(tuple_values)
    #Assert
        result = subtraction.get_result()
        logger.info("%s  - %s - %s = %s", index, row.value_1, row.value_2, result)
        assert result == subtraction_file_fixture['result'][index]
