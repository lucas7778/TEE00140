#Alunos:
#Daniel Gladston; Matrícula: 319038090
#Evelyn Galdino; Matrícula: 219038089
#Leonardo Tourino; Matrícula: 118038049

#Projeto 2:
op = 0
valor = 0
def menu():    
    print(f"\nMenu principal\n")
    print("1 - Cadrastar \n2 - Listar \n3 - Comprar \n4 - Carrinho \n5 - Sair")
carrinho = [
            ["Motor elétrico",1000,0],
            ["Controlador de motor",500,0],
            ["Bateria",10,0],
            ["BMS",5,0],
            ["Carregador",250,0],
            ["1m de Cabo",50,0],
            ["Conector",1,0]
            ]
while op != 5:
    menu()
    op = int(input("\nDigite uma das opções acima (apenas numero): "))
    if op > 5:
        print("\Valor invalido")
    if op == 1:
        controle = 0

        novoProduto = input("\nDigite o nome do novo produto: ")
        for i in range(len(carrinho)):
            if carrinho[i][0] == novoProduto:
                print("\nProduto ja cadrastado no sistema")
                controle = 0
                break
            else:
                controle = 1
        if controle == 1:
            valorEntrada = int(input("\nDigite o valor: "))
            cadrastrar = [novoProduto,valorEntrada,0]
            carrinho.append(cadrastrar)
            print(f"\nO item {carrinho[i+1][0]} foi cadrastado com sucesso!")
    if op == 2:
        print("\nOs nosso produtos são:")
        print("\nCodigo - Item - Valor\n")
        for i in range(len(carrinho)):
            print(f"{i} - {carrinho[i][0]} - {carrinho[i][1]} reais")
    if op == 3:
        print("\nOs nosso produtos são:")
        print("\nCodigo - Item - Valor\n")
        for i in range(len(carrinho)):
            print(f"{i} - {carrinho[i][0]} - {carrinho[i][1]} reais")
        comprar = int(input(f"\nDigite o codigo do item que deseja comprar? (apenas numero): \n"))
        if comprar <= len(carrinho):
            if carrinho[comprar][2] == 0:
                carrinho[comprar][2] = 1
                print(f"\nO/A {carrinho[comprar][0]} foi adicionado no carrinho\n")
            else:
                print("\nEste item ja consta no seu carrinho")
                carrinho[comprar][2] = int(input("\nQuantos itens desse deseja?: "))
                print(f"\nAdicionado {carrinho[comprar][2]} vezes o/a {carrinho[comprar][0]}\n")
        else:
            print("\nValor invalido")
    if op == 4:
        print("\nItens no carrinho:")
        print("\nItem - vezes")
        valor = 0
        for i in range(len(carrinho)):
            if carrinho[i][2] > 0:
                print(f"{carrinho[i][0]} - {carrinho[i][2]}" )
                valor = valor + carrinho[i][1]*carrinho[i][2]
        print(f"\nValor total: {valor} reais")
        fechar = input("\nDeseja finalizar a comprar? (s/n): ")
        if fechar == "s" or fechar == "S":
            print(f"\nValor total: {valor} reais")
            print("Obrigado pela comprar!\n")
            break
        else:
            print("\nVoltando...")
