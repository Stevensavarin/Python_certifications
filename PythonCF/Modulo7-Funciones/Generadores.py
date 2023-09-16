def pares(): #Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        yield numero

        print("Se reanuda la ejecución")

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print("El generador finalizo")
        break
