from api.v1.endpoints import app
import unittest
import pytest
from tests.endpoint_crud import entriescrud
import json
# Testing the entries endpoints


test_client = entriescrud(app)

# tests create entry with missing field value


@pytest.mark.parametrize("value", [("entry_title"), ("entry")])
def test_submit_entry_missing_entry_field(value):
    response = test_client.submit_entry_with_missing_form_value(value)
    data = json.loads(response.get_data(as_text=True))[
        "message"][value]
    assert data == "This field is required"


@pytest.mark.parametrize(
    "entry_title,entry", [
        ("", "entry"), ("entry_title", "")])
def test_submit_entry_with_empty_entry(entry_title, entry):
    response = test_client.submit_entry(entry_title, entry)
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "entry_title or entry or entry_date is empty"

# tests create full entry


def test_submit_entry():
    response = test_client.submit_entry("mm", "mmm")

    assert response.status_code == 201


# tests put entry with missing field value

@pytest.mark.parametrize("value", [("entry_title"), ("entry")])
def test_submit_entry_missing_put_entry_field(value):
    response = test_client.submit_put_entry_with_missing_form_value(value)
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "entry_title or entry or entry_date is empty"

# tests put entry with an empty entry value


@pytest.mark.parametrize(
    "entry_title,entry", [
        ("", "entry"), ("entry_title", "")])
def test_submit_entry_with_empty_put_entry(entry_title, entry):
    response = test_client.submit_put_entry(entry_title, entry)
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "entry_title or entry or entry_date is empty"

# tests put full entry


def test_submit_put_entry():
    response = test_client.submit_put_entry("mm", "mmm")
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "entry with id '1' has been edited"

# tests get single entries


def test_fetch_one_entry_id():
    response = test_client.test_fetch_one_entries()
    data = json.loads(response.get_data(as_text=True))[
        "entry_id"]
    assert data == 1

# tests get non existing  entry


def test_fetch_one_empty_entries():
    response = test_client.fetch_one_empty_entries()
    data = json.loads(response.get_data(as_text=True))[
        "message"]
    assert data == "entry with id '100' not found"

# tests get all entries


def test_fetch_all():
    response = test_client.test_fetch_all_entries()
    assert response.status_code == 200


# tests delete full entry

def test_delete_entry():
    response = test_client.submit_delete_entry()
    data = json.loads(response.get_data(as_text=True))["message"]
    assert data == "entry with id '1' has been deleted"

# tests delete empty entry


def test_delete_empty_entry():
    response = test_client.submit_delete_empty_entry()
    data = json.loads(response.get_data(as_text=True))["message"]
    assert data == "entry with id '200' not found"
