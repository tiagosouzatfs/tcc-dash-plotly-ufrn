import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output, callback
import dash

path_datasets = 'assets/'

df_final = pd.read_csv(f"{path_datasets}df_final.csv", sep=",")
#print(df_final)

df_final['semestre'] = df_final['semestre'].astype(str)


########################## Antes da pandemia #################################################
#APROVADOS
df = df_final.loc[((df_final['nome_componente'] == 'SISTEMAS DE TEMPO REAL') | (df_final['nome_componente'] == 'SISTEMAS OPERACIONAIS')
                   | (df_final['nome_componente'] == 'SISTEMAS DIGITAIS') | (df_final['nome_componente'] == 'PROCESSAMENTO DIGITAL DE SINAIS')
                   | (df_final['nome_componente'] == 'REDES DE COMPUTADORES'))
                   & ((df_final['semestre'] == '2018.1') | (df_final['semestre'] == '2018.2') 
                   | (df_final['semestre'] == '2019.1') | (df_final['semestre'] == '2019.2')) 
                   & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                   | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                   | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                   | (df_final['descricao'] == 'REPROVADO'))]

#REPROVADOS
df1 = df_final.loc[((df_final['nome_componente'] == 'MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS') | (df_final['nome_componente'] == 'PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA')
                   | (df_final['nome_componente'] == 'SISTEMAS DIGITAIS') | (df_final['nome_componente'] == 'PROCESSAMENTO DIGITAL DE SINAIS')
                   | (df_final['nome_componente'] == 'OTIMIZAÇÃO DE SISTEMAS'))
                   & ((df_final['semestre'] == '2018.1') | (df_final['semestre'] == '2018.2') 
                   | (df_final['semestre'] == '2019.1') | (df_final['semestre'] == '2019.2')) 
                   & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                   | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                   | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                   | (df_final['descricao'] == 'REPROVADO'))]

df = df.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

df1 = df1.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

########################## Durante a pandemia #################################################
#APROVADOS
df2 = df_final.loc[((df_final['nome_componente'] == 'SISTEMAS DE TEMPO REAL') | (df_final['nome_componente'] == 'SISTEMAS OPERACIONAIS')
                   | (df_final['nome_componente'] == 'COMPUTAÇÃO GRÁFICA') | (df_final['nome_componente'] == 'SISTEMAS DE CONTROLE - LABORATÓRIO')
                   | (df_final['nome_componente'] == 'CIÊNCIA DE DADOS'))
                   & ((df_final['semestre'] == '2020.5') | (df_final['semestre'] == '2020.6') 
                   | (df_final['semestre'] == '2020.2') | (df_final['semestre'] == '2021.1')
                   | (df_final['semestre'] == '2021.2')) 
                   & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                   | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                   | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                   | (df_final['descricao'] == 'REPROVADO'))]

#REPROVADOS
df3 = df_final.loc[((df_final['nome_componente'] == 'MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS') | (df_final['nome_componente'] == 'PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA')
                   | (df_final['nome_componente'] == 'TEORIA DE CIRCUITOS') | (df_final['nome_componente'] == 'CIRCUITOS DIGITAIS - TEORIA')
                   | (df_final['nome_componente'] == 'OTIMIZAÇÃO DE SISTEMAS'))
                   & ((df_final['semestre'] == '2020.5') | (df_final['semestre'] == '2020.6') 
                   | (df_final['semestre'] == '2020.2') | (df_final['semestre'] == '2021.1')
                   | (df_final['semestre'] == '2021.2')) 
                   & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                   | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                   | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                   | (df_final['descricao'] == 'REPROVADO'))]

df2 = df2.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

df3 = df3.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

########################## Depois da pandemia #################################################
#APROVADOS
df4 = df_final.loc[((df_final['nome_componente'] == 'SISTEMAS DE TEMPO REAL') | (df_final['nome_componente'] == 'SISTEMAS OPERACIONAIS')
                   | (df_final['nome_componente'] == 'SISTEMAS DIGITAIS') | (df_final['nome_componente'] == 'ALGORITMOS E ESTRUTURAS DE DADOS II')
                   | (df_final['nome_componente'] == 'LINGUAGENS FORMAIS E AUTÔMATOS'))
                   & ((df_final['semestre'] == '2022.1') | (df_final['semestre'] == '2022.2')) 
                   & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                   | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                   | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                   | (df_final['descricao'] == 'REPROVADO'))]

#REPROVADOS
df5 = df_final.loc[((df_final['nome_componente'] == 'MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS') | (df_final['nome_componente'] == 'PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA')
                   | (df_final['nome_componente'] == 'TEORIA DE CIRCUITOS') | (df_final['nome_componente'] == 'PROCESSAMENTO DIGITAL DE SINAIS')
                   | (df_final['nome_componente'] == 'ALGORITMOS E ESTRUTURAS DE DADOS I'))
                   & ((df_final['semestre'] == '2022.1') | (df_final['semestre'] == '2022.2')) 
                   & ((df_final['descricao'] == 'APROVADO') | (df_final['descricao'] == 'APROVADO POR NOTA')
                   | (df_final['descricao'] == 'REPROVADO POR MÉDIA E POR FALTAS') | (df_final['descricao'] == 'REPROVADO POR NOTA') 
                   | (df_final['descricao'] == 'REPROVADO POR NOTA E FALTA') | (df_final['descricao'] == 'REPROVADO POR FALTAS') 
                   | (df_final['descricao'] == 'REPROVADO'))]

df4 = df4.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

df5 = df5.replace(to_replace=["REPROVADO POR MÉDIA E POR FALTAS", "REPROVADO POR NOTA", 
                            "REPROVADO POR NOTA E FALTA", "REPROVADO POR FALTAS"], value="REPROVADO")

######################################################################################################

# Initialize the app
#app = Dash(__name__)

dash.register_page(__name__, path='/dash_web_tcc')

# App layout
#app.layout = html.Div([

layout = html.Div([

html.Div(children=[        
        html.Label('Dropdown - Situação da Pandemia:'),
        dcc.Dropdown(id="situacao_pandemia", options=["Antes", "Durante", "Depois"], value="Antes", clearable=False),
        html.Br(),
        html.Label('Dropdown - Situação das disciplinas:'),
        dcc.Dropdown(id="situacao_disciplina", options=["Mais aprovaram", "Mais reprovaram"], value="Mais aprovaram", clearable=False),
], style={'position':'relative', 'left':'40%', 'top':'50%', 'display': 'inline-block'}),

html.Br(),

html.Div(),
dcc.Graph(id="barras"),    

html.Div(),
dcc.Graph(id="histograma"),

html.Div(),
dcc.Graph(id="dispercao"),

html.Div(),
dcc.Graph(id="boxplot"),

html.Div(),
dcc.Graph(id="strip"),

html.Div(),
dcc.Graph(id="sunburst"),

html.Div(),
dcc.Graph(id="radar"),

html.A(html.Button("Voltar para o início!"), href="/dash_web_tcc")

])

#@app.callback(
@callback(
        Output("barras", "figure"),
        Output("histograma", "figure"),
        Output("dispercao", "figure"),
        Output("boxplot", "figure"),
        Output("strip", "figure"),
        Output("sunburst", "figure"),
        Output("radar", "figure"),
        Input("situacao_pandemia", "value"),
        Input("situacao_disciplina", "value"),
)

def generate_charts(situacao_pandemia, situacao_disciplina):

        if situacao_pandemia == "Antes" and situacao_disciplina == "Mais aprovaram":
                figure=px.bar(df, x="descricao", y="media_final", color="nome_componente", barmode="group",
                facet_row="semestre", height=800,
                title="Top 5 disciplinas que mais aprovaram e os estados de Aprovado, Aprovado por Nota e Reprovado")
        
                figure1=px.histogram(df, x="media_final", color="nome_componente", height=800, facet_row="semestre",
                title="Histograma das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure2=px.scatter(df, x="media_final", y="id", color="nome_componente", height=900, facet_row="semestre",
                size='media_final', 
                title="Dispersão das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure3=px.box(df, x="nome_componente", y="media_final", color="descricao", height=800,
                title="Boxplot das médias finais dos alunos antes da pandemia das 5 disciplinas que mais aprovaram").update_traces(quartilemethod="exclusive")

                figure4=px.strip(df, x='descricao', y='media_final', color='nome_componente', height=900, facet_row="semestre",
                title="Concentração de pontos das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure5=px.sunburst(data_frame=df, path=["nome_curso", "semestre", "nome_componente", "descricao", "media_final"],
                height=800, maxdepth=5, title="Gráfico de rajada das 5 disciplinas que mais aprovaram")

                figure6=px.line_polar(df, r="media_final", theta="descricao", color="nome_componente", 
                hover_name="nome_componente", hover_data={"nome_componente":False}, height=800,
                markers=True, title="Gráfico de radar das 5 disciplinas que mais aprovaram").update_traces(fill="toself")


        elif situacao_pandemia == "Antes" and situacao_disciplina == "Mais reprovaram":
                figure=px.bar(df1, x="descricao", y="media_final", color="nome_componente", barmode="group",
                facet_row="semestre", height=800,
                title="Top 5 disciplinas que mais aprovaram e os estados de Aprovado, Aprovado por Nota e Reprovado")
        
                figure1=px.histogram(df1, x="media_final", color="nome_componente", height=800, facet_row="semestre",
                title="Histograma das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")
    
                figure2=px.scatter(df1, x="media_final", y="id", color="nome_componente", height=900, facet_row="semestre",
                size='media_final', 
                title="Dispersão das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure3=px.box(df1, x="nome_componente", y="media_final", color="descricao", height=800,
                title="Boxplot das médias finais dos alunos antes da pandemia das 5 disciplinas que mais reprovaram").update_traces(quartilemethod="exclusive")

                figure4=px.strip(df1, x='descricao', y='media_final', color='nome_componente', height=900, facet_row="semestre",
                title="Concentração de pontos das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure5=px.sunburst(data_frame=df1, path=["nome_curso", "semestre", "nome_componente", "descricao", "media_final"],
                height=800, maxdepth=5, title="Gráfico de rajada das 5 disciplinas que mais reprovaram")

                figure6=px.line_polar(df1, r="media_final", theta="descricao", color="nome_componente", 
                hover_name="nome_componente", hover_data={"nome_componente":False}, height=800,
                markers=True, title="Gráfico de radar das 5 disciplinas que mais reprovaram").update_traces(fill="toself")

        elif situacao_pandemia == "Durante" and situacao_disciplina == "Mais aprovaram":
                figure=px.bar(df2, x="descricao", y="media_final", color="nome_componente", barmode="group",
                facet_row="semestre", height=800,
                title="Top 5 disciplinas que mais aprovaram e os estados de Aprovado, Aprovado por Nota e Reprovado")
        
                figure1=px.histogram(df2, x="media_final", color="nome_componente", height=800, facet_row="semestre",
                title="Histograma das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure2=px.scatter(df2, x="media_final", y="id", color="nome_componente", height=900, facet_row="semestre",
                size='media_final', 
                title="Dispersão das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure3=px.box(df2, x="nome_componente", y="media_final", color="descricao", height=800,
                title="Boxplot das médias finais dos alunos antes da pandemia das 5 disciplinas que mais aprovaram").update_traces(quartilemethod="exclusive")

                figure4=px.strip(df2, x='descricao', y='media_final', color='nome_componente', height=900, facet_row="semestre",
                title="Concentração de pontos das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure5=px.sunburst(data_frame=df2, path=["nome_curso", "semestre", "nome_componente", "descricao", "media_final"],
                height=800, maxdepth=5, title="Gráfico de rajada das 5 disciplinas que mais aprovaram")

                figure6=px.line_polar(df2, r="media_final", theta="descricao", color="nome_componente", 
                hover_name="nome_componente", hover_data={"nome_componente":False}, height=800,
                markers=True, title="Gráfico de radar das 5 disciplinas que mais aprovaram").update_traces(fill="toself")

        elif situacao_pandemia == "Durante" and situacao_disciplina == "Mais reprovaram":
                figure=px.bar(df3, x="descricao", y="media_final", color="nome_componente", barmode="group",
                facet_row="semestre", height=800,
                title="Top 5 disciplinas que mais aprovaram e os estados de Aprovado, Aprovado por Nota e Reprovado")
        
                figure1=px.histogram(df3, x="media_final", color="nome_componente", height=800, facet_row="semestre",
                title="Histograma das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure2=px.scatter(df3, x="media_final", y="id", color="nome_componente", height=900, facet_row="semestre",
                size='media_final', 
                title="Dispersão das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure3=px.box(df3, x="nome_componente", y="media_final", color="descricao", height=800,
                title="Boxplot das médias finais dos alunos antes da pandemia das 5 disciplinas que mais reprovaram").update_traces(quartilemethod="exclusive")

                figure4=px.strip(df3, x='descricao', y='media_final', color='nome_componente', height=900, facet_row="semestre",
                title="Concentração de pontos das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure5=px.sunburst(data_frame=df3, path=["nome_curso", "semestre", "nome_componente", "descricao", "media_final"],
                height=800, maxdepth=5, title="Gráfico de rajada das 5 disciplinas que mais reprovaram")

                figure6=px.line_polar(df3, r="media_final", theta="descricao", color="nome_componente", 
                hover_name="nome_componente", hover_data={"nome_componente":False}, height=800,
                markers=True, title="Gráfico de radar das 5 disciplinas que mais reprovaram").update_traces(fill="toself")

        elif situacao_pandemia == "Depois" and situacao_disciplina == "Mais aprovaram":
                figure=px.bar(df4, x="descricao", y="media_final", color="nome_componente", barmode="group",
                facet_row="semestre", height=800,
                title="Top 5 disciplinas que mais aprovaram e os estados de Aprovado, Aprovado por Nota e Reprovado")
        
                figure1=px.histogram(df4, x="media_final", color="nome_componente", height=800, facet_row="semestre",
                title="Histograma das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure2=px.scatter(df4, x="media_final", y="id", color="nome_componente", height=900, facet_row="semestre",
                size='media_final', 
                title="Dispersão das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure3=px.box(df4, x="nome_componente", y="media_final", color="descricao", height=800,
                title="Boxplot das médias finais dos alunos antes da pandemia das 5 disciplinas que mais aprovaram").update_traces(quartilemethod="exclusive")

                figure4=px.strip(df4, x='descricao', y='media_final', color='nome_componente', height=900, facet_row="semestre",
                title="Concentração de pontos das médias finais dos alunos por semestre das 5 disciplinas que mais aprovaram")

                figure5=px.sunburst(data_frame=df4, path=["nome_curso", "semestre", "nome_componente", "descricao", "media_final"],
                height=800, maxdepth=5, title="Gráfico de rajada das 5 disciplinas que mais aprovaram")

                figure6=px.line_polar(df4, r="media_final", theta="descricao", color="nome_componente", 
                hover_name="nome_componente", hover_data={"nome_componente":False}, height=800,
                markers=True, title="Gráfico de radar das 5 disciplinas que mais aprovaram").update_traces(fill="toself")

        elif situacao_pandemia == "Depois" and situacao_disciplina == "Mais reprovaram":
                figure=px.bar(df5, x="descricao", y="media_final", color="nome_componente", barmode="group",
                facet_row="semestre", height=800,
                title="Top 5 disciplinas que mais aprovaram e os estados de Aprovado, Aprovado por Nota e Reprovado")
        
                figure1=px.histogram(df5, x="media_final", color="nome_componente", height=800, facet_row="semestre",
                title="Histograma das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure2=px.scatter(df5, x="media_final", y="id", color="nome_componente", height=900, facet_row="semestre",
                size='media_final', 
                title="Dispersão das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure3=px.box(df5, x="nome_componente", y="media_final", color="descricao", height=800,
                title="Boxplot das médias finais dos alunos antes da pandemia das 5 disciplinas que mais reprovaram").update_traces(quartilemethod="exclusive")

                figure4=px.strip(df5, x='descricao', y='media_final', color='nome_componente', height=900, facet_row="semestre",
                title="Concentração de pontos das médias finais dos alunos por semestre das 5 disciplinas que mais reprovaram")

                figure5=px.sunburst(data_frame=df5, path=["nome_curso", "semestre", "nome_componente", "descricao", "media_final"],
                height=800, maxdepth=5, title="Gráfico de rajada das 5 disciplinas que mais reprovaram")

                figure6=px.line_polar(df5, r="media_final", theta="descricao", color="nome_componente", 
                hover_name="nome_componente", hover_data={"nome_componente":False}, height=800,
                markers=True, title="Gráfico de radar das 5 disciplinas que mais reprovaram").update_traces(fill="toself")

        return (figure, figure1, figure2, figure3, figure4, figure5, figure6)





# Run the app
#if __name__ == '__main__':
#    app.run_server(debug=True)