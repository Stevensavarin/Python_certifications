class Usuario:

    #__init__
    # object
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

user1 = Usuario("user1", "password1")
user2 = Usuario("user2", "password2")
user3 = Usuario("user3", "password3")

user4 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)