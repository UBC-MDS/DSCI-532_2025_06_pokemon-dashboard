from dash import Dash, html, dcc, callback, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

pokemon_data = pd.read_csv('../data/raw/pokemon.csv')

# Layout
app.layout = dbc.Container([
    html.Div([
        html.H1('Welcome to Pokédash'),
        html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
        html.P("This is an app created by Agam, Albert, Nicholas and Shannon")]),
    html.Label('Select type'),
    html.Br(),
    dcc.Dropdown(
        id='input_dropdown',
        options=['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice',
                 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug',
                 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'],
        multi=True,
        placeholder='Select multiple types'
    ),
    html.Br(),
    html.Div(id='output_area'),
])

# Server side callbacks/reactivity
@callback(
    Output('output_area', 'children'),
    Input('input_dropdown', 'value'))
def update_output(input_value):
    return input_value

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
