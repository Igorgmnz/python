def derivada(a, b):
    if a / 1 == a:
        print('A derivada de uma constante é 0')
    else:
        a *= b
        b -= 1
        print(f'A derivada é {a}**{b}')
derivada(3)