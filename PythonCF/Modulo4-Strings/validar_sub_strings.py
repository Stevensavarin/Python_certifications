titulo_curso = "Curso profesional de Python, donde aprenderemos Python"

contador = titulo_curso.count("o")
print(contador)

print("Python" in titulo_curso)
print("python" in titulo_curso)
print("python" in titulo_curso.lower())
print("python" in titulo_curso.upper())
print("codigofacil" not in titulo_curso.lower())
print(titulo_curso.startswith("Curso"))
print(titulo_curso.startswith("Python"))
print(titulo_curso.endswith("Curso"))
print(titulo_curso.endswith("Python"))