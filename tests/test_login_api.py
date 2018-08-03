from api.v1.endpoints import app
import unittest
import pytest
import json
# Testing the login feature


class test_login():
    def __init__(self, app):
        self.test_client = app.test_client()

    # logs in user with the provided args

    def login(self, phonenumber, password):
        return self.test_client.post('/api/v1/auth/login',
                                     data=dict(phonenumber=phonenumber,
                                               password=password
                                               )
                                     )
    # Signup default user for test

    def user_signup(self):
        return self.test_client.post('/api/v1/auth/signup',
                                     data=dict(phonenumber="+256753682060",
                                               password="sokool",
                                               name="kool"
                                               )
                                     )
    # requires name of the field to be skipped and returns a response from login

    def login_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "phonenumber":
            return self.test_client.post('/api/v1/auth/login',
                                         data=dict(name="paul",
                                                   password="5"
                                                   )
                                         )
        if missing_form_name == "password":
            return self.test_client.post('/api/v1/auth/login',
                                         data=dict(name="paul",
                                                   phonenumber="3"
                                                   )
                                         )


test_client = test_login(app)
# tests logging in a single user empty field


@pytest.mark.parametrize("phonenumber,password,key", [("", "password", "phonenumber"), ("name", "", "password")])
def test_login_user_empty_field(phonenumber, password, key):
    response = test_client.login(phonenumber, password)
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "The field '"+key+"' is empty. Please add "+key

# tests login a user with missing field


@pytest.mark.parametrize("value", [("phonenumber"), ("password")])
def test_login_user_missing_field(value):
    response = test_client.login_with_missing_form_value(value)
    data = json.loads(response.get_data(as_text=True))[
        "message"][value]
    assert data == "This field is required"

    # tests logging in wrong password


def test_login_user_wrong_password():
    test_client.user_signup()
    response = test_client.login("+256753682060", "120")
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "login failed  wrong password "

    # tests logging in wrong phone


def test_login_user_wrong_phone():
    test_client.user_signup()
    response = test_client.login("12ii", "10")
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "Login failed  phone number does not exist. First signup "
# tests logging in wrong password


def test_login_user_correct_password():
    test_client.user_signup()
    response = test_client.login("+256753682060", "sokool")
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "user 'kool' has been authorised."
