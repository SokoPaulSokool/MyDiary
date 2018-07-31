
from database.auth_crud import auth_crud
from passlib.hash import pbkdf2_sha256 as sha256
from api.v1.models.response_message import ResponseMessage
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class User():
    def __init__(self, name, phone_number, password):
        self.name = name
        self.phone_number = phone_number
        self.password = password
        self.isloged_in = False

    def get_user(self):
        return self

    def logout_user(self):
        self.isloged_in = False

    def login_user(self):
        self.isloged_in = True

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
            return {
                "user": {"user_id": check_result[0],
                         "name": check_result[1],
                         "phone_number": check_result[2],
                         "password": check_result[3]
                         }
            }, 200

    def authenticate_user(self):
        print("auth start")
        check_result = auth_crud().get_user_by_phone(
            self.phone_number)
        if check_result == 'failed':
            return ResponseMessage(
                "login failed  phone number does not exist ", 401).response()
        else:
            print(check_result[0])
            print(sha256.verify(self.password, check_result[3]))
            if sha256.verify(self.password, check_result[3]):
                access_token = create_access_token(identity=self.phone_number)
                refresh_token = create_refresh_token(
                    identity=self.phone_number)
                return {
                    "user": {"user_id": check_result[0],
                             "name": check_result[1],
                             "phone_number": check_result[2],
                             "password": check_result[3]
                             },
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
            else:
                return ResponseMessage(
                    "login failed  wrong password ", 401).response()
