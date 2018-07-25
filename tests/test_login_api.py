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
