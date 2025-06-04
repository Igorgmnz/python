def funcao_soma(valor1, valor2):
    return(valor1 + valor2)

def funcao_subtraçao(valor1, valor2):
    return(valor1 - valor2)

def funcao_multiplicacao(valor1, valor2):
    return(valor1 * valor2)

def funcao_divisao(valor1, valor2):
    return(valor1 / valor2)

def funcao_potencia(valor1, valor2):
    return(valor1 ** valor2)

def funcao_divisaoint(valor1, valor2):
    return(valor1 // valor2)

def funcao_resto(valor1, valor2):
    return(valor1 % valor2)

while True:
    print("_______________________________")
    print('\n Operações:\n Soma(+) \n subtração(-) \n multiplicação(*) \n divisão(/) \n divisão inteira(//) \n resto(%) \n potencia(**) \n  ')
    print("_______________________________")
    valor1 = int(input("insira um valor: "))
    operaçao = input("operaçao desejada: ")
    valor2 = int(input("insira outro valor: "))
    if operaçao == "+":
        resultado = funcao_soma()

    elif operaçao == "-":
        resultado = funcao_subtraçao()

    elif operaçao == "*":
        resultado = funcao_multiplicacao()

    elif operaçao == "/":
        resultado = funcao_divisao()

    elif operaçao == "**":
        resultado = funcao_potencia()

    elif operaçao == '//':
        resultado = funcao_divisaoint()

    elif operaçao == '%':
        resultado = funcao_resto()

    else:
        print("_______________________________")
        print("insira uma operação valida")
        print("_______________________________")
        break
    print('O resultado de {} {} {} = {:.1f}'.format(valor1, operaçao, valor2, resultado))
    break