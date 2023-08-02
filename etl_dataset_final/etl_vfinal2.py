import os
import sys
import pandas as pd
import sqlite3

#print("Criação e conexão com o banco sqlite3")
#connection = sqlite3.connect("tcc.db")
#cursor = connection.cursor()

#cursor.execute("CREATE TABLE tcc(id_curso, nome_curso, nome_componente, cod_componente, id_componente, id_turma, media_final, descricao)")

print("-----------------------------------------------------------------------------------")
################################################################

path_datasets = "/home/tiago/TCC/datasets"
#tudo começa aqui identificando o nome do curso
nome_curso = "ENGENHARIA DE COMPUTAÇÃO"

os.chdir(path_datasets)
#print(os.getcwd())
#print(os.listdir(path_datasets))

print("-----------------------------------------------------------------------------------")
##################################################################################

df_estrutura_curricular = pd.read_csv("estruturas-curriculares.csv", usecols=["id_curso", "nome_curso"], index_col="id_curso")
#print(df_estrutura_curricular)
filtro_nome_curso = df_estrutura_curricular["nome_curso"]==nome_curso
df_estrutura_curricular = df_estrutura_curricular[filtro_nome_curso]
#print(df_estrutura_curricular)

id_eng_comp = 0
for i in df_estrutura_curricular.itertuples():
    #print(i[0])
    id_eng_comp = i[0]

#print(id_eng_comp)

print("-----------------------------------------------------------------------------------")
###################################################################################

#NÃO ESTAVA BATENDO O NÚMERO DE TURMAS, ERA PQ AS TURMAS DE TEORIA E LABORAÓRIO TEM IDS DIFERENTE

#ELETRÔNICA : DCA0213
#ELETRÔNICA - TEORIA : DCA0213.0
#ELETRÔNICA - LABORATÓRIO : DCA0213.1

#CIRCUITOS DIGITAIS : DCA0212
#CIRCUITOS DIGITAIS - TEORIA : DCA0212.0
#CIRCUITOS DIGITAIS - LABORATÓRIO : DCA0212.1

#SISTEMAS DE CONTROLE : DCA0216
#SISTEMAS DE CONTROLE - TEORIA : DCA0216.0
#SISTEMAS DE CONTROLE - LABORATÓRIO : DCA0216.1

#PROGRAMAÇÃO AVANÇACA : DCA0212
#PROGRAMAÇÃO AVANÇADA : DCA0803 ?????CONSIDERAR?????

dict_cod_x_nome_disciplina = { "DCA0103":"ANÁLISE DE SINAIS E SISTEMAS", "DCA0100":"MATEMÁTICA DISCRETA", "DCA0105":"TEORIA DE CIRCUITOS", "DCA0118":"PROCESSAMENTO DIGITAL DE SINAIS",
                            "DCA0212.0":"CIRCUITOS DIGITAIS - TEORIA", "DCA0212.1":"CIRCUITOS DIGITAIS - LABORATÓRIO", "DCA0213.0":"ELETRÔNICA - TEORIA", "DCA0213.1":"ELETRÔNICA - LABORATÓRIO", 
                            "DCA1202":"PROGRAMAÇÃO AVANÇADA", "DCA0803":"PROGRAMAÇÃO AVANÇADA", "DCA0104":"ARQUITETURA DE COMPUTADORES", "DCA0110":"MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS", 
                            "DCA0115":"OTIMIZAÇÃO DE SISTEMAS", "DCA0130":"REDES DE COMPUTADORES", "DCA0205":"PROJETO E ENGENHARIA DE SOFTWARE", "DCA0207":"BANCO DE DADOS", 
                            "DCA0208":"ALGORITMOS E ESTRUTURAS DE DADOS I", "DCA0108":"SISTEMAS OPERACIONAIS", "DCA0119":"SISTEMAS DIGITAIS", "DCA0200":"INTELIGÊNCIA ARTIFICIAL", 
                            "DCA0210":"LINGUAGENS FORMAIS E AUTÔMATOS", "DCA0114":"COMPUTAÇÃO GRÁFICA", "DCA0209":"ALGORITMOS E ESTRUTURAS DE DADOS II", "DCA0211":"COMPILADORES", 
                            "DCA0123":"PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA", "DCA0125":"SISTEMAS DE TEMPO REAL", "DCA0216.0":"SISTEMAS DE CONTROLE - TEORIA", 
                            "DCA0216.1":"SISTEMAS DE CONTROLE - LABORATÓRIO", "DCA0131":"CIÊNCIA DE DADOS", "DCA0132":"ENGENHARIA DE DADOS", "DCA0800":"ALGORITMOS E LÓGICA DE PROGRAMAÇÃO" }

df_componentes_curriculares_presenciais = pd.read_csv("componentes-curriculares-presenciais.csv", usecols=["id_componente", "codigo", "nome"])
#print(df_componentes_curriculares_presenciais)
#cada nome de disciplina tem seu respectivo id_componente e codigo com essa informação, vou utilizar uma método do python que por uma determinada
# coluna do df eu posso fazer uma comparação com uma lista ou dicionário de elementos para verificar a presença das informações da na coluna do df 
# escolhida e compara com, no caso do dicionário, as chaves e retornar apenas os que forem iguais a coluna do df. Como eu fiz o dicionário com
# 26 elementos então esse filtro por coluna do df tem que retornar a mesma quantidade de registros de disciplinas para pegar o id_componente para 
# poder consultar e fazer a filtragem no próximo arquivo csv pelo id_componente das matérias que foram oferecidas nesse determinado semeste pesquisado.
df_filtro_codigo_componente = df_componentes_curriculares_presenciais[df_componentes_curriculares_presenciais.codigo.isin(dict_cod_x_nome_disciplina.keys())]
#print(df_filtro_codigo_componente)
#print(len(df_filtro_codigo_componente))
#print(len(dict_cod_x_nome_disciplina))

#criando discionário que contenha cod_disciplina e o id_componente para verificar se aquela matéria foi disponibilizada nas turmas do referido semestre
dict_cod_disciplina_x_id_componente = {}

for i in df_filtro_codigo_componente.itertuples():
    dict_cod_disciplina_x_id_componente[i[2]] = i[1]
    #print(i[1])
    #print(i[2])
    
#print(dict_cod_disciplina_x_id_componente)

print("-----------------------------------------------------------------------------------")
#######################################################################################

#Tive que explicitar o separador ";", em virtude de o arquivo ter algum defeito no padrão csv(Screenshot from 2023-04-04 23-47-02.png)
df_turmas_2021_2 = pd.read_csv("turmas-2021.2.csv", sep=";", usecols=["id_turma", "id_componente_curricular"])
#print(df_turmas_2021_2)
#fazendo a filtragem na coluna id_componente_curricular se existe esse id_componente com os valores do discionário e filtrar, significando
#que a matéria foi disponibilizada nas turmas desse semestre
df_filtro_id_componente_curricular = df_turmas_2021_2[df_turmas_2021_2.id_componente_curricular.isin(dict_cod_disciplina_x_id_componente.values())]
#print(df_filtro_id_componente_curricular)

#aí leio o df e faço um dicionário com o id_turma e o id_componente_componente curricular desse df
dict_id_turma_x_id_componente_curricular = {}
for i in df_filtro_id_componente_curricular.itertuples():
    dict_id_turma_x_id_componente_curricular[i[1]] = i[2]

#print(dict_id_turma_x_id_componente_curricular)
#print(len(dict_id_turma_x_id_componente_curricular))

print("-----------------------------------------------------------------------------------")
###########################################################################################

#Tive que explicitar o separador ";", em virtude de o arquivo ter algum defeito no padrão csv(Screenshot from 2023-04-05 00-09-40.png)
df_matriculas_2021_2 = pd.read_csv("matriculas-2021-2.csv", sep=";", usecols=["discente", "id_turma", "id_curso", "media_final", "descricao"])
#Tá vindo com .0 no id_curso desde aqui pq ele reconheceu esse campo como float
# print(df_matriculas_2021_2)

#Preenchimento de missing data em DataFrames com valor ZERO  #tem que tirar os valore NaN
df_matriculas_2021_2 = df_matriculas_2021_2.fillna(0) 
#print(df_matriculas_2021_2)

#como vem 3 registros de aluno pq ele mostra a nota das 3 unidades, logo remover as réplicas, e deixar
#apenas um registro por aluno
df_matriculas_2021_2 = df_matriculas_2021_2.drop_duplicates()

#selecionar apenas as matriculas das turmas de engenharia de computação pelo id_curso
filtro_id_curso = df_matriculas_2021_2["id_curso"]==id_eng_comp
df_matriculas_2021_2 = df_matriculas_2021_2[filtro_id_curso]
#print(df_matriculas_2021_2)

#gerando a mesma quantidade de registro do dataframe para preencher a primeira coluna com o nome_curso
list_nome_curso = []
for i in range(0,len(df_matriculas_2021_2)):
    list_nome_curso.append(nome_curso)

#print(list_nome_curso)
#print(list_nome_curso.count(nome_curso))

#Adicionar a coluna nome do curso no dataframe
df_matriculas_2021_2['nome_curso'] = list_nome_curso
#print(df_matriculas_2021_2)

#nova coluna (colocando o id_curso e nome_curso para frente para a primeira coluna)
novo_header = ["discente", "id_curso", "nome_curso", "id_turma", "media_final", "descricao"]
df_matriculas_2021_2 = df_matriculas_2021_2[novo_header]
#print(df_matriculas_2021_2)

#substituir as vírgulas por ponto para poder transformar a coluna media_final de str para float
#df_matriculas_2021_2 = df_matriculas_2021_2.replace({',':'.'}, regex=True) #aqui funciona para todo o dataframe
#aqui só para a coluna mefia_final
df_matriculas_2021_2['media_final'] = df_matriculas_2021_2['media_final'].str.replace(',', '.')
#print(df_matriculas_2021_2)

#Depois de trocar a vírgula pelo ponto apareceram campos NaN novamente, então vou substituir com 0
df_matriculas_2021_2 = df_matriculas_2021_2.fillna(0)
#print(df_matriculas_2021_2)

#Removendo o .0 do final do id_curso, na vdd esse valor não tem 0 na planilha mas o dataframe lê assim
#df_matriculas_2021_2['id_curso'] = df_matriculas_2021_2['id_curso'].apply(lambda x: x[:-2])
#print(df_matriculas_2021_2)

#alterar os campos id_curso, id_turma para int e media_final para float
df_matriculas_2021_2[['id_curso', "id_turma"]] = df_matriculas_2021_2[['id_curso', "id_turma"]].astype(int)
#essa função .apply(pd.to_numeric) reconhece automaticamente como float pq a coluna media_final 
# está com ponto, já a função a cima .astype() vc escolhe o formato que deseja
df_matriculas_2021_2[["media_final"]] = df_matriculas_2021_2[["media_final"]].apply(pd.to_numeric)
#print(df_matriculas_2021_2)

#gerar um index que seja uma coluna que seja equivalente a quantidade total de registros
# e depois substituir por esse index que o dataframe trouxe dos arquivos csv
index = []
for i in range(1,len(df_matriculas_2021_2)+1):
    index.append(i)

#print(index)

#adicionar a coluna index no dataframe
df_matriculas_2021_2['id'] = index
#definir a coluna criada id como index do dataframe
df_matriculas_2021_2.set_index('id', inplace=True)
#print(df_matriculas_2021_2)

#ver o df completo. é bom utilizar ele com redirecionamento de saída para um arquivo de texto
#é bom só para teste pq ele transforma tudo em texto mas se o df for só string dá certo, nesse 
#não pq tem colunas que são números
#print(df_matriculas_2021_2.to_string())

print("-----------------------------------------------------------------------------------")
###########################################################################################

#'''

#filtragem do id_turma do dicionário dict_id_turma_x_id_componente_curricular para adicionar as colunas no df que será convertido para sql
#!------------------------PARTE MUITO IMPORTANTE-------------------------!#

#Preparando o dataframe para converter para sql

#lista para testar a quantidade de registros
#lista_teste = []

#listas com os filtros para as colunas do df final
lista_discente = []
lista_id_curso = []
lista_nome_curso = []
lista_id_turma = []
lista_cod_componente = []
lista_nome_componente = []
lista_media_final = []
lista_descricao = []


#aqui restará apenas os nomes das matérias que foram declaradas no primeiro dicionário com o código e nome da disciplina

for i in df_matriculas_2021_2.itertuples():
    #print(i[3])
    for j,k in dict_id_turma_x_id_componente_curricular.items():
        #print(f"Chave={j} : Valor={k}")
        if i[4] == j:
            #print("Teste de verificação de acesso do for mais interno")
            for l,m in dict_cod_disciplina_x_id_componente.items():
                #print(f"Chave={l} : Valor={m}")
                if k == m:
                    for n,o in dict_cod_x_nome_disciplina.items():
                        #print(f"Chave={n} : Valor={o}")
                        if l == n:
                            #print(f"Chave={n} : Valor={o}")
                            #print(o)
                            #lista_teste.append(o)
                            lista_cod_componente.append(n)
                            lista_nome_componente.append(o)
                            lista_discente.append(i[1])
                            lista_id_curso.append(i[2])
                            lista_nome_curso.append(i[3])
                            lista_id_turma.append(i[4])
                            lista_media_final.append(i[5])
                            lista_descricao.append(i[6])

#### Criar um novo df vazio e ajustar o novo df com as novas linhas
df_to_sql = pd.DataFrame()
#print(df_to_sql)

#A saída dos vetores já estarão na ordem dos registros, prontos para serem adicionados nas colunas
# do dataframe final       

#print(len(lista_teste))
#print(len(lista_cod_componente))
#print(len(lista_nome_componente))

#Adicionandos as novas colunas cod_componente e nome_componente do curso no dataframe
df_to_sql['discente'] = lista_discente
df_to_sql['id_curso'] = lista_id_curso
df_to_sql['nome_curso'] = lista_nome_curso
df_to_sql['id_turma'] = lista_id_turma
df_to_sql['cod_componente'] = lista_cod_componente
df_to_sql['nome_componente'] = lista_nome_componente
df_to_sql['media_final'] = lista_media_final
df_to_sql['descricao'] = lista_descricao
#print(df_to_sql)

#Organizando as novas colunas criadas acima no header final
header_final = ["discente", "id_curso", "nome_curso", "id_turma","cod_componente", "nome_componente", "media_final", "descricao"]
df_to_sql = df_to_sql[header_final]

#gerar um novo index para o df final
novo_index = []
for i in range(1,len(df_to_sql)+1):
    novo_index.append(i)

#print(index)

#adicionar a coluna index no dataframe
df_to_sql['id'] = novo_index
#definir a coluna criada id como index do dataframe
df_to_sql.set_index('id', inplace=True)
#print(df_to_sql)

#Cada linha desse dataframe corresponde a um aluno que se matriculou em um componente naqueles que estão
#declarados no dicionário de código do componente por nome do componente
#print(df_to_sql)

#Visualizar todo o dataframe com redirecionamente de saída em arquivo de texto "python3 etl.py > teste.txt"
print(df_to_sql.to_string())

#'''

# Descobri depois de alguns testes que a disciplina de modelagem tem ids de discentes repetidos
#id_turma = 57689165
