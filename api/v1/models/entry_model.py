

class Entry():
    def __init__(self, entry_id, entry_title, entry, entry_date):
        self.entry_id = entry_id
        self.entry_title = entry_title
        self.entry = entry
        self.entry_date = entry_date

    def serialize(self):
        return {
            'entry_id': self.entry_id,
            'entry_title': self.entry_title,
            'entry': self.entry,
            'entry_date': self.entry_date,
        }
