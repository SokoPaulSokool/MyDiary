from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
import datetime
from database.entries_crud import entries_crud

from api.v1.models.entries_model import Entries

from api.v1.models.entry_model import Entry
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


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
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return Entries(current_user["user_id"]).entries_from_turple_list(), 200

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
            res = new_entry, 200
            return res
