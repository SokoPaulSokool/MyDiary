from api.v1.endpoints import app
import unittest
import pytest
from tests.endpoint_crud import entriescrud

# Testing the entries endpoints


test_client = entriescrud(app)

# tests create entry with missing field value


@pytest.mark.parametrize("value", [("entry_date"), ("entry"), ("entry_date")])
def test_submit_entry_missing_entry_field(value):
    response = test_client.submit_entry_with_missing_form_value(value)

    assert response.data == b'Either "entry_title" or "entry" or "entry_date"  is missing'

# tests create entry with an empty entry value


@pytest.mark.parametrize("entry_title,entry,entry_date", [("", "entry", "entry_date"), ("entry_title", "", "entry_date"), ("entry_title", "entry", "")])
def test_submit_entry_with_empty_entry(entry_title, entry, entry_date):
    response = test_client.submit_entry(entry_title, entry, entry_date)

    assert response.data == b'"entry_title" or "entry" or "entry_date" is empty'


# tests create full entry

def test_submit_entry():
    response = test_client.submit_entry("mm", "mmm", "mmm")

    assert response.data == b'success'


# tests put entry with missing field value

@pytest.mark.parametrize("value", [("entry_date"), ("entry"), ("entry_date")])
def test_submit_entry_missing_put_entry_field(value):
    response = test_client.submit_put_entry_with_missing_form_value(value)

    assert response.data == b'Either "entry_title" or "entry" or "entry_date"  is missing'

# tests put entry with an empty entry value


@pytest.mark.parametrize("entry_title,entry,entry_date", [("", "entry", "entry_date"), ("entry_title", "", "entry_date"), ("entry_title", "entry", "")])
def test_submit_entry_with_empty_put_entry(entry_title, entry, entry_date):
    response = test_client.submit_put_entry(entry_title, entry, entry_date)

    assert response.data == b'"entry_title" or "entry" or "entry_date" is empty'

# tests put full entry


def test_submit_put_entry():
    response = test_client.submit_put_entry("mm", "mmm", "mmm")

    assert response.status_code == 200

# tests get single entries


def test_fetch_one_entry_id():
    assert test_client.test_fetch_one_entries().status_code == 200

# tests get non existing  entry


def test_fetch_one_empty_entries():
    assert test_client.test_fetch_one_empty_entries().status_code == 200

# tests get all entries


def test_fetch_all():
    assert test_client.test_fetch_all_entries().status_code == 200


# tests delete entry with missing field value


@pytest.mark.parametrize("value", [("entry_id"), ("entry_date"), ("entry"), ("entry_date")])
def test_delete_entry_missing_entry_field(value):
    response = test_client.submit_delete_entry_with_missing_form_value(value)

    assert response.data == b'Either "entry_id"  "entry_title" or "entry" or "entry_date"  is missing'

# tests delete entry with an empty entry value


@pytest.mark.parametrize("entry_id,entry_title,entry,entry_date", [
    ("", "entry_title", "entry", "entry_date"),
    ("entry_id", "", "entry", "entry_date"),
    ("entry_id", "entry_title", "", "entry_date"),
    ("entry_id", "entry_title", "entry", "")
])
def test_delete_entry_with_empty_entry(entry_id, entry_title, entry, entry_date):
    response = test_client.submit_delete_entry(
        entry_id, entry_title, entry, entry_date)

    assert response.data == b'"entry_id" or "entry_title" or "entry" or "entry_date" is empty'


# tests delete full entry

def test_delete_entry():
    response = test_client.submit_delete_entry(1, "mm", "mmm", "mmm")

    assert response.data == b'deleted'
