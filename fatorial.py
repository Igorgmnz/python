#tentativa de criar um cálculo fatorial
n = int(input('digite aqui um número: '))
m = 1
numero = n
for num in range(n):
    fatorial = n * (n - 1)
    m = m * n
    n = n-1
resultado = m
print('O resultado de {}! é {}'.format(numero, m))