#Projeto 2#
#Gabrielle Moura da Silva Barroso e Vinícius Vieira de Brito Silva#
#Linguagens de Programação#


print('Seja bem vindo ao programa')

catálogo = []
preço = []
carrinho = []
preçototal = []
quantidade = []
def menu():
  print("""
Menu
0 - Finalizar programa
1 - Cadastrar produto
2 - Comprar produtos
3 - Ver carrinho e alterar produto
4 - Finalizar compra
""")


menu()
decisão = int(input('Digite sua escolha: '))
while decisão == 1:
  print('\n')
  item = input("Digite o produto que quer cadastrar: ")
  if item in catálogo:
    decisão = int(input('Produto já cadastrado anteriormente. Deseja cadastrar outro produto? 1 - SIM , 5 - NÃO:  '))
    print('\n')
    if decisão == 5:
      print('Os produtos cadastrados foram: ', catálogo)
      menu()
      decisão = int(input('Digite sua escolha: '))
  else: 
    catálogo.append(item)
    x = float(input('Digite o preço do produto: '))
    preço.append(x)
    print('\n')
    decisão = int(input('Deseja cadastrar outro produto? 1 - SIM , 5 - NÃO: '))
    if decisão == 5:
      print('\n')
      print('Os produtos cadastrados foram: ', catálogo)
      print('Com os seguintes preços respectivamente: ', preço)
      menu()
      decisão = int(input('Digite sua escolha: '))
while decisão == 2:
  print('\n')
  print('O catálogo é: ', catálogo)
  
  y = input('Escolha o produto que quer comprar: ')

  carrinho.append(y)
  p = catálogo.index(y)
  print('\n')
  quant = int(input('Digite a quantidade do produto: '))
  quantidade.append(quant)
  preçototal.append(preço[p])
  print('\n')
  decisão = int(input('Deseja comprar outro produto? : 2 - SIM , 5 - NÃO: '))
  if decisão == 5:
    print('\n')
    print('Compra efetuada.')
    menu()
    decisão = int(input('Digite sua escolha: '))
    
while decisão == 3:
  print('\n')
  print('Seu carrinho tem:', carrinho)
  print('\n')
  alterar = int(input('Deseja alterar algum produto ou quantidade do seu produto? 1 - SIM , 2 - NÃO:  '))
  while alterar == 1:
    print('\n')
    pos = int(input('Digite a posição do seu produto: '))
    posreal = pos-1
    ação = int(input('O que deseja fazer? 1 - REMOVER PRODUTO , 2 - ALTERAR QUANTIDADE:   '))
    if ação == 1:
      carrinho[posreal] = "REMOVIDO"
      preçototal[posreal] = 0
      print('\n')
      alterar = int(input('Deseja continuar removendo produtos? 1 - SIM , 2 - NÃO:  '))
      if alterar == 2:
        menu()
        decisão = int(input('Digite sua escolha: '))
    if ação == 2:
      print('\n')
      quantnova = int(input('Digite a quantidade nova: '))
      quantidade[posreal] = quantnova
      alterar = int(input('Deseja continuar removendo produtos? 1 - SIM , 2 - NÃO:  '))
      if alterar == 2:
        menu()
        decisão = int(input('Digite sua escolha: '))
while decisão == 4:
  print('\n')
  print('Os itens comprados foram: ',carrinho)
  produto = [x*y for x,y in zip(quantidade,preçototal)]
  print('Com um valor total de: R$% .2f' % (sum(produto)))
  decisão = 0

if decisão == 0:
  print('\n')
  print('Obrigado por utilizar o programa.')