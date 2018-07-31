from api.v1.endpoints import app
import unittest
import pytest
from tests.endpoint_crud import entriescrud

# Testing the entries endpoints


test_client = entriescrud(app)

# tests create entry with missing field value


@pytest.mark.parametrize("value", [("entry_title"), ("entry")])
def test_submit_entry_missing_entry_field(value):
    response = test_client.submit_entry_with_missing_form_value(value)

    # assert response.data == b'Either "entry_title" or "entry" or "entry_date"  is missing'
    assert response.status_code == 400

# tests create entry with an empty entry v
# alue


@pytest.mark.parametrize("entry_title,entry", [("", "entry"), ("entry_title", "")])
def test_submit_entry_with_empty_entry(entry_title, entry):
    response = test_client.submit_entry(entry_title, entry)

    # assert response.data == b'{"message": "entry_title or entry or entry_date is empty"}\n'
    assert response.status_code == 400


# tests create full entry

def test_submit_entry():
    response = test_client.submit_entry("mm", "mmm")

    assert response.status_code == 200


# tests put entry with missing field value

@pytest.mark.parametrize("value", [("entry_title"), ("entry")])
def test_submit_entry_missing_put_entry_field(value):
    response = test_client.submit_put_entry_with_missing_form_value(value)

    assert response.status_code == 400

# tests put entry with an empty entry value


@pytest.mark.parametrize("entry_title,entry", [("", "entry"), ("entry_title", "")])
def test_submit_entry_with_empty_put_entry(entry_title, entry):
    response = test_client.submit_put_entry(entry_title, entry)

    assert response.status_code == 400
    # assert response.data == b'{"message": "entry_title or entry or entry_date is empty"}\n'

# tests put full entry


def test_submit_put_entry():
    response = test_client.submit_put_entry("mm", "mmm")

    assert response.status_code == 200

# tests get single entries


def test_fetch_one_entry_id():
    assert test_client.test_fetch_one_entries().status_code == 200

# tests get non existing  entry


def test_fetch_one_empty_entries():
    assert test_client.fetch_one_empty_entries().status_code == 404

# tests get all entries


def test_fetch_all():
    assert test_client.test_fetch_all_entries().status_code == 200


# tests delete full entry

def test_delete_entry():
    response = test_client.submit_delete_entry()
    assert response.status_code == 200

# tests delete empty entry


def test_delete_empty_entry():
    response = test_client.submit_delete_empty_entry()
    assert response.status_code == 404
