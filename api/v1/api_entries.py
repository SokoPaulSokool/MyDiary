from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
import datetime
from database.entries_crud import entries_crud

from api.v1.models.entries_model import Entries
import json

from api.v1.models.entry_model import Entry
import json
from flask_restful_swagger import swagger
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


@swagger.model
class EntryModel:
    "Model describing inputs for documetation"

    def __init__(self, entry, entry_title):
        pass

# endpoint to Fetch all entries or create an entry to diary


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
    @swagger.operation(
        notes="Documentation for get entry  ",
        parameters=[
            {
                "name": "Authorization",
                "description": "After loging in, get the access_token add 'Beaer' +access_token",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "header"
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
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return Entries(current_user["user_id"]).entries_from_turple_list(), 200

    "Documentation for create entry"
    @swagger.operation(
        notes="Documentation for create entry",
        parameters=[
             {
                "name": "Authorization",
                "description": "After loging in, get the access_token add 'Beaer' +access_token",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "header"
            },
            {
                "name": "Add new entry body",
                "description": "requires ones entry title  and entry ",
                "required": True,
                "allowMultiple": False,
                "dataType": EntryModel.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 401,
                "message": "The reason should be in the returned message"
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ]
    )
    @jwt_required
    def post(self):
        args = parser.parse_args()
        entry = args['entry']
        entry_title = args['entry_title']
        entry_id = 1
        current_user = get_jwt_identity()
        if not entry or not entry_title:
            res = ResponseMessage(
                'entry_title or entry or entry_date is empty', 400).response()
            return res
        else:
            # adds new entry to list of diary entries
            entry_date = datetime.datetime.now().timestamp()
            new_entry = Entries(current_user["user_id"]).add_entry(Entry(
                entry_id, current_user["user_id"], entry_title, entry, entry_date))
            res = new_entry
            return res
