from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.first_data import entry_list
import datetime

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
        return entry_list.get_string()

    @jwt_required
    def post(self):
        args = parser.parse_args()
        entry = args['entry']
        entry_title = args['entry_title']
        entry_id = 1
        if not entry or not entry_title:
            res = ResponseMessage(
                'entry_title or entry or entry_date is empty', 400).response()
            return res
        else:
            # adds new entry to list of diary entries
            entry_date = datetime.datetime.now().timestamp()
            new_entry = Entry(entry_id, entry_title, entry, entry_date)
            entry_list.add_entry(new_entry)
            res = new_entry.serialize(), 200
            return res
