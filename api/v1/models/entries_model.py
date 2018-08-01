from api.v1.models.response_message import ResponseMessage
from flask import jsonify
from api.v1.models.entry_model import Entry
from database.entries_crud import entries_crud


class Entries:
    def __init__(self, user_id):
        self.entry_list = []
        self.user_id = user_id

    def add_entry(self, entry):
        self.entry_list.append(entry)
        entry_turple = entries_crud().add_entry(self.user_id, entry)
        new_entry = Entry(entry_turple[0], entry_turple[1],
                          entry_turple[2], entry_turple[3], entry_turple[4])

        return new_entry.serialize()

    def get_entry(self, entry_id):
        print(entries_crud().get_entry_by_id(
            self.user_id, entry_id))
        try:
            entry_got_from_db = entries_crud().get_entry_by_id(
                self.user_id, entry_id)
            new_entry = Entry(entry_got_from_db[0], entry_got_from_db[1],
                              entry_got_from_db[2], entry_got_from_db[3], entry_got_from_db[4])

            return new_entry.serialize()
        except:
            return ResponseMessage("not found", 404).response()

    def remove_entry(self, entry_id):
        try:
            entry_deleted_from_db = entries_crud().delete_entry(
                self.user_id, entry_id)

            return ResponseMessage(entry_deleted_from_db, 200).response()
        except:
            return ResponseMessage("not found", 404).response()

    def replace_entry(self,  entry):
        edited = entries_crud().edit_entry(self.user_id, entry)
        if edited:
            edited_entry = Entry(edited[0], edited[1],
                                 edited[2], edited[3], edited[4])

            return edited_entry.serialize()
        else:
            return ResponseMessage("not found", 404).response()

    def entries_from_turple_list(self):
        items = []
        got_from_database = entries_crud().get_all_user_entries(self.user_id)
        print(got_from_database)
        for entry_turple in got_from_database:
            entry = Entry(entry_turple[0], entry_turple[1],
                          entry_turple[2], entry_turple[3], entry_turple[4])
            items.append(entry.serialize())
        return items
