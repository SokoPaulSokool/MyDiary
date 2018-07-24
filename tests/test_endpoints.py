from api.v1.endpoints import app
import unittest
import pytest

# Testing the login feature


class test_login(unittest.TestCase):
    test_client = app.test_client()

    # logs in user with the provided args

    def login(self, phonenumber, password):
        return self.test_client.post('/api/v1/login',
                                     data=dict(phonenumber=phonenumber,
                                               password=password
                                               )
                                     )
    # Signup default user for test

    def user_signup(self):
        return self.test_client.post('/api/v1/signup',
                                     data=dict(phonenumber="12",
                                               password="24",
                                               name="kool"
                                               )
                                     )
    # requires name of the field to be skipped and returns a response from login

    def login_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "phonenumber":
            return self.test_client.post('/api/v1/login',
                                         data=dict(name="paul",
                                                   password="5"
                                                   )
                                         )
        if missing_form_name == "password":
            return self.test_client.post('/api/v1/login',
                                         data=dict(name="paul",
                                                   phonenumber="3"
                                                   )
                                         )

    # tests logging in a single user empty phonenumber

    def test_login_user_empty_phonenumber(self):
        response = self.login("", "12")

        assert response.data == b'"phonenumber" or Password" is empty'

    # tests logging in a single user empty Passssword

    def test_login_user_empty_password(self):
        response = self.login("1", "")
        assert response.data == b'"phonenumber" or Password" is empty'

      # tests login a  user with missing phonenumber

    def test_login_user_missing_phomenumber_field(self):
        response = self.login_with_missing_form_value("phonenumber")

        assert response.data == b'Either "phonenumber" or Poassword" is missing'

    # tests login a user with missing password

    def test_login_user_missing_password_field(self):
        response = self.login_with_missing_form_value("password")

        assert response.data == b'Either "phonenumber" or Poassword" is missing'

     # tests logging in wrong password

    def test_login_user_wrong_password(self):
        self.user_signup()
        response = self.login("12", "120")

        assert response.data == b'login failed wrong password'

      # tests logging in wrong phone

    def test_login_user_wrong_phone(self):
        self.user_signup()
        response = self.login("12ii", "10")

        assert response.data == b'not yet registered or wrong phonenumber'

# Testing the signup feature


class test_signup(unittest.TestCase):

    test_client = app.test_client()

    # signs  up user with the provided args

    def signup(self, name, phonenumber, password):
        return self.test_client.post('/api/v1/signup',
                                     data=dict(name=name,
                                               phonenumber=phonenumber,
                                               password=password
                                               )
                                     )
    # requires name of the field to be skipped and returns a response from sigbup

    def signup_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "name":
            return self.test_client.post('/api/v1/signup',
                                         data=dict(
                                             phonenumber="3",
                                             password="5"
                                         )
                                         )
        if missing_form_name == "phonenumber":
            return self.test_client.post('/api/v1/signup',
                                         data=dict(name="paul",
                                                   password="5"
                                                   )
                                         )
        if missing_form_name == "password":
            return self.test_client.post('/api/v1/signup',
                                         data=dict(name="paul",
                                                   phonenumber="3"
                                                   )
                                         )
    # tests adding a single user

    def test_signup_add_user(self):
        response = self.signup("paul", "1", "12")

        assert response.data == b'added'

    # tests adding a single user empty name

    def test_signup_add_user_empty_name(self):
        response = self.signup("", "1", "12")

        assert response.data == b'Either "name" or "phonenumber" or Passssword" is empty'

    # tests adding a single user empty phonenumber

    def test_signup_add_user_empty_phonenumber(self):
        response = self.signup("paul", "", "12")

        assert response.data == b'Either "name" or "phonenumber" or Passssword" is empty'

    # tests adding a single user empty Passssword

    def test_signup_add_user_empty_password(self):
        response = self.signup("paul", "1", "")

        assert response.data == b'Either "name" or "phonenumber" or Passssword" is empty'

    # tests adding a single user with missing name

    def test_signup_add_user_missing_name_field(self):
        response = self.signup_with_missing_form_value("name")

        assert response.data == b'Either "name" or "phonenumber" or Poassword" is missing'

    # tests adding a single user with missing phonenumber

    def test_signup_add_user_missing_phomenumber_field(self):
        response = self.signup_with_missing_form_value("phonenumber")

        assert response.data == b'Either "name" or "phonenumber" or Poassword" is missing'

    # tests adding a single user with missing password

    def test_signup_add_user_missing_password_field(self):
        response = self.signup_with_missing_form_value("password")

        assert response.data == b'Either "name" or "phonenumber" or Poassword" is missing'

    # Test adding an existing user

    def test_signup_add_existing_user(self):
        self.test_client.post('/api/v1/signup', data=dict(name="soko",
                                                          phonenumber="123",
                                                          password="8"
                                                          )
                              )
        response = self.test_client.post('/api/v1/signup',
                                         data=dict(name="soko",
                                                   phonenumber="123",
                                                   password="8"
                                                   )
                                         )

        assert response.data == b'exists'


# Testing the entries feature
class test_entries(unittest.TestCase):
    test_client = app.test_client()

    # Fetch all entries

    def test_fetch_all_entries(self):
        response = self.test_client.get('/api/v1/entries')
        assert response.status_code == 200

    # Fetch single entries

    def test_fetch_one_entries(self):
        response = self.test_client.get('/api/v1/entries/0')
        assert response.status_code == 200

      # Fetch empty entries

    def test_fetch_one_empty_entries(self):
        response = self.test_client.get('/api/v1/entries/9')
        assert response.status_code == 200

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
       # tests adding a single user with missing name

    def test_submit_entry_missing_entry_title_field(self):
        response = self.submit_entry_with_missing_form_value("entry_title")

        assert response.data == b'Either "entry_title" or "entry" or "entry_date"  is missing'

        # tests adding a single user with missing entry

    def test_submit_entry_missing_entry_field(self):
        response = self.submit_entry_with_missing_form_value("entry")

        assert response.data == b'Either "entry_title" or "entry" or "entry_date"  is missing'

        # tests adding a single user with missing name

    def test_submit_entry_missing_entry_date_field(self):
        response = self.submit_entry_with_missing_form_value("entry_date")

        assert response.data == b'Either "entry_title" or "entry" or "entry_date"  is missing'

     # tests adding a single user empty entry title

    def test_submit_entry_with_empty_entry_title(self):
        response = self.submit_entry("", "dd", "dd")

        assert response.data == b'"entry_title" or "entry" or "entry_date" is empty'

    # tests adding a single user empty entry

    def test_submit_entry_with_empty_entry(self):
        response = self.submit_entry("mm", "", "dd")

        assert response.data == b'"entry_title" or "entry" or "entry_date" is empty'

    # tests adding a single user empty entry  date

    def test_submit_entry_with_empty_entry_date(self):
        response = self.submit_entry("mm", "mmm", "")

        assert response.data == b'"entry_title" or "entry" or "entry_date" is empty'

    # tests adding a single user empty entry  date

    def test_submit_entry(self):
        response = self.submit_entry("mm", "mmm", "mmm")

        assert response.data == b'success'
