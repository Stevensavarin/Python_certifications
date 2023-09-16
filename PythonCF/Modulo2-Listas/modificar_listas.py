lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"] 
lista_cursos_2 = ["C", "C++", "Docker"]
print(lista_cursos)
print(len(lista_cursos))

#añadir elementos al final de la lista
lista_cursos.append("MongoDB")
lista_cursos.append("C#")
lista_cursos.append(10)
lista_cursos.append("JavaScript")

#añadir elementos en un indice especifico en la lista
lista_cursos.insert(1, "Rails")
lista_cursos.insert(0, "PyGame")

#Combinar listas
lista_cursos.extend(lista_cursos_2)

print(lista_cursos)
print(len(lista_cursos))

#Eliminar elementos de una lista
lista_cursos.remove("MongoDB")
del lista_cursos[0]

print(lista_cursos)
print(len(lista_cursos))

lista_cursos.clear()
print(lista_cursos)
print(len(lista_cursos))