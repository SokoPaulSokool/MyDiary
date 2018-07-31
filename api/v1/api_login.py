from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.user_model import User
from api.v1.models.first_data import diary_users
from database.auth_crud import auth_crud

from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

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
    def post(self):
        args = parser.parse_args()
        phonenumber = args['phonenumber']
        password = args['password']
        res = ''
        if not phonenumber or not password:
            res = ResponseMessage(
                '"phonenumber" or Password" is empty', 400).response()
        else:

            new_user = User("", phonenumber, password)
            res = new_user.authenticate_user()

            # new_user = User("", phonenumber, password)
            # if phonenumber in diary_users:
            #     current_user = diary_users.get(
            #         phonenumber)

            #     if current_user.password == password:
            #         current_user.login_user()

            #     else:
            #         current_user.logout_user()

            #     if current_user.isloged_in:

            #         res = current_user, 200

            #     else:
            #         res = ResponseMessage(
            #             "login failed wrong password", 401).response()
            # else:
            #     res = ResponseMessage(
            #         "not yet registered or wrong phonenumber", 401).response()
        return res
