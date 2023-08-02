import dash
from dash import html

dash.register_page(__name__, path='/')

image_path = '../assets/componentes.png'

layout = html.Div(children=[
    html.Div(children=[
        html.Br(),
        html.H2('Gráficos interativos e comparativos das 5 disciplinas que \
                mais aprovaram e 5 disciplinas que mais reprovaram nos períodos \
                de antes, durante e depois da pandemia do curso de Engenharia de Computação.'),
        html.Br(),
        html.H3('* O período de antes da pandemia corresponde aos semestres 2018.1 ao 2019.2;'),
        html.H3('* O período de durante da pandemia corresponde aos semestres 2020.5 ao 2021.2;'),
        html.H3('* O período de depois da pandemia corresponde aos semestres 2022.1 ao 2022.2;'),
        html.Br(),
        html.H3('As disciplinas consideradas neste estudo cosntam na imagem abaixo:', 
                style={"text-align":"center"}),
        html.Img(src=image_path, height="800px", width="1200px", 
                 style={"text-align":"center", "margin": "auto", "display": "block"}),
]), 

])
