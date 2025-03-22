import os

mensagens = []

nome = input("insira seu nome: ")

while True:
    #limpando o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    #obtendo o texto
    print("__________________")        
    texto = input("message: ")
    if texto == "fim":
        break

    #add as mensagens na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
    