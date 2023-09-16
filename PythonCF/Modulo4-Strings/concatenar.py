nombre = "Pepito Pepito"
apellido = "Garcia"

nombre_completo = "Mr." + nombre + " " + apellido + "."
print(nombre_completo)

nombre_completo = "Mr.%s %s %s." %(nombre, apellido, "Perez")
print(nombre_completo)

nombre_completo = "Mr.{} {} {}.".format(nombre, apellido,"Perez")
print(nombre_completo)