from api.v1.models.response_message import ResponseMessage
from flask import jsonify
from api.v1.models.entry_model import Entry


class Entries:
    def __init__(self):
        self.entry_list = []

    def add_entry(self, entry):
        self.entry_list.append(entry)
        id = self.entry_list.index(entry)
        self.entry_list[id].entry_id = id

    def get_entry(self, entry_id):
        try:
            entry_got_from_list = self.entry_list[entry_id].serialize()
            print(entry_got_from_list)
            return ResponseMessage(str(entry_got_from_list), 200).response()
        except:
            return ResponseMessage("not found", 404).response()

    def remove_entry(self, entry_id):
        try:
            self.entry_list.pop(entry_id)
            return ResponseMessage("deleted", 200).response()
        except:
            return ResponseMessage("not found", 404).response()

    def replace_entry(self, entry_id, entry):
        try:
            if self.get_entry(entry_id)["message"] == "not found":
                return ResponseMessage("not found", 404).response()
            else:
                try:
                    self.entry_list.insert(entry_id, entry)
                    self.add_entry(entry)
                    return ResponseMessage("success", 200).response()
                except:
                    return ResponseMessage("not found", 404).response()

        except:
            try:
                self.entry_list.insert(entry_id, entry)
                self.add_entry(entry)
                return ResponseMessage("success", 200).response()
            except:
                return ResponseMessage("not found", 404).response()

    def get_string(self):
        items = []
        for item in self.entry_list:
            items.append(item.serialize())
        return jsonify(items)
