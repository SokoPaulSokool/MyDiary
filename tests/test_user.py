from api.v1.user import User


def test_add_user():
    person = User('soko', "00", "00")
    assert person.get_user().name == 'sko'
