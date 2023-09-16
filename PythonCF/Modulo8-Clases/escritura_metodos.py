class SerVivo:
    def dormir(self):
        print("El ser duerme.")

class Animal(SerVivo):  #clase padre
       
    def comer(self):
        print("El animal come.")
    
    #def dormir(self):
        #print("El animal duerme.")

class Mascota(Animal):

    def comer(self):
        print("La mascota come")

class Felino:
    
    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino): #Clase hija


    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f"{self.nombre} come.")

    #def dormir(self):
        #print(f"{self.nombre} duerme.")

patricio = Gato("Patricio")

patricio.comer()
patricio.dormir()