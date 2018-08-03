from api.v1.endpoints import app
import unittest
import pytest
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
    # requires name of the field to be skipped and returns a response   from sigbup

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

    assert response.status_code == 201

# tests adding a single user empty field


@pytest.mark.parametrize("name,phonenumber,password", [("", "phonenumber", "password"), ("name", "", "password"), ("name", "phonenumber", ""), ])
def test_signup_add_user_empty_field(name, phonenumber, password):
    response = test_client.signup(name, phonenumber, password)
    assert response.status_code == 400


# tests adding a single user with missing field

@pytest.mark.parametrize("value", [("name"), ("phonenumber"), ("password")])
def test_login_user_missing_field(value):
    response = test_client.signup_with_missing_form_value(value)
    assert response.status_code == 400

# Test adding an existing user


def test_signup_add_existing_user():
    test_client.test_client.post('/api/v1/auth/signup', data=dict(name="kool",
                                                                  phonenumber="+256753682060",
                                                                  password="sokool"
                                                                  )
                                 )
    response = test_client.test_client.post('/api/v1/auth/signup',
                                            data=dict(name="kool",
                                                      phonenumber="+256753682060",
                                                      password="sokool"
                                                      )
                                            )

    assert response.status_code == 401
