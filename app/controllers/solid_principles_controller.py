from app.controllers.controller import ControllerBase
from flask import render_template

class SolidPrinciplesController(ControllerBase):
    @staticmethod
    def get():
        return render_template('solidPrinciples.html')
