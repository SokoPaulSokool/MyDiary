from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.user_model import User
from api.v1.models.first_data import diary_users
from database.auth_crud import auth_crud
from flask_restful_swagger import swagger

from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


  
@swagger.model
class LoginModel:
    "Model describing inputs for documetation"

    def __init__(self, phonenumber="123", password="12rr"):
        pass


parser = reqparse.RequestParser()
parser.add_argument('phonenumber',
                    type=str,
                    required=True,
                    help="This field is required"
                    ),
parser.add_argument('password',
                    type=str,
                    required=True,
                    help="This field is required"
                    )

class LoginApi(Resource):
    "Documentation for login" 
    @swagger.operation(
        notes='Send a json object as decribed in the schema. User is authorized if they are aready registered',
        parameters=[
            {
                "name": "Login body",
                "description": "requires ones phonenumber and password to authenticate them",
                "required": True,
                "allowMultiple": False,
                "dataType": LoginModel.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 401,
                "message": "Not authorised. The reason should be in the returned message"
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ]
    )
    def post(self):
        args = parser.parse_args()
        phonenumber = args['phonenumber']
        password = args['password']
        res = ''
        if not phonenumber or not password:
            res = ResponseMessage(
                "'phonenumber' or 'Password' is empty", 400).response()
        else:

            new_user = User("", phonenumber, password)
            res = new_user.authenticate_user()
        return res
