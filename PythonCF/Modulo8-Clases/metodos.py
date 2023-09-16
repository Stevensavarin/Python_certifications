class Usuario:
    
    def inicializar(self, username, password):
        #Añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

user1.inicializar("User1", "password1")
user2.inicializar("User2", "password2")
user3.inicializar("Cody", "password3")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)