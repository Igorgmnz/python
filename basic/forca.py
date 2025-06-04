from random import choice

tentativas = 6
frutas = ['morango', 'abacaxi', 'limao', 'coco', 'mamao', 'manga', 'pitanga']
objetos = ['faca', 'tesoura', 'lapis', 'caneta', 'colher', 'ventilador']
animais = ['vaca', 'gato', 'cachorro', 'rato', 'cavalo', 'macaco']
opcoes = [frutas, objetos, animais]
tema = choice(opcoes)
palavra = choice(tema)
letras = []
while True:
    for letra in palavra:
        if letra.lower() in letras:
            print(letra, end='')
        else:
            print('_ ', end='')
    print('')
    tentativa = input('digite uma letra para tentar: ')
    letras.append(tentativa.lower())
    ganhou = True
    if tentativa not in palavra:
        tentativas -= 1
    for letra in palavra:
        if letra.lower() not in letras:
            ganhou = False
    print(f'Você ainda tem {tentativas} tentativas!')
    if tentativas == 0 or ganhou:
        break
if ganhou:
    print(f'parabéns, você ganhou, a palavra era {palavra}!')

else:
    print(f'você perdeu, a palavra era {palavra}!')