print("Bem vindo à calculadora de médias")

notas = []
quantos_numeros = int(input("quantas notas deseja adicionar?: "))
for i in range (quantos_numeros):
    notas.append(int(input("insira aqui sua nota: ")))
soma = sum(notas)
media = soma / len(notas)
print("A média das suas notas é:", media)