contador = 1

while contador <= 10:
    print(contador)

    contador = contador +1

num = 123456789
contador_digitos = 0

while num >= 1:
    contador_digitos += 1
    num = num / 10
else:
    print("Fin de el ciclo While")
print(contador_digitos)
