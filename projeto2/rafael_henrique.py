# PRATICANDO PYTHON - PROJETO 2
# ALUNOS: HENRIQUE MACEDO TORRES, RAFAEL ECKHARDT LUCENA
# TEE00140 - LINGUAGENS DE PROGRAMAÇÃO PARA ENGENHARIA

produtos = []
preco = []
carpro = []
carpre = []
carquan = []
opcao = 0
conf = 1
conf_2 = 1
contcar = 0
i = 0
k = 0
h = 0
u = 0
total = 0

while opcao != 5:
    print('''    [1] Cadastrar produtos
    [2] Mostrar produtos
    [3] Comprar produtos
    [4] Mostrar carrinho
    [5] Sair do programa''')
    opcao = int(input('>>Qual sua opção? '))
    if opcao == 1:
        while conf == 1:
            if conf == 1:
                prod = str(input('Digite o produto a ser cadastrado: '))
                produtos.append(prod)
                p = float(input('Digite o preço do produto: '))
                preco.append(p)
                i = i + 1
                conf = int(input('Digite 1 para cadastrar novos produtos e 2 para parar: '))

    elif opcao == 2:
        for k in range(0, i, 1):
            j = k + 1
            print('Produto ', j, ':', produtos[k], 'PreçoR$:', preco[k])
    elif opcao == 3:
        while conf_2 == 1:
            if conf_2 == 1:
                c = int(input('Digite o número do produto a ser comprado: '))
                carpro.append(c)
                carpre.append(preco[c - 1])
                carquan.append(1)
                contcar = contcar + 1
                if contcar >= 2:
                    for h in range(0, contcar -1, 1):
                        if c == carpro[h]:
                            carquan[h] = carquan[h] + 1
                            carpre[h] = carpre[h] + preco[h]
                            carpro.pop()
                            carpre.pop()
                            carquan.pop()
                            contcar = contcar - 1
            conf_2 = int(input('Digite 1 para adicionar mais produtos ao carrinho e 2 para parar: '))
    elif opcao == 4:
        for u in range(0, contcar, 1):
            print('Produto(s) escolhido(s):', carquan[u], '  ', produtos[u], '   Preço R$:', carpre[u])
            total = total + carpre[u]
        print('O valor total do carrinho é de R$:', total)
    else:
        print('Opção inválida. Tente novamente')
    print('=.=' * 10)
    conf = 1
    conf_2 = 1
print('Fim do programa. Volte Sempre!')
