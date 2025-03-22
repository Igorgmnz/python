print("Bem vindo ao RPG mais simples do universo!")
print("__________________________________________")
print("A princípio, insira suas informações: ")
print("__________________________________________")
#classes do RPG
classes = [
    {"nome": "barbaro", "hp": 40, "atk": 15},
    {"nome": "curandeiro", "hp": 50, "atk": 8},
    {"nome": "arqueiro", "hp": 35, "atk": 18},
    {"nome": "tank", "hp": 60, "atk": 8},
]
print("__________________________________________")
#informações do usuário
User = {
    "nome": input("insira seu user: "),
    "idade": int(input("insira sua idade: ")),
    "classe": [input("insira sua classe: ")],
}
print("Aqui estão as classes do nosso RPG")
print(classes[0])
print("__________________________________________")
print(classes[1])
print("__________________________________________")
print(classes[2])
print("__________________________________________")
print(classes[3])
print("__________________________________________")
print(User)