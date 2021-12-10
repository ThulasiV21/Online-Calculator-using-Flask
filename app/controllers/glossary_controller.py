from app.controllers.controller import ControllerBase
from flask import render_template

class GlossaryController(ControllerBase):
    @staticmethod
    def get():
        return render_template('glossary.html')
