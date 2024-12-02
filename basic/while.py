notas = []

contador = 1

while contador <=5:
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    resultado = [nome, nota]
    notas.append(resultado)

    #alternativa: contador +=1

    contador += 1

print("Quantidade de Notas", len(notas))