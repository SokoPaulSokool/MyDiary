from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.first_data import diary_users
from api.v1.models.user_model import User
from database.auth_crud import auth_crud
from flask_restful_swagger import swagger


# signup user  endpoint


@swagger.model
class SignupModel:
    "Model describing inputs for documetation"

    def __init__(self, name, phonenumber="123", password="12rr"):
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
parser.add_argument('name',
                    type=str,
                    required=True,
                    help="This field is required"
                    )


class SignUpApi(Resource):
    "Documentation for signup"
    @swagger.operation(
        notes="Send a json object as decribed in the schema. User is registered if the phone number has not been used already",
        parameters=[
            {
                "name": "Signup body",
                "description": "requires ones name phonenumber and password to authenticate them",
                "required": True,
                "allowMultiple": False,
                "dataType": SignupModel.__name__,
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
        name = args['name']
        res = ''
        if not name or not phonenumber or not password:
            res = ResponseMessage(
                "'phonenumber' or 'Password' is empty",
                400).response()
        else:
            diary_user = User(name, phonenumber, password)
            res = diary_user.signup_user()
        return res
