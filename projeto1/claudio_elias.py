# Projeto 1
# Alunos: Claudio Coelho da Silva Junior (120.038.029), Elias da Silva Dutra (220.038.092)
# Linguagens de Programação para Engenharia
# TEE00140


# DESCRIÇÃO DOS OBJETOS DO PROGRAMA
# v = volume em m³
# p = preço dos produtos

# DIÁLOGO DE ENTRADA DE DADOS
p = [999.9, 2499.9, 299.29, 3999.9, 2199.12, 199.9, 849, 4346.99, 3999.9, 2999.9, 1999.9, 429.9, 429.9, 1199.98]
v = [0.751, 0.00350, 0.0319, 0.527, 0.000089, 0.496, 0.635, 0.400, 0.290, 0.200, 0.498, 0.0544, 0.0424, 0.870]

razao = [p[0]/v[0], p[1]/v[1], p[2]/v[2], p[3]/v[3], p[4]/v[4], p[5]/v[5], p[6]/v[6], p[7]/v[7],
         p[8]/v[8], p[9]/v[9], p[10]/v[10], p[11]/v[11], p[12]/v[12], p[13]/v[13]]

soma_preco = 0
soma_volume = 0
cont1 = 13
cont2 = 13
cont3 = 13
cont4 = 0
lista_volume = sorted(razao)
lista_preco = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista_produtos = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']

# PROCESSAMENTO
while cont1 >= 0:
    if lista_volume[cont1] == p[0]/v[0]:
        lista_volume[cont1] = v[0]
        lista_preco[cont1] = p[0]
        lista_produtos[cont1] = 'Geladeira'
        cont1 -= 1
    elif lista_volume[cont1] == p[1]/v[1]:
        lista_volume[cont1] = v[1]
        lista_preco[cont1] = p[1]
        lista_produtos[cont1] = 'Notebook Dell'
        cont1 -= 1
    elif lista_volume[cont1] == p[2] / v[2]:
        lista_volume[cont1] = v[2]
        lista_preco[cont1] = p[2]
        lista_produtos[cont1] = 'Microondas X'
        cont1 -= 1
    elif lista_volume[cont1] == p[3] / v[3]:
        lista_volume[cont1] = v[3]
        lista_preco[cont1] = p[3]
        lista_produtos[cont1] = 'Notebook ASUS'
        cont1 -= 1
    elif lista_volume[cont1] == p[4] / v[4]:
        lista_volume[cont1] = v[4]
        lista_preco[cont1] = p[4]
        lista_produtos[cont1] = 'iPhone 8'
        cont1 -= 1
    elif lista_volume[cont1] == p[5] / v[5]:
        lista_volume[cont1] = v[5]
        lista_preco[cont1] = p[5]
        lista_produtos[cont1] = 'Ventilador Gelado'
        cont1 -= 1
    elif lista_volume[cont1] == p[6] / v[6]:
        lista_volume[cont1] = v[6]
        lista_preco[cont1] = p[6]
        lista_produtos[cont1] = 'Freezer'
        cont1 -= 1
    elif lista_volume[cont1] == p[7] / v[7]:
        lista_volume[cont1] = v[7]
        lista_preco[cont1] = p[7]
        lista_produtos[cont1] = "TV 55'"
        cont1 -= 1
    elif lista_volume[cont1] == p[8] / v[8]:
        lista_volume[cont1] = v[8]
        lista_preco[cont1] = p[8]
        lista_produtos[cont1] = "TV 50'"
        cont1 -= 1
    elif lista_volume[cont1] == p[9] / v[9]:
        lista_volume[cont1] = v[9]
        lista_preco[cont1] = p[9]
        lista_produtos[cont1] = "TV 42'"
        cont1 -= 1
    elif lista_volume[cont1] == p[10] / v[10]:
        lista_volume[cont1] = v[10]
        lista_preco[cont1] = p[10]
        lista_produtos[cont1] = 'Notebook Lenovo'
        cont1 -= 1
    elif lista_volume[cont1] == p[11] / v[11]:
        lista_volume[cont1] = v[11]
        lista_preco[cont1] = p[11]
        lista_produtos[cont1] = 'Microondas Y'
        cont1 -= 1
    elif lista_volume[cont1] == p[12] / v[12]:
        lista_volume[cont1] = v[12]
        lista_preco[cont1] = p[12]
        lista_produtos[cont1] = 'Microondas Z'
        cont1 -= 1
    elif lista_volume[cont1] == p[13] / v[13]:
        lista_volume[cont1] = v[13]
        lista_preco[cont1] = p[13]
        lista_produtos[cont1] = 'Geladeira faz Frio'
        cont1 -= 1

while soma_volume < 3:
    soma_volume = soma_volume + lista_volume[cont2]
    cont2 -= 1
if soma_volume > 3:
    cont2 += 1
    soma_volume = soma_volume - lista_volume[cont2]
while cont3 > cont2:
    soma_preco = soma_preco + lista_preco[cont3]
    cont3 -= 1
while cont4 <= cont3:
    lista_produtos.pop(0)
    cont4 += 1

# EMISSÃO DO RELATÓRIO DE SAÍDA
print(f'\nO melhor conjunto a ser transportado é: {lista_produtos}')
print(f'\nO frete desse conjunto seria: R$ {soma_preco:.2f}')
print(f'\nO volume desse conjunto seria: {soma_volume:.4f} m³')

# DESPEDIDA
print('\nPrograma executado com sucesso.')
