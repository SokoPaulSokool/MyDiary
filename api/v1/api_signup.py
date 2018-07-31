from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.first_data import diary_users
from api.v1.models.user_model import User
from database.auth_crud import auth_crud


# signup user  endpoint


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
    def post(self):
        args = parser.parse_args()
        phonenumber = args['phonenumber']
        password = args['password']
        name = args['name']
        res = ''
        if not name or not phonenumber or not password:
            res = ResponseMessage(
                'Either "name" or "phonenumber" or Passssword" is empty',
                400).response()
        else:
            diary_user = User(name, phonenumber, password)
            res = diary_user.signup_user()
        return res
