n = int(input('digite aqui um número: '))
m = 1
for num in range(n):
    fatorial = n * (n - 1)
    m = m * n
    n = n-1
resultado = m
print(resultado)