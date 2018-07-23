
class User():
    def __init__(self, name, phone_number, password):
        self.name = name
        self.phone_number = phone_number
        self.password = password

    def get_user(self):
        return self


if __name__ == "__main__":
    person = User("a", 9, 0)
    print(person.get_user())
