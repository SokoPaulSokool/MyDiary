from api.v1.authentication import app
import unittest
import pytest

# Testing the signup feature

# checks adding a single user


class test_signup(unittest.TestCase):

    test_client = app.test_client()

    # signs  up user with the provided args

    def signup(self, name, phonenumber, password):
        return self.test_client.post('/signup',
                                     data=dict(name=name,
                                               phonenumber=phonenumber,
                                               password=password
                                               )
                                     )
    # requires name of the field to be skipped and returns a response from sigbup

    def signup_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "name":
            return self.test_client.post('/signup',
                                         data=dict(
                                             phonenumber="3",
                                             password="5"
                                         )
                                         )
        if missing_form_name == "phonenumber":
            return self.test_client.post('/signup',
                                         data=dict(name="paul",
                                                   password="5"
                                                   )
                                         )
        if missing_form_name == "password":
            return self.test_client.post('/signup',
                                         data=dict(name="paul",
                                                   phonenumber="3"
                                                   )
                                         )

    def test_signup_add_user(self):
        response = self.signup("paul", "1", "12")

        assert response.data == b'added'

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
        self.test_client.post('/signup', data=dict(name="soko",
                                                   phonenumber="123",
                                                   password="8"
                                                   )
                              )
        response = self.test_client.post('/signup',
                                         data=dict(name="soko",
                                                   phonenumber="123",
                                                   password="8"
                                                   )
                                         )

        assert response.data == b'exists'
