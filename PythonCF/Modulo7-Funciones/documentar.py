# Docstring
# __doc__ (Módulos, Clases, Métodos, Funciones)

def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parámetros.

    
    #>>> suma(10, 20)
    30

    #>>> suma(100, 200)
    300

    TODO:
        *

    """
    return numero_1 + numero_2

print(suma.__doc__)
# print(help(suma))