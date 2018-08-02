from api.v1.models.response_message import ResponseMessage
from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.entry_model import Entry
from api.v1.models.entries_model import Entries
from database.entries_crud import entries_crud
import datetime
from flask_restful_swagger import swagger
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


@swagger.model
class EntryModel:
    "Model describing inputs for documetation"

    def __init__(self, entry, entry_title):
        pass


parser = reqparse.RequestParser()
parser.add_argument('entry',
                    type=str,
                    required=False
                    ),
parser.add_argument('entry_title',
                    type=str,
                    required=False
                    )


class EntryApi(Resource):
    "Documentation for get by id"
    @swagger.operation(
        notes="""This gets a specific entry from the user's entries.\n
        First login using the login end point and obtain the user's 
        access token to use for Authorization""",
        nickname="get entry by id",
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
                "allowMultiple": False,
                "dataType": "string",
                "description": """This is the id of the entry to be obtained. 
                Its better to first get all entries for the user to idetify the id""",
                "name": "enty_id",
                "paramType": "path",
                "required": True
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
    def get(self, enty_id):
        current_user = get_jwt_identity()
        return Entries(current_user["user_id"]).get_entry(enty_id)

    #
    # "Documentation for put"
    #
    @swagger.operation(
        notes="""This edits a specific entry from the user's entries.\n
        First login using the login end point and obtain the user's 
        access token to use for Authorization. Then send the edited title and the entry in the body as described in the Shema""",
        nickname="edit entry",
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
                "allowMultiple": False,
                "dataType": "string",
                "description": """This is the id of the entry to be obtained. 
                                Its better to first get all entries for the user to idetify the id""",
                "name": "enty_id",
                "paramType": "path",
                "required": True
            },
            {
                "name": "Edit entry body",
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
                "message": "Not authorised. The reason should be in the returned message"
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ]
    )
    @jwt_required
    def put(self, enty_id):
        args = parser.parse_args()
        entry = args['entry']
        entry_title = args['entry_title']
        current_user = get_jwt_identity()

        if not entry or not entry_title:
            res = 'entry_title or entry or entry_date is empty'
            return ResponseMessage(res, 400).response()
        else:
            entry_date = datetime.datetime.now().timestamp()

            entry = Entry(
                enty_id, current_user["user_id"], entry_title, entry, entry_date)
            # replaces entry at a given id with the new data sent
            res = Entries(current_user["user_id"]
                          ).replace_entry(entry)
            return res

    # "Documentation for delete"
    @swagger.operation(
        notes="""Theis deletes an entry from user's entries using an id. 
        First login using the login end point and obtain the user's 
        access token to use for Authorization. Then add the entry id if the item to delete.""",
        nickname='delete entry',
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
                "allowMultiple": False,
                "dataType": "string",
                "description": """This is the id of the entry to be obtained. 
                Its better to first get all entries for the user to idetify the id""",
                "name": "enty_id",
                "paramType": "path",
                "required": True
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
    def delete(self, enty_id):
        current_user = get_jwt_identity()
        res = Entries(current_user["user_id"]).remove_entry(enty_id)
        return res
