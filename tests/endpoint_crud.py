
class entriescrud():

    def __init__(self, app):
        self.test_client = app.test_client()

    # Fetch all entries

    def test_fetch_all_entries(self):
        return self.test_client.get('/api/v1/entries')

    # Fetch single entry

    def test_fetch_one_entries(self):
        self.submit_entry("mm", "mm", "MM")
        return self.test_client.get('/api/v1/entries/0')

    # Fetch empty entries

    def fetch_one_empty_entries(self):
        return self.test_client.get('/api/v1/entries/100')

    # post put entry with the provided args

    def submit_entry(self, entry_title, entry, entry_date):
        return self.test_client.post('/api/v1/entries',
                                     data=dict(entry_title=entry_title,
                                               entry=entry,
                                               entry_date=entry_date
                                               )
                                     )

    # post entry with some form key  missing

    def submit_entry_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "entry_title":
            return self.test_client.post('/api/v1/entries',
                                         data=dict(entry="entry",
                                                   entry_date="entry_date"
                                                   )
                                         )
        if missing_form_name == "entry":
            return self.test_client.post('/api/v1/entries',
                                         data=dict(entry_title="entry_title",
                                                   entry_date="entry_date"
                                                   )
                                         )
        if missing_form_name == "entry_date":
            return self.test_client.post('/api/v1/entries',
                                         data=dict(entry_title="entry_title",
                                                   entry="entry"
                                                   )
                                         )
    # put entry with the provided args

    def submit_put_entry(self, entry_title, entry, entry_date):
        self.submit_entry("kk", "kk", "kkk")
        return self.test_client.put('/api/v1/entries/0',
                                    data=dict(entry_title=entry_title,
                                              entry=entry,
                                              entry_date=entry_date
                                              )
                                    )
    # put entry with some form key  missing

    def submit_put_entry_with_missing_form_value(self, missing_form_key):
        self.submit_entry("mm", "mm", "MM")
        if missing_form_key == "entry_title":
            return self.test_client.put('/api/v1/entries/0',
                                        data=dict(entry="entry",
                                                  entry_date="entry_date"
                                                  )
                                        )
        if missing_form_key == "entry":
            return self.test_client.put('/api/v1/entries/0',
                                        data=dict(entry_title="entry_title",
                                                  entry_date="entry_date"
                                                  )
                                        )
        if missing_form_key == "entry_date":
            return self.test_client.put('/api/v1/entries/0',
                                        data=dict(entry_title="entry_title",
                                                  entry="entry"
                                                  )
                                        )
    # delete entry with the provided args

    def submit_delete_entry(self):
        self.submit_entry("mm", "mm", "MM")
        return self.test_client.delete('/api/v1/entries/0')

    def submit_delete_empty_entry(self):
        return self.test_client.get('/api/v1/entries/200')
