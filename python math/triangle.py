import math

quest1 = str(input('qual tipo de triangulo? '))
if quest1 == '1':
    l1 = int(input('insira a base: '))
    l2 = int(input('insira a altura: '))
    area = l1 * l2 / 2
    print(f'A área é: {area}')
elif quest1 == '2':
    l1 = int(input('insira a base: '))
    l2 = int(input('insira o valor da diagonal: '))
    altura =  math.sqrt(l2**2 - (l1 / 2)**2)
    area = l1 * altura / 2
    print(f'A área é: {area}')
if quest1 == '3':
    print()
    quest2 = (int(input(f'Selecione o lado do triangulo: ')))
    area = quest2**2 * math.sqrt(3) / 4
    print(f'A área é: {area}')