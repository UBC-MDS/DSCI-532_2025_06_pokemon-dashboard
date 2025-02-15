from dash import Dash, html

import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Layout
app.layout = html.Div()
app.layout = html.Div([
    html.H1('Welcome to Pokédash'),
    html.P('Pokédash is your personal Pokéguide to understand your lil pocket monster'),
    html.P("This is an app created by Agam, Albert, Nicholas and Shannon")
])

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)