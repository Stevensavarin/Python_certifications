def promedio(*args):#tupla *
    return sum(args) / len(args)

def usuarios(**kwargs): #Dict **
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], 
         fernando=[10, 9, 9])


def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)
combinacion(1, 2, 3, 4, 5, cody=True, curso="Python")