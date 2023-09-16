lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print(lista)

#Menor a mayor
lista.sort()
print(lista) 
print(lista[0]) #obtener numero menor en la lista

#Mayor a menor
lista.sort(reverse=True) 
print(lista)
print(lista[0])#Obtener numero mayor en la lista

print()

#ejemplo 2
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print(lista)
lista.sort()
print(lista)
print(lista[0]) #obtener numero menor en la lista
print(lista[-1])#Obtener numero mayor en la lista

print()

#ejemplo 3
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print(lista)
print(min(lista))
print(max(lista))
#buscar elemento en lista

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print()
print(10 in lista)
print(5 in lista)
