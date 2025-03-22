
nome = "Igor Andre Gimenez"

email = "igor@gmail.com"

arroba = email.find("@")

servidor = email[arroba:]

ajuda = nome.find(" ")

primeiro_nome = nome[:ajuda]

arroba_criptografado = email[0]
print(servidor)

print(primeiro_nome)

mensagem = f"usuario {primeiro_nome} foi cadastrado com sucesso usando o email: {email} "

print(mensagem)

mensagem2 = f"enviamos um codigo de confirmacao para o email {arroba_criptografado}***{servidor}"

print(mensagem2)