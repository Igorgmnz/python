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

while True:
    print("_______________________________")
    print("Operações: ")
    print("soma(+)")
    print("subtracao(-)")
    print("multiplicacao(*)")
    print("divisao(/)")
    print("potencia(**)")
    print("_______________________________")
    valor1 = int(input("insira um valor: "))
    valor2 = int(input("insira outro valor: "))
    operaçao = input("operaçao desejada: ")
    if operaçao == "soma":
        resultado = funcao_soma(valor1, valor2)
        print("resutado:",valor1, "+", valor2, "=", resultado )

    elif operaçao == "subtracao":
        resultado = funcao_subtraçao(valor1, valor2)
        print("resutado:",valor1, "-", valor2, "=", resultado )

    elif operaçao == "multiplicacao":
        resultado = funcao_multiplicacao(valor1, valor2)
        print("resutado:",valor1, "*", valor2, "=", resultado )

    elif operaçao == "divisao":
        resultado = funcao_divisao(valor1, valor2)
        print("resutado:",valor1, "/", valor2, "=", resultado )

    elif operaçao == "potencia":
        resultado = funcao_potencia(valor1, valor2)
        print("resutado:",valor1, "**", valor2, "=", resultado )
    else:
        print("_______________________________")
        print("insira uma operação valida")
        print("_______________________________")
        break