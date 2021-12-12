"""Validates input from user to be numeric"""

import re
from flask import render_template, request, flash, redirect, url_for
# import logging
# logger = logging.getLogger(__name__)
class InputValidator:
    """Input Validator class"""
    def __init__(self, input_value1, input_value2):
        self._input_value1 = input_value1
        self._input_value2 = input_value2

    @property
    def input_value1(self):
        return self._input_value1

    @property
    def input_value2(self):
        return self._input_value2

    def validate(self):
        """Method to check whether the user's input is numeric or not"""
        regex = '^[0-9]+$'
        value1_check = False
        value2_check = False
        if re.search(regex, self.input_value1):
            value1_check = True
        if re.search(regex, self.input_value2):
            value2_check = True
        if not value1_check or not value2_check:
            return False
        else:
            return self._input_value1, self._input_value2
