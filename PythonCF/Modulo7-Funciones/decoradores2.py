def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes del llamado")
        
        resultado = funcion_b(*args, **kwargs)
        
        print(">>> Después del llamado")
    
        return resultado
   
    return funcion_c

@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(10, 20)
print(resultado)