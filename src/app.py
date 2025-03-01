
from dash import Dash, dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate
import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

df = pd.read_csv("data/raw/pokemon.csv")
df['generation'] = df['generation'].astype('category')
a = df[["name"]]
a = a.rename(columns={"name": "label"})
a["value"] = df["pokedex_number"]

stats_columns = ['sp_attack', 'sp_defense', 'attack', 'defense', 'hp', 'speed']
df['average_stat'] = df[stats_columns].mean(axis=1)
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
    {'label': 'Normal', 'value': 'normal'},
    {'label': 'Fire', 'value': 'fire'},
    {'label': 'Water', 'value': 'water'},
    {'label': 'Electric', 'value': 'electric'},
    {'label': 'Grass', 'value': 'grass'},
    {'label': 'Ice', 'value': 'ice'},
    {'label': 'Fighting', 'value': 'fighting'},
    {'label': 'Poison', 'value': 'poison'},
    {'label': 'Ground', 'value': 'ground'},
    {'label': 'Flying', 'value': 'flying'},
    {'label': 'Psychic', 'value': 'psychic'},
    {'label': 'Bug', 'value': 'bug'},
    {'label': 'Rock', 'value': 'rock'},
    {'label': 'Ghost', 'value': 'ghost'},
    {'label': 'Dragon', 'value': 'dragon'},
    {'label': 'Dark', 'value': 'dark'},
    {'label': 'Steel', 'value': 'steel'},
    {'label': 'Fairy', 'value': 'fairy'}
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
                html.P([
                    "The GitHub repository can be found ",
                    html.A("here", href="https://github.com/UBC-MDS/DSCI-532_2025_06_pokemon-dashboard")
                    ])
            ], style={"textAlign": "left"}),

            # Pokemon Dropdown
            html.Div([
                html.Div([
                    html.H2("Choose your Pokemon"),
                    html.Div(
                        dcc.Dropdown(id="pokemon_dropdown", search_value="Pikachu", value=25, clearable=False),
                        style={'width': '100%'}
                    ),
                    html.Div(id="pokemon_dropdown_output"),
                ]),
            ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px'}),

            # Image
            html.Div(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(id='pokemon_image', style={'width': '75%'}),
                            width=6,
                            style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
                        ),
                        dbc.Col(
                            dbc.Row([ 
                                dbc.Col(html.Img(id='pokemon_type_1')),
                                dbc.Col(html.Img(id='pokemon_type_2')) if not None else None
                            ], justify="center", align="center"),
                        ),
                    ],
                    justify="center",
                    align="center",
                )
            ),

            # Generation Dropdown
            html.Div([
                html.H2("Select Generation"),
                dcc.Dropdown(
                    id="generation_dropdown",
                    options=[{'label': str(i), 'value': i} for i in range(1, 8)],  # Generations 1 to
                    multi=True,
                    placeholder="Select Generation(s)",
                    value=[1, 3, 5],
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
                            className="type-dropdown-style",
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
                            className="type-dropdown-style",
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
                        id="hp_range_slider",
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
                        id="attack_range_slider",
                        min=0,
                        max=200,
                        step=1,
                        value=[0, 200],
                        marks={0: '0', 200: '200'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    html.Br(),                    
                    html.H2("Defense"),
                    dcc.RangeSlider(
                        id="defense_range_slider",
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
                        id="sp_attack_range_slider",
                        min=0,
                        max=250,
                        step=1,
                        value=[0, 250],
                        marks={0: '0', 250: '250'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    html.Br(),                    
                    html.H2("Sp. Defense"),
                    dcc.RangeSlider(
                        id="sp_defense_range_slider",
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
                        id="speed_range_slider",
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
                html.H2('Scatterplot: Comparing Pokémon Metrics'),
                html.Div([
                    html.Label("x-axis metric:", style={"marginRight": "10px"}),
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
                    html.Label("y-axis metric:", style={"marginRight": "10px"}),
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
                html.H2("Comparison with Top 7 Pokémon by Avg Stats"),
                dvc.Vega(id='top_7_chart', spec={}, style={'width': '100%'})  # Vega chart
            ], style={'padding': '1vh'})

        ], width=5),  # Right column width

        # Second Output Column
        dbc.Col([
            # First Row
            html.Div([
                html.H2('Type Disadvantage: Examining Pokémon Weaknesses'),
                html.Div([
                    dvc.Vega(
                        id="type_matchup",
                        style={"minWidth": "100px", "flex": "1"},
                    ),
                    ],
                    style={"display": "flex", "alignItems": "center", 'height': '100%'},
                ),
                html.Br(),
                dvc.Vega(id='vstype', spec={}, style={'width': '100%'}),
            ]),

            # Second Row
            html.Div([
                html.H2('Boxplot: Examining Pokémon Stat Distributions by Type'),
                html.Div([
                    html.Label("x-axis label:", style={"marginRight": "10px"}),
                    dcc.Dropdown(
                        id="x_col_boxplot",
                        options=scatterplot_options,
                        value="speed",
                        clearable=False,
                        placeholder="x-axis property",
                        style={"minWidth": "100px", "flex": "1"},
                    ),
                    ],
                    style={"display": "flex", "alignItems": "center", 'height': '100%'},
                ),
                html.Br(),
                dvc.Vega(id='boxplot', spec={}, style={'width': '100%'}),
            ])

        ], width=5)  # Right column width
    ], align="start")
], fluid=True, style={"height": "100vh", "padding": "4vh"})


@callback(
    Output("pokemon_dropdown", "options"),
    Input("pokemon_dropdown", "search_value"),
)
def update_options(search_value):
    """
    Dynamically updates the options for the Pokemon dropdown based on the search value entered.
    """
    options = a.to_dict(orient="records")
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


@callback(
    Output("pokemon_dropdown_output", "children"),
    Input("pokemon_dropdown", "value")
)
def update_output(input_value):
    """
    Display Pokédex number of selected Pokémon.
    """
    return f"Pokedex Number: {input_value}"


@callback(
    Output('pokemon_image', 'src'),
    Output('pokemon_type_1', 'src'),
    Output('pokemon_type_2', 'src'),
    Input('pokemon_dropdown', 'value')
)
def update_image(selected_pokemon_id):
    """
    Display image and type of selected Pokémon.
    """
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png"
    selected_pokemon = df.loc[df['pokedex_number'] == selected_pokemon_id]
    selected_pokemon_type_1 = selected_pokemon['type1'].values[0]
    selected_pokemon_type_2 = selected_pokemon['type2'].values[0] if not pd.isna(selected_pokemon['type2'].values[0]) else None
    type_1_path = f"/assets/types/{selected_pokemon_type_1}.png"
    type_2_path = f"/assets/types/{selected_pokemon_type_2}.png" if selected_pokemon_type_2 else None
    return image_url, type_1_path, type_2_path


@callback(
    Output("scatter", "spec"),
    Input("x_col", "value"),
    Input("y_col", "value"),
    Input("pokemon_dropdown", "value")
)
def create_chart(x_col, y_col, selected_pokemon_id):
    """
    Create scatterplot of Pokémon stats.
    """
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
    ).mark_image(
        url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png",
        width=50,
        height=50
    ).encode(
        x=x_col,
        y=y_col,
        tooltip="name"
    )
    return alt.layer(base, selected_plot).interactive().to_dict()


def filterData(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
               selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range):
    """
    Filters the Pokémon dataset based on the selected criteria for generation, types, and stat ranges.
    """
    # Filter by generation
    filtered_df = df[df['generation'].isin(selected_generation)].copy()

    # Filter by types
    filtered_df = filtered_df[filtered_df['type1'].isin(selected_type_1)]
    filtered_df = filtered_df[filtered_df['type2'].isin(selected_type_2)]

    # Filter by stat ranges
    filtered_df = filtered_df[
        (filtered_df['hp'] >= selected_hp_range[0]) & (filtered_df['hp'] <= selected_hp_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['attack'] >= selected_attack_range[0]) & (filtered_df['attack'] <= selected_attack_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['speed'] >= selected_speed_range[0]) & (filtered_df['speed'] <= selected_speed_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['sp_defense'] >= selected_sp_defense_range[0]) & (filtered_df['sp_defense'] <= selected_sp_defense_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['sp_attack'] >= selected_sp_attack_range[0]) & (filtered_df['sp_attack'] <= selected_sp_attack_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['defense'] >= selected_defense_range[0]) & (filtered_df['defense'] <= selected_defense_range[1])
    ]
    return filtered_df


def getTop7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
            selected_attack_range, selected_speed_range, selected_sp_defense_range,
            selected_sp_attack_range, selected_defense_range):
    """
    Calculate average stats for each Pokémon.
    """
    filtered_df = filterData(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
                             selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

    # Sort by average stats and return top 7
    top_7 = filtered_df[attributes].sort_values(by='average_stat', ascending=False).head(7)

    return top_7


@callback(
    Output("top_7_chart", "spec"),
    Input("pokemon_dropdown", "value"),
    Input("generation_dropdown", "value"),
    Input("type1_dropdown", "value"),
    Input("type2_dropdown", "value"),
    Input("hp_range_slider", "value"),
    Input("attack_range_slider", "value"),
    Input("speed_range_slider", "value"),
    Input("sp_defense_range_slider", "value"),
    Input("sp_attack_range_slider", "value"),
    Input("defense_range_slider", "value")
)
def create_top7_histogram(selected_pokemon_id, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
                          selected_attack_range, selected_speed_range, selected_sp_defense_range, selected_sp_attack_range,
                          selected_defense_range):
    """
    Creates a bar chart displaying the top 7 Pokémon based on their average stats and highlights the selected Pokémon.
    """
    if not selected_generation:
        selected_generation = list(range(1, 8))

    if not selected_type_1:
        selected_type_1 = [option['value'] for option in type_options]

    if not selected_type_2:
        selected_type_2 = [option['value'] for option in type_options]

    # Filter the selected Pokémon based on the dropdown value
    attributes = ['name', 'average_stat', 'hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']
    selected_pokemon = df[df['pokedex_number'] == selected_pokemon_id][attributes]
    top_7 = getTop7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
                    selected_attack_range, selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

    # If the selected Pokémon is not in the top 7, we add it
    if selected_pokemon['name'].values[0] not in top_7['name'].values:
        top_7 = pd.concat([top_7, selected_pokemon]).drop_duplicates(subset='name').nlargest(7, 'average_stat')  
    else:
        top_7 = top_7  # Keep the original top 7 if already in the list

    # Base bar chart for the top 7 Pokémon
    base_chart = alt.Chart(top_7, width="container", height=400).mark_bar().encode(
        x=alt.X('average_stat', title='Average Stats'),
        y=alt.Y('name', title='Pokémon', sort=top_7['name'].tolist()),
        tooltip=attributes,
        color=alt.value('steelblue')
    )

    # Highlight the selected Pokémon in red
    highlight_chart = alt.Chart(selected_pokemon).mark_bar(color='red').encode(
        x=alt.X('average_stat'),
        y=alt.Y('name', sort=top_7['name'].tolist()),
        tooltip=attributes
    )

    # Combine the base chart with the highlighted selected Pokémon
    return alt.layer(base_chart, highlight_chart).to_dict()


@callback(
    Output("boxplot", "spec"),
    Input("x_col_boxplot", "value"),
    Input("pokemon_dropdown", "value")
)
def create_type_boxplot(x_col, selected_pokemon_id):
    """
    Creates a boxplot for a given stat (specified by `x_col`) across Pokémon types and highlights the selected Pokémon.
    """
    base = alt.Chart(df, width="container").mark_boxplot().encode(
        x=x_col,   # Chosen stat
        y="type1",   # Just type1 for now. Can be changed to accomodate dropdown of type1 or type2 later
        color=alt.Color("type1", legend=None)
    )
    selected_pokemon = alt.Chart(
        df.loc[df['pokedex_number'] == selected_pokemon_id],
        width="container"
    ).mark_image(
        url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png",
        width=50,
        height=50
    ).encode(
        x=x_col,
        y="type1",
        tooltip="name"    # Add mark of chosen pokemon as a point in the appropriate type
    )

    # Return both charts (boxplot, and point of the selected Pokémon) layered together
    return alt.layer(base, selected_pokemon).to_dict()


# Create dataframe containing type matchup
df2 = df[['against_bug', 'against_dark', 'against_dragon',
          'against_electric', 'against_fairy', 'against_fight', 'against_fire',
          'against_flying', 'against_ghost', 'against_grass', 'against_ground',
          'against_ice', 'against_normal', 'against_poison', 'against_psychic',
          'against_rock', 'against_steel', 'against_water', 'name']]

# Flip the rows and columns to obtain each pokemon as an iterable
df2 = df2.set_index("name").transpose()


@callback(
    Output("vstype", "spec"),
    Input("type_matchup", "value"),
    Input("pokemon_dropdown", "value")
)
def create_type_comparison(x_col, selected_pokemon_id):
    """
    Creates a bar chart comparing type matchups for the selected Pokémon.
    """
    base = alt.Chart(df2.reset_index()).mark_bar().encode(
        x=alt.X(
            df.loc[df['pokedex_number'] == selected_pokemon_id]['name'].to_list()[-1],
            axis=alt.Axis(values=[0, 0.5, 1, 1.5, 2, 4])),
        y="index",
        tooltip=df.loc[df['pokedex_number'] == selected_pokemon_id]['name'].to_list()[-1]
    )
    return alt.layer(base).configure_axis(grid=False).to_dict()


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
