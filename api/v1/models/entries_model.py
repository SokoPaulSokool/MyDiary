from api.v1.models.response_message import ResponseMessage
from flask import jsonify
import json
from api.v1.models.entry_model import Entry
from database.entries_crud import entries_crud
import datetime


class Entries:
    def __init__(self, user_id):
        self.entry_list = []
        self.user_id = user_id

    def add_entry(self, entry):
        entry_turple = entries_crud().add_entry(self.user_id, entry)
        if entry_turple == "failed":
            message = "Failed to create entry"
            return ResponseMessage(
                message, 400).response()
        elif entry_turple == "user not found":
            message = "Your account does not exist"
            return ResponseMessage(
                message, 400).response()
        else:
            new_entry = Entry(entry_turple[0],
                              entry_turple[1],
                              entry_turple[2],
                              entry_turple[3],
                              entry_turple[4])
            message = "Entry with title '"+new_entry.entry_title + \
                "' has been successfully created"
            return {"message": message,
                    "entry_id": str(new_entry.entry_id)
                    }, 201

    def get_entry(self, entry_id):
        print(entries_crud().get_entry_by_id(
            self.user_id, entry_id))
        try:
            entry_got_from_db = entries_crud().get_entry_by_id(
                self.user_id, entry_id)
            new_entry = Entry(entry_got_from_db[0],
                              entry_got_from_db[1],
                              entry_got_from_db[2],
                              entry_got_from_db[3],
                              self.timestamp_to_date(entry_got_from_db[4]))

            return new_entry.serialize()
        except:
            return ResponseMessage("entry with id '"+str(entry_id)+"' not found", 404).response()

    def remove_entry(self, entry_id):
        entry_deleted_from_db = entries_crud().delete_entry(
            self.user_id, entry_id)
        print(entry_deleted_from_db)
        if entry_deleted_from_db == 1:
            message = "entry with id '"+str(entry_id)+"' has been deleted"
            return ResponseMessage(message, 200).response()
        else:
            return ResponseMessage("entry with id '"+str(entry_id)+"' not found", 404).response()

    def replace_entry(self,  entry):
        edited = entries_crud().edit_entry(self.user_id, entry)
        if edited:
            edited_entry = Entry(edited[0], edited[1],
                                 edited[2], edited[3], edited[4])

            message = "entry with id '" + \
                str(edited_entry.entry_id)+"' has been edited"
            return ResponseMessage(message, 200).response()
        else:
            return ResponseMessage("entry with id '"+str(entry.entry_id)+"' not found", 404).response()

    def entries_from_turple_list(self):
        items = []
        got_from_database = entries_crud().get_all_user_entries(self.user_id)
        print(got_from_database)
        for entry_turple in got_from_database:
            entry = Entry(entry_turple[0],
                          entry_turple[1],
                          entry_turple[2],
                          entry_turple[3],
                          self.timestamp_to_date(entry_turple[4]))
            items.append(entry.serialize())
        return items

    def timestamp_to_date(self, timestamp):
        return datetime.datetime.fromtimestamp(
            float(timestamp)
        ).strftime('%Y-%m-%d %H:%M:%S')
