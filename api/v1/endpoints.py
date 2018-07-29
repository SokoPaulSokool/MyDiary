from flask import Flask
import os
from api.v1.models.response_message import ResponseMessage
from flask_restful import Resource, Api, reqparse
from api.v1.api_entry import EntryApi
from api.v1.api_entries import EntriesApi
from api.v1.api_login import LoginApi
from api.v1.api_signup import SignUpApi

app = Flask(__name__)


api = Api(app)

api.add_resource(EntriesApi, '/api/v1/entries')
api.add_resource(EntryApi, '/api/v1/entries/<int:enty_id>')
api.add_resource(SignUpApi, '/api/v1/auth/signup')
api.add_resource(LoginApi, '/api/v1/auth/login')


app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'this_should_be_configured')
