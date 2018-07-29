from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.first_data import diary_users

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
            if phonenumber in diary_users:
                current_user = diary_users.get(
                    phonenumber)

                if current_user.password == password:
                    current_user.login_user()

                else:
                    current_user.logout_user()

                if current_user.isloged_in:
                    res = ResponseMessage(
                        "login success", 200).response()
                else:
                    res = ResponseMessage(
                        "login failed wrong password", 401).response()
            else:
                res = ResponseMessage(
                    "not yet registered or wrong phonenumber", 401).response()
        return res
