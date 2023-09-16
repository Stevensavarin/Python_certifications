#Atributos de clase

class Usuario:
    username = "Username por default"
    email = ""

Usuario.username = "User1"
Usuario.email = "info@python.com"

print(Usuario.username)
print(Usuario.email)

print("--------------------------")
#Atributos de instancia

class User:
    name = "Username por default"
    mail = ""

#__dict__

user1 = User()
print(user1.name)

print(user1.__dict__) #Dict