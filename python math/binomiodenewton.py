import math

conf = []
a = input('valor de a: ')
b = input('valor de b: ')
n = int(input('valor de n: '))
formula = (f'({a} + {b})^^{n}')
ifx = 0
conf.append(list(a))
conf.append(list(b))
if a[0] == 'x':
    a = 1
    ifx += 1
elif 'x' in a:
    a = int(a[0])
    ifx += 1
else:
    a = int(a)

if b[0] == 'x':
    b = 1
    ifx += 1
elif 'x' in b:
    b = int(b[0])
    ifx += 1
else:
    b = int(b)

print(f'sua fórmula: {formula}')
p = int(input(f'qual dos {n + 1} termos gostaria de saber? '))
p -= 1
Tp = (math.factorial(n) / (math.factorial(p) * math.factorial(n - p))) * (a**(n - p)) * b**p
if ifx >= 1:
    if n - p == 0:
        print(f'O resultado do {p} termo é: {Tp:.0f}')
    elif Tp == 1:
        print(f'O resultado do {p} termo é: x^^{n - p}')
    else:
        print(f'O resultado do {p} termo é: {Tp:.0f}x^^{n - p}')
else:
    print(f'O resultado do {p} termo é: {Tp:.0f}')