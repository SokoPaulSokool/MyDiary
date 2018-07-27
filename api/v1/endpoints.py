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


class ResponseMessage():
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def response(self):
        response = self.message, self.code
        return response


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


class KoolConverter():
    @staticmethod
    def turple_list_to_entry_list(turple_list):
        new_list = []
        for item in turple_list:
            ent = Entry(item[0], item[1], item[2], item[3])
            new_list.append(ent)
        return new_list

    @staticmethod
    def turple_to_entry(turple):
        ent = Entry(turple[0], turple[1], turple[2], turple[3])
        return ent



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
        self.entry_list.clear()

    def get_entry(self, entry_id):
        try:
            entry_got_from_list = self.entry_list[entry_id].serialize()
            return str(entry_got_from_list)
        except:
            return ResponseMessage("not found", 404).response()

    def remove_entry(self, entry_id):
        try:
            self.entry_list.pop(entry_id)
            return ResponseMessage("deleted", 200).response()
        except:
            return ResponseMessage("not found", 404).response()

    def replace_entry(self, entry_id, entry):
        if self.get_entry(entry_id) != "not found":
            self.entry_list.pop(entry_id)
            self.add_entry(entry)
            return ResponseMessage("success", 200).response()
        else:
            return ResponseMessage("not found", 404).response()

    def get_string(self):
        items = []
        for item in self.entry_list:
            items.append(item.serialize())
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
                    res = ResponseMessage(
                        '"phonenumber" or Password" is empty', 400).response()
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
                            res = ResponseMessage(
                                "login success", 200).response()
                        else:
                            res = ResponseMessage(
                                "login failed wrong password", 401).response()
                    else:
                        res = ResponseMessage(
                            "not yet registered or wrong phonenumber", 401).response()

        except:
            res = ResponseMessage(
                'Either "phonenumber" or Poassword" is missing', 400).response()
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
                    res = ResponseMessage(
                        'Either "name" or "phonenumber" or Passssword" is empty', 400).response()
                else:
                    diary_user = User(name, phonenumber, password)
                    if phonenumber in diary_users:
                        res = ResponseMessage("exists", 401).response()
                    else:
                        diary_users[str(phonenumber)] = diary_user
                        res = ResponseMessage("added", 200).response()
        except:
            res = ResponseMessage(
                'Either "name" or "phonenumber" or Poassword" is missing', 400).response()
            return res
        return res


# endpoint to Fetch all entries or create an entry to diary


@app.route('/api/v1/entries', methods=['GET', 'POST', 'DELETE'])
def entries():
    res = ''
    if request.method == 'GET':
        return ResponseMessage(entry_list.get_string(), 200).response()
    elif request.method == 'POST':
        try:
            if request.form['entry'] != None or request.form['entry_date'] != None or request.form['entry_title'] != None:
                entry = request.form['entry']
                entry_title = request.form['entry_title']
                entry_date = request.form['entry_date']
                entry_id = ""
                if not entry or not entry_title or not entry_date:
                    res = ResponseMessage(
                        '"entry_title" or "entry" or "entry_date" is empty', 400).response()
                    return res
                else:
                    # adds new entry to list of diary entries
                    entry_list.add_entry(
                        Entry(entry_id, entry_title, entry, entry_date))
                    res = ResponseMessage("success", 200).response()
                    return res
            else:
                res = ResponseMessage(
                    'Either "entry_title" or "entry" or "entry_date"  is missing', 400).response()
                return res
        except:
            res = ResponseMessage(
                'Either "entry_title" or "entry" or "entry_date"  is missing', 500).response()
            return res

# endpoint to Fetch a single entry or Modify an entry


@app.route('/api/v1/entries/<int:entryId>', methods=['GET', 'PUT', 'DELETE'])
def single_entries(entryId):
    res = ''
    Id = entryId
    if request.method == 'GET':
        return entry_list.get_entry(entryId)

    elif request.method == 'PUT':
        try:
            if request.form['entry'] != None or request.form['entry_date'] != None or request.form['entry_title'] != None:
                entry = request.form['entry']
                entry_title = request.form['entry_title']
                entry_date = request.form['entry_date']
                id = 1
                if not entry or not entry_title or not entry_date:
                    res = '"entry_title" or "entry" or "entry_date" is empty'
                    return ResponseMessage(res, 400).response()
                else:
                    entry = Entry(
                        id, entry_title, entry, entry_date)
                    # replaces entry at a given id with the new data sent
                    res = entry_list.replace_entry(Id, entry)
                    return ResponseMessage(res, 200).response()
            else:
                res = ResponseMessage(
                    'Either "entry_title" or "entry" or "entry_date"  is missing', 400).response()
                return res

        except:
            res = ResponseMessage(
                'Either "entry_title" or "entry" or "entry_date"  is missing', 500).response()
            return res
    elif request.method == 'DELETE':
        res = entry_list.remove_entry(Id)
        return ResponseMessage(res, 200).response()


app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'this_should_be_configured')
