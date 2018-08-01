import json


class entriescrud():

    def __init__(self, app):
        self.test_client = app.test_client()

    def signup_get_token(self):
        self.test_client.post('/api/v1/auth/signup',
                              data=dict(phonenumber="122",
                                        password="112",
                                        name="kool"
                                        )
                              )
        response = self.test_client.post('/api/v1/auth/login',
                                         data=dict(phonenumber="122",
                                                   password="112"
                                                   )
                                         )
        return json.loads(response.get_data(as_text=True))["access_token"]

    # Fetch all entries

    def test_fetch_all_entries(self):

        return self.test_client.get('/api/v1/entries', headers={'Authorization': 'Bearer ' + self.signup_get_token()})

    # Fetch single entry

    def test_fetch_one_entries(self):
        self.submit_entry("mm", "mm")
        return self.test_client.get('/api/v1/entries/1', headers={'Authorization': 'Bearer ' + self.signup_get_token()})

    # Fetch empty entries

    def fetch_one_empty_entries(self):
        return self.test_client.get('/api/v1/entries/100', headers={'Authorization': 'Bearer ' + self.signup_get_token()})

    # post put entry with the provided args

    def submit_entry(self, entry_title, entry):
        return self.test_client.post('/api/v1/entries',
                                     data=dict(entry_title=entry_title,
                                               entry=entry
                                               ), headers={'Authorization': 'Bearer ' + self.signup_get_token()}
                                     )

    # post entry with some form key  missing

    def submit_entry_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "entry_title":
            return self.test_client.post('/api/v1/entries',
                                         data=dict(entry="entry",
                                                   entry_date="entry_date"
                                                   ), headers={'Authorization': 'Bearer ' + self.signup_get_token()}
                                         )
        if missing_form_name == "entry":
            return self.test_client.post('/api/v1/entries',
                                         data=dict(entry_title="entry_title"
                                                   ), headers={'Authorization': 'Bearer ' + self.signup_get_token()}
                                         )
    # put entry with the provided args

    def submit_put_entry(self, entry_title, entry):
        self.submit_entry("kk", "kk")
        return self.test_client.put('/api/v1/entries/1',
                                    data=dict(entry_title=entry_title,
                                              entry=entry
                                              ), headers={'Authorization': 'Bearer ' + self.signup_get_token()}
                                    )
    # put entry with some form key  missing

    def submit_put_entry_with_missing_form_value(self, missing_form_key):
        self.submit_entry("mm", "mm")
        if missing_form_key == "entry_title":
            return self.test_client.put('/api/v1/entries/1',
                                        data=dict(entry="entry"
                                                  ), headers={'Authorization': 'Bearer ' + self.signup_get_token()}
                                        )
        if missing_form_key == "entry":
            return self.test_client.put('/api/v1/entries/1',
                                        data=dict(entry_title="entry_title"
                                                  ), headers={'Authorization': 'Bearer ' + self.signup_get_token()}
                                        )
    # delete entry with the provided args

    def submit_delete_entry(self):
        self.submit_entry("mm", "mm")
        return self.test_client.delete('/api/v1/entries/1', headers={'Authorization': 'Bearer ' + self.signup_get_token()})

    def submit_delete_empty_entry(self):
        return self.test_client.get('/api/v1/entries/200', headers={'Authorization': 'Bearer ' + self.signup_get_token()})
