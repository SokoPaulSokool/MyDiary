from flask import send_from_directory
from flask_restful import Resource


class StartPage(Resource):
    def get(self):
        return send_from_directory('./templates', 'index.html')
