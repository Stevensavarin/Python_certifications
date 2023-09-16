class User:
    name = "Username por default"
    mail = ""

#__dict__

user1 = User()


user1.name = "Cody"
user1.password = "1234"

print(user1.name)# De instancia

user1.password = "password"

print(id(user1.name))
print(id(User.name))

print(user1.__dict__) #Dict