from app.controllers.controller import ControllerBase
from flask import render_template

class OopsConceptsController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oopsconcepts.html')
