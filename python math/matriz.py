matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
contagem = 1
maior = 0
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para a posição [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        if contagem == 2:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    contagem += 1
print('-=' * 30)
print()
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
print('-=' * 30)
print(f'a soma da coluna 2 é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'a soma dos numeros pares é {sum(pares)}')
print(f'o maior numero da linha 2 é o {maior}')