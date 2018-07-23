from flask import Flask, render_template, url_for, request, flash
from user import User
app = Flask(__name__)

diary_users = []
# uses post data which must include phone number and password to be used for user authentication


@app.route('/login', methods=['POST'])
def login():
    res = ''
    if request.method == 'POST':
        if request.form['phonenumber'] != '00' or request.form['password'] != 'admin':
            res = 'Invalid credentials. Please try again'
        else:
            res = "True"
    return res

# uses post data which must include "phone number", "name", "password"  to be used for user registration


@app.route('/signup', methods=['POST'])
def signup():
    res = ''
    if request.method == 'POST':
        if request.form['name'] != '00' or request.form['phonenumber'] != '00' or request.form['password'] != 'admin':
            res = 'Invalid credentials. Please try again'
        else:
            name = request.form['name']
            phonenumber = request.form['phonenumber']
            password = request.form['password']
            diary_user = User(name, phonenumber, password)
            diary_users.append(diary_user)
            print(diary_users)
    return diary_users.


# route to Fetch all entries or create an entry to diary


@app.route('/entries', methods=['GET', 'POST'])
def entries():
    return "kool"

# route to Fetch a single entry or Modify an entry


@app.route('/entries/<entryId>', methods=['GET', 'POST'])
def entry():
    return "kool"


if __name__ == '__main__':
    app.run(debug=True)
