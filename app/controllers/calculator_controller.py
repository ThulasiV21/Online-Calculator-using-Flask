from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.utils.file_writer import FileWriter
from calc.utils.input_validator import InputValidator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        flash('Please provide values by separating them with ";"')

        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'The values cannot be empty'
            return render_template('calculator.html', error=error)
        elif not InputValidator(request.form['value1'], request.form['value2']).validate():
            error = 'Please enter numeric values'
            return render_template('calculator.html', error=error)
        else:

            flash('Calculation was successful')
            # get the values out of the form
            # values = request.form['value'].split(";")
            # value1 = request.form['value1']
            # value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            user_input = ('value1', 'value2', operation)
            # this will call the correct operation
            FileWriter(user_input).write_to_file()
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_calculation_from_result())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)

    @staticmethod
    def get():
        return render_template('calculator.html')