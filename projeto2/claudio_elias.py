# Projeto 2
# Alunos: Claudio Coelho da Silva Junior (120.038.029) e Elias da Silva Dutra (220.038.092)
# Linguagens de Programação para Engenharia
# TEE00140

lista_cadastro = []
lista_carrinho = []
lista_preco = []
lista_valorproduto = []
lista_contador = []
lista_resultado = []
lista_carrinho_final = []
opcao = ' '
cadastro = ' '
compra = ' '
lista = ' '
carrinho = ' '
preco = ' '
contador = 0
x = 0

while opcao != 5:

    cadastro = ' '
    compra = ' '
    lista = ' '
    carrinho = ' '
    repetidos = 0

    print(f'''\n   MENU
        [1] Cadastrar produto
        [2] Comprar
        [3] Listar produtos
        [4] Visualizar carrinho
        [5] Sair\n''')
    opcao = int(input('Escolha uma opção de 1 a 5: '))

    if opcao == 1:
        while cadastro != "Menu":
            cadastro = input('Para cadastrar, digite o nome do produto ou "Menu" para voltar ao menu: ').capitalize()
            if cadastro in lista_cadastro:
                print('Produto já cadastrado.')
            if cadastro != 'Menu' and cadastro not in lista_cadastro:
                lista_cadastro.append(cadastro)
                preco = int(input('Digite o preço do produto: '))
                lista_preco.append(preco)

    if opcao == 2:
        while compra != "Menu":
            print(f'Produtos disponíveis: {lista_cadastro}')
            compra = input('Para comprar, digite o nome do produto ou "Menu" para voltar ao menu: ').capitalize()
            if compra in lista_carrinho and compra in lista_cadastro:
                repetidos = int(input('Produto já adicionado ao carrinho. '
                                      'Qual a quantidade desse produto que você deseja adicionar ao carrinho? '))
                for k in range(repetidos - 1):
                    lista_carrinho.append(compra)
            if compra in lista_cadastro:
                lista_carrinho.append(compra)
            if compra not in lista_cadastro and compra != 'Menu':
                print('Produto não disponível. Escolha um dos produtos cadastrados.')

    if opcao == 3:
        while lista != 'Menu':
            lista = input('Para exibir a lista, digite "lista" ou "Menu" para voltar ao menu: ').capitalize()
            if lista == 'Lista':
                print(f'Os produtos cadastrados são: {lista_cadastro}')

    if opcao == 4:
        while carrinho != 'Menu':
            carrinho = input('Para exibir o carrinho de compras, '
                             'digite "carrinho" ou "Menu" para voltar ao menu: ').capitalize()
            if carrinho == 'Carrinho':
                print(f'Seu carrinho de compras:')
                for i in set(lista_carrinho):
                    print(f'{lista_carrinho.count(i)} {i}')

lista_valorproduto = dict(zip(lista_cadastro, lista_preco))
lista_valorfinal = lista_valorproduto.values()
lista_valorfinal2 = list(lista_valorfinal)
lista_valorfinal2int = list(map(int, lista_valorfinal2))

for b in lista_carrinho:
    if b not in lista_carrinho_final:
        lista_carrinho_final.append(b)

for x in (lista_carrinho_final):
    contador = lista_carrinho.count(x)
    lista_contador.append(contador)

for a in range(0, len(lista_valorfinal2int)):
    lista_resultado.append(lista_valorfinal2int[a] * lista_contador[a])

print(f'\nCompra finalizada! Seu pedido:\n')

for j in lista_carrinho_final:
    print(f'{lista_carrinho.count(j)} {j}')

print(f'O valor da sua compra foi de {sum(lista_resultado)} R$')

print(f'\nParabéns pela sua aquisição, volte sempre!')