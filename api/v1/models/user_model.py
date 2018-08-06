
from database.auth_crud import auth_crud
from passlib.hash import pbkdf2_sha256 as sha256
from api.v1.models.response_message import ResponseMessage
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)
import json
from flask import jsonify


class User():
    """User class

    Keyword arguments: name, email, password
    name -- name of the user
    email -- email of the user
    password -- password of the user
    """

    def __init__(self, name, email, password):
        """Initialize the args"""
        self.name = name
        self.email = email
        self.password = password

    def signup_user(self):
        """Uses the data in the context to signup a user

        Return: returns Response object or a message with a status code
        """
        check_result = auth_crud().add_user(
            User(self.name, self.email, sha256.hash(self.password)))

        if check_result == 'failed':
            print(check_result)
            return ResponseMessage("failed to create user", 400).response()
        elif check_result == 'user exists':
            print(check_result)
            return ResponseMessage(
                "The email is already being used", 401).response()
        else:
            print(check_result)
            message = check_result[1] + \
                " has been successfully registered. You can now login"
            return {
                "message": message
            }, 201

    def authenticate_user(self):
        """Uses the data in the context to authenticate a user

        Return: returns Response object
        """
        check_result = auth_crud().get_user_by_email(
            self.email)
        if check_result == 'failed':
            return ResponseMessage(
                "Login failed  email does not exist. First signup",
                401).response()
        else:
            if sha256.verify(self.password, check_result[3]):
                access_token = create_access_token(
                    identity={
                        "user_id": check_result[0],
                        "name": check_result[1],
                        "email": check_result[2]})
                message = check_result[1] + \
                    " has been authorised."
                return {
                    "message": message,
                    'access_token': access_token
                }, 200
            else:
                return ResponseMessage(
                    "login failed  wrong password ", 401).response()
