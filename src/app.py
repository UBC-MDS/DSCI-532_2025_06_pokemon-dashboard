from dash import Dash, html, dcc

import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Layout
app.layout = dbc.Container([
    html.Div([
    html.H1('Welcome to Pokédash'),
    html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
    html.P("This is an app created by Agam, Albert, Nicholas and Shannon")]),
    html.Label('Filter for weight in kg'),
    dcc.RangeSlider(
        min=1,
        max=1000,
        #value=[1, 3],  # A list since it's a range slideer
        step=1,  # The step between values
        marks={1: '>=1', 1000: '1000'},  # The marks/labels on the slider
        tooltip={'always_visible': True, 'placement': 'bottom'}  # Show the current values
    ),
    html.Br(),  # Add whitespace; br = "break"
    html.Label('Filter for Height in cm'),
    dcc.RangeSlider(
        min=4,
        max=2000,
        #value=[1, 3],  # A list since it's a range slideer
        step=1,  # The step between values
        marks={4: '4', 2000: '2000'},  # The marks/labels on the slider
        tooltip={'always_visible': True, 'placement': 'bottom'}  # Show the current values
    ),
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
    )
])

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)