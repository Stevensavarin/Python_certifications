#Scope
animal = "León" #Variable global -> función, condición o ciclo

def imprimir_animal():
    animal = "Ballena" #Variable local
    
    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))