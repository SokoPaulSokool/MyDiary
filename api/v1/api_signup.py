from api.v1.models.response_message import ResponseMessage
from flask_restful import Resource, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.first_data import diary_users
from api.v1.models.user_model import User
from database.auth_crud import auth_crud
from flask_restful_swagger import swagger
from re import match


@swagger.model
class SignupModel:
    "Model describing inputs for documetation"

    def __init__(self, name, email, password):
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
parser.add_argument('name',
                    type=str,
                    required=True,
                    help="This field is required"
                    )


class SignUpApi(Resource):
    "Documentation for signup"
    @swagger.operation(
        notes="Send a json object as decribed in the schema. User is registered if the email  has not been used already",
        parameters=[
            {
                "name": "Signup body",
                "description": "requires ones name email and password to authenticate them",
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
        email = args['email']
        password = args['password']
        name = args['name']
        res = ''
        if not name:
            return ResponseMessage(
                "name is empty. Please add name",
                400).response()
        if not email:
            return ResponseMessage(
                "email is empty. Please add email",
                400).response()
        if not password:
            return ResponseMessage(
                "password is empty. Please add password",
                400).response()

        if not name.isalpha():
            return ResponseMessage(
                "The name " +
                name +
                " is not accepted. Please use a different name",
                400).response()

        if not bool(
            match(
                r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
                email)):
            print(email.isdigit())
            return ResponseMessage(
                "email is not valid. use example soko@andela.com",
                400).response()
        if len(password) < 5:
            return ResponseMessage(
                "password is too short. mut have atleats 5 characters",
                400).response()

        if name or email or password:
            diary_user = User(name, email, password)
            res = diary_user.signup_user()
            return res
