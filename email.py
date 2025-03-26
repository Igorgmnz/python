
nome = "Igor Andre Gimenez"

email = "igor@gmail.com"

arroba = email.find("@")

servidor = email[arroba:]

ajuda = nome.find(" ")

primeiro_nome = nome[:ajuda]

arroba_criptografado = email[0]
print(servidor)

print(primeiro_nome)

mensagem = ('usuario {} foi cadastrado com sucesso usando o email: {}'.format(primeiro_nome, email))

print(mensagem)

mensagem2 = ('enviamos um codigo de confirmacao para o email {}***{}'.format(arroba_criptografado, servidor))

print(mensagem2)