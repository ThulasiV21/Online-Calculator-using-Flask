"""Testing Addition"""
import logging
from calc.calculations.addition import Addition

logger = logging.getLogger(__name__)

def test_static_calculation_addition(addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    #Arrange
    for index, row in addition_file_fixture.iterrows():

        tuple_values = (row.value_1, row.value_2)
    #Act
        addition = Addition.create(tuple_values)
    #Assert
        result = addition.get_result()
        logger.info("%s  - %s + %s = %s", index, row.value_1, row.value_2, result)
        assert result == row.result
