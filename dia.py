# Exibe uma mensagem de boas-vindas ao sistema
print("|-----Bem vindo ao Horussec-----|")

# Informa ao usuário que ele deve fornecer os dados em ordem por usuário
print("defina os dados em ordem por usuario!")

# Criação de listas vazias para armazenar as informações de cada cliente
nomes = []             # Lista para armazenar os nomes dos usuários
problema = []          # Lista para armazenar os problemas relatados
custo = []             # Lista para armazenar o custo de cada operação
data = []              # Lista para armazenar a data da operação
cidade_usuario = []    # Lista para armazenar a cidade de cada usuário

# Laço WHILE: repete até que a lista 'nomes' tenha 5 nomes
while len(nomes) < 5:
    nome = input('digite seus usuarios:')  # Recebe o nome de um usuário
    nomes.append(nome)                     # Adiciona o nome à lista

# Laço WHILE: repete até que a lista 'problema' tenha 5 descrições de problema
while len(problema) < 5:
    problemas = input('digite o problema dos usuarios:')  # Recebe o problema do usuário
    problema.append(problemas)                             # Adiciona o problema à lista

# Laço WHILE: repete até que a lista 'custo' tenha 5 valores
while len(custo) < 5:
    custos = int(input('digite o custo da resolução:'))  # Recebe o custo como número inteiro
    custo.append(custos)                                 # Adiciona o custo à lista

# Laço WHILE: repete até que a lista 'data' tenha 5 datas preenchidas
while len(data) < 5:
    datas = input('digite a data da operação:')  # Recebe a data da operação
    data.append(datas)                           # Adiciona à lista de datas

# Laço WHILE: repete até que a lista 'cidade_usuario' tenha 5 cidades
while len(cidade_usuario) < 5:
    cidade = input('digite a cidade do seu cliente:')  # Recebe a cidade do cliente
    cidade_usuario.append(cidade)                      # Adiciona à lista de cidades

# Exibe todas as listas preenchidas, mostrando os dados coletados
print(nomes)             # Exibe os nomes dos usuários
print(problema)          # Exibe os problemas relatados
print(custo)             # Exibe os custos das operações
print(data)              # Exibe as datas das operações
print(cidade_usuario)    # Exibe as cidades dos usuários

# Mostra um resumo detalhado dos dados do primeiro usuário (índice 0)
print(f"usuario {nomes[0]}, teve o problema {problema[0]}\n para seu reparo foi um custo total de {custo[0]} a operação foi realizada no dia {data[0]}\ne a localidade do cliente é na cidade {cidade_usuario[0]}")




#o codigo foi finalizado com 5 laços de repetição, com 8 prints, contendo 5 arrays para armazenamento
# e no total dentro dos laços de repetição que se repetem 5 vezes possuem 25 inputs, sendo que cada um adiciona valores aos arrays.
