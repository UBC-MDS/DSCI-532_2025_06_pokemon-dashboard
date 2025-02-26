from dash import Dash, dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd


df = pd.read_csv("data/raw/pokemon.csv")
df['generation'] = df['generation'].astype('category')
a = df[["name"]]
a = a.rename(columns={"name": "label"})
a["value"] = df["pokedex_number"]

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

scatterplot_options = [
    {"label": "Attack", "value": "attack"},
    {"label": "Defense", "value": "defense"},
    {"label": "Special Attack", "value": "sp_attack"},
    {"label": "Special Defense", "value": "sp_defense"},
    {"label": "Speed", "value": "speed"},
    {"label": "HP", "value": "hp"},
    {"label": "Height (m)", "value": "height_m"},
    {"label": "Weight (kg)", "value": "weight_kg"},
]

# Layout
app.layout = dbc.Container([
    html.Div([
        html.H1("Welcome to Pokédash"),
        html.P("Pokédash is your personal Pokéguide to understand your lil pocket monster"),
        html.P("This is an app created by Agam, Albert, Nicholas, and Shannon"),
        ]),
    html.Br(),
    html.Div([
        "Single dynamic Dropdown",
        dcc.Dropdown(id="my_dynamic_dropdown", search_value="Pikachu", value=25),
        html.Div(id="output_area"),
        ]),
    html.Br(),
    html.Div([
        html.H2('Scatterplot'),
        html.Div([
            html.Label("x-axis label:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id="x_col",
                options=scatterplot_options,
                value="speed",
                clearable=False,
                placeholder="x-axis property",
                style={"minWidth": "100px", "flex": "1"},
                ),
                ],
                style={"display": "flex", "alignItems": "center"},
            ),
        html.Div([
            html.Label("y-axis label:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id="y_col",
                options=scatterplot_options,
                value="attack",
                clearable=False,
                placeholder="y-axis property",
                style={"minWidth": "100px", "flex": "1"},
                ),
                ],
                style={"display": "flex", "alignItems": "center"},
            ),
        html.Br(),
        dvc.Vega(id='scatter', spec={}, style={'width': '100%'}),
    ]),
])


@callback(
    Output("my_dynamic_dropdown", "options"),
    Input("my_dynamic_dropdown", "search_value"),
)
def update_options(search_value):
    options = a.to_dict(orient="records")
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


@callback(
    Output("output_area", "children"),
    Input("my_dynamic_dropdown", "value")
)
def update_output(input_value):
    return f"Pokedex Number: {input_value}"


@callback(
    Output("scatter", "spec"),
    Input("x_col", "value"),
    Input("y_col", "value"),
    Input("my_dynamic_dropdown", "value")
)
def create_chart(x_col, y_col, selected_pokemon_id):
    brush = alt.selection_interval()
    click = alt.selection_point(fields=['generation'], bind='legend', empty='all')
    base = alt.Chart(df, width="container").mark_point(
        filled=True,
        size=100
    ).encode(
        x=x_col,
        y=y_col,
        tooltip="name",
        color=alt.condition(brush, 'generation', alt.value('lightgray')),
        opacity=alt.condition(click, alt.value(0.9), alt.value(0.2))
    ).add_params(brush, click)

    selected_plot = alt.Chart(
        df.loc[df['pokedex_number'] == selected_pokemon_id],
        width="container"
    ).mark_point(
        color="black",
        shape="diamond",
        filled=True,
        size=600
    ).encode(
        x=x_col,
        y=y_col,
        tooltip="name"
    )
    return alt.layer(base, selected_plot).interactive().to_dict()


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=True)
