import os

mensagens = []

nome = input("Nome: ")

while True:


    #limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for x in mensagens:
            print(x['nome'], "-", x['texto'])

    print("___________________")

    #obetendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })    