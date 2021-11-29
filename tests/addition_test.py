"""Testing Addition"""
from calc.calculations.addition import Addition

def test_static_calculation_addition(addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    #Assert
    for index, row in addition_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
    #Act
        addition = Addition.create(tuple_values)
    #Assert
        assert addition.get_result() == row.result
