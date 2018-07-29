from api.v1.endpoints import app
import unittest
import pytest
# Testing the login feature


class test_login():
    def __init__(self, app):
        self.test_client = app.test_client()

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


test_client = test_login(app)
# tests logging in a single user empty field


@pytest.mark.parametrize("phonenumber,password", [("", "password"), ("name", "")])
def test_login_user_empty_field(phonenumber, password):
    response = test_client.login(phonenumber, password)

    assert response.status_code == 400

# tests login a user with missing field


@pytest.mark.parametrize("value", [("phonenumber"), ("password")])
def test_login_user_missing_field(value):
    response = test_client.login_with_missing_form_value(value)

    assert response.status_code == 400

    # tests logging in wrong password


def test_login_user_wrong_password():
    test_client.user_signup()
    response = test_client.login("12", "120")

    assert response.status_code == 401

    # tests logging in wrong phone


def test_login_user_wrong_phone():
    test_client.user_signup()
    response = test_client.login("12ii", "10")

    assert response.status_code == 401
# tests logging in wrong password


def test_login_user_correct_password():
    test_client.user_signup()
    response = test_client.login("12", "24")

    assert response.status_code == 200
