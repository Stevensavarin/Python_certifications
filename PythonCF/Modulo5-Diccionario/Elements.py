diccionario = {"a": 1, 
               "b": 2,
               "c": 3,
               "d": 4
               }
print("a" in diccionario)
print("z" in diccionario)
#get
value = diccionario.get("a")
print(value)
value = diccionario.get("z", "La llave no existe en el dict.")
print(value)
#setdefault
value = diccionario.setdefault("e", 5)
print(value)
print(diccionario)