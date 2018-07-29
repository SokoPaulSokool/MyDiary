from api.v1.models.response_message import ResponseMessage
from api.v1.models.response_message import ResponseMessage
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api, reqparse
from api.v1.models.first_data import entry_list
from api.v1.models.entry_model import Entry

parser = reqparse.RequestParser()
parser.add_argument('entry',
                    type=str,
                    required=True,
                    help="This field is required"
                    ),
parser.add_argument('entry_date',
                    type=str,
                    required=True,
                    help="This field is required"
                    )
parser.add_argument('entry_title',
                    type=str,
                    required=True,
                    help="This field is required"
                    )


class EntryApi(Resource):
    def get(self, enty_id):
        return entry_list.get_entry(enty_id)

    def put(self, enty_id):
        args = parser.parse_args()
        entry = args['entry']
        entry_date = args['entry_date']
        entry_title = args['entry_title']

        if not entry or not entry_title or not entry_date:
            res = 'entry_title or entry or entry_date is empty'
            return ResponseMessage(res, 400).response()
        else:
            entry = Entry(
                enty_id, entry_title, entry, entry_date)
            # replaces entry at a given id with the new data sent
            res = entry_list.replace_entry(enty_id, entry)
            return res

    def delete(self, enty_id):
        res = entry_list.remove_entry(enty_id)
        return res
