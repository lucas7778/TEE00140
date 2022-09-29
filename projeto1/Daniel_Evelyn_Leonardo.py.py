#Alunos:
#Daniel Gladston; Matrícula: 319038090
#Evelyn Galdino; Matrícula: 219038089
#Leonardo Tourino; Matrícula: 118038049

#Projeto 1
Tabeladeitens = [[1, "Geladeira", 0.751, 999.90, 999.90/0.751],
                [2, "Notebook Dell", 0.00350, 2499.90, 2499.90/0.00350],
                [3, "Microondas capacidade", 0.0319, 299.29, 299.29/0.0319],
                [4, "Notebook ASUS", 0.527, 3999.90, 3999.90/0.527],
                [5, "iPhone 8", 0.000089, 2199.12, 2199.12/0.000089],
                [6, "Ventilador Gelado", 0.496, 199.90, 199.90/0.496],
                [7, "Freezer", 0.635, 849.00, 849.00/0.635],
                [8, "TV 55", 0.400, 4346.99, 4346.99/0.400],
                [9, "TV 50", 0.290, 3999.90, 3999.90/0.290],
                [10, "TV 42", 0.200, 2999.90, 2999.90/0.200],
                [11, "Notebook Lenovo", 0.498, 1999.90, 1999.90/0.498],
                [12, "Microondas Y", 0.0544, 429.90, 429.90/0.0544],
                [13, "Microondas Z", 0.0424, 429.90, 429.90/0.0424],
                [14, "Geladeira faz Frio", 0.870, 1199.98, 1199.98/0.870]]

# Ordenando a tabela a partir da coluna de preço por metro cubico
Tabeladeitens.sort(key=lambda capacidade: capacidade[4], reverse=True)

capacidade = 3
i = 0
valor = 0
espacoTotal = 0

for i in range(0, len(Tabeladeitens)):
   # cada espaco é ocupado por um único produto
   espaco = Tabeladeitens[i][2]
   quantidade = 1
   capacidade = capacidade - espacoTotal
   # enquanto o espaço ocupado for menor ou igual a 3 m³
   while espaco <= capacidade:
       espaco = espaco + Tabeladeitens[i][2]
       # Adicionar item de melhor custo beneficio ao caminhao
       if espaco <= capacidade:
           espacoTotal = espaco
           quantidade = quantidade + 1
       # Printar dados do item que foi adicionado
       else:
           print(f"\nProduto: ", Tabeladeitens[i][1], " | Quantidade: ", quantidade)
           print(f"\nEspaço ocupado: ", espacoTotal)
           print(f"\nEspaço restante: %0.16f" % (capacidade - espacoTotal))
           print(f"\nValor do frete: R$ ", (quantidade * Tabeladeitens[i][3]))2