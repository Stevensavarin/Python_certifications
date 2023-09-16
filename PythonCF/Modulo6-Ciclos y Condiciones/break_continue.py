curso = "Curso profesional de Python"

for caracter in curso:
    if caracter == "o":
        break

    print(caracter)

    curso = "Curso profesional de Python"

print("".center(50, "."))

for caracter in curso:
    if caracter == " ":
        continue

    print(caracter)