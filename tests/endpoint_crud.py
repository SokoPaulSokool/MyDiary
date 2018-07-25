
class entriescrud():

    def __init__(self, app):
        self.test_client = app.test_client()

    # Fetch all entries

    def test_fetch_all_entries(self):
        return self.test_client.get('/api/v1/entries')

    # Fetch single entries

    def test_fetch_one_entries(self):
        return self.test_client.get('/api/v1/entries/0')

      # Fetch empty entries

    def test_fetch_one_empty_entries(self):
        return self.test_client.get('/api/v1/entries/9')

     # submit entry  up user with the provided args

    def submit_entry(self, entry_title, entry, entry_date):
        return self.test_client.post('/api/v1/entries',
                                     data=dict(entry_title=entry_title,
                                               entry=entry,
                                               entry_date=entry_date
                                               )
                                     )

    # requires name of the field to be skipped and returns a response from sigbup

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
     # submit entry  up user with the provided args

    def submit_put_entry(self, entry_title, entry, entry_date):
        return self.test_client.put('/api/v1/entries/0',
                                    data=dict(entry_title=entry_title,
                                              entry=entry,
                                              entry_date=entry_date
                                              )
                                    )
    # requires name of the field to be skipped and returns a response from sigbup

    def submit_put_entry_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "entry_title":
            return self.test_client.put('/api/v1/entries/0',
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
