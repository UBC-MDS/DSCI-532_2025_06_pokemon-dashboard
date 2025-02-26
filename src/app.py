from dash import Dash, dcc, html, Input, Output, State, callback
from dash.exceptions import PreventUpdate
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd


df = pd.read_csv('data/raw/pokemon.csv')
a = df[['name']]
a = a.rename(columns={'name': 'label'})
a['value'] = df['pokedex_number']

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Layout
app.layout = dbc.Container([
    html.Div([
        html.H1('Welcome to Pokédash'),
        html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
        html.P('This is an app created by Agam, Albert, Nicholas, and Shannon')]),
    html.Br(),
    html.Div([
        'Single dynamic Dropdown',
        dcc.Dropdown(id='my_dynamic_dropdown')
    ]),
    html.Br(),
    html.Div(id='output_area')
])


@callback(
    Output('my_dynamic_dropdown', 'options'),
    Input('my_dynamic_dropdown', 'search_value')
)
def update_options(search_value):
    options = a.to_dict(orient='records')
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o['label']]


@callback(
    Output('output_area', 'children'),
    Input('my_dynamic_dropdown', 'value'))
def update_output(input_value):
    return f'Pokedex Number: {input_value}'


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
