class Animal():  #clase padre
       
    def comer(self):
        print("El animal come.")
    
    def dormir(self):
        print("El animal duerme.")

class Mascota(Animal): 
    pass

class Felino:
    
    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino): #Clase hija
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()

