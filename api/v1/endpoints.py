from flask import Flask
import os
from api.v1.models.response_message import ResponseMessage
from flask_restful import Resource, Api, reqparse
from api.v1.api_entry import EntryApi
from api.v1.api_entries import EntriesApi
from api.v1.api_login import LoginApi
from api.v1.api_signup import SignUpApi
from api.v1.models.first_data import diary_users
from database.create_tables import create_tables
from flask_jwt_extended import JWTManager

from flask_restful_swagger import swagger
from flask_restful_swagger import swagger


app = Flask(__name__)

# api = Api(app)
api = swagger.docs(Api(app), apiVersion='0.1')

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

create_tables().users_drop_table()
create_tables().entries_drop_table()
create_tables().users_table()
create_tables().entries_table()
print("starting")


api.add_resource(EntriesApi, '/api/v1/entries')
api.add_resource(EntryApi, '/api/v1/entries/<int:enty_id>')
api.add_resource(SignUpApi, '/api/v1/auth/signup')
api.add_resource(LoginApi, '/api/v1/auth/login')


app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'this_should_be_configured')
