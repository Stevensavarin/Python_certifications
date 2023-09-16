#and, or y not 

#and
resultado_final = True and True 
print(resultado_final)
resultado_final = True and True and True 
print(resultado_final)
resultado_final = True and True and True and False
print(resultado_final)
resultado_final = True and True and 10 > 20
print(resultado_final)
resultado_final = True and True and 100 > 20
print(resultado_final)

#or
resultado_final = True or True or 100 > 20
print(resultado_final)
resultado_final = False or False or 100 > 20
print(resultado_final)
resultado_final = False or False or 10 > 20
print(resultado_final)

#not #convierte True a False y Flase a True
resultado_final = not True
print(resultado_final)
resultado_final = not False
print(resultado_final)






