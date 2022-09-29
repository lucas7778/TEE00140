#Grupo: Gabrielle Moura da Silva Barroso e Vinícius Vieira de Brito Silva


#Primeiro vamos definir o valor total
print('\n')
print('Bem vindo ao programa.')
caminhao = {}

def valor_total(items, Volume_maximo):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) <= Volume_maximo else 0


#Após iremos resolver o problema de otimização
def problema_caminhao(lista_itens, volume_Max_Caminhao):
    if not lista_itens:
        return ()
    if (lista_itens, volume_Max_Caminhao) not in caminhao:

        inicio = lista_itens[0]
        fim = lista_itens[1:]
        adiciona = (inicio,) + problema_caminhao(fim, volume_Max_Caminhao - inicio[1])
        nao_adiciona = problema_caminhao(fim, volume_Max_Caminhao)

        if valor_total(adiciona, volume_Max_Caminhao) > valor_total(nao_adiciona, volume_Max_Caminhao):
              resposta = adiciona
        else: resposta = nao_adiciona

        caminhao[(lista_itens, volume_Max_Caminhao)] = resposta
    return caminhao[(lista_itens, volume_Max_Caminhao)]


# Depois, definimos a capacidade máxima e listamos os itens com seus valores e volumes
  
capacidadeMaxima = 3
itens = (
    ("Geladeira", 0.751, 999.90), ("Notebook Dell", 0.00350, 2499.90),
    ("Microondas X", 0.0319, 299.90), ("Notebook ASUS", 0.527, 3999.90),
    ("iPhone 8", 0.000089, 2199.12), ("Ventilador Gelado", 0.496, 199.90),
    ("Freezwe", 0.635, 849.00), ("TV 55", 0.400, 4346.99),
    ("TV 50", 0.290, 3999.90), ("TV 42", 0.200, 2999.90),
    ("Notebook Lenovo", 0.498, 1999.90), ("Microondas Y", 0.0544, 429.90),
    ("Microondas Z", 0.0424, 429.90), ("Geladeira Faz Frio", 0.870, 1199.98)
    
)

solucao = problema_caminhao(itens, capacidadeMaxima)

print("\n")
print("Os items que irei levar no caminhão são:\n")

for item in solucao:
    print(item[0])
  
# Após isso, retornamos os valores encontrados
print('\n')  
print('E com um preço de R$ %.2f' % valor_total(solucao, capacidadeMaxima))
print('E com um preço de R$ %.2f' % sum([x[1] for x in solucao]), 'm³')
print("Obrigado por utilizar o programa.")
print('\n')