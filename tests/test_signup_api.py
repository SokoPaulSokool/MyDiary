from api.v1.endpoints import app
import unittest
import pytest
import json
# Testing the signup feature


class test_signup():

    def __init__(self, app):
        self.test_client = app.test_client()

    # signs  up user with the provided args

    def signup(self, name, phonenumber, password):
        return self.test_client.post('/api/v1/auth/signup',
                                     data=dict(name=name,
                                               phonenumber=phonenumber,
                                               password=password
                                               )
                                     )
    # requires name of the field to be skipped and returns a response   from
    # sigbup

    def signup_with_missing_form_value(self, missing_form_name):
        if missing_form_name == "name":
            return self.test_client.post('/api/v1/auth/signup',
                                         data=dict(
                                             phonenumber="3",
                                             password="5"
                                         )
                                         )
        if missing_form_name == "phonenumber":
            return self.test_client.post('/api/v1/auth/signup',
                                         data=dict(name="paul",
                                                   password="5"
                                                   )
                                         )
        if missing_form_name == "password":
            return self.test_client.post('/api/v1/auth/signup',
                                         data=dict(name="paul",
                                                   phonenumber="3"
                                                   )
                                         )


test_client = test_signup(app)
# tests adding a single user


def test_signup_add_user():
    response = test_client.signup("paul", "+256753000000", "password")
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "user 'paul' has been successfully registered. You can now login"

# tests adding a single user empty field


@pytest.mark.parametrize("name,phonenumber,password,key",
                         [("",
                           "phonenumber",
                           "password",
                           "name"),
                          ("name",
                           "",
                           "password",
                           "phonenumber"),
                             ("name",
                              "phonenumber",
                              "",
                              "password"),
                          ])
def test_signup_add_user_empty_field(name, phonenumber, password, key):
    response = test_client.signup(name, phonenumber, password)
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "The field '" + key + "' is empty. Please add " + key


# tests adding a single user with missing field

@pytest.mark.parametrize("value", [("name"), ("phonenumber"), ("password")])
def test_login_user_missing_field(value):
    response = test_client.signup_with_missing_form_value(value)
    data = json.loads(response.get_data(as_text=True))[
        "message"][value]
    assert data == "This field is required"

# Test adding an existing user


def test_signup_add_existing_user():
    test_client.signup("kool", "+256753682060", "sokool")
    response = test_client.signup("kool", "+256753682060", "sokool")
    # assert response.status_code == 401
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "phone number is already being used"
