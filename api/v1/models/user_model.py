

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
