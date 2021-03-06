from api.v1.models.response_message import ResponseMessage
from flask_restful import Resource, reqparse
import datetime
from database.entries_crud import entries_crud

from api.v1.models.entries_model import Entries
import json

from api.v1.models.entry_model import Entry
import json
from flask_restful_swagger import swagger
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


@swagger.model
class EntryModel:
    "Model describing inputs for documetation"

    def __init__(self, entry, entry_title):
        pass


parser = reqparse.RequestParser()
parser.add_argument('entry',
                    type=str,
                    required=True,
                    help="This field is required"
                    ),
parser.add_argument('entry_title',
                    type=str,
                    required=True,
                    help="This field is required"
                    )


class EntriesApi(Resource):
    "Documentation for get"
    @swagger.operation(notes="""Gets all entries of a given user.
        First login using the login end point and obtain the user's
        access token to use for Authorization""",
                       nickname='fetch entries',
                       parameters=[{"name": "Authorization",
                                    "description": "After loging in, get the access_token add 'Beaer' +access_token",
                                    "required": True,
                                    "allowMultiple": False,
                                    "dataType": "string",
                                    "paramType": "header"}],
                       responseMessages=[{"code": 401,
                                          "message": "The reason should be in the returned message"},
                                         {"code": 400,
                                          "message": "The reason should be in the returned message"}])
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        if current_user["user_id"]:
            return Entries(current_user["user_id"]).entries_from_turple_list(), 200
        else:
            return ResponseMessage("Wrong token", 401)

    "Documentation for create entry"
    @swagger.operation(notes="""This adds an entry to the user's entries.\n
        First login using the login end point and obtain the user's
        access token to use for Authorization\n
        Then send the entry and tittle through the body as described in the schema""",
                       nickname="add entry",
                       parameters=[{"name": "Authorization",
                                    "description": "After loging in, get the access_token add 'Beaer' +access_token",
                                    "required": True,
                                    "allowMultiple": False,
                                    "dataType": "string",
                                    "paramType": "header"},
                                   {"name": "Add new entry body",
                                    "description": "requires ones entry title  and entry ",
                                    "required": True,
                                    "allowMultiple": False,
                                    "dataType": EntryModel.__name__,
                                    "paramType": "body"}],
                       responseMessages=[{"code": 401,
                                          "message": "The reason should be in the returned message"},
                                         {"code": 405,
                                          "message": "Invalid input"}])
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user["user_id"]:
            args = parser.parse_args()
            entry = args['entry']
            entry_title = args['entry_title']
            entry_id = 1
            if not entry or not entry_title:
                res = ResponseMessage(
                    'entry_title or entry or entry_date is empty', 400).response()
                return res
            else:
                entry_date = datetime.datetime.now().timestamp()
                new_entry = Entries(
                    current_user["user_id"]).add_entry(
                    Entry(
                        entry_id,
                        current_user["user_id"],
                        entry_title,
                        entry,
                        entry_date))
                res = new_entry
                return res
        else:
            return ResponseMessage("Wrong token", 401)
