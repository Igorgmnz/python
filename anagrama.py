from math import factorial

palavra = str(input('digite aqui uma palavra: '))

palavra_separada = list(palavra)

contagem = len(palavra)

num = 0
letras_separadas = 0
numero_repetido = []
lista_repeticao = []

for letra in range(contagem):
    if palavra_separada[letras_separadas] in lista_repeticao:
        num = num + 1
    else:
        repeticao = palavra.count(palavra[num])
        num = num + 1
        if repeticao >= 2:
            numero_repetido.append(repeticao)
            lista_repeticao.append(palavra_separada[letras_separadas])
        letras_separadas = letras_separadas + 1

num_ = 0
calculo = 1

for intens in lista_repeticao:
    divisisores = factorial(numero_repetido[num_])
    calculo = calculo * divisisores
    num_ = num_ + 1

resultado = factorial(contagem) / calculo

print(f'A palavra {palavra} tem {contagem} caracteres e {resultado:.0f} anagramas!')