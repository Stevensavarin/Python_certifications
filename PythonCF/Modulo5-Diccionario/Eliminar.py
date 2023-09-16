diccionario = {"a": 1,
               "b": 2,
               "c": 3,
               "d": 4
               }

del diccionario["a"] # 1 to delete
print(diccionario)
#pop
valor = diccionario.pop("b") #2 to delete
print(valor)
print(diccionario)
#clear
diccionario.clear()
print(diccionario)