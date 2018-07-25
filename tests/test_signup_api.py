from api.v1.endpoints import app
import unittest
import pytest
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
