while True:


  precos = [1500, 1000, 800, 2000]
 
  produtos = ["celular", "camera", "fone de ouvido", "monitor"]

  adicao_de_produto = input("digite o produto para inserir: ")
  produtos.append(adicao_de_produto)

  adicao_de_produto = adicao_de_produto.lower()

  adicao_de_preco = input(("digite o preço do produto: "))
  precos.append(int(adicao_de_preco))

  print("atualizacao de lista: ")
  print(produtos)
  print(precos)
  pergunta = input("deseja cadastrar outro produto? ")
  pergunta = pergunta.lower()
  if pergunta == "nao":
    break