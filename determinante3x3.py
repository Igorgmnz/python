matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]
contagem = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para a posição [{l}][{c}]: '))
for l in range(0, 3):
    for c in range(3, 5):
        matriz[l][c] = matriz[l][contagem]
        contagem += 1
    contagem = contagem * 0

print('-=' * 30)
print('MATRIZ:')
print()
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
print('-=' * 30)
print()
det1 = matriz[0][2] * matriz[1][3] * matriz[2][4] + matriz[0][1] * matriz[1][2] * matriz[2][3] + matriz[0][0] * matriz[1][1] * matriz[2][2]
det2 = matriz[0][2] * matriz[1][1] * matriz[2][0] + matriz[0][3] * matriz[1][2] * matriz[2][1] + matriz[0][4] * matriz[1][3] * matriz[2][2]
Determinante = det1 - det2
print(f'A determinante da matriz 3x3 é {Determinante}!')