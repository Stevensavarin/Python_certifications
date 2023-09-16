class Mascota: #clase padre
    
    def comer(self):
        print("La mascota come.")
    
    def dormir(self):
        print("La mascota duerme.")

class Perro(Mascota): #clase hija
    pass

class Gato(Mascota):
    pass

duke = Perro()

duke.comer()
duke.dormir()

patricio = Gato()

patricio.comer()
patricio.dormir()