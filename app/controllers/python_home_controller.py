from app.controllers.controller import ControllerBase
from flask import render_template

class PythonHomeController(ControllerBase):
    @staticmethod
    def get():
        return render_template('pythonHome.html')
