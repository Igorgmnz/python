from random import randint
from time import sleep



numero_sorteado = randint(1, 3)

print("bem vindo ao jogo de adivinhar!")
print("escolha um numero de 1 à 3 e teste sua intuição!")
print('\033[7;30;40m-=-\033[m' * 20)
print('\033[3;32;40m                      (1) (2) (3)                           \033[m')
print('\033[7;30;40m-=-\033[m' * 20)
valor_usuario = int(input("insira aqui seu número: "))
print('\033[31mPROCESSANDO...\033[m')
sleep(3)
if valor_usuario > 3:
    print("insira um valor entre 1 e 3 jumento!!!")
if valor_usuario == numero_sorteado:
    print(f"Parabéns, realmente era \033[32m{valor_usuario}\033[m!")
else: print(f"Errou feio, \033[31m{numero_sorteado}\033[m era o número certo rs")