promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 90

print(promedio(10, 10, 9, 8, 7))
print(aprobatorio(5))

def mostar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con {promedio}.")
    else:
        print("No aprobaste la materia.")

mostar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)