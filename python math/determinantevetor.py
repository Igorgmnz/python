vetores =[[0, '', 0],
          ['i', 'j', 'k'],
          [0, 0, 0],
          [0, 0, 0],
          ['i', '', 'k']]
contagem1 = 1
for l in range(2, 4):
    contagem = 1
    for c in range(0, 3):
        vetores[l][c] = int(input(f'digite o {contagem}° valor do vetor {contagem1}: '))
        contagem += 1
    contagem1 += 1
vetores[0][0] = vetores[3][0]
vetores[0][2] = vetores[3][2]
print('-=' * 30)
print()
print(f'Vetor 1 = {vetores[2]}')
print(f'Vetor 2 = {vetores[3]}')
print()
print('-=' * 30)
print()
for l in range (0, 5):
    for c in range(0, 3):
        print(f'[{vetores[l][c]:^5}]', end='')
    print()
print()
print('-=' * 30)
print()
i_ = (vetores[2][1] * vetores[3][2]) - (vetores[2][2] * vetores[3][1])
j_ = (vetores[0][0] * vetores[2][2]) - (vetores[0][2] * vetores[2][0])
k_ = (vetores[2][0] * vetores[3][1]) - (vetores[2][1] * vetores[3][0])
print(f'i = {i_}, j = {j_}, k = {k_}')
print()
determinante = (i_ * vetores[2][0]) + (j_ * vetores[2][1]) + (k_ * vetores[2][2])
if determinante != 0:
    print(f'DETERMINANTE: {determinante}, OS VETORES SÃO DEPENDENTES!')
else:
    print(f'DETERMINANTE: {determinante}, OS VETORES SÃO INDEPENDENTES!')
print('-=' * 30)