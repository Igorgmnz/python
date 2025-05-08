import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

delta = b**2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / 2 * a
x2 = (-b - math.sqrt(delta)) / 2 * a
print(f'As raízes do trinomio {a, b, c} são {x1} e {x2}')