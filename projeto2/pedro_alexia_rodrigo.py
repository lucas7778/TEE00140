def restricao(f, h):
    cont4 = 0
    cont5 = 0
    for m in (vetor3):  # restricao para substituiçao do item
        if m == f:
            cont4 = cont4 + 1
            if cont4 > 1:
                vetor3.pop()
                vetor4.pop()
                for n in (vetor3):  # substituindo o item
                    if n == f:
                        cont5 = cont5 + 1
                        if cont5 == 1:
                            vetor4[vetor3.index(n)] = h
                            print('\no produto antigo (de mesmo modelo) foi substituido pelo atual!\n')  # aviso


def restricao2(b):
    cont6 = 0
    for o in (vetor1):  # restricao para remover repeticoes
        if o == b:
            cont6 = cont6 + 1
            if cont6 > 1:
                vetor1.pop()
                print('\npor favor, nao repita o mesmo item!\n')


cont1 = 0  # contador
cont2 = 0  # contador
cont3 = 0  # contador
vetor1 = ['Mouse', 'Teclado', 'Headset', 'Monitor']  # vetor auxiliar com itens pre-selecionados
vetor2 = []  # vetor auxiliar
vetor3 = []  # vetor auxiliar
vetor4 = []  # vetor auxiliar
print(f'\nBem vindo sr. usuário. O que deseja realizar?'
      f'\n1- Visualizar produtos disponíveis;'
      f'\n2- Cadastro e compra de itens;'
      f'\n3- Sair da aplicação.')
a = int(input(f'\nDigite o número da sua escolha: '))
if a == 1:
    print(f'\nItens disponíveis:')
    for i in range(0, (len(vetor1))):
        print(f'- {vetor1[i]}')  # imprimindo itens cadastrados
elif a == 2:
    print('\nVeja abaixo o menu de produtos que estão disponiveis!')
    print('\n***********************************************')
    print('              Menu de produtos')
    print('***********************************************')
    for i in range(0, (len(vetor1))):
        print('item: ', vetor1[i])  # imprimindo itens
    print('***********************************************')
    a = str(input('\nDeseja cadastrar um novo produto? Digite S para sim ou N para não \n')).lower()
    if (a == 's'):
        while (cont1 != 1):
            b = str(input('\nQual é o produto? (Não repita o mesmo item)\n'))  # escolhendo itens
            vetor1.append(b)
            restricao2(b)
            d = str(input('\nDeseja continuar o cadastro? Escreva S ou N - ')).lower()
            if (d == 'n'):
                cont1 = cont1 + 1
        print('\n\n***********************************************')
        print('Todos os itens disponíveis após cadastro:')
        print('***********************************************')
        for i in range(0, (len(vetor1))):
            print(f'- {vetor1[i]}')  # imprimindo itens cadastrados
    print(f'\nEscolha o que deseja fazer agora:'
          f'\n1- Fazer compras'
          f'\n2- Finalizar o programa.')
    b = int(input(f'Digite o número da sua escolha: '))
    if b == 1:
        print('\n***********************************************')
        print(f'Menu de produtos:')
        print('***********************************************')
        for i in range(0, (len(vetor1))):
            print(f'- {vetor1[i]}')
        print('***********************************************')
        print('\nAgora, você deve selecionar os itens que irão para o carrinho de compras!')
        while (cont2 != 1):
            f = str(input('\nEscolha um item: '))  # listando itens
            h = int(input('\nQuantos? '))  # quantidade de itens escolhidos
            if (f in vetor1) == True:  # restricao que associa o 'cadastro' com a 'listagem'
                vetor3.append(f)
                vetor4.append(h)
                restricao(f, h)
            else:
                print('\nItem não adicionado! Indique apenas um item do menu!')
            g = str(input('\nMais algum produto? Digite S para sim ou N para não')).lower()
            if (g == 'n'):
                for i in range(0, len(vetor3)):
                    print('\nItem escolhido: ', vetor3[i], '; Quantidade depois da escolha:', vetor4[i])
                cont2 = cont2 + 1
        j = str(input(f'\nDeseja remover algum produto? Digite S para sim ou N para não\n')).lower()
        if (j == 's'):
            while (cont3 != 1):
                n = str(input('\nAinda quer remover? Digite S para sim ou N para não.\n')).lower()
                if (n == 's'):
                    k = str(input('\nQual item?'))
                    vetor4.remove(vetor4[vetor3.index(k)])
                    vetor3.remove(k)
                    print('\nO item ', k, 'foi removido!')
                else:
                    cont3 = cont3 + 1
        if vetor3 != []:
            l = str(input('\nDeseja efetuar a compra? Digite S para sim ou N para não\n')).lower()  # finalizando a compra
            if (l == 's'):
                print('\n\***********************************************')
                print('Itens selecionados para uma possível compra:')
                print('***********************************************')
                for i in range(0, len(vtor3)):
                    print('► ', vetor3[i], '; Quantidade depois da escolha:', vetor4[i])
                print('***********************************************')
                print('\nCompra efetuada! Obrigada \U0001F600.')
            else:
                print('\nCompra não finalizada!\n')
    else:
        exit()
elif a == 3:
    exit()
else:
    print(f'Uma das opcões deve ser escolhida. Tente novamente.')
