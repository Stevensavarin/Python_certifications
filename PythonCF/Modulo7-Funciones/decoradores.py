"""
a -> La función principal (Decorador)
b -> La función de decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado")
        funcion_b()
        print("Nos econtramos en la función C")
        print(">>> Después del llamado")
    return funcion_c

@funcion_a
def saludar():
    print("Hola, Nos encontramos en una función")

saludar()