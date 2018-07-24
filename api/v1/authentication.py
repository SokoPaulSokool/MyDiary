from flask import Flask, render_template, url_for, request, flash

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


diary_users = dict()
# uses post data which must include phone number and password to be used for user authentication


@app.route('/api/v1/login', methods=['POST'])
def login():
    res = ''
    if request.method == 'POST':
        # try:
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
        else:
            res = 'Either "phonenumber" or Poassword" is missing'
        # except:
        #     res = 'Either "name" or "phonenumber" or Poassword" is missing'
    else:
        pass
    return res

# uses post data which must include "phone number", "name", "password"  to be used for user registration


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
            else:
                res = 'Either "name" or "phonenumber" or Poassword" is missing'
        except:
            res = 'Either "name" or "phonenumber" or Poassword" is missing'

    return res


# route to Fetch all entries or create an entry to diary


@app.route('/api/v1/entries', methods=['GET', 'POST'])
def entries():
    return "kool"

# route to Fetch a single entry or Modify an entry


@app.route('/entries/<entryId>', methods=['GET', 'POST'])
def entry():
    return "kool"


if __name__ == '__main__':
    app.run(debug=True)
