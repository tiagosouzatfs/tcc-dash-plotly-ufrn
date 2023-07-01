import os
import pandas as pd

################################################################################

path_datasets = "/home/tiago/TCC/datasets"
#tudo começa aqui identificando o nome do curso
nome_curso = "ENGENHARIA DE COMPUTAÇÃO"

os.chdir(path_datasets)
#print(os.getcwd())
#print(os.listdir(path_datasets))

##################################################################################

df_estrutura_curricular = pd.read_csv("estruturas-curriculares.csv", sep=";", usecols=["id_curso", "nome_curso"], index_col="id_curso")
#print(df_estrutura_curricular)
filtro_nome_curso = df_estrutura_curricular["nome_curso"]==nome_curso
df_estrutura_curricular = df_estrutura_curricular[filtro_nome_curso]
#print(df_estrutura_curricular)

id_eng_comp = 0
for i in df_estrutura_curricular.itertuples():
    #print(i[0])
    id_eng_comp = i[0]

#print(id_eng_comp)

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
#PROGRAMAÇÃO AVANÇADA : DCA0803 ?????CONSIDERAR????? o professor pediu para remover pois essa turma é de mecatrônica

dict_cod_x_nome_disciplina = { "DCA0103":"ANÁLISE DE SINAIS E SISTEMAS", 
"DCA0100":"MATEMÁTICA DISCRETA", "DCA0105":"TEORIA DE CIRCUITOS", 
"DCA0118":"PROCESSAMENTO DIGITAL DE SINAIS",
"DCA0212.0":"CIRCUITOS DIGITAIS - TEORIA", 
"DCA0212.1":"CIRCUITOS DIGITAIS - LABORATÓRIO", 
"DCA0213.0":"ELETRÔNICA - TEORIA", "DCA0213.1":"ELETRÔNICA - LABORATÓRIO", 
"DCA1202":"PROGRAMAÇÃO AVANÇADA", "DCA0104":"ARQUITETURA DE COMPUTADORES", 
"DCA0110":"MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS", 
"DCA0115":"OTIMIZAÇÃO DE SISTEMAS", "DCA0130":"REDES DE COMPUTADORES", 
"DCA0205":"PROJETO E ENGENHARIA DE SOFTWARE", "DCA0207":"BANCO DE DADOS", 
"DCA0208":"ALGORITMOS E ESTRUTURAS DE DADOS I", "DCA0108":"SISTEMAS OPERACIONAIS", 
"DCA0119":"SISTEMAS DIGITAIS", "DCA0200":"INTELIGÊNCIA ARTIFICIAL", 
"DCA0210":"LINGUAGENS FORMAIS E AUTÔMATOS", "DCA0114":"COMPUTAÇÃO GRÁFICA", 
"DCA0209":"ALGORITMOS E ESTRUTURAS DE DADOS II", "DCA0211":"COMPILADORES", 
"DCA0123":"PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA", "DCA0125":"SISTEMAS DE TEMPO REAL", 
"DCA0216.0":"SISTEMAS DE CONTROLE - TEORIA", 
"DCA0216.1":"SISTEMAS DE CONTROLE - LABORATÓRIO", "DCA0131":"CIÊNCIA DE DADOS", 
"DCA0132":"ENGENHARIA DE DADOS", "DCA0800":"ALGORITMOS E LÓGICA DE PROGRAMAÇÃO" }

df_componentes_curriculares_presenciais = pd.read_csv("componentes-curriculares-presenciais.csv", sep=";", usecols=["id_componente", "codigo", "nome"])
#print(df_componentes_curriculares_presenciais)
# cada nome de disciplina tem seu respectivo id_componente e codigo com essa informação, vou utilizar uma método do python que por uma determinada
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

##################################################################################

#read all csv
dict_matric_x_turmas_csv = {"matriculas-2022.1.csv" : "turmas-2022.1.csv",
                            "matriculas-2022.2.csv" : "turmas-2022.2.csv",
                            "matriculas-2021-1.csv" : "turmas-2021.1.csv", 
                            "matriculas-2021-2.csv" : "turmas-2021.2.csv", 
                            "matricula-componente-20206.csv" : "turmas-2020.6.csv",
                            "matricula-componente-20205.csv" : "turmas-2020.5.csv", 
                            "matriculas-2020-2.csv" : "turmas-2020.2.csv", 
                            "matricula-componente-20191.csv" : "turmas-2019.1.csv",
                            "matricula-componente-20192.csv" : "turmas-2019.2.csv",
                            "matricula-componente-20181.csv" : "turmas-2018.1.csv",
                            "matricula-componente-20182.csv" : "turmas-2018.2.csv"}

# linha removida do dicionário acima pois existem os arquivos no sigaa mas não houve essas turma por causa da pandemia
# "matricula-componente-20201.csv", "turmas-2020.1.csv",

#dataframe final vazio com as colunas do df final
#df_final = pd.DataFrame({"id", "discente", "id_curso", "nome_curso", "id_turma", "cod_componente", 
#                "nome_componente", "media_final", "descricao", "semestre"})
df_final = pd.DataFrame()

#contador para descrever o semestre baseado na sequencia das turmas lidas e pela lista de semestres
contador = 0

for i,j in dict_matric_x_turmas_csv.items():
    contador = contador + 1
    #print(i)
    #matriculas = pd.read_csv(i, sep=";")
    #turmas = pd.read_csv(j, sep=";")

    #Tive que explicitar o separador ";", em virtude de o arquivo ter algum defeito no padrão csv(Screenshot from 2023-04-05 00-09-40.png)
    df_matriculas = pd.read_csv(i, sep=";", usecols=["discente", "id_turma", "id_curso", "media_final", "descricao"])
    #Tá vindo com .0 no id_curso desde aqui pq ele reconheceu esse campo como float
    # print(df_matriculas)

    #Preenchimento de missing data em DataFrames com valor ZERO  #tem que tirar os valore NaN
    df_matriculas = df_matriculas.fillna(0) 
    #print(df_matriculas)

    #como vem 3 registros de aluno pq ele mostra a nota das 3 unidades, logo remover as réplicas, e deixar
    #apenas um registro por aluno
    df_matriculas = df_matriculas.drop_duplicates()

    #selecionar apenas as matriculas das turmas de engenharia de computação pelo id_curso
    filtro_id_curso = df_matriculas["id_curso"]==id_eng_comp
    df_matriculas = df_matriculas[filtro_id_curso]
    #print(df_matriculas)

    #gerando a mesma quantidade de registro do dataframe para preencher a primeira coluna com o nome_curso
    list_nome_curso = []
    for i in range(0,len(df_matriculas)):
        list_nome_curso.append(nome_curso)

    #print(list_nome_curso)
    #print(list_nome_curso.count(nome_curso))

    #Adicionar a coluna nome do curso no dataframe
    df_matriculas['nome_curso'] = list_nome_curso
    #print(df_matriculas)

    #nova coluna (colocando o id_curso e nome_curso para frente para a primeira coluna)
    novo_header = ["discente", "id_curso", "nome_curso", "id_turma", "media_final", "descricao"]
    df_matriculas = df_matriculas[novo_header]
    #print(df_matriculas)

    #substituir as vírgulas por ponto para poder transformar a coluna media_final de str para float
    #df_matriculas = df_matriculas.replace({',':'.'}, regex=True) #aqui funciona para todo o dataframe
    #aqui só para a coluna mefia_final
    df_matriculas['media_final'] = df_matriculas['media_final'].str.replace(',', '.')
    #print(df_matriculas)

    #Depois de trocar a vírgula pelo ponto apareceram campos NaN novamente, então vou substituir com 0
    df_matriculas = df_matriculas.fillna(0)
    #print(df_matriculas)

    #alterar os campos id_curso, id_turma para int e media_final para float
    df_matriculas[['id_curso', "id_turma"]] = df_matriculas[['id_curso', "id_turma"]].astype(int)
    #essa função .apply(pd.to_numeric) reconhece automaticamente como float pq a coluna media_final 
    # está com ponto, já a função a cima .astype() vc escolhe o formato que deseja
    df_matriculas[["media_final"]] = df_matriculas[["media_final"]].apply(pd.to_numeric)
    #print(df_matriculas)

    ###########################################################################################

    #Tive que explicitar o separador ";", em virtude de o arquivo ter algum defeito no padrão csv(Screenshot from 2023-04-04 23-47-02.png)
    df_turmas = pd.read_csv(j, sep=";", usecols=["id_turma", "id_componente_curricular"])
    #print(df_turmas)
    #fazendo a filtragem na coluna id_componente_curricular se existe esse id_componente com os valores do discionário e filtrar, significando
    #que a matéria foi disponibilizada nas turmas desse semestre
    df_filtro_id_componente_curricular = df_turmas[df_turmas.id_componente_curricular.isin(dict_cod_disciplina_x_id_componente.values())]
    #print(df_filtro_id_componente_curricular)

    #aí leio o df e faço um dicionário com o id_turma e o id_componente_componente curricular desse df
    dict_id_turma_x_id_componente_curricular = {}
    for i in df_filtro_id_componente_curricular.itertuples():
        dict_id_turma_x_id_componente_curricular[i[1]] = i[2]

    #print(dict_id_turma_x_id_componente_curricular)
    #print(len(dict_id_turma_x_id_componente_curricular))

    ###########################################################################################

    #filtragem do id_turma do dicionário dict_id_turma_x_id_componente_curricular para adicionar as colunas no df final
    
    #!------------------------PARTE MUITO IMPORTANTE-------------------------!#

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

    for i in df_matriculas.itertuples():
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

    #A saída dos vetores já estarão na ordem dos registros, prontos para serem adicionados nas colunas
    # do dataframe final       

    #print(len(lista_teste))
    #print(len(lista_cod_componente))
    #print(len(lista_nome_componente))

    #### Criar um novo df vazio temporário para cada semestre e ajustar o novo df com as novas colunas
    df_temp = pd.DataFrame()
    #print(df_temp)

    #Adicionandos as novas colunas cod_componente e nome_componente do curso no dataframe
    df_temp['discente'] = lista_discente
    df_temp['id_curso'] = lista_id_curso
    df_temp['nome_curso'] = lista_nome_curso
    df_temp['id_turma'] = lista_id_turma
    df_temp['cod_componente'] = lista_cod_componente
    df_temp['nome_componente'] = lista_nome_componente
    df_temp['media_final'] = lista_media_final
    df_temp['descricao'] = lista_descricao

    #colocar o semestre atual pela sequencia de leitura dos arquivos
    lista_semestres = ["2022.1", "2022.2", 
                      "2021.1", "2021.2", 
                      "2020.6", "2020.5", "2020.2", 
                      "2019.1", "2019.2",
                      "2018.1", "2018.2",]

    if contador == 1:
        semestre = lista_semestres[0]
    elif contador == 2:
        semestre = lista_semestres[1]
    elif contador == 3:
        semestre = lista_semestres[2]
    elif contador == 4:
        semestre = lista_semestres[3]
    elif contador == 5:
        semestre = lista_semestres[4]
    elif contador == 6:
        semestre = lista_semestres[5]
    elif contador == 7:
        semestre = lista_semestres[6]
    elif contador == 8:
        semestre = lista_semestres[7]
    elif contador == 9:
        semestre = lista_semestres[8]
    elif contador == 10:
        semestre = lista_semestres[9]
    else :
        semestre = lista_semestres[10]

    #gerar uma lista com a mesma quantidade de linhas do df_temp para o semestre atual
    lista_semestre_atual = []
    for i in range(1,len(df_temp)+1):
        lista_semestre_atual.append(semestre)

    #adicionando a coluna semestre no df
    df_temp['semestre'] = lista_semestre_atual

    #Organizando as novas colunas criadas acima no header final
    header_final = ["discente", "id_curso", "nome_curso", "id_turma", "cod_componente", 
                    "nome_componente", "media_final", "descricao", "semestre"]
    
    df_temp = df_temp[header_final]

    #gerar um novo index para o df
    novo_index = []
    for i in range(1,len(df_temp)+1):
        novo_index.append(i)

    #print(index)

    #adicionar a coluna index no dataframe
    df_temp['id'] = novo_index
    #definir a coluna criada id como index do dataframe
    df_temp.set_index('id', inplace=True)
    #print(df_temp)

    #utilizando o método contat do pandas para concatenar os df gerados
    df_final = pd.concat([df_final, df_temp])

#Visualizar todo o dataframe com redirecionamente de saída em arquivo de texto "python3 etl.py > teste.txt"
#print(df_final.to_string())

#transformar em csv e salvar
df_final.to_csv("df_final.csv")


