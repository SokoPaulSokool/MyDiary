
from database.auth_crud import auth_crud
from passlib.hash import pbkdf2_sha256 as sha256
from api.v1.models.response_message import ResponseMessage
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import json
from flask import jsonify


class User():
    def __init__(self, name, phone_number, password):
        self.name = name
        self.phone_number = phone_number
        self.password = password

    def signup_user(self):
        check_result = auth_crud().add_user(
            User(self.name, self.phone_number, sha256.hash(self.password)))

        if check_result == 'failed':
            print(check_result)
            return ResponseMessage("failed to create user", 500).response()
        elif check_result == 'user exists':
            print(check_result)
            return ResponseMessage(
                "phone number is already being used", 401).response()
        else:
            print(check_result)
            message = "user '" + \
                check_result[1] + \
                "' has been successfully registered. You can now login"
            return {
                "message": message
            }, 200

    def authenticate_user(self):
        print("auth start")
        check_result = auth_crud().get_user_by_phone(
            self.phone_number)
        if check_result == 'failed':
            return ResponseMessage(
                "Login failed  phone number does not exist. First signup ", 401).response()
        else:
            print(check_result[0])
            print(sha256.verify(self.password, check_result[3]))
            if sha256.verify(self.password, check_result[3]):
                access_token = create_access_token(identity={
                                                   "user_id": check_result[0], "name": check_result[1], "phone_number": check_result[2]})
                message = "user '" + \
                    check_result[1] + \
                    "' has been authorised."
                return {
                    "message": message,
                    'access_token': access_token
                }, 200
            else:
                return ResponseMessage(
                    "login failed  wrong password ", 401).response()
