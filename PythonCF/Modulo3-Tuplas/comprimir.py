lista = [1, 2, 3, 4, 5, 6, 7, 8] #6, 7, 8 el programa no los toma en cuenta ya que las tuplas deben tener la misma cantidad de elementos

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) # -- zip
resultado = tuple(resultado)

print(resultado)
