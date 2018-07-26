from flask import Flask, render_template, url_for, request, flash, jsonify
import os
app = Flask(__name__)


class User():
    def __init__(self, name, phone_number, password):
        self.name = name
        self.phone_number = phone_number
        self.password = password
        self.isloged_in = False

    def get_user(self):
        return self

    def logout_user(self):
        self.isloged_in = False

    def login_user(self):
        self.isloged_in = True

#  single diary entry


class Entry():
    def __init__(self, entry_id, entry_title, entry, entry_date):
        self.entry_id = entry_id
        self.entry_title = entry_title
        self.entry = entry
        self.entry_date = entry_date

    def serialize(self):
        return {
            'entry_id': self.entry_id,
            'entry_title': self.entry_title,
            'entry': self.entry,
            'entry_date': self.entry_date,
        }


# dictionary to store all users
diary_users = dict()

# Manages all entries


class Entries:
    def __init__(self):
        self.entry_list = []

    def add_entry(self, entry):
        self.entry_list.append(entry)
        id = self.entry_list.index(entry)
        self.entry_list[id].entry_id = id

    def get_entry(self, entry_id):
        try:
            entry_got = self.entry_list[entry_id].serialize()
            return str(entry_got)
        except:
            return "not found"

    def remove_entry(self, entry_id):
        try:
            self.entry_list.pop(entry_id)
            return "deleted"
        except:
            return "not found"

    def replace_entry(self, entry_id, entry):
        if self.get_entry(entry_id) != "not found":
            self.entry_list.pop(entry_id)
            self.add_entry(entry)
            return "success"
        else:
            return "not found"

    def get_string(self):
        items = []
        for u in self.entry_list:
            items.append(u.serialize())
        return jsonify(items)


entry_list = Entries()

# login endpoint


@app.route('/api/v1/login', methods=['POST'])
def login():
    res = ''
    if request.method == 'POST':
        try:
            if request.form['phonenumber'] != None or request.form['password'] != None:
                phonenumber = request.form['phonenumber']
                password = request.form['password']
                if not phonenumber or not password:
                    res = '"phonenumber" or Password" is empty'
                else:
                    if phonenumber in diary_users:
                        current_user = diary_users.get(
                            phonenumber)

                        print(current_user)
                        if current_user.password == password:
                            current_user.login_user()

                        else:
                            current_user.logout_user()

                        if current_user.isloged_in:
                            res = "login success"
                        else:
                            res = "login failed wrong password"
                    else:
                        res = "not yet registered or wrong phonenumber"

        except:
            res = 'Either "phonenumber" or Poassword" is missing'
            return res
    return res

# signup user endpoint


@app.route('/api/v1/signup', methods=['POST'])
def signup():
    res = ''
    if request.method == 'POST':
        try:
            if request.form['name'] != None or request.form['phonenumber'] != None or request.form['password'] != None:
                name = request.form['name']
                phonenumber = request.form['phonenumber']
                password = request.form['password']
                if not name or not phonenumber or not password:
                    res = 'Either "name" or "phonenumber" or Passssword" is empty'
                else:
                    diary_user = User(name, phonenumber, password)
                    if phonenumber in diary_users:
                        res = "exists"
                    else:
                        diary_users[str(phonenumber)] = diary_user
                        res = "added"
        except:
            res = 'Either "name" or "phonenumber" or Poassword" is missing'
            return res
        return res


# endpoint to Fetch all entries or create an entry to diary


@app.route('/api/v1/entries', methods=['GET', 'POST', 'DELETE'])
def entries():
    res = ''
    if request.method == 'GET':
        # add dummy entry
        # entry_one = Entry(1, "My title", "my entry body", "20/ july /2018")
        # entry_list.add_entry(entry_one)
        # returns all entries
        return entry_list.get_string()
    elif request.method == 'POST':
        try:
            if request.form['entry'] != None or request.form['entry_date'] != None or request.form['entry_title'] != None:
                entry = request.form['entry']
                entry_title = request.form['entry_title']
                entry_date = request.form['entry_date']
                entry_id = ""
                if not entry or not entry_title or not entry_date:
                    res = '"entry_title" or "entry" or "entry_date" is empty'
                else:
                    # adds new entry to list of diary entries
                    entry_list.add_entry(
                        Entry(entry_id, entry_title, entry, entry_date))
                    res = "success"
                return res
        except:
            res = 'Either "entry_title" or "entry" or "entry_date"  is missing'
            return res
    elif request.method == 'DELETE':
        try:
            if request.form['entry_id'] != None or request.form['entry'] != None or request.form['entry_date'] != None or request.form['entry_title'] != None:
                entry = request.form['entry']
                entry_title = request.form['entry_title']
                entry_date = request.form['entry_date']
                entry_id = request.form['entry_id']
                if not entry_id or not entry or not entry_title or not entry_date:
                    res = '"entry_id" or "entry_title" or "entry" or "entry_date" is empty'

                else:
                    entrygot = Entry(
                        int(entry_id), entry_title, entry, entry_date)
                    res = entry_list.remove_entry(entrygot.entry_id)
                return res
        except:
            res = 'Either "entry_id"  "entry_title" or "entry" or "entry_date"  is missing'
            return res
# endpoint to Fetch a single entry or Modify an entry


@app.route('/api/v1/entries/<int:entryId>', methods=['GET', 'PUT'])
def single_entries(entryId):
    res = ''
    Id = entryId
    if request.method == 'GET':
        # entry_one = Entry(1, "dd", "kk", "ll")
        # entry_list.add_entry(entry_one)
        # return single entry of a give id
        return str(entry_list.get_entry(entryId))

    elif request.method == 'PUT':
        try:
            if request.form['entry'] != None or request.form['entry_date'] != None or request.form['entry_title'] != None:
                entry = request.form['entry']
                entry_title = request.form['entry_title']
                entry_date = request.form['entry_date']
                id = 1
                if not entry or not entry_title or not entry_date:
                    res = '"entry_title" or "entry" or "entry_date" is empty'
                else:
                    entry = Entry(
                        id, entry_title, entry, entry_date)
                    # replaces entry at a given id with the new data sent
                    res = entry_list.replace_entry(Id, entry)
                return res
        except:
            res = 'Either "entry_title" or "entry" or "entry_date"  is missing'
            return res


app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'this_should_be_configured')
