# for = percorre sequencias, repetindo acoes para cada elemento
# while = loop que execute acoes enquanto as condicoes forem verdadeiras

notas = []

for x in range(3):
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    resultado = [nome, nota]
    notas.append(resultado)

print("Quantidades de notas", len(notas))

for n in notas:
    nome_aluno = n[0]
    nota_aluno = n[1]
    print(nome_aluno, nota_aluno)