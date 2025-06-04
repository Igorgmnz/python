num = int(input('digite aqui um número: '))
m = 1
for i in range(num, 0, -1):
    m = m * i
print(f'O resultado de {num}! é {m}')