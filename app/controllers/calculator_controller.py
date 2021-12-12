import pandas as pd
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.utils.file_reader import PandasFileReader
from calc.utils.file_writer import FileWriter
from calc.utils.input_validator import InputValidator
from flask import render_template, request, flash, redirect, url_for

INPUT_FILE_NAME = "input.csv"
OUTPUT_FILE_NAME = "output.csv"

class CalculatorController(ControllerBase):

    @staticmethod
    def get():
        return render_template('calculator.html')

    @staticmethod
    def post():
        # flash('Please provide values by separating them with ";"')

        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'The values cannot be empty'
            return render_template('calculator.html', error=error)
        elif not InputValidator(request.form['value1'], request.form['value2']).validate():
            error = 'Please enter numeric values'
            return render_template('calculator.html', error=error)
        else:
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            user_input = (value1, value2, operation)
            # Calling the class to write the user input to csv
            FileWriter(user_input, INPUT_FILE_NAME).write_to_file(columns=['value1', 'value2', 'operation'])
            flash('Values added successfully')
            return render_template('calculator.html')

    @staticmethod
    def get_result():
        flash('Calculation was successful')
        df_csv = PandasFileReader(INPUT_FILE_NAME).read_file()
        # this will call the correct operation
        calculation_results = []
        for index, row in df_csv.iterrows():
            function_handler = getattr(Calculator, row.result)

            try:
                function_handler((row.value_1, row.value_2))
                result = str(Calculator.get_last_calculation_from_result())
            except ZeroDivisionError:
                 result = 'ZeroDivisionError'
            calculation_result = (str(row.value_1), str(row.value_2), str(row.result), result)
            calculation_results.append(calculation_result)

        for row in calculation_results:
            file_path = FileWriter(
                row,
                OUTPUT_FILE_NAME
           ).write_to_file(columns=['value1', 'value2', 'operation', 'result'])

        return render_template('result.html', results=calculation_results)


