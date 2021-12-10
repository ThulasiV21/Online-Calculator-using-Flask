from app.controllers.controller import ControllerBase
from flask import render_template

class TestingController(ControllerBase):
    @staticmethod
    def get():
        return render_template('pythontesting.html')
