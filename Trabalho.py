import pandas as pd
from matplotlib import pyplot as plt

# Lendo dados do arquivo 'dados4.csv'
df = pd.read_csv('dados/dados4.csv')

# # Criando variáveis para idade
ageColumn = df["age"]
ageMode = ageColumn.mode()[0]

# Preenche os valores nulos na coluna 'ageColumn'
ageColumn.fillna(ageMode , inplace=True)
df["age"] = ageColumn.astype(int)

#################
# Exercício nº1 #
#################

# Criação do arquivo e escrita dos dados

# Criando o arquivo de resposta
arquivo = open("Resposta01.txt","w")

# Criando as colunas com os nomes, idades e sexo
arquivo.write(str(df[["name","sex","age"]].to_string()))
arquivo.close()

####################################################################################################

#################
# Exercício nº2 #
#################

# # Variáveis para o sexo
# sexColumn = df["sex"]
# sexMode = sexColumn.mode()[0]

# # Preenchimentos de campos nulos na coluna 'sexCollumn'
# sexColumn.fillna(sexMode, inplace=True)

# # Variáveis para contagem de cada sexo
# maleCount = 0
# femaleCount = 0

# # for para a contagem dos sexos
# for item in sexColumn:
#     if(item == "male"):
#         maleCount += 1
#     elif( item == "female"):
#         femaleCount += 1

# # Retorna no terminal a quatidade de homens e mulheres embarcados
# print("\nNo barco haviam "+str(maleCount)+" homens e haviam "+str(femaleCount)+" mulheres\n")

# ##################################################################################################

# #################
# # Exercício nº3 #
# #################

# # Variáveil de sobrevivente
# survivedColumn = df["survived"]
# survivedMode = survivedColumn.mode()[0]

# # Preenchimento de campos nulos na coluna 'survivedColumn'
# survivedColumn.fillna(survivedMode , inplace=True)

# # Variáveis de contagem de mortos e sobreviventes
# survivedCount = 0
# deadCount = 0

# # for para a contagem de mortos e sobreviventes
# for item in survivedColumn:
#     if(item == 0):
#         deadCount += 1
#     elif( item == 1):
#         survivedCount += 1

# # Utilizando um array para guardar os dados para o gráfico(pizza)
# dados = [deadCount,survivedCount]

# # Gráfico(pizza) com porcentagem de sobreviventes e não sobreviventes
# plt.pie(dados, labels = ['Não Sobreviventes','Sobreviventes'], autopct='%1.0f%%')
# plt.show()

# ##################################################################################################

# #################
# # Exercício nº4 #
# #################

# # Variáveis para a coluna tarifa
# fareColumn = df["fare"]
# fareMode = fareColumn.mode()[0]

# # Preenchendo os campos nulos da coluna tarifa
# fareColumn.fillna(fareMode, inplace=True)

# # Grafico de disperção da idade
# plt.scatter ( ageColumn, fareColumn, alpha=0.5 )

# # Titulo do gráfico
# plt.title("idade por tarifa")

# # Nome 'idade' no eixo 'X'
# plt.xlabel("idade")

# # Nome 'tarifa' no eixo 'Y'
# plt.ylabel("tarifa")
# plt.show()