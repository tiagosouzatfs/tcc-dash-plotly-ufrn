import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, Dash, html, dcc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    
    html.Div(
    [
        dbc.Button("Informações sobre o projeto", id="open-dismiss"),
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle("TCC - INFORMAÇÕES"), close_button=False
                ),
                dbc.ModalBody(
                    "-> Docente: Luis Affonso Guedes "
                    "-> Discente: Tiago Felipe de Souza "
                    "-> Título: Avaliação de desempenho dos alunos do curso de "
                    "Engenharia de Computação da UFRN."
                ),
                dbc.ModalFooter(dbc.Button("Close", id="close-dismiss")),
            ],
            id="modal-dismiss",
            keyboard=False,
            backdrop="static",
            ),
        ],
    ),

	html.H1("Projeto Final - TCC", style={'display': 'flex', 'align-items': 'center', 
                                       'justify-content': 'center'}),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container 
], style={"font-family": "Times"})


@app.callback(
    Output("modal-dismiss", "is_open"),
    [Input("open-dismiss", "n_clicks"), Input("close-dismiss", "n_clicks")],
    [State("modal-dismiss", "is_open")],
)
def toggle_modal(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open


if __name__ == '__main__':
	app.run_server(host="0.0.0.0", debug=False, port=8050)
