import pandas as pd
from dash import html, dcc, callback, Input, Output
import dash
import plotly.express as px

path_datasets = 'assets/'

df_final = pd.read_csv(f"{path_datasets}df_final.csv", sep=",")
#print(df_final)

df_final['semestre'] = df_final['semestre'].astype(str)

###############################################################################################

# APROVADO
# APROVADO POR NOTA
# REPROVADO = REPROVADO, REPROVADO POR MÉDIA E POR FALTAS, REPROVADO POR NOTA, REPROVADO POR NOTA E FALTA, REPROVADO POR FALTAS

################################################################################################

dash.register_page(__name__, path='/dash_web_geral')

layout = html.Div(children=[
    html.H2(children='Análise inicial geral e por componente em gráfico de barras', style={"text-align":"center"}),
    html.Br(),
	html.Div([
        "Selecione uma opção para pesquisa: ",
        dcc.RadioItems(id='type_chart', options=['Geral', 'Por disciplina'], value="Geral")
    ]),

    html.Br(),
    html.Label('Dropdown - Selecione uma disciplina:'),
    dcc.Dropdown(id="list_componente", options=["", "ANÁLISE DE SINAIS E SISTEMAS", "MATEMÁTICA DISCRETA", "TEORIA DE CIRCUITOS","PROCESSAMENTO DIGITAL DE SINAIS",
                            "CIRCUITOS DIGITAIS - TEORIA", "CIRCUITOS DIGITAIS - TEORIA", "ELETRÔNICA - TEORIA", "ELETRÔNICA - LABORATÓRIO", 
                            "PROGRAMAÇÃO AVANÇADA", "ARQUITETURA DE COMPUTADORES", "MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS", 
                            "OTIMIZAÇÃO DE SISTEMAS", "REDES DE COMPUTADORES", "PROJETO E ENGENHARIA DE SOFTWARE", "BANCO DE DADOS", 
                            "ALGORITMOS E ESTRUTURAS DE DADOS I", "SISTEMAS OPERACIONAIS", "SISTEMAS DIGITAIS", "INTELIGÊNCIA ARTIFICIAL", 
                            "LINGUAGENS FORMAIS E AUTÔMATOS", "COMPUTAÇÃO GRÁFICA", "ALGORITMOS E ESTRUTURAS DE DADOS II", "COMPILADORES", 
                            "PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA", "SISTEMAS DE TEMPO REAL", "SISTEMAS DE CONTROLE - TEORIA", 
                            "SISTEMAS DE CONTROLE - LABORATÓRIO", "CIÊNCIA DE DADOS", "ENGENHARIA DE DADOS", "ALGORITMOS E LÓGICA DE PROGRAMAÇÃO" ], value=" ", clearable=False),
    
    html.Br(),
    html.Label('Dropdown - Selecione um semestre:'),
    dcc.Dropdown(id="list_semestre", options=["", "2018.1", "2018.2", "2019.1", "2019.2", "2020.5", "2020.6", "2020.2", "2021.1", "2021.2", "2022.1", "2022.2", "Todos"], value=" ", clearable=False),
    
    html.Br(),
    dcc.Graph(id='chart')
])

@callback(
    Output('chart', 'figure'),
    Input('type_chart', 'value'),
    Input('list_componente', 'value'),
    Input('list_semestre', 'value')
)

def update_city_selected(type_chart, list_componente, list_semestre):
    if type_chart == "Geral":
        df = df_final.loc[((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                | (df_final['descricao'] == 'REPROVADO'))]
        
        df = df.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

        figure = px.bar(df, x="nome_componente", y="media_final", color="descricao", height=800, title="Gráfico de todas as disciplinas do semestre 2018.1 ao 2022.2 por situação dos alunos")
        
    elif type_chart == 'Por disciplina' and list_semestre == "Todos":
        df = df_final.loc[((df_final['nome_componente'] == list_componente) & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                | (df_final['descricao'] == 'REPROVADO')))]

        df = df.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")
    
        figure=px.bar(df, x="semestre", y="media_final", color="descricao", text="descricao", height=500)

    elif type_chart == 'Por disciplina' and list_semestre != "Todos":
        df = df_final.loc[((df_final['nome_componente'] == list_componente) & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                | (df_final['descricao'] == 'REPROVADO')) & (df_final['semestre'] == list_semestre))]

        df = df.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")
    
        figure=px.bar(df, x="semestre", y="media_final", color="descricao", text="descricao", height=500)

    return figure


