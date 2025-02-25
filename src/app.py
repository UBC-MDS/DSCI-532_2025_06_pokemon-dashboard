from dash import Dash, dcc, html, Input, Output, State, callback
from dash.exceptions import PreventUpdate
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd


df = pd.read_csv('data/raw/pokemon.csv')
a = df[["name"]]
a = a.rename(columns={"name": "label"})
a["value"] = df['pokedex_number']

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

pokemon_data = pd.read_csv('../data/raw/pokemon.csv')

# Layout
app.layout = dbc.Container([
    html.Div([
        html.H1('Welcome to Pokédash'),
        html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
        html.P("This is an app created by Agam, Albert, Nicholas and Shannon")]),
<<<<<<< HEAD
    html.H1('Welcome to Pokédash'),
    html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
    html.P("This is an app created by Agam, Albert, Nicholas and Shannon")]),
    html.Label('Filter for weight in kg'),
=======
>>>>>>> e0d30f2 (remove old components and add relevant scatterplot code. Add linting changes.)
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
    html.Div([
        "Single dynamic Dropdown",
        dcc.Dropdown(id="my-dynamic-dropdown")
    ]),
    html.Br(),
    html.Div(id='output_area'),
])

options = a.to_dict(orient='records')


@callback(
    Output("my-dynamic-dropdown", "options"),
    Input("my-dynamic-dropdown", "search_value")
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


# Server side callbacks/reactivity
@callback(
    Output('output_area', 'children'),
    Input('input_dropdown', 'value'))
def update_output(input_value):
    return input_value


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
