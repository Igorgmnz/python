while True:

    from random import randint

    numero_sorteado = randint(1, 3)

    print("bem vindo ao jogo de adivinhar!")
    print("escolha um numero de 1 a 3 e teste sua intuição!")
    print("(1) (2) (3)")
    valor_usuario = int(input("insira aqui seu número: "))
    if valor_usuario > 3:
        print("insira um valor entre 1 e 3 jumento!!!")
        break
    if valor_usuario == numero_sorteado:
        print("Parabéns por nada!!! ;)")
    else: print(f"Errou feio, {numero_sorteado} era o certo rs")