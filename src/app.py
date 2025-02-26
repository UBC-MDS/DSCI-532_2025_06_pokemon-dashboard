from dash import Dash, dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("data/raw/pokemon.csv")
df['generation'] = df['generation'].astype('category')
a = df[["name"]]
a = a.rename(columns={"name": "label"})
a["value"] = df["pokedex_number"]

# Calculate average stats for each Pokémon
stats_columns = ['sp_attack', 'sp_defense', 'attack', 'defense', 'hp']
df['average_stat'] = df[stats_columns].mean(axis=1)

# Sort by average stats
top_7 = df[['name', 'average_stat']].sort_values(by='average_stat', ascending=False).head(7)


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

type_options = [
    {'label': 'Normal', 'value': 'Normal'}, 
    {'label': 'Fire', 'value': 'Fire'}, 
    {'label': 'Water', 'value': 'Water'}, 
    {'label': 'Electric', 'value': 'Electric'}, 
    {'label': 'Grass', 'value': 'Grass'}, 
    {'label': 'Ice', 'value': 'Ice'}, 
    {'label': 'Fighting', 'value': 'Fighting'}, 
    {'label': 'Poison', 'value': 'Poison'}, 
    {'label': 'Ground', 'value': 'Ground'}, 
    {'label': 'Flying', 'value': 'Flying'}, 
    {'label': 'Psychic', 'value': 'Psychic'}, 
    {'label': 'Bug', 'value': 'Bug'}, 
    {'label': 'Rock', 'value': 'Rock'}, 
    {'label': 'Ghost', 'value': 'Ghost'}, 
    {'label': 'Dragon', 'value': 'Dragon'}, 
    {'label': 'Dark', 'value': 'Dark'}, 
    {'label': 'Steel', 'value': 'Steel'}, 
    {'label': 'Fairy', 'value': 'Fairy'}
]

# Layout
app.layout = dbc.Container([
    dbc.Row([
        # Navigation Bar
        dbc.Col([

            # Welcome Message
            html.Div([
                html.H1([
                    html.Span("Pokédash"),
                ]),
                html.P("Pokédash is your personal Pokéguide to understand your lil pocket monster"),
                html.P("This is an app created by Agam, Albert, Nicholas, and Shannon"),
            ], style={"textAlign": "left"}),

            # Pokemon Dropdown
            html.Div([
                html.Div([
                    html.H2("Choose your Pokemon"),
                    html.Div(
                        dcc.Dropdown(id="pokemon_dropdown", search_value="Pikachu", value=25),
                        style={'width': '100%'}
                    ),
                    html.Div(id="output_area"),
                ]),
            ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px'}),

            # Image
            html.Div(
                html.Img(id='pokemon_image', style={'width': '75%'}),
                style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
            ),
            
            # Generation Dropdown
            html.Div([
                html.H2("Select Generation"),
                dcc.Dropdown(
                    id="generation_dropdown",
                    options=[{'label': str(i), 'value': i} for i in range(1, 9)],  # Generations 1 to 8
                    multi=True,
                    placeholder="Select Generation(s)",
                    style={'width': '100%'}
                ),
            ], style={'width': '100%', 'margin-bottom': '20px'}),
            
            # Type Dropdowns
            html.Div([
                # Container to hold both dropdowns side by side
                html.Div([
                    # Type 1 Dropdown
                    html.Div([
                        html.H2("Select Type 1"),
                        dcc.Dropdown(
                            id="type1_dropdown",
                            options=type_options,
                            multi=True,
                            placeholder="Select Type 1",
                            style={'width': '100%'}
                        ),
                    ], style={'flex': 1, 'margin-right': '10px'}),  # Type 1 with right margin

                    # Type 2 Dropdown
                    html.Div([
                        html.H2("Select Type 2"),
                        dcc.Dropdown(
                            id="type2_dropdown",
                            options=type_options,
                            multi=True,
                            placeholder="Select Type 2",
                            style={'width': '100%'}
                        ),
                    ], style={'flex': 1}),
                ], style={'display': 'flex', 'gap': '20px'}),  
            ], style={'width': '100%'}),

            # Stats RangeSliders
            html.Div([
                # Column 1 for RangeSliders
                html.Div([
                    html.H2("HP"),
                    dcc.RangeSlider(
                        id="hp_RangeSlider",
                        min=0,
                        max=255,
                        step=1,
                        value=[0, 255],
                        marks={0: '0', 255: '255'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    html.Br(),                    
                    html.H2("Attack"),
                    dcc.RangeSlider(
                        id="attack_RangeSlider",
                        min=0,
                        max=190,
                        step=1,
                        value=[0, 190],
                        marks={0: '0', 190: '190'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    html.Br(),                    
                    html.H2("Defense"),
                    dcc.RangeSlider(
                        id="defense_RangeSlider",
                        min=0,
                        max=250,
                        step=1,
                        value=[0, 250],
                        marks={0: '0', 250: '250'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                ], style={'flex': 1, 'marginTop': '1vh'}),  # Right column

                # Column 2 for RangeSliders
                html.Div([
                    html.H2("Sp. Attack"),
                    dcc.RangeSlider(
                        id="sp_attack_RangeSlider",
                        min=0,
                        max=190,
                        step=1,
                        value=[0, 190],
                        marks={0: '0', 190: '190'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    html.Br(),                    
                    html.H2("Sp. Defense"),
                    dcc.RangeSlider(
                        id="sp_defense_RangeSlider",
                        min=0,
                        max=250,
                        step=1,
                        value=[0, 250],
                        marks={0: '0', 250: '250'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    html.Br(),
                    html.H2("Speed"),
                    dcc.RangeSlider(
                        id="speed_RangeSlider",
                        min=0,
                        max=200,
                        step=1,
                        value=[0, 200],
                        marks={0: '0', 200: '200'},
                        tooltip={"placement": "bottom", "always_visible": True},
                    ),
                ], style={'flex': 1, 'marginTop': '1vh'}),  # Right column
            ], style={'display': 'flex', 'marginTop': '1vh'}),  # Flex container for two columns of RangeSliders
               
        ], width=2),  # Left column width
        
        # First Output Column
        dbc.Col([
            # First Row
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

            # Second Row
            html.Div([
                html.H2("Top 7 Pokémon by Stats"),
                dvc.Vega(id='top_7_chart', spec={}, style={'width': '100%'})  # Vega chart
            ], style={'padding': '1vh'})
            
        ], width=5),  # Right column width

        # Second Output Column
        dbc.Col([
            # First Row
            html.Div(
                dcc.Graph(
                    # figure=fig
                ),
                style={'width': '100%', 'height': '100%', 'padding': '1vh'}
            ),

            # Second Row
            html.Div(
                dcc.Graph(
                    # figure=fig
                ),
                style={'width': '100%', 'height': '100%', 'padding': '1vh'}
            )
        ], width=5)  # Right column width
    ], align="start")
], fluid=True, style={"height": "100vh", "padding": "4vh"})

@callback(
    Output("pokemon_dropdown", "options"),
    Input("pokemon_dropdown", "search_value"),
)
def update_options(search_value):
    options = a.to_dict(orient="records")
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


@callback(
    Output("output_area", "children"),
    Input("pokemon_dropdown", "value")
)
def update_output(input_value):
    return f"Pokedex Number: {input_value}"


@callback(
    Output('pokemon_image', 'src'),
    Input('pokemon_dropdown', 'value')
)
def update_image(selected_pokemon_id):
    # Construct the image URL based on the selected Pokemon ID
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png"
    return image_url


@callback(
    Output("scatter", "spec"),
    Input("x_col", "value"),
    Input("y_col", "value"),
    Input("pokemon_dropdown", "value")
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

@callback(
    Output("top_7_chart", "spec"),
    Input("pokemon_dropdown", "value")
)
def create_top7_histogram(selected_pokemon_id):
    # Filter the selected Pokémon based on the dropdown value
    selected_pokemon = df[df['pokedex_number'] == selected_pokemon_id][['name', 'average_stat']]
    top_7_updated = top_7.copy()  # Create a copy to avoid modifying the original top_7

    # If the selected Pokémon is not in the top 7, we add it
    if selected_pokemon['name'].values[0] not in top_7['name'].values:
        top_7_updated = pd.concat([top_7, selected_pokemon]).drop_duplicates(subset='name').nlargest(7, 'average_stat')  
    else:
        top_7_updated = top_7  # Keep the original top 7 if already in the list
    
    # Sort the Pokémon by 'average_stat' in descending order
    top_7_updated = top_7_updated.sort_values(by='average_stat', ascending=True)
    
    # Base bar chart for the top 7 Pokémon
    base_chart = alt.Chart(top_7_updated, width="container").mark_bar().encode(
        x=alt.X('average_stat', title='Average Stat'),
        y=alt.Y('name', sort='-x', title='Pokémon'),
        tooltip=['name', 'average_stat'],
        color=alt.value('steelblue')  # Default color for all bars
    )

    # Highlight the selected Pokémon in red
    highlight_chart = alt.Chart(selected_pokemon).mark_bar(color='red').encode(
        x='average_stat',
        y='name',
        tooltip=['name', 'average_stat']
    )

    # Combine the base chart with the highlighted selected Pokémon
    return alt.layer(base_chart, highlight_chart).to_dict()


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=True)
