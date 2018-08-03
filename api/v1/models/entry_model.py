

class Entry():
    """Model of an Entry 

    Keyword arguments: entry_id, user_id, entry_title, entry, entry_date
    entry_id -- unique id to identify the entry
    user_id -- unique id to identify the ouner of the entry 
    entry_title -- brief description of the entry
    entry -- detailed entry
    entry_date -- date of the entry
    """

    def __init__(self, entry_id, user_id, entry_title, entry, entry_date):
        self.entry_id = entry_id
        self.entry_title = entry_title
        self.entry = entry
        self.entry_date = entry_date
        self.user_id = user_id

    def serialize(self):
        return {
            'entry_id': self.entry_id,
            'entry_title': self.entry_title,
            'entry': self.entry,
            'entry_date': self.entry_date,
            'user_id': self.user_id
        }
