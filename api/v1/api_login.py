from api.v1.models.response_message import ResponseMessage
from flask_restful import Resource, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.user_model import User
from api.v1.models.first_data import diary_users
from flask_restful_swagger import swagger

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity)


@swagger.model
class LoginModel:
    "Model describing inputs for documetation"

    def __init__(self, email, password):
        pass


parser = reqparse.RequestParser()
parser.add_argument('email',
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
        email = args['email']
        password = args['password']
        res = ''
        if not email:
            return ResponseMessage(
                "The field 'phonenumber' is empty. Please add email",
                400).response()
        if not password:
            return ResponseMessage(
                "The field 'password' is empty. Please add password",
                400).response()

        if email or password:
            new_user = User("", email, password)
            res = new_user.authenticate_user()
            return res
