from flask import redirect, url_for, send_from_directory
from flask_restful import Resource, Api, reqparse


class StartPage(Resource):
    def get(self):
        return send_from_directory('./templates', 'index.html')
