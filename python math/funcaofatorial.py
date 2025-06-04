def funcao_fatorial(n):
    m = 1
    for i in range(n, 0, -1):
        m *= i
    return m