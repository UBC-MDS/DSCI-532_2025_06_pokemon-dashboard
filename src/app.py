import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dcc, Input, Output, State, callback
from dash.exceptions import PreventUpdate
import pandas as pd

df=pd.read_csv('data/raw/pokemon.csv')
a=df[["name"]]
a=a.rename(columns={"name":"label"})
a["value"]=df['pokedex_number']

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Layout
app.layout = dbc.Container([
    html.Div([
    html.H1('Welcome to Pokédash'),
    html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
    html.P("This is an app created by Agam, Albert, Nicholas and Shannon")]),
    html.Label('Filter for weight in kg'),
    html.Label('Select type'),
    # dcc.Dropdown(
    #     options=['New York City', 'Montreal', 'San Francisco'],
    #     value='Montreal',
    # ),
    html.Br(),
    # A widget with a self-explanatory placeholder does not need a label
    dcc.Dropdown(
        options=['Normal','Fire', 'Water', 'Electric', 'Grass', 'Ice',
                 'Fighting', 'Poison','Ground', 'Flying', 'Psychic', 'Bug', 
                 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'],
        multi=True,
        placeholder='Select multiple types'
    ),
    html.Div([
        "Single dynamic Dropdown",
        dcc.Dropdown(id="my-dynamic-dropdown")
    ]),
])
options=a.to_dict(orient='records')
@callback(
    Output("my-dynamic-dropdown", "options"),
    Input("my-dynamic-dropdown", "search_value")
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)